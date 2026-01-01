package com.cambodia.market.dto;

import com.cambodia.market.model.ItemCategory;
import com.cambodia.market.model.ItemCondition;
import com.cambodia.market.model.SourcePlatform;

import java.math.BigDecimal;
import java.time.OffsetDateTime;

public class SearchResultDto {
    private String id;
    private String title;
    private String description;
    private ItemCategory category;
    private ItemCondition condition;
    private BigDecimal priceUsd;
    private BigDecimal originalPrice;
    private String originalCurrency;
    private String location;
    private SourcePlatform platform;
    private String sourceUrl;
    private String imageUrl;
    private String contactPhone;
    private String directChatUrl;

    // Structured Entity Details
    private String brand;
    private String modelName;
    private String storageCapacity;
    private int duplicateHitCount = 1;

    // Phase 6 Market Intelligence
    private String priceEvaluation = "FAIR_PRICE"; // "GREAT_DEAL", "FAIR_PRICE", "OVERPRICED", "SUSPICIOUS_OUTLIER"
    private BigDecimal fairMarketValueUsd;

    private Double similarityScore;
    private String postedDate; // "Today, 11:20 AM", "Yesterday, 3:45 PM", etc.
    private OffsetDateTime createdAt;

    public SearchResultDto() {}

    public static Builder builder() {
        return new Builder();
    }

    public static class Builder {
        private final SearchResultDto dto = new SearchResultDto();

        public Builder id(String id) { dto.id = id; return this; }
        public Builder title(String title) { dto.title = title; return this; }
        public Builder description(String description) { dto.description = description; return this; }
        public Builder category(ItemCategory category) { dto.category = category; return this; }
        public Builder condition(ItemCondition condition) { dto.condition = condition; return this; }
        public Builder priceUsd(BigDecimal priceUsd) { dto.priceUsd = priceUsd; return this; }
        public Builder originalPrice(BigDecimal originalPrice) { dto.originalPrice = originalPrice; return this; }
        public Builder originalCurrency(String originalCurrency) { dto.originalCurrency = originalCurrency; return this; }
        public Builder location(String location) { dto.location = location; return this; }
        public Builder platform(SourcePlatform platform) { dto.platform = platform; return this; }
        public Builder sourceUrl(String sourceUrl) { dto.sourceUrl = sourceUrl; return this; }
        public Builder imageUrl(String imageUrl) { dto.imageUrl = imageUrl; return this; }
        public Builder contactPhone(String contactPhone) { dto.contactPhone = contactPhone; return this; }
        public Builder directChatUrl(String directChatUrl) { dto.directChatUrl = directChatUrl; return this; }
        public Builder brand(String brand) { dto.brand = brand; return this; }
        public Builder modelName(String modelName) { dto.modelName = modelName; return this; }
        public Builder storageCapacity(String storageCapacity) { dto.storageCapacity = storageCapacity; return this; }
        public Builder duplicateHitCount(int duplicateHitCount) { dto.duplicateHitCount = duplicateHitCount; return this; }
        public Builder priceEvaluation(String priceEvaluation) { dto.priceEvaluation = priceEvaluation; return this; }
        public Builder fairMarketValueUsd(BigDecimal fairMarketValueUsd) { dto.fairMarketValueUsd = fairMarketValueUsd; return this; }
        public Builder similarityScore(Double similarityScore) { dto.similarityScore = similarityScore; return this; }
        public Builder postedDate(String postedDate) { dto.postedDate = postedDate; return this; }
        public Builder createdAt(OffsetDateTime createdAt) { dto.createdAt = createdAt; return this; }

        public SearchResultDto build() { return dto; }
    }

    // Getters and Setters
    public String getId() { return id; }
    public void setId(String id) { this.id = id; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public ItemCategory getCategory() { return category; }
    public void setCategory(ItemCategory category) { this.category = category; }
    public ItemCondition getCondition() { return condition; }
    public void setCondition(ItemCondition condition) { this.condition = condition; }
    public BigDecimal getPriceUsd() { return priceUsd; }
    public void setPriceUsd(BigDecimal priceUsd) { this.priceUsd = priceUsd; }
    public BigDecimal getOriginalPrice() { return originalPrice; }
    public void setOriginalPrice(BigDecimal originalPrice) { this.originalPrice = originalPrice; }
    public String getOriginalCurrency() { return originalCurrency; }
    public void setOriginalCurrency(String originalCurrency) { this.originalCurrency = originalCurrency; }
    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }
    public SourcePlatform getPlatform() { return platform; }
    public void setPlatform(SourcePlatform platform) { this.platform = platform; }
    public String getSourceUrl() { return sourceUrl; }
    public void setSourceUrl(String sourceUrl) { this.sourceUrl = sourceUrl; }
    public String getImageUrl() { return imageUrl; }
    public void setImageUrl(String imageUrl) { this.imageUrl = imageUrl; }
    public String getContactPhone() { return contactPhone; }
    public void setContactPhone(String contactPhone) { this.contactPhone = contactPhone; }
    public String getDirectChatUrl() { return directChatUrl; }
    public void setDirectChatUrl(String directChatUrl) { this.directChatUrl = directChatUrl; }
    public String getBrand() { return brand; }
    public void setBrand(String brand) { this.brand = brand; }
    public String getModelName() { return modelName; }
    public void setModelName(String modelName) { this.modelName = modelName; }
    public String getStorageCapacity() { return storageCapacity; }
    public void setStorageCapacity(String storageCapacity) { this.storageCapacity = storageCapacity; }
    public int getDuplicateHitCount() { return duplicateHitCount; }
    public void setDuplicateHitCount(int duplicateHitCount) { this.duplicateHitCount = duplicateHitCount; }
    public String getPriceEvaluation() { return priceEvaluation; }
    public void setPriceEvaluation(String priceEvaluation) { this.priceEvaluation = priceEvaluation; }
    public BigDecimal getFairMarketValueUsd() { return fairMarketValueUsd; }
    public void setFairMarketValueUsd(BigDecimal fairMarketValueUsd) { this.fairMarketValueUsd = fairMarketValueUsd; }
    public Double getSimilarityScore() { return similarityScore; }
    public void setSimilarityScore(Double similarityScore) { this.similarityScore = similarityScore; }
    public String getPostedDate() { return postedDate; }
    public void setPostedDate(String postedDate) { this.postedDate = postedDate; }
    public OffsetDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(OffsetDateTime createdAt) { this.createdAt = createdAt; }
}
