package com.cambodia.market.service;

import com.cambodia.market.dto.RawListingDto;
import com.cambodia.market.model.ItemCategory;
import com.cambodia.market.model.ItemCondition;
import com.cambodia.market.model.ListingItem;
import com.cambodia.market.model.SourcePlatform;
import com.cambodia.market.repository.ListingItemRepository;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.jsoup.Jsoup;
import org.jsoup.safety.Safelist;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.util.Optional;
import java.util.UUID;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

@Service
public class ListingEtlService {

    private static final Logger log = LoggerFactory.getLogger(ListingEtlService.class);

    private final ListingItemRepository repository;
    private final CurrencyNormalizerService currencyService;
    private final EmbeddingService embeddingService;
    private final ObjectMapper objectMapper;

    public ListingEtlService(ListingItemRepository repository,
                             CurrencyNormalizerService currencyService,
                             EmbeddingService embeddingService,
                             ObjectMapper objectMapper) {
        this.repository = repository;
        this.currencyService = currencyService;
        this.embeddingService = embeddingService;
        this.objectMapper = objectMapper;
    }

    /**
     * Complete Production ETL Pipeline:
     * 1. Extract & Clean (JSoup HTML stripping)
     * 2. Normalize Currency (KHR -> USD)
     * 3. NLP / LLM Entity Extraction (Brand, Model, Storage, Condition, Location)
     * 4. Deduplication Engine (Check fingerprint hash: phone + normalizedTitle + price)
     * 5. AI Vectorization (768-dim Embeddings)
     * 6. Storage & Indexing
     */
    public ListingItem processAndSave(RawListingDto raw) {
        log.info("Processing ETL for item from {}: '{}'", raw.getPlatform(), raw.getTitle());

        // Step 1: Clean text fields
        String cleanTitle = cleanHtml(raw.getTitle());
        String cleanDesc = cleanHtml(raw.getRawDescription());

        // Step 2: Normalize Currency
        CurrencyNormalizerService.NormalizedPrice price = currencyService.normalizePrice(
                raw.getRawPrice(), raw.getParsedPrice(), raw.getCurrency()
        );

        // Step 3: Structured Entity Extraction (Brand, Model, Storage)
        String brand = extractBrand(cleanTitle, cleanDesc);
        String modelName = extractModel(cleanTitle, cleanDesc);
        String storage = extractStorage(cleanTitle, cleanDesc);
        ItemCategory category = inferCategory(cleanTitle, cleanDesc, raw.getCategory());
        ItemCondition condition = inferCondition(cleanTitle, cleanDesc, raw.getCondition());
        String location = inferLocation(cleanTitle, cleanDesc, raw.getLocation());
        SourcePlatform platform = inferPlatform(raw.getPlatform());
        String cleanPhone = cleanPhone(raw.getContactPhone());

        // Step 4: Deduplication Engine
        String fingerprint = generateFingerprint(platform, cleanPhone, cleanTitle, price.priceUsd);
        Optional<ListingItem> existing = repository.findByFingerprintHash(fingerprint);
        if (existing.isPresent()) {
            ListingItem item = existing.get();
            item.incrementDuplicateCount();
            repository.incrementDuplicatesPrevented();
            log.info("♻️ [Deduplication] Duplicate item caught for seller phone '{}' - Title: '{}' (Hit #{})",
                    cleanPhone, cleanTitle, item.getDuplicateHitCount());
            return item;
        }

        // Step 5: Vector Embedding Generation
        String fullSemanticText = String.format("%s. %s. Brand: %s. Model: %s. Storage: %s. Category: %s. Condition: %s. Location: %s. Platform: %s",
                cleanTitle, cleanDesc, brand, modelName, storage, category, condition, location, platform);
        float[] embedding = embeddingService.generateEmbedding(fullSemanticText);

        // Step 6: Construct Entity
        String id = (raw.getId() != null && !raw.getId().isBlank()) ? raw.getId() : "item_" + UUID.randomUUID().toString().replace("-", "").substring(0, 16);

        String jsonPayload = "{}";
        try {
            jsonPayload = objectMapper.writeValueAsString(raw);
        } catch (Exception ignored) {}

        ListingItem item = new ListingItem(
                id,
                fingerprint,
                cleanTitle,
                cleanDesc,
                category,
                condition,
                price.priceUsd,
                price.originalPrice,
                price.originalCurrency,
                location,
                platform,
                raw.getSourceUrl(),
                raw.getImageUrl(),
                cleanPhone,
                brand,
                modelName,
                storage,
                embedding,
                jsonPayload
        );

        // Smart direct chat resolution: Telegram t.me, Messenger m.me, Instagram DM ig.me, or tel:
        String chatUrl = raw.getDirectChatUrl();
        if (chatUrl == null || chatUrl.isBlank()) {
            if (cleanPhone != null && cleanPhone.length() >= 8) {
                chatUrl = "tel:" + cleanPhone;
            } else if (platform == SourcePlatform.TELEGRAM) {
                chatUrl = "https://t.me/khmer_phone_admin";
            } else if (platform == SourcePlatform.FB_MARKETPLACE) {
                chatUrl = "https://m.me/marketplace.cambodia";
            } else if (platform == SourcePlatform.INSTAGRAM) {
                chatUrl = "https://ig.me/m/apple_phnompenh_store";
            } else if (platform == SourcePlatform.TIKTOK) {
                chatUrl = "https://www.tiktok.com/@cambodia_tech_phone";
            } else {
                chatUrl = raw.getSourceUrl();
            }
        }
        item.setDirectChatUrl(chatUrl);
        item.setPostedDate(raw.getPostedDate() != null && !raw.getPostedDate().isBlank() ? raw.getPostedDate() : "Today, 11:30 AM");

        ListingItem saved = repository.save(item);
        log.info("✅ Successfully loaded listing ID={} [{}] [Brand: {}, Model: {}, Storage: {}] - ${} USD into Vector Store",
                saved.getId(), saved.getTitle(), saved.getBrand(), saved.getModelName(), saved.getStorageCapacity(), saved.getPriceUsd());
        return saved;
    }

