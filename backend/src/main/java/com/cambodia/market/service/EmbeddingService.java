package com.cambodia.market.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;

@Service
public class EmbeddingService {

    private static final Logger log = LoggerFactory.getLogger(EmbeddingService.class);

    @Value("${app.ai.embedding-provider:local}")
    private String embeddingProvider;

    @Value("${app.ai.api-key:}")
    private String apiKey;

    public static final int VECTOR_DIMENSION = 768;

    public float[] generateEmbedding(String text) {
        if (text == null || text.isBlank()) {
            return new float[VECTOR_DIMENSION];
        }
        return computeSemanticEmbedding(text);
    }

    private float[] computeSemanticEmbedding(String text) {
        float[] embedding = new float[VECTOR_DIMENSION];
        String normalized = text.toLowerCase().trim();

        // 1. Word tokenization
        String[] words = normalized.split("[\\s,./\\-_|()]+");
        for (String word : words) {
            if (word.length() < 2) continue;
            applyTokenHash(word, embedding, 1.0f);
        }

        // 2. Character 3-grams for morphological/Khmer syllable matching
        for (int i = 0; i <= normalized.length() - 3; i++) {
            String tri = normalized.substring(i, i + 3);
            applyTokenHash(tri, embedding, 0.4f);
        }

        // 3. Domain semantic boosting for market terms
        boostDomainKeywords(normalized, embedding);

        // 4. L2 Normalization (Unit vector for Cosine Similarity)
        normalizeL2(embedding);

        return embedding;
    }

    private void applyTokenHash(String token, float[] embedding, float weight) {
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] hash = md.digest(token.getBytes(StandardCharsets.UTF_8));
            for (int i = 0; i < hash.length - 1; i += 2) {
                int index = (Math.abs((hash[i] << 8) | (hash[i + 1] & 0xFF))) % VECTOR_DIMENSION;
                float sign = ((hash[i] & 1) == 0) ? 1.0f : -1.0f;
                embedding[index] += sign * weight;
            }
        } catch (Exception e) {
            int idx = Math.abs(token.hashCode()) % VECTOR_DIMENSION;
            embedding[idx] += weight;
        }
    }

    private void boostDomainKeywords(String text, float[] embedding) {
        String[][] clusters = {
            {"iphone", "apple", "អាយហ្វូន", "ios"},
            {"samsung", "galaxy", "សាំស៊ុង"},
            {"dream", "honda", "ដ្រីម", "ហុងដា", "scopy", "click", "moto", "ម៉ូតូ"},
            {"car", "prius", "toyota", "lexus", "ឡាន", "រថយន្ត"},
            {"house", "rent", "room", "apartment", "បន្ទប់ជួល", "ផ្ទះជួល", "ខុនដូ", "condo"},
            {"used", "secondhand", "second hand", "មួយទឹក", "ជជុះ", "មួយតឹក"},
            {"new", "box", "ថ្មី", "កេះ", "ប្រអប់"},
            {"phnom penh", "phnompenh", "ភ្នំពេញ", "toul kork", "ទួលគោក", "sen sok", "សែនសុខ"}
        };

        for (int c = 0; c < clusters.length; c++) {
            for (String synonym : clusters[c]) {
                if (text.contains(synonym)) {
                    int baseIdx = (c * 80) % VECTOR_DIMENSION;
                    for (int k = 0; k < 10; k++) {
                        embedding[(baseIdx + k) % VECTOR_DIMENSION] += 2.5f;
                    }
                }
            }
        }
    }

    private void normalizeL2(float[] vector) {
        double sumSq = 0.0;
        for (float v : vector) {
            sumSq += v * v;
        }
        if (sumSq > 1e-9) {
            float norm = (float) Math.sqrt(sumSq);
            for (int i = 0; i < vector.length; i++) {
                vector[i] /= norm;
            }
        }
    }
}
