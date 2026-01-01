package com.cambodia.market.dto;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

public class SearchResponse {
    private String originalQuery;
    private String parsedIntentSummary;
    private Long totalResults = 0L;
    private BigDecimal averagePriceUsd = BigDecimal.ZERO;
    private BigDecimal lowestPriceUsd = BigDecimal.ZERO;
    private BigDecimal highestPriceUsd = BigDecimal.ZERO;
    private BigDecimal smartFairMarketValue = BigDecimal.ZERO;
    private Integer outliersFilteredCount = 0;
    private List<SearchResultDto> items = new ArrayList<>();

    public SearchResponse() {}

    public static Builder builder() {
        return new Builder();
    }

    public static class Builder {
        private final SearchResponse resp = new SearchResponse();

        public Builder originalQuery(String originalQuery) { resp.originalQuery = originalQuery; return this; }
        public Builder parsedIntentSummary(String parsedIntentSummary) { resp.parsedIntentSummary = parsedIntentSummary; return this; }
        public Builder totalResults(Long totalResults) { resp.totalResults = totalResults; return this; }
        public Builder averagePriceUsd(BigDecimal averagePriceUsd) { resp.averagePriceUsd = averagePriceUsd; return this; }
        public Builder lowestPriceUsd(BigDecimal lowestPriceUsd) { resp.lowestPriceUsd = lowestPriceUsd; return this; }
        public Builder highestPriceUsd(BigDecimal highestPriceUsd) { resp.highestPriceUsd = highestPriceUsd; return this; }
        public Builder smartFairMarketValue(BigDecimal smartFairMarketValue) { resp.smartFairMarketValue = smartFairMarketValue; return this; }
        public Builder outliersFilteredCount(Integer outliersFilteredCount) { resp.outliersFilteredCount = outliersFilteredCount; return this; }
        public Builder items(List<SearchResultDto> items) { resp.items = items; return this; }

        public SearchResponse build() { return resp; }
    }

    // Getters and Setters
    public String getOriginalQuery() { return originalQuery; }
    public void setOriginalQuery(String originalQuery) { this.originalQuery = originalQuery; }
    public String getParsedIntentSummary() { return parsedIntentSummary; }
    public void setParsedIntentSummary(String parsedIntentSummary) { this.parsedIntentSummary = parsedIntentSummary; }
    public Long getTotalResults() { return totalResults; }
    public void setTotalResults(Long totalResults) { this.totalResults = totalResults; }
    public BigDecimal getAveragePriceUsd() { return averagePriceUsd; }
    public void setAveragePriceUsd(BigDecimal averagePriceUsd) { this.averagePriceUsd = averagePriceUsd; }
    public BigDecimal getLowestPriceUsd() { return lowestPriceUsd; }
    public void setLowestPriceUsd(BigDecimal lowestPriceUsd) { this.lowestPriceUsd = lowestPriceUsd; }
    public BigDecimal getHighestPriceUsd() { return highestPriceUsd; }
    public void setHighestPriceUsd(BigDecimal highestPriceUsd) { this.highestPriceUsd = highestPriceUsd; }
    public BigDecimal getSmartFairMarketValue() { return smartFairMarketValue; }
    public void setSmartFairMarketValue(BigDecimal smartFairMarketValue) { this.smartFairMarketValue = smartFairMarketValue; }
    public Integer getOutliersFilteredCount() { return outliersFilteredCount; }
    public void setOutliersFilteredCount(Integer outliersFilteredCount) { this.outliersFilteredCount = outliersFilteredCount; }
    public List<SearchResultDto> getItems() { return items; }
    public void setItems(List<SearchResultDto> items) { this.items = items; }
}
