package com.cambodia.market.controller;

import com.cambodia.market.dto.RawListingDto;
import com.cambodia.market.model.ListingItem;
import com.cambodia.market.model.SourcePlatform;
import com.cambodia.market.repository.ListingItemRepository;
import com.cambodia.market.service.ListingEtlService;
import com.cambodia.market.service.LiveMarketSearchEngine;
import jakarta.annotation.PostConstruct;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.math.BigDecimal;
import java.util.*;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api/v1/ingest")
@CrossOrigin(origins = "*")
public class IngestionController {

    private static final Logger log = LoggerFactory.getLogger(IngestionController.class);

    private final ListingEtlService etlService;
    private final ListingItemRepository repository;
    private final LiveMarketSearchEngine liveSearchEngine;

    public IngestionController(ListingEtlService etlService,
                               ListingItemRepository repository,
                               LiveMarketSearchEngine liveSearchEngine) {
        this.etlService = etlService;
        this.repository = repository;
        this.liveSearchEngine = liveSearchEngine;
    }

    @PostConstruct
    public void init() {
        log.info("🚀 Market AI Core started in Clean Real-Time Search Mode. Ready for live queries.");
    }

    @PostMapping("/clear-data")
    public ResponseEntity<Map<String, Object>> clearData() {
        repository.clearAll();
        log.info("🧹 All mock and cached listings cleared successfully.");
        Map<String, Object> resp = new HashMap<>();
        resp.put("status", "SUCCESS");
        resp.put("totalDatabaseListings", repository.countAllListings());
        resp.put("message", "Database cleared! All mock data removed. System is ready for live real searches.");
        return ResponseEntity.ok(resp);
    }

    @PostMapping("/live-search")
    public ResponseEntity<Map<String, Object>> triggerLiveSearch(@RequestParam("q") String query) {
        int count = liveSearchEngine.executeLiveMarketSearch(query);
        Map<String, Object> resp = new HashMap<>();
        resp.put("status", "SUCCESS");
        resp.put("query", query);
        resp.put("newItemsIngested", count);
        resp.put("totalDatabaseListings", repository.countAllListings());
        return ResponseEntity.ok(resp);
    }

    @PostMapping("/item")
    public ResponseEntity<ListingItem> ingestItem(@RequestBody RawListingDto rawItem) {
        ListingItem saved = etlService.processAndSave(rawItem);
        return ResponseEntity.ok(saved);
    }

    @GetMapping("/stats")
    public ResponseEntity<Map<String, Object>> getStats() {
        Map<String, Object> stats = new HashMap<>();
        stats.put("totalListings", repository.countAllListings());
        stats.put("averagePriceUsd", repository.findAveragePriceUsd());
        stats.put("minPriceUsd", repository.findMinPriceUsd());
        stats.put("maxPriceUsd", repository.findMaxPriceUsd());
        stats.put("duplicatesPrevented", repository.getDuplicatesPreventedCount());
        return ResponseEntity.ok(stats);
    }

    @GetMapping("/pipeline-status")
    public ResponseEntity<Map<String, Object>> getPipelineStatus() {
        Map<String, Object> status = new HashMap<>();
        status.put("totalListings", repository.countAllListings());
        status.put("duplicatesPrevented", repository.getDuplicatesPreventedCount());

        Map<SourcePlatform, Long> byPlatform = repository.findAll().stream()
                .collect(Collectors.groupingBy(ListingItem::getPlatform, Collectors.counting()));
        status.put("platformCounts", byPlatform);
        return ResponseEntity.ok(status);
    }

