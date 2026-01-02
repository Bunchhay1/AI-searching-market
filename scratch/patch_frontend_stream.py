import re

with open("frontend/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. In searchWithAi, reset currentPriceTierFilter and pill buttons
old_search_prep = """        const container = document.getElementById("results-container");
        container.innerHTML = "";
        streamedItems = [];
        document.getElementById("stat-count").innerText = "0";"""

new_search_prep = """        const container = document.getElementById("results-container");
        container.innerHTML = "";
        streamedItems = [];
        document.getElementById("stat-count").innerText = "0";
        currentPriceTierFilter = "ALL";
        document.querySelectorAll(".tier-pill-btn").forEach(b => b.classList.remove("active"));
        const btnAll = document.querySelector('.tier-pill-btn[onclick*="ALL"]');
        if (btnAll) btnAll.classList.add("active");"""

if old_search_prep in content:
    content = content.replace(old_search_prep, new_search_prep, 1)
    print("Updated searchWithAi prep")
else:
    print("Warning: old_search_prep not found")

# 2. In evtSource item listener, filter by currentPriceTierFilter and periodic tier count update
old_item_append = """                    if (matchesTabPlatform && matchesDropdownPlatform && matchesTimeframe && matchesCondition) {
                        const cardHtml = createCardHtml(item, streamedItems.length - 1, true);
                        const tempDiv = document.createElement("div");
                        tempDiv.innerHTML = cardHtml;
                        const cardElem = tempDiv.firstElementChild;
                        container.appendChild(cardElem);
                    }"""

new_item_append = """                    if (matchesTabPlatform && matchesDropdownPlatform && matchesTimeframe && matchesCondition) {
                        const cardHtml = createCardHtml(item, streamedItems.length - 1, true);
                        const tempDiv = document.createElement("div");
                        tempDiv.innerHTML = cardHtml;
                        const cardElem = tempDiv.firstElementChild;
                        if (currentPriceTierFilter !== "ALL" && item.priceTier !== currentPriceTierFilter) {
                            cardElem.style.display = "none";
                        }
                        container.appendChild(cardElem);
                    }

                    if (streamedItems.length % 5 === 0 || streamedItems.length < 10) {
                        updateTierCounts(streamedItems);
                    }"""

if old_item_append in content:
    content = content.replace(old_item_append, new_item_append, 1)
    print("Updated item append")
else:
    print("Warning: old_item_append not found")

# 3. In evtSource agent-insights event, call renderPriceModelSpectrum if present
old_insights_event = """            evtSource.addEventListener("agent-insights", (e) => {
                try {
                    const insights = JSON.parse(e.data);
                    renderAgentInsights(insights);
                } catch (err) {}
            });"""

new_insights_event = """            evtSource.addEventListener("agent-insights", (e) => {
                try {
                    const insights = JSON.parse(e.data);
                    renderAgentInsights(insights);
                    if (insights.priceModelSpectrum) {
                        renderPriceModelSpectrum(insights.priceModelSpectrum);
                    }
                } catch (err) {}
            });"""

if old_insights_event in content:
    content = content.replace(old_insights_event, new_insights_event, 1)
    print("Updated agent-insights event")
else:
    print("Warning: old_insights_event not found")

# 4. In evtSource complete event, call updateTierCounts and applyClientTierFilter
old_complete_event = """                if (streamStatus) streamStatus.innerText = `✅ បណ្តាញម៉ាស៊ីន AI ទាំង ១០០ បានបញ្ចប់ការស្វែងរក និងវិភាគ Real Data (${streamedItems.length} ទំនិញ)!`;
                btnText.innerHTML = 'ស្វែងរក AI';
                evtSource.close();
                currentEventSource = null;
                updatePipelineStatus();"""

new_complete_event = """                updateTierCounts(streamedItems);
                applyClientTierFilter();
                if (streamStatus) streamStatus.innerText = `✅ បណ្តាញម៉ាស៊ីន AI ទាំង ១០០ បានបញ្ចប់ការស្វែងរក និងវិភាគ Real Data (${streamedItems.length} ទំនិញ)!`;
                btnText.innerHTML = 'ស្វែងរក AI';
                evtSource.close();
                currentEventSource = null;
                updatePipelineStatus();"""

if old_complete_event in content:
    content = content.replace(old_complete_event, new_complete_event, 1)
    print("Updated complete event")
else:
    print("Warning: old_complete_event not found")

# 5. In renderResults, updateTierCounts
old_render_results = """    function renderResults(data) {
        const container = document.getElementById("results-container");
        
        document.getElementById("stat-count").innerText = data.totalResults || 0;"""

new_render_results = """    function renderResults(data) {
        const container = document.getElementById("results-container");
        streamedItems = data.items || [];
        updateTierCounts(streamedItems);
        applyClientTierFilter();
        
        document.getElementById("stat-count").innerText = data.totalResults || 0;"""

if old_render_results in content:
    content = content.replace(old_render_results, new_render_results, 1)
    print("Updated renderResults")
else:
    print("Warning: old_render_results not found")

with open("frontend/index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Finished updating frontend/index.html")
