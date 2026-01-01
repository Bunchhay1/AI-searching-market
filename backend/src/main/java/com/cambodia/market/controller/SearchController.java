package com.cambodia.market.controller;

import com.cambodia.market.dto.SearchRequest;
import com.cambodia.market.dto.SearchResponse;
import com.cambodia.market.model.ItemCategory;
import com.cambodia.market.model.ItemCondition;
import com.cambodia.market.model.SourcePlatform;
import com.cambodia.market.service.LiveMarketSearchEngine;
import com.cambodia.market.service.SearchService;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.method.annotation.SseEmitter;

import java.math.BigDecimal;

@RestController
@RequestMapping("/api/v1/search")
@CrossOrigin(origins = "*")
public class SearchController {

    private final SearchService searchService;
    private final LiveMarketSearchEngine liveMarketSearchEngine;

    public SearchController(SearchService searchService, LiveMarketSearchEngine liveMarketSearchEngine) {
        this.searchService = searchService;
        this.liveMarketSearchEngine = liveMarketSearchEngine;
    }

    @GetMapping(value = "/stream", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public SseEmitter streamSearch(@RequestParam(name = "q", defaultValue = "") String query) {
        return liveMarketSearchEngine.streamLiveSearch(query);
    }

    @GetMapping
    public ResponseEntity<SearchResponse> searchGet(
            @RequestParam(name = "q", required = false, defaultValue = "") String query,
            @RequestParam(name = "category", required = false) ItemCategory category,
            @RequestParam(name = "condition", required = false) ItemCondition condition,
            @RequestParam(name = "minPrice", required = false) BigDecimal minPrice,
            @RequestParam(name = "maxPrice", required = false) BigDecimal maxPrice,
            @RequestParam(name = "location", required = false) String location,
            @RequestParam(name = "platform", required = false) SourcePlatform platform,
            @RequestParam(name = "sortBy", required = false, defaultValue = "PRICE_ASC") String sortBy,
            @RequestParam(name = "limit", required = false, defaultValue = "20") Integer limit
    ) {
        SearchRequest req = SearchRequest.builder()
                .query(query)
                .category(category)
                .condition(condition)
                .minPrice(minPrice)
                .maxPrice(maxPrice)
                .location(location)
                .platform(platform)
                .sortBy(sortBy)
                .limit(limit)
                .build();

        return ResponseEntity.ok(searchService.search(req));
    }

    @PostMapping
    public ResponseEntity<SearchResponse> searchPost(@RequestBody SearchRequest request) {
        return ResponseEntity.ok(searchService.search(request));
    }
}
