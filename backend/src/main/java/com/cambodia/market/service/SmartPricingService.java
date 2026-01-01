package com.cambodia.market.service;

import com.cambodia.market.model.ListingItem;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class SmartPricingService {

    private static final Logger log = LoggerFactory.getLogger(SmartPricingService.class);

    public static class PriceAnalysisResult {
        private final BigDecimal fairMarketValueUsd;
        private final BigDecimal minUsd;
        private final BigDecimal maxUsd;
        private final int sampleSize;
        private final int outliersCount;

        public PriceAnalysisResult(BigDecimal fairMarketValueUsd, BigDecimal minUsd, BigDecimal maxUsd, int sampleSize, int outliersCount) {
            this.fairMarketValueUsd = fairMarketValueUsd;
            this.minUsd = minUsd;
            this.maxUsd = maxUsd;
            this.sampleSize = sampleSize;
            this.outliersCount = outliersCount;
        }

        public BigDecimal getFairMarketValueUsd() { return fairMarketValueUsd; }
        public BigDecimal getMinUsd() { return minUsd; }
        public BigDecimal getMaxUsd() { return maxUsd; }
        public int getSampleSize() { return sampleSize; }
        public int getOutliersCount() { return outliersCount; }
    }

    /**
     * Phase 6: Outlier Detection using Interquartile Range (IQR Method)
     * Filters out scam/spam prices (e.g. iPhone 13 for $50) and calculates Fair Market Value.
     */
    public PriceAnalysisResult calculateMarketIntelligence(List<ListingItem> items) {
        if (items == null || items.isEmpty()) {
            return new PriceAnalysisResult(BigDecimal.ZERO, BigDecimal.ZERO, BigDecimal.ZERO, 0, 0);
        }

        List<Double> prices = items.stream()
                .map(i -> i.getPriceUsd().doubleValue())
                .sorted()
                .collect(Collectors.toList());

        if (prices.size() < 4) {
            double avg = prices.stream().mapToDouble(Double::doubleValue).average().orElse(0.0);
            return new PriceAnalysisResult(
                    BigDecimal.valueOf(Math.round(avg * 100.0) / 100.0),
                    BigDecimal.valueOf(prices.get(0)),
                    BigDecimal.valueOf(prices.get(prices.size() - 1)),
                    prices.size(),
                    0
            );
        }

        // Compute Q1, Q3, and IQR
        double q1 = getPercentile(prices, 25);
        double q3 = getPercentile(prices, 75);
        double iqr = q3 - q1;
        double lowerBound = Math.max(10.0, q1 - (1.5 * iqr)); // minimum realistic price floor
        double upperBound = q3 + (1.5 * iqr);

        List<Double> validPrices = new ArrayList<>();
        int outliers = 0;

        for (Double p : prices) {
            if (p < lowerBound || p > upperBound) {
                outliers++;
                log.info("⚠️ [IQR Outlier Detected] Price ${} is outside valid market range [${} - ${}]", p, lowerBound, upperBound);
            } else {
                validPrices.add(p);
            }
        }

        if (validPrices.isEmpty()) {
            validPrices = prices; // fallback
        }

        double fairMarketValue = validPrices.stream().mapToDouble(Double::doubleValue).average().orElse(0.0);
        Collections.sort(validPrices);

        return new PriceAnalysisResult(
                BigDecimal.valueOf(Math.round(fairMarketValue * 100.0) / 100.0),
                BigDecimal.valueOf(validPrices.get(0)),
                BigDecimal.valueOf(validPrices.get(validPrices.size() - 1)),
                items.size(),
                outliers
        );
    }

    /**
     * Determines whether an individual item is a Great Deal, Fair Price, Overpriced, or Outlier
     */
    public String evaluatePriceStatus(BigDecimal itemPrice, BigDecimal fairMarketValue) {
        if (itemPrice == null || fairMarketValue == null || fairMarketValue.compareTo(BigDecimal.ZERO) == 0) {
            return "FAIR_PRICE";
        }
        double price = itemPrice.doubleValue();
        double fair = fairMarketValue.doubleValue();

        // If price is unrealistically low (> 65% below market), flag as potential scam/outlier
        if (price < fair * 0.35) {
            return "SUSPICIOUS_OUTLIER";
        }
        // 10% to 50% below market value = GREAT_DEAL
        if (price <= fair * 0.90) {
            return "GREAT_DEAL";
        }
        // Within 10%
        if (price <= fair * 1.12) {
            return "FAIR_PRICE";
        }
        return "OVERPRICED";
    }

    /**
     * Levenshtein Distance algorithm for cross-platform duplicate detection
     */
    public int calculateLevenshteinDistance(String s1, String s2) {
        if (s1 == null || s2 == null) return 100;
        int[][] dp = new int[s1.length() + 1][s2.length() + 1];

        for (int i = 0; i <= s1.length(); i++) dp[i][0] = i;
        for (int j = 0; j <= s2.length(); j++) dp[0][j] = j;

        for (int i = 1; i <= s1.length(); i++) {
            for (int j = 1; j <= s2.length(); j++) {
                int cost = (s1.charAt(i - 1) == s2.charAt(j - 1)) ? 0 : 1;
                dp[i][j] = Math.min(Math.min(
                                dp[i - 1][j] + 1,
                                dp[i][j - 1] + 1),
                        dp[i - 1][j - 1] + cost);
            }
        }
        return dp[s1.length()][s2.length()];
    }

    private double getPercentile(List<Double> sortedList, double percentile) {
        int index = (int) Math.ceil((percentile / 100.0) * sortedList.size()) - 1;
        index = Math.max(0, Math.min(sortedList.size() - 1, index));
        return sortedList.get(index);
    }
}
