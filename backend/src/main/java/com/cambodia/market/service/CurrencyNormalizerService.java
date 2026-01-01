package com.cambodia.market.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

@Service
public class CurrencyNormalizerService {

    private static final Logger log = LoggerFactory.getLogger(CurrencyNormalizerService.class);

    @Value("${app.currency.khr-to-usd-rate:4100.0}")
    private double khrToUsdRate;

    private static final Pattern PRICE_NUMBER_PATTERN = Pattern.compile("([0-9]+(?:[,.][0-9]+)*)");

    public static class NormalizedPrice {
        public final BigDecimal priceUsd;
        public final BigDecimal originalPrice;
        public final String originalCurrency;

        public NormalizedPrice(BigDecimal priceUsd, BigDecimal originalPrice, String originalCurrency) {
            this.priceUsd = priceUsd;
            this.originalPrice = originalPrice;
            this.originalCurrency = originalCurrency;
        }
    }

    public String convertKhmerNumeralsToLatin(String input) {
        if (input == null) return "";
        char[] khmerDigits = {'០', '១', '២', '៣', '៤', '៥', '៦', '៧', '៨', '៩'};
        char[] latinDigits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};

        StringBuilder sb = new StringBuilder();
        for (char c : input.toCharArray()) {
            boolean replaced = false;
            for (int i = 0; i < khmerDigits.length; i++) {
                if (c == khmerDigits[i]) {
                    sb.append(latinDigits[i]);
                    replaced = true;
                    break;
                }
            }
            if (!replaced) {
                sb.append(c);
            }
        }
        return sb.toString();
    }

    public NormalizedPrice normalizePrice(String rawPriceString, BigDecimal parsedFallbackPrice, String fallbackCurrency) {
        if (parsedFallbackPrice != null && parsedFallbackPrice.compareTo(BigDecimal.ZERO) > 0) {
            String currency = (fallbackCurrency != null && !fallbackCurrency.isBlank()) ? fallbackCurrency.toUpperCase() : "USD";
            if (currency.contains("KHR") || currency.contains("៛") || currency.contains("រៀល")) {
                BigDecimal usd = parsedFallbackPrice.divide(BigDecimal.valueOf(khrToUsdRate), 2, RoundingMode.HALF_UP);
                return new NormalizedPrice(usd, parsedFallbackPrice, "KHR");
            } else {
                return new NormalizedPrice(parsedFallbackPrice, parsedFallbackPrice, "USD");
            }
        }

        if (rawPriceString == null || rawPriceString.isBlank()) {
            return new NormalizedPrice(BigDecimal.ZERO, BigDecimal.ZERO, "USD");
        }

        String cleaned = convertKhmerNumeralsToLatin(rawPriceString).trim();
        boolean isKhr = cleaned.contains("៛") || cleaned.contains("រៀល") || cleaned.toUpperCase().contains("KHR");

        Matcher matcher = PRICE_NUMBER_PATTERN.matcher(cleaned.replaceAll("\\s+", ""));
        if (matcher.find()) {
            String numStr = matcher.group(1).replace(",", "");
            try {
                BigDecimal amount = new BigDecimal(numStr);
                if (isKhr) {
                    BigDecimal usd = amount.divide(BigDecimal.valueOf(khrToUsdRate), 2, RoundingMode.HALF_UP);
                    return new NormalizedPrice(usd, amount, "KHR");
                } else {
                    return new NormalizedPrice(amount, amount, "USD");
                }
            } catch (Exception e) {
                log.warn("Failed to parse number string: {}", numStr);
            }
        }

        return new NormalizedPrice(BigDecimal.ZERO, BigDecimal.ZERO, "USD");
    }
}
