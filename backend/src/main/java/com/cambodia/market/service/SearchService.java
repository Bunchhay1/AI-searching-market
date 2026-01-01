package com.cambodia.market.service;

import com.cambodia.market.dto.SearchRequest;
import com.cambodia.market.dto.SearchResponse;
import com.cambodia.market.dto.SearchResultDto;
import com.cambodia.market.model.ItemCategory;
import com.cambodia.market.model.ItemCondition;
import com.cambodia.market.model.ListingItem;
import com.cambodia.market.repository.ListingItemRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

@Service
public class SearchService {

    private static final Logger log = LoggerFactory.getLogger(SearchService.class);

    private final ListingItemRepository repository;
    private final EmbeddingService embeddingService;
    private final CurrencyNormalizerService currencyService;
    private final SmartPricingService smartPricingService;
    private final LiveMarketSearchEngine liveSearchEngine;

    public SearchService(ListingItemRepository repository,
                         EmbeddingService embeddingService,
                         CurrencyNormalizerService currencyService,
                         SmartPricingService smartPricingService,
                         LiveMarketSearchEngine liveSearchEngine) {
        this.repository = repository;
        this.embeddingService = embeddingService;
        this.currencyService = currencyService;
        this.smartPricingService = smartPricingService;
        this.liveSearchEngine = liveSearchEngine;
    }

    public SearchResponse search(SearchRequest request) {
        String rawQuery = request.getQuery() != null ? request.getQuery().trim() : "";
        log.info("🔍 Received Natural Language Market Search Request: '{}' (Stateless Live Processing)", rawQuery);

        // Stateless Live Processing via Python AI Engine / In-Memory Generator (0 items saved to DB)
        return liveSearchEngine.searchStateless(rawQuery);
    }

    private static class ExtractedIntent {
        ItemCategory category;
        ItemCondition condition;
        BigDecimal minPrice;
        BigDecimal maxPrice;
        String location;
        String summary;
    }

    private ExtractedIntent extractIntent(String query, SearchRequest req) {
        ExtractedIntent intent = new ExtractedIntent();
        intent.category = req.getCategory();
        intent.condition = req.getCondition();
        intent.minPrice = req.getMinPrice();
        intent.maxPrice = req.getMaxPrice();
        intent.location = req.getLocation();

        String q = currencyService.convertKhmerNumeralsToLatin(query).toLowerCase();

        // 1. Auto-detect condition if not specified explicitly
        if (intent.condition == null) {
            if (q.contains("មួយទឹក") || q.contains("used") || q.contains("second") || q.contains("ជជុះ")) {
                intent.condition = ItemCondition.USED_SECOND_HAND;
            } else if (q.contains("ថ្មី") || q.contains("new") || q.contains("កេះ")) {
                intent.condition = ItemCondition.NEW;
            }
        }

        // 2. Auto-detect max price: e.g. "ក្រោម $400", "under 400", "< 400", "ក្រោម 400$"
        if (intent.maxPrice == null) {
            Pattern underPattern = Pattern.compile("(?:ក្រោម|under|below|<|<=)\\s*\\$?([0-9]+(?:\\.[0-9]+)?)");
            Matcher m = underPattern.matcher(q);
            if (m.find()) {
                intent.maxPrice = new BigDecimal(m.group(1));
            }
        }

        // 3. Auto-detect category
        if (intent.category == null) {
            String[] carKeywords = {
                "car", "auto", "suv", "sedan", "crossover", "cross", "yaris", "raize", "corolla", "camry", "crown",
                "fortuner", "hilux", "revo", "vigo", "land cruiser", "cruiser", "prado", "alphard", "vellfire", "prius",
                "lexus", "lx", "rx", "nx", "gx", "ford", "ranger", "raptor", "wildtrak", "everest", "f150",
                "hyundai", "kia", "mazda", "mitsubishi", "pajero", "isuzu", "d-max", "tank", "byd", "ឡាន", "រថយន្ត"
            };
            boolean isCar = false;
            for (String kw : carKeywords) {
                if (q.contains(kw)) {
                    isCar = true;
                    break;
                }
            }

            if (isCar) {
                intent.category = ItemCategory.CARS;
            } else if (q.contains("dream") || q.contains("honda") || q.contains("moto") || q.contains("ម៉ូតូ") || q.contains("scopy") || q.contains("click") || q.contains("pcx") || q.contains("adv") || q.contains("125cc") || q.contains("160cc")) {
                intent.category = ItemCategory.MOTOS;
            } else if (q.contains("rent") || q.contains("room") || q.contains("house") || q.contains("បន្ទប់ជួល") || q.contains("ផ្ទះជួល") || q.contains("ដី") || q.contains("condo")) {
                intent.category = ItemCategory.REAL_ESTATE;
            } else if (q.contains("iphone") || q.contains("samsung") || q.contains("phone") || q.contains("ទូរស័ព្ទ") || q.contains("pixel") || q.contains("xiaomi")) {
                intent.category = ItemCategory.PHONES;
            }
        }

        // 4. Auto-detect location
        if (intent.location == null) {
            if (q.contains("ភ្នំពេញ") || q.contains("phnom penh")) intent.location = "Phnom Penh";
            else if (q.contains("ទួលគោក") || q.contains("toul kork")) intent.location = "Toul Kork";
            else if (q.contains("សែនសុខ") || q.contains("sen sok")) intent.location = "Sen Sok";
            else if (q.contains("សៀមរាប") || q.contains("siem reap")) intent.location = "Siem Reap";
            else if (q.contains("បាត់ដំបង") || q.contains("battambang")) intent.location = "Battambang";
        }

        StringBuilder sb = new StringBuilder("AI Filter Intent: ");
        if (intent.category != null) sb.append("Category=").append(intent.category).append(" | ");
        if (intent.condition != null) sb.append("Condition=").append(intent.condition).append(" | ");
        if (intent.maxPrice != null) sb.append("MaxPrice=$").append(intent.maxPrice).append(" | ");
        if (intent.location != null) sb.append("Location=").append(intent.location).append(" | ");
        intent.summary = sb.toString();

        return intent;
    }
}
