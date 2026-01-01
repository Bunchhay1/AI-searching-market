package com.cambodia.market.repository;

import com.cambodia.market.model.ItemCategory;
import com.cambodia.market.model.ItemCondition;
import com.cambodia.market.model.ListingItem;
import com.cambodia.market.model.SourcePlatform;
import org.springframework.stereotype.Repository;

import java.math.BigDecimal;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;

@Repository
public class ListingItemRepository {

    private final Map<String, ListingItem> store = new ConcurrentHashMap<>();
    private final Map<String, String> fingerprintIndex = new ConcurrentHashMap<>(); // hash -> itemId
    private final AtomicInteger duplicatesDeduplicatedCount = new AtomicInteger(0);

    public ListingItem save(ListingItem item) {
        if (item.getId() == null || item.getId().isBlank()) {
            item.setId("item_" + UUID.randomUUID().toString().replace("-", "").substring(0, 12));
        }
        store.put(item.getId(), item);
        if (item.getFingerprintHash() != null) {
            fingerprintIndex.put(item.getFingerprintHash(), item.getId());
        }
        return item;
    }

    public Optional<ListingItem> findByFingerprintHash(String hash) {
        if (hash == null) return Optional.empty();
        String id = fingerprintIndex.get(hash);
        if (id != null) {
            return Optional.ofNullable(store.get(id));
        }
        return Optional.empty();
    }

    public void incrementDuplicatesPrevented() {
        duplicatesDeduplicatedCount.incrementAndGet();
    }

    public void clearAll() {
        store.clear();
        fingerprintIndex.clear();
        duplicatesDeduplicatedCount.set(0);
    }

    public int getDuplicatesPreventedCount() {
        return duplicatesDeduplicatedCount.get();
    }

    public Optional<ListingItem> findById(String id) {
        return Optional.ofNullable(store.get(id));
    }

    public List<ListingItem> findAll() {
        return new ArrayList<>(store.values());
    }

    public long countAllListings() {
        return store.size();
    }

    public BigDecimal findAveragePriceUsd() {
        if (store.isEmpty()) return BigDecimal.ZERO;
        double avg = store.values().stream()
                .mapToDouble(i -> i.getPriceUsd().doubleValue())
                .average()
                .orElse(0.0);
        return BigDecimal.valueOf(Math.round(avg * 100.0) / 100.0);
    }

    public BigDecimal findMinPriceUsd() {
        if (store.isEmpty()) return BigDecimal.ZERO;
        return store.values().stream()
                .map(ListingItem::getPriceUsd)
                .min(BigDecimal::compareTo)
                .orElse(BigDecimal.ZERO);
    }

    public BigDecimal findMaxPriceUsd() {
        if (store.isEmpty()) return BigDecimal.ZERO;
        return store.values().stream()
                .map(ListingItem::getPriceUsd)
                .max(BigDecimal::compareTo)
                .orElse(BigDecimal.ZERO);
    }

    public static class ScoredItem {
        public final ListingItem item;
        public final double similarity;

        public ScoredItem(ListingItem item, double similarity) {
            this.item = item;
            this.similarity = similarity;
        }
    }

    public List<ScoredItem> searchSemantic(
            float[] queryVector,
            ItemCategory category,
            ItemCondition itemCondition,
            BigDecimal minPrice,
            BigDecimal maxPrice,
            String location,
            SourcePlatform platform,
            String sortBy,
            int limit
    ) {
        return store.values().stream()
                // 1. Filter Category
                .filter(i -> category == null || i.getCategory() == category)
                // 2. Filter Condition
                .filter(i -> itemCondition == null || i.getCondition() == itemCondition)
                // 3. Filter Price range
                .filter(i -> minPrice == null || i.getPriceUsd().compareTo(minPrice) >= 0)
                .filter(i -> maxPrice == null || i.getPriceUsd().compareTo(maxPrice) <= 0)
                // 4. Filter Location
                .filter(i -> location == null || location.isBlank() ||
                        (i.getLocation() != null && i.getLocation().toLowerCase().contains(location.toLowerCase())))
                // 5. Filter Platform
                .filter(i -> platform == null || i.getPlatform() == platform)
                // 6. Calculate Cosine Similarity
                .map(i -> new ScoredItem(i, calculateCosineSimilarity(queryVector, i.getEmbedding())))
                // 7. Sort
                .sorted((a, b) -> {
                    if ("PRICE_ASC".equalsIgnoreCase(sortBy)) {
                        return a.item.getPriceUsd().compareTo(b.item.getPriceUsd());
                    } else if ("PRICE_DESC".equalsIgnoreCase(sortBy)) {
                        return b.item.getPriceUsd().compareTo(a.item.getPriceUsd());
                    } else {
                        return Double.compare(b.similarity, a.similarity);
                    }
                })
                .limit(limit > 0 ? limit : 20)
                .collect(Collectors.toList());
    }

    private double calculateCosineSimilarity(float[] vecA, float[] vecB) {
        if (vecA == null || vecB == null || vecA.length != vecB.length) {
            return 0.0;
        }
        double dotProduct = 0.0;
        double normA = 0.0;
        double normB = 0.0;
        for (int i = 0; i < vecA.length; i++) {
            dotProduct += vecA[i] * vecB[i];
            normA += vecA[i] * vecA[i];
            normB += vecB[i] * vecB[i];
        }
        if (normA <= 1e-9 || normB <= 1e-9) {
            return 0.0;
        }
        return dotProduct / (Math.sqrt(normA) * Math.sqrt(normB));
    }
}
