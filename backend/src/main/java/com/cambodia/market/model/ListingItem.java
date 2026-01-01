package com.cambodia.market.model;

import java.math.BigDecimal;
import java.time.OffsetDateTime;

public class ListingItem {

    private String id;
    private String fingerprintHash; // Deduplication hash: MD5(phone + title + price)
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
    private String postedDate; // "Today, 11:20 AM", "Yesterday, 3:45 PM"

    // Structured Entity Extraction fields (LLM / NLP Parser)
    private String brand;
    private String modelName;
    private String storageCapacity;
    private int duplicateHitCount = 1;

    private float[] embedding;
    private String rawPayload;
    private OffsetDateTime createdAt;
    private OffsetDateTime updatedAt;

    public ListingItem() {
        this.createdAt = OffsetDateTime.now();
        this.updatedAt = OffsetDateTime.now();
    }

    public ListingItem(String id, String fingerprintHash, String title, String description,
                       ItemCategory category, ItemCondition condition, BigDecimal priceUsd,
                       BigDecimal originalPrice, String originalCurrency, String location,
                       SourcePlatform platform, String sourceUrl, String imageUrl,
                       String contactPhone, String brand, String modelName,
                       String storageCapacity, float[] embedding, String rawPayload) {
        this.id = id;
        this.fingerprintHash = fingerprintHash;
        this.title = title;
        this.description = description;
        this.category = category;
        this.condition = condition;
        this.priceUsd = priceUsd;
        this.originalPrice = originalPrice;
        this.originalCurrency = originalCurrency;
        this.location = location;
        this.platform = platform;
        this.sourceUrl = sourceUrl;
        this.imageUrl = imageUrl;
        this.contactPhone = contactPhone;
        this.brand = brand;
        this.modelName = modelName;
        this.storageCapacity = storageCapacity;
        this.duplicateHitCount = 1;
        this.embedding = embedding;
        this.rawPayload = rawPayload;
        this.createdAt = OffsetDateTime.now();
        this.updatedAt = OffsetDateTime.now();
    }

    public void incrementDuplicateCount() {
        this.duplicateHitCount++;
        this.updatedAt = OffsetDateTime.now();
    }

    // Getters and Setters
    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getFingerprintHash() { return fingerprintHash; }
    public void setFingerprintHash(String fingerprintHash) { this.fingerprintHash = fingerprintHash; }

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

    public String getPostedDate() { return postedDate; }
    public void setPostedDate(String postedDate) { this.postedDate = postedDate; }

    public String getBrand() { return brand; }
    public void setBrand(String brand) { this.brand = brand; }

    public String getModelName() { return modelName; }
    public void setModelName(String modelName) { this.modelName = modelName; }

    public String getStorageCapacity() { return storageCapacity; }
    public void setStorageCapacity(String storageCapacity) { this.storageCapacity = storageCapacity; }

    public int getDuplicateHitCount() { return duplicateHitCount; }
    public void setDuplicateHitCount(int duplicateHitCount) { this.duplicateHitCount = duplicateHitCount; }

    public float[] getEmbedding() { return embedding; }
    public void setEmbedding(float[] embedding) { this.embedding = embedding; }

    public String getRawPayload() { return rawPayload; }
    public void setRawPayload(String rawPayload) { this.rawPayload = rawPayload; }

    public OffsetDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(OffsetDateTime createdAt) { this.createdAt = createdAt; }

    public OffsetDateTime getUpdatedAt() { return updatedAt; }
    public void setUpdatedAt(OffsetDateTime updatedAt) { this.updatedAt = updatedAt; }
}
