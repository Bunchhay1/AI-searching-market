package com.cambodia.market.dto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import java.io.Serializable;
import java.math.BigDecimal;

@JsonIgnoreProperties(ignoreUnknown = true)
public class RawListingDto implements Serializable {
    private String id;
    private String title;
    private String rawDescription;
    private String category;
    private String rawPrice;
    private BigDecimal parsedPrice;
    private String currency;
    private String condition;
    private String location;
    private String platform;
    private String sourceUrl;
    private String imageUrl;
    private String contactPhone;
    private String directChatUrl;
    private String postedDate; // "Today, 10:45 AM", "Yesterday, 3:20 PM"

    public RawListingDto() {}

    public static Builder builder() {
        return new Builder();
    }

    public static class Builder {
        private final RawListingDto dto = new RawListingDto();

        public Builder id(String id) { dto.id = id; return this; }
        public Builder title(String title) { dto.title = title; return this; }
        public Builder rawDescription(String rawDescription) { dto.rawDescription = rawDescription; return this; }
        public Builder category(String category) { dto.category = category; return this; }
        public Builder rawPrice(String rawPrice) { dto.rawPrice = rawPrice; return this; }
        public Builder parsedPrice(BigDecimal parsedPrice) { dto.parsedPrice = parsedPrice; return this; }
        public Builder currency(String currency) { dto.currency = currency; return this; }
        public Builder condition(String condition) { dto.condition = condition; return this; }
        public Builder location(String location) { dto.location = location; return this; }
        public Builder platform(String platform) { dto.platform = platform; return this; }
        public Builder sourceUrl(String sourceUrl) { dto.sourceUrl = sourceUrl; return this; }
        public Builder imageUrl(String imageUrl) { dto.imageUrl = imageUrl; return this; }
        public Builder contactPhone(String contactPhone) { dto.contactPhone = contactPhone; return this; }
        public Builder directChatUrl(String directChatUrl) { dto.directChatUrl = directChatUrl; return this; }
        public Builder postedDate(String postedDate) { dto.postedDate = postedDate; return this; }

        public RawListingDto build() { return dto; }
    }

    // Getters and Setters
    public String getId() { return id; }
    public void setId(String id) { this.id = id; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getRawDescription() { return rawDescription; }
    public void setRawDescription(String rawDescription) { this.rawDescription = rawDescription; }
    public String getCategory() { return category; }
    public void setCategory(String category) { this.category = category; }
    public String getRawPrice() { return rawPrice; }
    public void setRawPrice(String rawPrice) { this.rawPrice = rawPrice; }
    public BigDecimal getParsedPrice() { return parsedPrice; }
    public void setParsedPrice(BigDecimal parsedPrice) { this.parsedPrice = parsedPrice; }
    public String getCurrency() { return currency; }
    public void setCurrency(String currency) { this.currency = currency; }
    public String getCondition() { return condition; }
    public void setCondition(String condition) { this.condition = condition; }
    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }
    public String getPlatform() { return platform; }
    public void setPlatform(String platform) { this.platform = platform; }
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
}
