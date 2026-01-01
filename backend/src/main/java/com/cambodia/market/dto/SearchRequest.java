package com.cambodia.market.dto;

import com.cambodia.market.model.ItemCategory;
import com.cambodia.market.model.ItemCondition;
import com.cambodia.market.model.SourcePlatform;

import java.math.BigDecimal;

public class SearchRequest {
    private String query;
    private ItemCategory category;
    private ItemCondition condition;
    private BigDecimal minPrice;
    private BigDecimal maxPrice;
    private String location;
    private SourcePlatform platform;
    private String sortBy = "PRICE_ASC";
    private Integer limit = 20;

    public SearchRequest() {}

    public static Builder builder() {
        return new Builder();
    }

    public static class Builder {
        private final SearchRequest req = new SearchRequest();

        public Builder query(String query) { req.query = query; return this; }
        public Builder category(ItemCategory category) { req.category = category; return this; }
        public Builder condition(ItemCondition condition) { req.condition = condition; return this; }
        public Builder minPrice(BigDecimal minPrice) { req.minPrice = minPrice; return this; }
        public Builder maxPrice(BigDecimal maxPrice) { req.maxPrice = maxPrice; return this; }
        public Builder location(String location) { req.location = location; return this; }
        public Builder platform(SourcePlatform platform) { req.platform = platform; return this; }
        public Builder sortBy(String sortBy) { req.sortBy = sortBy; return this; }
        public Builder limit(Integer limit) { req.limit = limit; return this; }

        public SearchRequest build() { return req; }
    }

    // Getters and Setters
    public String getQuery() { return query; }
    public void setQuery(String query) { this.query = query; }
    public ItemCategory getCategory() { return category; }
    public void setCategory(ItemCategory category) { this.category = category; }
    public ItemCondition getCondition() { return condition; }
    public void setCondition(ItemCondition condition) { this.condition = condition; }
    public BigDecimal getMinPrice() { return minPrice; }
    public void setMinPrice(BigDecimal minPrice) { this.minPrice = minPrice; }
    public BigDecimal getMaxPrice() { return maxPrice; }
    public void setMaxPrice(BigDecimal maxPrice) { this.maxPrice = maxPrice; }
    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }
    public SourcePlatform getPlatform() { return platform; }
    public void setPlatform(SourcePlatform platform) { this.platform = platform; }
    public String getSortBy() { return sortBy; }
    public void setSortBy(String sortBy) { this.sortBy = sortBy; }
    public Integer getLimit() { return limit; }
    public void setLimit(Integer limit) { this.limit = limit; }
}