    @PostMapping("/seed-sample-data")
    public ResponseEntity<Map<String, Object>> seedSampleData() {
        List<RawListingDto> dataset = new ArrayList<>();

        // ==========================================
        // 1. TELEGRAM PUBLIC TRADING CHANNELS
        // ==========================================
        dataset.add(RawListingDto.builder()
                .id("tg_p01")
                .title("iPhone 14 Pro Max 256GB ស្អាត 98% សំណុំហ្ស៊ីន")
                .rawDescription("Telegram Channel Post: លក់ប្រញាប់លុយ iPhone 14 Pro Max 256GB ស្អាត 98% សំណុំហ្ស៊ីន ពណ៌ខ្មៅ Space Black តម្លៃ 690$ ទីតាំងទួលគោក 097 888 7766")
                .category("PHONES")
                .rawPrice("$690")
                .parsedPrice(new BigDecimal("690"))
                .currency("USD")
                .condition("used")
                .location("Toul Kork, Phnom Penh")
                .platform("TELEGRAM")
                .sourceUrl("https://t.me/khmer_phone_market/4492")
                .imageUrl("https://images.unsplash.com/photo-1695048133142-1a20484d2569?auto=format&fit=crop&w=600&q=80")
                .contactPhone("097 888 7766")
                .build());

        // Duplicate simulation for tg_p01 (same seller phone + title + price)
        dataset.add(RawListingDto.builder()
                .id("tg_p01_repost")
                .title("iPhone 14 Pro Max 256GB ស្អាត 98% សំណុំហ្ស៊ីន")
                .rawDescription("Telegram Channel Repost: សួស្តីបងប្អូន លក់ iPhone 14 Pro Max 256GB ស្អាត 98% ធានាសំណុំហ្ស៊ីន តម្លៃ 690$ 097 888 7766")
                .category("PHONES")
                .rawPrice("$690")
                .parsedPrice(new BigDecimal("690"))
                .currency("USD")
                .condition("used")
                .location("Toul Kork, Phnom Penh")
                .platform("TELEGRAM")
                .sourceUrl("https://t.me/khmer_phone_market/4510")
                .imageUrl("https://images.unsplash.com/photo-1695048133142-1a20484d2569?auto=format&fit=crop&w=600&q=80")
                .contactPhone("097 888 7766")
                .build());

        dataset.add(RawListingDto.builder()
                .id("tg_p02")
                .title("iPhone 13 128G ZIN 99% ថ្ម 88% ពណ៌ខៀវ")
                .rawDescription("Telegram Group: iPhone 13 128G ZIN 99% ថ្ម 88% ពណ៌ខៀវ តម្លៃធូរ 365$ មកមើលបាននៅសែនសុខ call 012 334 999")
                .category("PHONES")
                .rawPrice("$365")
                .parsedPrice(new BigDecimal("365"))
                .currency("USD")
                .condition("used")
                .location("Sen Sok, Phnom Penh")
                .platform("TELEGRAM")
                .sourceUrl("https://t.me/secondhand_phnompenh/8821")
                .imageUrl("https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=600&q=80")
                .contactPhone("012 334 999")
                .build());

        dataset.add(RawListingDto.builder()
                .id("tg_p03")
                .title("Samsung Galaxy S23 Ultra 512GB មួយទឹក 99%")
                .rawDescription("Telegram Phone Dealer: S23 Ultra 512GB RAM 12GB Phantom Black សំណុំកូរ៉េ ស្អាត 99% គ្មានស្នាម តម្លៃ 710$ 088 777 222")
                .category("PHONES")
                .rawPrice("$710")
                .parsedPrice(new BigDecimal("710"))
                .currency("USD")
                .condition("used")
                .location("BKK, Phnom Penh")
                .platform("TELEGRAM")
                .sourceUrl("https://t.me/khmer_phone_market/4522")
                .imageUrl("https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?auto=format&fit=crop&w=600&q=80")
                .contactPhone("088 777 222")
                .build());

        dataset.add(RawListingDto.builder()
                .id("tg_m01")
                .title("Honda Scoopy 2023 Smartkey កង់ធំ ភ្នំពេញ")
                .rawDescription("Telegram Moto Trade: Scoopy 2023 ស្មាតឃី កង់ធំ ម្ចាស់ប្រញាប់លុយបង់ធនាគារ តម្លៃ 1,720$ ចរចា ភ្នំពេញ 086 554 332")
                .category("MOTOS")
                .rawPrice("$1,720")
                .parsedPrice(new BigDecimal("1720"))
                .currency("USD")
                .condition("used")
                .location("Phnom Penh")
                .platform("TELEGRAM")
                .sourceUrl("https://t.me/moto_cambodia_trade/1092")
                .imageUrl("https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?auto=format&fit=crop&w=600&q=80")
                .contactPhone("086 554 332")
                .build());

        // ==========================================
        // 2. FACEBOOK MARKETPLACE LISTINGS
        // ==========================================
        dataset.add(RawListingDto.builder()
                .id("fb_p01")
                .title("iPhone 13 128GB Midnight Secondhand Zin 95%")
                .rawDescription("ត្រូវការលុយបន្ទាន់ លក់ iPhone 13 មួយទឹក ស្នាមតិចតួច ដំណើរការធម្មតា ថែមឆ្នាំងសាក Fast Charge 20W Facebook Marketplace")
                .category("PHONES")
                .rawPrice("$350")
                .parsedPrice(new BigDecimal("350"))
                .currency("USD")
                .condition("used")
                .location("Sen Sok, Phnom Penh")
                .platform("FB_MARKETPLACE")
                .sourceUrl("https://facebook.com/marketplace/item/1029384756")
                .imageUrl("https://images.unsplash.com/photo-1591337676887-a217a6970a8a?auto=format&fit=crop&w=600&q=80")
                .contactPhone("097 555 4433")
                .build());

        dataset.add(RawListingDto.builder()
                .id("fb_p02")
                .title("iPhone 13 Pro 128GB Sierra Blue មួយទឹក 98% ថ្ម 89%")
                .rawDescription("Facebook Marketplace Phnom Penh: iPhone 13 Pro ពណ៌ខៀវ គ្មានស្នាមធ្លាក់ ស្កេនមុខដើរលឿន សំណុំហ្ស៊ីនទាំងអស់")
                .category("PHONES")
                .rawPrice("$480")
                .parsedPrice(new BigDecimal("480"))
                .currency("USD")
                .condition("មួយទឹក")
                .location("Toul Kork, Phnom Penh")
                .platform("FB_MARKETPLACE")
                .sourceUrl("https://facebook.com/marketplace/item/99281726")
                .imageUrl("https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=600&q=80")
                .contactPhone("012 334 455")
                .build());

        dataset.add(RawListingDto.builder()
                .id("fb_p03")
                .title("Samsung Galaxy S22 Ultra 5G មួយទឹកស្អាតខ្លាំង")
                .rawDescription("Samsung Galaxy S22 Ultra 256GB RAM 12GB សំណុំស្រុកក្រៅ គ្មានស្នាម ប៊ិច SPen ដំណើរការល្អ ម្ចាស់លក់ផ្ទាល់លើ Facebook")
                .category("PHONES")
                .rawPrice("1,640,000 ៛")
                .parsedPrice(new BigDecimal("1640000"))
                .currency("KHR")
                .condition("មួយទឹក")
                .location("Chamkarmon, Phnom Penh")
                .platform("FB_MARKETPLACE")
                .sourceUrl("https://facebook.com/marketplace/item/203948572")
                .imageUrl("https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?auto=format&fit=crop&w=600&q=80")
                .contactPhone("010 333 777")
                .build());

        dataset.add(RawListingDto.builder()
                .id("fb_p04")
                .title("iPhone 12 64GB Black មួយទឹក 99% សំណុំហ្ស៊ីន")
                .rawDescription("FB Marketplace: iPhone 12 64GB ពណ៌ខ្មៅ ថ្ម 85% មិនដែលជួសជុល ធានាម៉ាស៊ីន 1 ខែ តម្លៃធូរថ្លៃ")
                .category("PHONES")
                .rawPrice("$270")
                .parsedPrice(new BigDecimal("270"))
                .currency("USD")
                .condition("used")
                .location("BKK, Phnom Penh")
                .platform("FB_MARKETPLACE")
                .sourceUrl("https://facebook.com/marketplace/item/12003948")
                .imageUrl("https://images.unsplash.com/photo-1605236453806-6ff36851218e?auto=format&fit=crop&w=600&q=80")
                .contactPhone("098 777 111")
                .build());

        dataset.add(RawListingDto.builder()
                .id("fb_m01")
                .title("Honda Scoopy 2022 Club12 Smartkey មួយទឹកស្អាត 98%")
                .rawDescription("Scoopy 2022 ស្មាតឃី កង់ធំ ពណ៌សក្រហម ជិះបានតិចគីឡូ សំបកកង់ថ្មី ម៉ាស៊ីនអែម Facebook Marketplace")
                .category("MOTOS")
                .rawPrice("7,175,000 ៛")
                .parsedPrice(new BigDecimal("7175000"))
                .currency("KHR")
                .condition("មួយទឹក")
                .location("Sen Sok, Phnom Penh")
                .platform("FB_MARKETPLACE")
                .sourceUrl("https://facebook.com/marketplace/item/33445566")
                .imageUrl("https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?auto=format&fit=crop&w=600&q=80")
                .contactPhone("078 999 111")
                .build());

        dataset.add(RawListingDto.builder()
                .id("fb_m02")
                .title("Honda Dream 2021 តែមក្រហម មួយទឹក 99% សំណុំ")
                .rawDescription("Dream 2021 តែមក្រហម ម៉ាស៊ីនស្ងាត់ មិនធ្លាប់បុកប៉ះ ផ្លាកលេខភ្នំពេញ 1JC ម្ចាស់ផ្ទាល់លក់ប្រញាប់លុយ")
                .category("MOTOS")
                .rawPrice("$1,580")
                .parsedPrice(new BigDecimal("1580"))
                .currency("USD")
                .condition("used")
                .location("Toul Kork, Phnom Penh")
                .platform("FB_MARKETPLACE")
                .sourceUrl("https://facebook.com/marketplace/item/dream2021")
                .imageUrl("https://images.unsplash.com/photo-1558981403-c5f9899a28bc?auto=format&fit=crop&w=600&q=80")
                .contactPhone("012 556 677")
                .build());

        dataset.add(RawListingDto.builder()
                .id("fb_r02")
                .title("បន្ទប់ជួលតម្លៃធូរថ្លៃ សុវត្ថិភាព 24h នៅជិតផ្សារស្ទឹងមានជ័យ")
                .rawDescription("បន្ទប់ជួលទំហំ 4x5m បន្ទប់ទឹកក្នុង ទឹកស្អាតរដ្ឋ ភ្លើងរដ្ឋ ម៉ូតូចតក្នុងផ្ទះមានកាមេរ៉ាសុវត្ថិភាព តម្លៃត្រឹមតែ 50$/ខែ")
                .category("REAL_ESTATE")
                .rawPrice("$50")
                .parsedPrice(new BigDecimal("50"))
                .currency("USD")
                .condition("used")
                .location("Stung Meanchey, Phnom Penh")
                .platform("FB_MARKETPLACE")
                .sourceUrl("https://facebook.com/marketplace/item/room-stungmeanchey")
                .imageUrl("https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=600&q=80")
                .contactPhone("011 889 900")
                .build());

        // ==========================================
        // 3. INSTAGRAM SHOPS (@ig_shop_kh)
        // ==========================================
        dataset.add(RawListingDto.builder()
                .id("ig_p01")
                .title("iPhone 13 128GB Pink Cute មួយទឹក 99% (@apple_phnompenh)")
                .rawDescription("Instagram Shop @apple_phnompenh: iPhone 13 ពណ៌ផ្កាឈូក Pink សំណុំហ្ស៊ីនស្អាត 99% ថែម Case + កញ្ចក់ការពារ + ឆ្នាំងសាក Fast")
                .category("PHONES")
                .rawPrice("$375")
                .parsedPrice(new BigDecimal("375"))
                .currency("USD")
                .condition("used")
                .location("BKK, Phnom Penh")
                .platform("INSTAGRAM")
                .sourceUrl("https://instagram.com/p/C3xY901abc")
                .imageUrl("https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=600&q=80")
                .contactPhone("096 888 7771")
                .build());

        dataset.add(RawListingDto.builder()
                .id("ig_p03")
                .title("iPhone 15 Pro 128GB Natural Titanium (@khmer_gadget_hub)")
                .rawDescription("Instagram Post: iPhone 15 Pro Natural Titanium ថ្មីកេះ ប្រអប់មិនទាន់ bóc ធានាក្រុមហ៊ុន 1 ឆ្នាំ")
                .category("PHONES")
                .rawPrice("$920")
                .parsedPrice(new BigDecimal("920"))
                .currency("USD")
                .condition("new")
                .location("BKK, Phnom Penh")
                .platform("INSTAGRAM")
                .sourceUrl("https://instagram.com/p/C5zz9912")
                .imageUrl("https://images.unsplash.com/photo-1695048133142-1a20484d2569?auto=format&fit=crop&w=600&q=80")
                .contactPhone("010 998 877")
                .build());

        dataset.add(RawListingDto.builder()
                .id("ig_e01")
                .title("Apple Watch Series 8 45mm Midnight មួយទឹក 99% (@apple_phnompenh)")
                .rawDescription("Instagram: Apple Watch Series 8 45mm GPS ថ្ម 100% ស្នាមគ្មាន ថែមខ្សែ 2 ឈុត")
                .category("ELECTRONICS")
                .rawPrice("$235")
                .parsedPrice(new BigDecimal("235"))
                .currency("USD")
                .condition("used")
                .location("Chamkarmon, Phnom Penh")
                .platform("INSTAGRAM")
                .sourceUrl("https://instagram.com/p/C2watch88")
                .imageUrl("https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?auto=format&fit=crop&w=600&q=80")
                .contactPhone("096 888 7771")
                .build());

        dataset.add(RawListingDto.builder()
                .id("ig_e02")
                .title("AirPods Pro 2nd Gen Type-C សំណុំហ្ស៊ីន មួយទឹក (@cambodia_audio)")
                .rawDescription("Instagram audio shop: AirPods Pro 2 ប្រើរន្ធ Type-C មុខងារ Noise Cancelling ដំណើរការល្អខ្លាំង ថែមស្រោម Case")
                .category("ELECTRONICS")
                .rawPrice("$155")
                .parsedPrice(new BigDecimal("155"))
                .currency("USD")
                .condition("used")
                .location("Toul Kork, Phnom Penh")
                .platform("INSTAGRAM")
                .sourceUrl("https://instagram.com/p/C9airpods")
                .imageUrl("https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?auto=format&fit=crop&w=600&q=80")
                .contactPhone("015 334 499")
                .build());

        dataset.add(RawListingDto.builder()
                .id("ig_e03")
                .title("MacBook Air M2 13-inch 256GB Space Gray (@mac_cambodia)")
                .rawDescription("Instagram: MacBook Air M2 ថ្ម 98% ជិះស្រួល ស្តើង ស្រាល ប្រើសម្រាប់រៀន និងធ្វើការ design ថែម hub")
                .category("ELECTRONICS")
                .rawPrice("$790")
                .parsedPrice(new BigDecimal("790"))
                .currency("USD")
                .condition("used")
                .location("Sen Sok, Phnom Penh")
                .platform("INSTAGRAM")
                .sourceUrl("https://instagram.com/p/C7macm2")
                .imageUrl("https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=600&q=80")
                .contactPhone("089 778 811")
                .build());

        // ==========================================
        // 4. KHMER24 LISTINGS
        // ==========================================
        dataset.add(RawListingDto.builder()
                .id("kh24_p101")
                .title("iPhone 13 128GB មួយទឹកស្អាត 99% សំណុំហ្ស៊ីន")
                .rawDescription("iPhone 13 ពណ៌ខៀវ សភាពស្អាត 99% ថ្ម 87% មិនដែលជួសជុល ធានាម៉ាស៊ីនហ្ស៊ីន មកមើលដល់កន្លែងបាន នៅទួលគោក")
                .category("PHONES")
                .rawPrice("$380")
                .parsedPrice(new BigDecimal("380"))
                .currency("USD")
                .condition("មួយទឹក")
                .location("Toul Kork, Phnom Penh")
                .platform("KHMER24")
                .sourceUrl("https://www.khmer24.com/en/property/sample-iphone-13-380.html")
                .imageUrl("https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=600&q=80")
                .contactPhone("012 888 999")
                .build());

        dataset.add(RawListingDto.builder()
                .id("kh24_m201")
                .title("Honda Dream 2020 តែមខ្មៅ ម៉ាស៊ីនសំណុំ ផ្លាកលេខភ្នំពេញ 1II")
                .rawDescription("Honda Dream 125cc ស៊េរីឆ្នាំ 2020 ម៉ូតូជិះផ្ទាល់ខ្លួន ម៉ាស៊ីនស្ងាត់ មិនធ្លាប់បុកប៉ះ មានពន្ធត្រឹមត្រូវ កាតគ្រីម្ចាស់ដើម")
                .category("MOTOS")
                .rawPrice("$1,450")
                .parsedPrice(new BigDecimal("1450"))
                .currency("USD")
                .condition("មួយទឹក")
                .location("Toul Kork, Phnom Penh")
                .platform("KHMER24")
                .sourceUrl("https://www.khmer24.com/en/honda-dream-2020.html")
                .imageUrl("https://images.unsplash.com/photo-1558981403-c5f9899a28bc?auto=format&fit=crop&w=600&q=80")
                .contactPhone("092 778 899")
                .build());

        dataset.add(RawListingDto.builder()
                .id("kh24_r301")
                .title("បន្ទប់ជួលតម្លៃធូរថ្លៃ មានម៉ាស៊ីនត្រជាក់ នៅជិតផ្សារទួលគោក")
                .rawDescription("បន្ទប់ជួលទំហំ 4x6m បន្ទប់ទឹកក្នុង មានយ៉មុខបន្ទប់ សុវត្ថិភាពល្អ មានកាមេរ៉ា 24h អគ្គិសនីរដ្ឋ ទឹកស្អាតរដ្ឋ ជិតផ្សារមាន់អាំងទួលគោក")
                .category("REAL_ESTATE")
                .rawPrice("$80")
                .parsedPrice(new BigDecimal("80"))
                .currency("USD")
                .condition("USED")
                .location("Toul Kork, Phnom Penh")
                .platform("KHMER24")
                .sourceUrl("https://www.khmer24.com/en/room-rent-toulkork-80.html")
                .imageUrl("https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=600&q=80")
                .contactPhone("016 444 888")
                .build());

        // ==========================================
        // 5. TIKTOK SHOP & LIVE VIDEO LISTINGS
        // ==========================================
        dataset.add(RawListingDto.builder()
                .id("tt_p01")
                .title("iPhone 13 Pro Max 256GB 99% សំណុំហ្ស៊ីន (@tiktok_phone_kh)")
                .rawDescription("TikTok Live Deal! iPhone 13 Pro Max 256G ពណ៌ Sierra Blue ថ្ម 90% ធានាសំណុំហ្ស៊ីន មកមើលដល់ហាងទួលគោក តម្លៃពិសេស 580$ #iphone13promax")
                .category("PHONES")
                .rawPrice("$580")
                .parsedPrice(new BigDecimal("580"))
                .currency("USD")
                .condition("used")
                .location("Toul Kork, Phnom Penh")
                .platform("TIKTOK")
                .sourceUrl("https://www.tiktok.com/@tiktok_phone_kh/video/73918237192")
                .imageUrl("https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=600&q=80")
                .contactPhone("098 112 233")
                .build());

        dataset.add(RawListingDto.builder()
                .id("tt_p02")
                .title("iPhone 11 128GB Yellow ស្អាត 99% (@gadget_tiktok_kh)")
                .rawDescription("លក់ឡាយសាក iPhone 11 128GB ពណ៌លឿង សំណុំស្រុកក្រៅ តម្លៃត្រឹមតែ 230$ ដឹកហ្វ្រី 25 ខេត្តក្រុង 015 667 788 #iphone11")
                .category("PHONES")
                .rawPrice("$230")
                .parsedPrice(new BigDecimal("230"))
                .currency("USD")
                .condition("used")
                .location("Phnom Penh")
                .platform("TIKTOK")
                .sourceUrl("https://www.tiktok.com/@gadget_tiktok_kh/video/7291828731")
                .imageUrl("https://images.unsplash.com/photo-1574755393849-623942496936?auto=format&fit=crop&w=600&q=80")
                .contactPhone("015 667 788")
                .build());

        dataset.add(RawListingDto.builder()
                .id("tt_m01")
                .title("Honda Dream 2022 តែមក្រហម កាតគ្រីម្ចាស់ដើម (@moto_store_tiktok)")
                .rawDescription("TikTok Review: Dream 2022 ម៉ាស៊ីនស្ងាត់ណាស់បងប្អូន ជិះបាន 12,000km តម្លៃ 1,690$ ចរចាបាន 077 889 900 #hondadream2022")
                .category("MOTOS")
                .rawPrice("$1,690")
                .parsedPrice(new BigDecimal("1690"))
                .currency("USD")
                .condition("used")
                .location("Sen Sok, Phnom Penh")
                .platform("TIKTOK")
                .sourceUrl("https://www.tiktok.com/@moto_store_tiktok/video/73118237192")
                .imageUrl("https://images.unsplash.com/photo-1558981403-c5f9899a28bc?auto=format&fit=crop&w=600&q=80")
                .contactPhone("077 889 900")
                .build());

        // ==========================================
        // 6. OUTLIER / SCAM LISTING FOR IQR TESTING
        // ==========================================
        dataset.add(RawListingDto.builder()
                .id("scam_p99")
                .title("iPhone 13 128GB លក់បន្ទាន់ខ្លាំង 45$ (IQR Outlier Test)")
                .rawDescription("Spam / Fraud Listing: iPhone 13 ស្អាតកប់ លក់ត្រឹមតែ 45$ ផ្ញើលុយមុនទើបផ្ញើឥវ៉ាន់ (Flagged as Outlier by AI)")
                .category("PHONES")
                .rawPrice("$45")
                .parsedPrice(new BigDecimal("45"))
                .currency("USD")
                .condition("used")
                .location("Phnom Penh")
                .platform("FB_MARKETPLACE")
                .sourceUrl("https://facebook.com/marketplace/item/scam_test")
                .imageUrl("https://images.unsplash.com/photo-1591337676887-a217a6970a8a?auto=format&fit=crop&w=600&q=80")
                .contactPhone("099 000 000")
                .build());

        int count = 0;
        for (RawListingDto item : dataset) {
            etlService.processAndSave(item);
            count++;
        }

        Map<String, Object> resp = new HashMap<>();
        resp.put("status", "SUCCESS");
        resp.put("seededCount", count);
        resp.put("totalDatabaseListings", repository.countAllListings());
        resp.put("duplicatesPrevented", repository.getDuplicatesPreventedCount());
        resp.put("message", "Successfully ingested listings from Telegram, Facebook, Instagram, and Khmer24!");
        return ResponseEntity.ok(resp);
    }
}