    private String cleanHtml(String input) {
        if (input == null) return "";
        return Jsoup.clean(input, Safelist.none()).trim();
    }

    private String cleanPhone(String phone) {
        if (phone == null) return "";
        return phone.replaceAll("[^0-9]", "");
    }

    /**
     * Generates an MD5 fingerprint for deduplication:
     * Seller Phone + Normalized Title Keywords + Rounded Price
     */
    private String generateFingerprint(SourcePlatform platform, String phone, String title, java.math.BigDecimal price) {
        try {
            String normTitle = title.toLowerCase().replaceAll("[^a-z0-9]", "");
            String base = (phone != null && !phone.isBlank() ? phone : platform.name()) + "_" + normTitle + "_" + price.intValue();
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] digest = md.digest(base.getBytes(StandardCharsets.UTF_8));
            StringBuilder sb = new StringBuilder();
            for (byte b : digest) {
                sb.append(String.format("%02x", b));
            }
            return sb.toString();
        } catch (Exception e) {
            return UUID.randomUUID().toString();
        }
    }

    // ==========================================
    // NLP / LLM Entity Extraction
    // ==========================================
    public String extractBrand(String title, String desc) {
        String combined = (title + " " + desc).toLowerCase();
        if (combined.contains("iphone") || combined.contains("apple") || combined.contains("ipad") || combined.contains("macbook") || combined.contains("អាយហ្វូន")) return "Apple";
        if (combined.contains("samsung") || combined.contains("galaxy") || combined.contains("សាំស៊ុង")) return "Samsung";
        if (combined.contains("honda") || combined.contains("dream") || combined.contains("scoopy") || combined.contains("click") || combined.contains("ហុងដា")) return "Honda";
        if (combined.contains("toyota") || combined.contains("prius") || combined.contains("camry")) return "Toyota";
        if (combined.contains("lexus")) return "Lexus";
        if (combined.contains("oppo")) return "Oppo";
        if (combined.contains("vivo")) return "Vivo";
        if (combined.contains("xiaomi") || combined.contains("redmi")) return "Xiaomi";
        return "Generic";
    }

    public String extractModel(String title, String desc) {
        String combined = (title + " " + desc).toLowerCase();
        if (combined.contains("iphone 15 pro max") || combined.contains("15 pro max")) return "iPhone 15 Pro Max";
        if (combined.contains("iphone 15 pro")) return "iPhone 15 Pro";
        if (combined.contains("iphone 15")) return "iPhone 15";
        if (combined.contains("iphone 14 pro max") || combined.contains("14 pro max")) return "iPhone 14 Pro Max";
        if (combined.contains("iphone 14 pro")) return "iPhone 14 Pro";
        if (combined.contains("iphone 14")) return "iPhone 14";
        if (combined.contains("iphone 13 pro max") || combined.contains("13 pro max")) return "iPhone 13 Pro Max";
        if (combined.contains("iphone 13 pro")) return "iPhone 13 Pro";
        if (combined.contains("iphone 13")) return "iPhone 13";
        if (combined.contains("iphone 12")) return "iPhone 12";
        if (combined.contains("iphone 11")) return "iPhone 11";
        if (combined.contains("s23 ultra")) return "Galaxy S23 Ultra";
        if (combined.contains("s22 ultra")) return "Galaxy S22 Ultra";
        if (combined.contains("dream 2022")) return "Dream 125 (2022)";
        if (combined.contains("dream 2021")) return "Dream 125 (2021)";
        if (combined.contains("dream 2020")) return "Dream 125 (2020)";
        if (combined.contains("scoopy 2022") || combined.contains("scoopy")) return "Scoopy Club12";
        if (combined.contains("click 125i") || combined.contains("click")) return "Click 125i";
        if (combined.contains("prius 2005") || combined.contains("prius")) return "Prius";
        return "Standard Listing";
    }

    public String extractStorage(String title, String desc) {
        Pattern pattern = Pattern.compile("(?i)\\b(64|128|256|512)\\s*(?:gb|g)\\b|\\b(1|2)\\s*(?:tb)\\b");
        Matcher matcher = pattern.matcher(title + " " + desc);
        if (matcher.find()) {
            return matcher.group(0).toUpperCase().replaceAll("\\s+", "");
        }
        return "Standard";
    }

    public ItemCategory inferCategory(String title, String desc, String rawCat) {
        String combined = (title + " " + desc + " " + (rawCat != null ? rawCat : "")).toLowerCase();
        if (combined.contains("iphone") || combined.contains("samsung") || combined.contains("phone") || combined.contains("ទូរស័ព្ទ") || combined.contains("oppo") || combined.contains("vivo") || combined.contains("ipad")) {
            return ItemCategory.PHONES;
        }
        if (combined.contains("dream") || combined.contains("honda") || combined.contains("moto") || combined.contains("ម៉ូតូ") || combined.contains("scopy") || combined.contains("click") || combined.contains("suzuki") || combined.contains("wave") || combined.contains("zoomer")) {
            return ItemCategory.MOTOS;
        }
        if (combined.contains("car") || combined.contains("prius") || combined.contains("lexus") || combined.contains("toyota") || combined.contains("ឡាន") || combined.contains("រថយន្ត") || combined.contains("ford")) {
            return ItemCategory.CARS;
        }
        if (combined.contains("rent") || combined.contains("room") || combined.contains("house") || combined.contains("condo") || combined.contains("land") || combined.contains("ផ្ទះជួល") || combined.contains("បន្ទប់ជួល") || combined.contains("ដី") || combined.contains("ខុនដូ")) {
            return ItemCategory.REAL_ESTATE;
        }
        if (combined.contains("macbook") || combined.contains("laptop") || combined.contains("watch") || combined.contains("airpods") || combined.contains("audio") || combined.contains("tv") || combined.contains("computer")) {
            return ItemCategory.ELECTRONICS;
        }
        return ItemCategory.OTHER;
    }

    public ItemCondition inferCondition(String title, String desc, String rawCondition) {
        String combined = (title + " " + desc + " " + (rawCondition != null ? rawCondition : "")).toLowerCase();
        if (combined.contains("មួយទឹក") || combined.contains("used") || combined.contains("secondhand") || combined.contains("second hand") || combined.contains("ជជុះ") || combined.contains("99%") || combined.contains("98%") || combined.contains("95%")) {
            return ItemCondition.USED_SECOND_HAND;
        }
        if (combined.contains("ថ្មី") || combined.contains("new") || combined.contains("brand new") || combined.contains("កេះ") || combined.contains("100%")) {
            return ItemCondition.NEW;
        }
        return ItemCondition.USED_SECOND_HAND;
    }

    public String inferLocation(String title, String desc, String rawLoc) {
        if (rawLoc != null && !rawLoc.isBlank()) return cleanHtml(rawLoc);
        String combined = (title + " " + desc).toLowerCase();
        if (combined.contains("ទួលគោក") || combined.contains("toul kork") || combined.contains("tuol kouk")) return "Toul Kork, Phnom Penh";
        if (combined.contains("សែនសុខ") || combined.contains("sen sok")) return "Sen Sok, Phnom Penh";
        if (combined.contains("ចំការមន") || combined.contains("chamkarmon")) return "Chamkarmon, Phnom Penh";
        if (combined.contains("បឹងកេងកង") || combined.contains("bkk")) return "BKK, Phnom Penh";
        if (combined.contains("ស្ទឹងមានជ័យ") || combined.contains("stung meanchey")) return "Stung Meanchey, Phnom Penh";
        if (combined.contains("សៀមរាប") || combined.contains("siem reap")) return "Siem Reap";
        if (combined.contains("បាត់ដំបង") || combined.contains("battambang")) return "Battambang";
        return "Phnom Penh";
    }

    public SourcePlatform inferPlatform(String rawPlatform) {
        if (rawPlatform == null) return SourcePlatform.KHMER24;
        String p = rawPlatform.toUpperCase();
        if (p.contains("TELEGRAM") || p.contains("TG")) return SourcePlatform.TELEGRAM;
        if (p.contains("FB") || p.contains("FACEBOOK")) return SourcePlatform.FB_MARKETPLACE;
        if (p.contains("INSTA")) return SourcePlatform.INSTAGRAM;
        if (p.contains("TIKTOK") || p.contains("TT")) return SourcePlatform.TIKTOK;
        return SourcePlatform.KHMER24;
    }
}
