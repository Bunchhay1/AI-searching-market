import re

with open('frontend/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS styles
css_target = "        .item-card {"
spectrum_css = """        /* ─── SMART AI PRICE & MODEL SPECTRUM STYLES ─── */
        .tier-mix-filter-bar {
            background: rgba(15, 23, 42, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 10px 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 18px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }

        .tier-pill-btn {
            background: rgba(30, 41, 59, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.12);
            color: #cbd5e1;
            padding: 7px 14px;
            border-radius: 999px;
            font-size: 0.82rem;
            font-weight: 700;
            cursor: pointer;
            font-family: inherit;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s ease;
        }

        .tier-pill-btn:hover {
            border-color: rgba(255, 255, 255, 0.3);
            transform: translateY(-1px);
        }

        .tier-pill-btn.active {
            background: linear-gradient(135deg, #3b82f6, #2563eb);
            border-color: #60a5fa;
            color: #ffffff;
            box-shadow: 0 2px 10px rgba(59, 130, 246, 0.4);
        }

        .tier-pill-btn.tpill-cheap.active {
            background: linear-gradient(135deg, #10b981, #059669);
            border-color: #34d399;
            color: #ffffff;
            box-shadow: 0 2px 10px rgba(16, 185, 129, 0.4);
        }

        .tier-pill-btn.tpill-fair.active {
            background: linear-gradient(135deg, #f59e0b, #d97706);
            border-color: #fbbf24;
            color: #ffffff;
            box-shadow: 0 2px 10px rgba(245, 158, 11, 0.4);
        }

        .tier-pill-btn.tpill-expensive.active {
            background: linear-gradient(135deg, #8b5cf6, #7c3aed);
            border-color: #a78bfa;
            color: #ffffff;
            box-shadow: 0 2px 10px rgba(139, 92, 246, 0.4);
        }

        .tpill-count {
            background: rgba(0, 0, 0, 0.3);
            padding: 2px 7px;
            border-radius: 999px;
            font-size: 0.74rem;
        }

        .spectrum-container {
            background: rgba(15, 23, 42, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            padding: 16px;
            margin-bottom: 20px;
        }

        .spectrum-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 14px;
            margin-top: 12px;
        }

        .spectrum-card {
            border-radius: 12px;
            padding: 14px 16px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: transform 0.2s, border-color 0.2s;
        }

        .spectrum-card:hover {
            transform: translateY(-2px);
        }

        .spectrum-card-cheap {
            border: 1px solid rgba(16, 185, 129, 0.45);
            background: linear-gradient(180deg, rgba(16, 185, 129, 0.08) 0%, rgba(15, 23, 42, 0.85) 100%);
        }

        .spectrum-card-fair {
            border: 1px solid rgba(245, 158, 11, 0.45);
            background: linear-gradient(180deg, rgba(245, 158, 11, 0.08) 0%, rgba(15, 23, 42, 0.85) 100%);
        }

        .spectrum-card-expensive {
            border: 1px solid rgba(139, 92, 246, 0.45);
            background: linear-gradient(180deg, rgba(139, 92, 246, 0.08) 0%, rgba(15, 23, 42, 0.85) 100%);
        }

"""

content = content.replace(css_target, spectrum_css + css_target)
print("Injected CSS styles.")

# 2. Insert AI Spectrum Matrix and Mix Filter Bar above #results-container
target_results = '    <!-- Results Grid -->\n    <div class="results-grid" id="results-container">'

replacement_results = '''    <!-- AI SMART PRICE & MODEL SPECTRUM MATRIX (CHEAP vs FAIR vs EXPENSIVE) -->
    <div id="ai-spectrum-container" class="spectrum-container" style="display: none;">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="font-size: 1.3rem;">📊</span>
                <div>
                    <h3 style="margin: 0; font-size: 1.05rem; color: #fde68a; font-weight: 800;">
                        តារាងវិភាគកម្រិតតម្លៃ & ម៉ូដែល AI (Smart Price & Model Spectrum)
                    </h3>
                    <div style="font-size: 0.8rem; color: #94a3b8;" id="spectrum-subtitle">
                        ការបែងចែកច្បាស់លាស់រវាងជម្រើសធូរថ្លៃ (Budget Deals) និងជម្រើសកម្រិតខ្ពស់ (Premium Flagships)
                    </div>
                </div>
            </div>
            <span class="tag" style="background: rgba(59, 130, 246, 0.2); border: 1px solid rgba(59, 130, 246, 0.45); color: #60a5fa; font-size: 0.76rem; font-weight: 700;">
                🧠 វិភាគដោយ AI ស្វ័យប្រវត្តិ
            </span>
        </div>
        <div class="spectrum-grid" id="spectrum-grid-cards">
            <!-- Rendered dynamically by JavaScript -->
        </div>
    </div>

    <!-- INTERACTIVE PRICE MIX FILTER BAR (1-Click Switcher) -->
    <div class="tier-mix-filter-bar" id="price-mix-filter-bar" style="display: none;">
        <div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
            <span style="font-size: 0.84rem; color: #94a3b8; font-weight: 700; margin-right: 2px;">🔀 តម្រៀបតម្លៃ:</span>
            <button class="tier-pill-btn active" id="tpill-all" onclick="filterByPriceTier('ALL', this)">
                🌐 ទាំងអស់ (Mix All) <span class="tpill-count" id="tcnt-all">0</span>
            </button>
            <button class="tier-pill-btn tpill-cheap" id="tpill-cheap" onclick="filterByPriceTier('CHEAP', this)">
                ⚡ ជម្រើសធូរថ្លៃ (Budget Deals) <span class="tpill-count" id="tcnt-cheap">0</span>
            </button>
            <button class="tier-pill-btn tpill-fair" id="tpill-fair" onclick="filterByPriceTier('FAIR', this)">
                ⚖️ តម្លៃទីផ្សារមធ្យម (Fair Market) <span class="tpill-count" id="tcnt-fair">0</span>
            </button>
            <button class="tier-pill-btn tpill-expensive" id="tpill-expensive" onclick="filterByPriceTier('EXPENSIVE', this)">
                💎 កម្រិតខ្ពស់ / ថ្មីកេះ (Premium & New) <span class="tpill-count" id="tcnt-expensive">0</span>
            </button>
        </div>
        <div style="font-size: 0.8rem; color: #38bdf8; font-weight: 600;" id="tier-filter-status-text">
            ⚡ បង្ហាញទំនិញចម្រុះគ្រប់កម្រិតតម្លៃ
        </div>
    </div>

    <!-- Results Grid -->
    <div class="results-grid" id="results-container">'''

content = content.replace(target_results, replacement_results)
print("Injected Spectrum Matrix and Filter Bar HTML.")

# 3. Update createItemCardHtml to include prominent tags:
# - priceTierTag (⚡ ធូរថ្លៃ / ⚖️ ទីផ្សារ / 💎 កម្រិតខ្ពស់)
# - modelYear tag (📅 ឆ្នាំ ...)
# - modelName tag (🏷️ ...)
# - seriesTrim tag (⚙️ ...)
# - portalTag with platformSiteName from 700 platforms
card_tags_target = '''                    <div class="tags-row">
                        ${platformTag}
                        ${portalBadge}
                        ${recencyTag}
                        ${item.conditionBadge ? `<span class="tag" style="background: ${item.conditionGrade === 'NEW_100' ? 'rgba(52, 211, 153, 0.2)' : (item.conditionGrade === 'LIKE_NEW_99' ? 'rgba(56, 189, 248, 0.2)' : 'rgba(148, 163, 184, 0.2)')}; border: 1px solid ${item.conditionGrade === 'NEW_100' ? 'rgba(52, 211, 153, 0.45)' : (item.conditionGrade === 'LIKE_NEW_99' ? 'rgba(56, 189, 248, 0.45)' : 'rgba(148, 163, 184, 0.4)')}; color: ${item.conditionGrade === 'NEW_100' ? '#6ee7b7' : (item.conditionGrade === 'LIKE_NEW_99' ? '#7dd3fc' : '#cbd5e1')}; font-weight: 700;">${item.conditionBadge}</span>` : ''}
                        ${item.isSmartCheap ? `<span class="tag" style="background: linear-gradient(135deg, rgba(245, 158, 11, 0.25), rgba(239, 68, 68, 0.25)); border: 1px solid rgba(245, 158, 11, 0.55); color: #fde68a; font-weight: 800;">⚡ តម្លៃធូរ (Smart Deal)</span>` : ''}
                        ${evalBadge}
                        ${scamTag}
                        ${dedupTag}
                        ${item.modelYear ? `<span class="tag" style="background: rgba(59, 130, 246, 0.2); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.4); font-weight: 700;">📅 ឆ្នាំ ${item.modelYear}</span>` : ''}
                        ${item.seriesTrim ? `<span class="tag" style="background: rgba(168, 85, 247, 0.2); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.4); font-weight: 700;">⚙️ ${item.seriesTrim}</span>` : ''}
                        <span class="tag tag-score">🎯 AI: ${scorePercent}%</span>
                    </div>'''

card_tags_new = '''                    <div class="tags-row">
                        <!-- Smart AI Price Tier Badge -->
                        ${item.priceTier === 'CHEAP' 
                            ? `<span class="tag" style="background: rgba(16, 185, 129, 0.25); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.6); font-weight: 800;">⚡ ធូរថ្លៃ / Budget Deal</span>`
                            : (item.priceTier === 'EXPENSIVE' 
                                ? `<span class="tag" style="background: rgba(139, 92, 246, 0.25); color: #c4b5fd; border: 1px solid rgba(139, 92, 246, 0.6); font-weight: 800;">💎 កម្រិតខ្ពស់ / Flagship Spec</span>`
                                : `<span class="tag" style="background: rgba(245, 158, 11, 0.22); color: #fde68a; border: 1px solid rgba(245, 158, 11, 0.55); font-weight: 800;">⚖️ តម្លៃទីផ្សារ / Fair Market</span>`
                            )
                        }
                        <!-- Detail Model & Year Badges -->
                        ${item.modelYear ? `<span class="tag" style="background: rgba(59, 130, 246, 0.22); color: #93c5fd; border: 1px solid rgba(59, 130, 246, 0.5); font-weight: 800;">📅 ឆ្នាំ ${item.modelYear}</span>` : ''}
                        ${item.modelName ? `<span class="tag" style="background: rgba(236, 72, 153, 0.2); color: #f472b6; border: 1px solid rgba(236, 72, 153, 0.45); font-weight: 700;">🏷️ ${item.modelName}</span>` : ''}
                        ${item.seriesTrim ? `<span class="tag" style="background: rgba(168, 85, 247, 0.22); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.5); font-weight: 700;">⚙️ ${item.seriesTrim}</span>` : ''}
                        
                        <!-- Verified Platform from 700 Portals -->
                        <span class="tag" style="background: rgba(245, 158, 11, 0.18); border: 1px solid rgba(245, 158, 11, 0.45); color: #fde68a; font-weight: 700;">
                            🌐 ${item.platformSiteName || portalName || 'វិបសាយផ្លូវការ'}
                        </span>
                        ${item.conditionBadge ? `<span class="tag" style="background: ${item.conditionGrade === 'NEW_100' ? 'rgba(52, 211, 153, 0.2)' : (item.conditionGrade === 'LIKE_NEW_99' ? 'rgba(56, 189, 248, 0.2)' : 'rgba(148, 163, 184, 0.2)')}; border: 1px solid ${item.conditionGrade === 'NEW_100' ? 'rgba(52, 211, 153, 0.45)' : (item.conditionGrade === 'LIKE_NEW_99' ? 'rgba(56, 189, 248, 0.45)' : 'rgba(148, 163, 184, 0.4)')}; color: ${item.conditionGrade === 'NEW_100' ? '#6ee7b7' : (item.conditionGrade === 'LIKE_NEW_99' ? '#7dd3fc' : '#cbd5e1')}; font-weight: 700;">${item.conditionBadge}</span>` : ''}
                        ${evalBadge}
                        ${recencyTag}
                        <span class="tag tag-score">🎯 AI: ${scorePercent}%</span>
                    </div>'''

content = content.replace(card_tags_target, card_tags_new)
print("Updated Card tags with Model, Year, Platform & Price Tier.")

# 4. Add JavaScript logic for Price Tier Filtering and Spectrum Rendering
js_hook = "let selectedPlatform = \"\";"

new_js_logic = """let selectedPlatform = "";
    let currentPriceTierFilter = "ALL";
    let latestPriceModelSpectrum = null;

    function filterByPriceTier(tier, btnElem) {
        currentPriceTierFilter = tier;
        document.querySelectorAll(".tier-pill-btn").forEach(b => b.classList.remove("active"));
        if (btnElem) btnElem.classList.add("active");

        const statusEl = document.getElementById("tier-filter-status-text");
        if (statusEl) {
            if (tier === 'CHEAP') {
                statusEl.innerHTML = "⚡ កំពុងបង្ហាញជម្រើសធូរថ្លៃបំផុត (Budget Deals)";
                statusEl.style.color = "#34d399";
            } else if (tier === 'FAIR') {
                statusEl.innerHTML = "⚖️ កំពុងបង្ហាញជម្រើសតម្លៃទីផ្សារមធ្យម (Fair Market)";
                statusEl.style.color = "#fde68a";
            } else if (tier === 'EXPENSIVE') {
                statusEl.innerHTML = "💎 កំពុងបង្ហាញជម្រើសកម្រិតខ្ពស់ & ថ្មីកេះ (Premium & New)";
                statusEl.style.color = "#c084fc";
            } else {
                statusEl.innerHTML = "🌐 កំពុងបង្ហាញទំនិញចម្រុះគ្រប់កម្រិតតម្លៃ (Mix All)";
                statusEl.style.color = "#38bdf8";
            }
        }

        applyClientTierFilter();
    }

    function applyClientTierFilter() {
        const cards = document.querySelectorAll(".item-card");
        let visibleCount = 0;
        cards.forEach(card => {
            const cardTier = card.getAttribute("data-price-tier") || "FAIR";
            if (currentPriceTierFilter === "ALL" || cardTier === currentPriceTierFilter) {
                card.style.display = "";
                visibleCount++;
            } else {
                card.style.display = "none";
            }
        });
    }

    function updateTierCounts(items) {
        if (!items || !Array.isArray(items)) return;
        const c_cheap = items.filter(it => it.priceTier === 'CHEAP').length;
        const c_fair = items.filter(it => it.priceTier === 'FAIR' || !it.priceTier).length;
        const c_exp = items.filter(it => it.priceTier === 'EXPENSIVE').length;

        const elAll = document.getElementById("tcnt-all");
        const elCheap = document.getElementById("tcnt-cheap");
        const elFair = document.getElementById("tcnt-fair");
        const elExp = document.getElementById("tcnt-expensive");
        const filterBar = document.getElementById("price-mix-filter-bar");

        if (elAll) elAll.innerText = items.length;
        if (elCheap) elCheap.innerText = c_cheap;
        if (elFair) elFair.innerText = c_fair;
        if (elExp) elExp.innerText = c_exp;
        if (filterBar) filterBar.style.display = "flex";
    }

    function renderPriceModelSpectrum(spectrum) {
        if (!spectrum || !spectrum.hasSpectrum) return;
        latestPriceModelSpectrum = spectrum;
        const container = document.getElementById("ai-spectrum-container");
        const grid = document.getElementById("spectrum-grid-cards");
        if (!container || !grid) return;

        const c = spectrum.cheapTier || {};
        const f = spectrum.fairTier || {};
        const e = spectrum.expensiveTier || {};

        grid.innerHTML = `
            <!-- 1. CHEAP TIER CARD -->
            <div class="spectrum-card spectrum-card-cheap" onclick="filterByPriceTier('CHEAP', document.getElementById('tpill-cheap'))" style="cursor: pointer;">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <span style="font-weight: 800; color: #34d399; font-size: 0.95rem;">⚡ ជម្រើសធូរថ្លៃ (Budget)</span>
                        <span class="tag" style="background: rgba(16, 185, 129, 0.25); color: #34d399; font-weight: 800; font-size: 0.75rem;">${c.count || 0} មុខទំនិញ</span>
                    </div>
                    <div style="font-size: 1.35rem; font-weight: 800; color: #6ee7b7; margin-bottom: 6px;">
                        $${(c.minPrice || 0).toLocaleString()} - $${(c.maxPrice || 0).toLocaleString()}
                    </div>
                    <div style="font-size: 0.8rem; color: #94a3b8; margin-bottom: 8px;">
                        មធ្យម: <strong style="color: #34d399;">$${(c.avgPrice || 0).toLocaleString()}</strong>
                    </div>
                    <div style="font-size: 0.8rem; color: #e2e8f0; line-height: 1.5; margin-bottom: 10px;">
                        ${c.whyCheapKhmer || 'ស៊េរីឆ្នាំទាបបន្តិច ឬ Option មធ្យម (ស្អាត 95%-99%) សន្សំប្រាក់បានច្រើន'}
                    </div>
                </div>
                <div style="border-top: 1px solid rgba(16, 185, 129, 0.2); padding-top: 8px; font-size: 0.78rem; color: #a7f3d0;">
                    🎯 ${c.targetBuyerKhmer || 'សម្រាប់អ្នកចង់ចំណាយតិច'}
                </div>
            </div>

            <!-- 2. FAIR TIER CARD -->
            <div class="spectrum-card spectrum-card-fair" onclick="filterByPriceTier('FAIR', document.getElementById('tpill-fair'))" style="cursor: pointer;">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <span style="font-weight: 800; color: #fde68a; font-size: 0.95rem;">⚖️ តម្លៃទីផ្សារ (Fair Market)</span>
                        <span class="tag" style="background: rgba(245, 158, 11, 0.25); color: #fde68a; font-weight: 800; font-size: 0.75rem;">${f.count || 0} មុខទំនិញ</span>
                    </div>
                    <div style="font-size: 1.35rem; font-weight: 800; color: #fde68a; margin-bottom: 6px;">
                        $${(f.minPrice || 0).toLocaleString()} - $${(f.maxPrice || 0).toLocaleString()}
                    </div>
                    <div style="font-size: 0.8rem; color: #94a3b8; margin-bottom: 8px;">
                        មធ្យម: <strong style="color: #fde68a;">$${(f.avgPrice || 0).toLocaleString()}</strong>
                    </div>
                    <div style="font-size: 0.8rem; color: #e2e8f0; line-height: 1.5; margin-bottom: 10px;">
                        ${f.whyFairKhmer || 'គុណភាពស្អាត 99% គ្រឿងហ្ស៊ីន 100% និងតម្លៃស្តង់ដារពេញនិយម'}
                    </div>
                </div>
                <div style="border-top: 1px solid rgba(245, 158, 11, 0.2); padding-top: 8px; font-size: 0.78rem; color: #fef08a;">
                    🎯 ${f.targetBuyerKhmer || 'ជម្រើសពេញនិយមដាច់គេ'}
                </div>
            </div>

            <!-- 3. EXPENSIVE TIER CARD -->
            <div class="spectrum-card spectrum-card-expensive" onclick="filterByPriceTier('EXPENSIVE', document.getElementById('tpill-expensive'))" style="cursor: pointer;">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <span style="font-weight: 800; color: #c4b5fd; font-size: 0.95rem;">💎 កម្រិតខ្ពស់ (Flagship Spec)</span>
                        <span class="tag" style="background: rgba(139, 92, 246, 0.25); color: #c4b5fd; font-weight: 800; font-size: 0.75rem;">${e.count || 0} មុខទំនិញ</span>
                    </div>
                    <div style="font-size: 1.35rem; font-weight: 800; color: #ddd6fe; margin-bottom: 6px;">
                        $${(e.minPrice || 0).toLocaleString()} - $${(e.maxPrice || 0).toLocaleString()}
                    </div>
                    <div style="font-size: 0.8rem; color: #94a3b8; margin-bottom: 8px;">
                        មធ្យម: <strong style="color: #c4b5fd;">$${(e.avgPrice || 0).toLocaleString()}</strong>
                    </div>
                    <div style="font-size: 0.8rem; color: #e2e8f0; line-height: 1.5; margin-bottom: 10px;">
                        ${e.whyExpensiveKhmer || 'ស៊េរីឆ្នាំចុងក្រោយ ថ្មីកេះ 100% Option ពេញ ឬធានាផ្លូវការ'}
                    </div>
                </div>
                <div style="border-top: 1px solid rgba(139, 92, 246, 0.2); padding-top: 8px; font-size: 0.78rem; color: #e9d5ff;">
                    🎯 ${e.targetBuyerKhmer || 'សម្រាប់អ្នកចង់បានគុណភាពល្អបំផុត'}
                </div>
            </div>
        `;

        container.style.display = "block";
    }
"""

content = content.replace(js_hook, new_js_logic)
print("Injected JS logic for filterByPriceTier and renderPriceModelSpectrum.")

# 5. Attach data-price-tier attribute to .item-card element in createItemCardHtml
card_class_target = '<div class="item-card ${isAnimated ? \'animated-drop\' : \'\'}">'
card_class_new = '<div class="item-card ${isAnimated ? \'animated-drop\' : \'\'}" data-price-tier="${item.priceTier || \'FAIR\'}">'
content = content.replace(card_class_target, card_class_new)

# 6. Call updateTierCounts and renderPriceModelSpectrum in performSearch or render pipeline
# Let's find where agent insights are handled
insights_hook = "renderAgentInsights(data);"
insights_replacement = """renderAgentInsights(data);
                if (data.priceModelSpectrum) {
                    renderPriceModelSpectrum(data.priceModelSpectrum);
                }"""
content = content.replace(insights_hook, insights_replacement)

# When items arrive, call updateTierCounts(currentItems)
render_items_hook = "renderSearchResults(currentItems);"
if render_items_hook in content:
    content = content.replace(render_items_hook, "renderSearchResults(currentItems);\n        updateTierCounts(currentItems);")

# Also on stream completion
stream_hook = "updateTierCounts(currentItems);"

with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated frontend/index.html with Smart Spectrum UI and Price Mix Filter!")
