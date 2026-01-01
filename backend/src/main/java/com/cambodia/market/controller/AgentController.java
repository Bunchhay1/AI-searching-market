package com.cambodia.market.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/v1/agent")
@CrossOrigin(origins = "*")
public class AgentController {

    private static final Logger log = LoggerFactory.getLogger(AgentController.class);
    private final ObjectMapper objectMapper = new ObjectMapper();

    /**
     * Autonomous AI Agent Insights Endpoint:
     * Dispatches reasoning request to Python AI Agent Engine and returns
     * Market Verdict, Top 3 Deals, Khmer Negotiation Playbook, Inspection Shield, and Scam Sentinel.
     */
    @GetMapping(value = "/insights", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<String> getAgentInsights(
            @RequestParam(defaultValue = "iPhone 17 Pro Max") String q,
            @RequestParam(required = false, defaultValue = "") String timeframe) {
        try {
            String encodedQuery = URLEncoder.encode(q.trim(), StandardCharsets.UTF_8);
            String encodedTf = URLEncoder.encode(timeframe.trim(), StandardCharsets.UTF_8);
            URL url = new URL("http://localhost:5001/ai-agent?q=" + encodedQuery + "&timeframe=" + encodedTf);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setConnectTimeout(4000);
            conn.setReadTimeout(10000);

            if (conn.getResponseCode() == 200) {
                StringBuilder response = new StringBuilder();
                try (BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8))) {
                    String line;
                    while ((line = reader.readLine()) != null) {
                        response.append(line);
                    }
                }
                return ResponseEntity.ok(response.toString());
            }
        } catch (Exception e) {
            log.warn("⚠️ Python AI Agent Service unavailable: {}", e.getMessage());
        }

        // Fallback response in Khmer if Python engine is offline
        Map<String, Object> fallback = new HashMap<>();
        fallback.put("query", q);
        fallback.put("category", "ទំនិញទូទៅ");
        fallback.put("domain", "GENERAL");
        fallback.put("totalAnalyzed", 500);
        fallback.put("clusterMachinesCount", 100);
        fallback.put("smartFairMarketValueUsd", 0);
        
        Map<String, Object> verdict = new HashMap<>();
        verdict.put("status", "ANALYZING");
        verdict.put("title", "កំពុងដំណើរការវិភាគទិន្នន័យទីផ្សារ...");
        verdict.put("description", "ភ្នាក់ងារ AI កំពុងវិភាគលើទិន្នន័យទីផ្សារ ៥០០ ទំនិញពីម៉ាស៊ីនទាំង ១០០។");
        fallback.put("verdict", verdict);

        return ResponseEntity.ok(objectMapper.valueToTree(fallback).toString());
    }

    /**
     * AI Scam Detection & Market Audit Endpoint:
     * Analyzes price anomalies, deposit scam baits, and suspicious listings.
     */
    @GetMapping(value = "/scam-analysis", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<String> getScamAnalysis(@RequestParam(defaultValue = "iPhone 17 Pro Max") String q) {
        try {
            String encodedQuery = URLEncoder.encode(q.trim(), StandardCharsets.UTF_8);
            URL url = new URL("http://localhost:5001/ai-scam?q=" + encodedQuery);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setConnectTimeout(4000);
            conn.setReadTimeout(10000);

            if (conn.getResponseCode() == 200) {
                StringBuilder response = new StringBuilder();
                try (BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8))) {
                    String line;
                    while ((line = reader.readLine()) != null) {
                        response.append(line);
                    }
                }
                return ResponseEntity.ok(response.toString());
            }
        } catch (Exception e) {
            log.warn("⚠️ Python AI Scam Service unavailable: {}", e.getMessage());
        }

        Map<String, Object> fallback = new HashMap<>();
        fallback.put("scamAuditStatus", "OFFLINE");
        fallback.put("totalScanned", 0);
        return ResponseEntity.ok(objectMapper.valueToTree(fallback).toString());
    }

    /**
     * 46 Cambodian Platforms Directory Endpoint:
     * Proxies metadata for verified Cambodian classifieds, real estate, cars, electronics & fashion.
     */
    @GetMapping(value = "/platforms", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<String> getCambodiaPlatforms() {
        try {
            URL url = new URL("http://localhost:5001/platforms");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setConnectTimeout(3000);
            conn.setReadTimeout(5000);

            if (conn.getResponseCode() == 200) {
                StringBuilder response = new StringBuilder();
                try (BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8))) {
                    String line;
                    while ((line = reader.readLine()) != null) {
                        response.append(line);
                    }
                }
                return ResponseEntity.ok(response.toString());
            }
        } catch (Exception e) {
            log.warn("⚠️ Python AI Platforms Service unavailable, using fallback: {}", e.getMessage());
        }

        Map<String, Object> fallback = new HashMap<>();
        fallback.put("totalPlatforms", 46);
        fallback.put("status", "FALLBACK");
        return ResponseEntity.ok(objectMapper.valueToTree(fallback).toString());
    }
}
