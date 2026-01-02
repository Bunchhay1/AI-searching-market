import re

with open('frontend/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update button labels
content = content.replace("🏪 ២០០ វេទិកាទីផ្សារកម្ពុជា (200 Portals)", "🏪 ៧០០ វេទិកាទីផ្សារកម្ពុជា (700 Portals)")
content = content.replace("មើលបញ្ជី ២០០ វេទិកាទីផ្សារ", "មើលបញ្ជី ៧០០ វេទិកាទីផ្សារ")
content = content.replace("បញ្ជី ២០០ វេទិកាទីផ្សារកម្ពុជាផ្លូវការ (200 Verified Cambodian Portals)", "បញ្ជី ៧០០ វេទិកាទីផ្សារ & ម៉ាកយីហោល្បីៗនៅកម្ពុជា (700 Verified Cambodian Portals & Brands)")
content = content.replace("២០០ វេទិកាផ្លូវការ", "៧០០ វេទិកាផ្លូវការ")
content = content.replace("លើ ២០០ វេទិកាឈានមុខគេនៅកម្ពុជា", "លើ ៧០០ វេទិកាឈានមុខគេនៅកម្ពុជា")

# 2. Update category pills
pills_old = '''        <div class="dir-category-pills">
            <button class="dir-pill active" onclick="setDirCategory('ALL', this)">🌐 ទាំងអស់ (All 200)</button>
            <button class="dir-pill" onclick="setDirCategory('GENERAL', this)">🛒 ទីផ្សារទូទៅ (20)</button>
            <button class="dir-pill" onclick="setDirCategory('COMPUTERS', this)">💻 កុំព្យូទ័រ & IT (20)</button>
            <button class="dir-pill" onclick="setDirCategory('PHONES', this)">📱 ទូរស័ព្ទ & Mobile (20)</button>
            <button class="dir-pill" onclick="setDirCategory('CARS', this)">🚗 រថយន្ត & គ្រឿងយន្ត (20)</button>
            <button class="dir-pill" onclick="setDirCategory('REAL_ESTATE', this)">🏠 អចលនទ្រព្យ (20)</button>
            <button class="dir-pill" onclick="setDirCategory('FASHION', this)">👗 ម៉ូដ & សម្លៀកបំពាក់ (20)</button>
            <button class="dir-pill" onclick="setDirCategory('BEAUTY', this)">💄 សម្រស់ & សុខភាព (20)</button>
            <button class="dir-pill" onclick="setDirCategory('FURNITURE', this)">🛋️ គ្រឿងសង្ហារិម (20)</button>
            <button class="dir-pill" onclick="setDirCategory('GROCERIES', this)">🥩 ផ្សារទំនើប & គ្រឿងទេស (20)</button>
            <button class="dir-pill" onclick="setDirCategory('SERVICES', this)">📦 សៀវភៅ & ដឹកជញ្ជូន (20)</button>
        </div>'''

pills_new = '''        <div class="dir-category-pills">
            <button class="dir-pill active" onclick="setDirCategory('ALL', this)">🌐 ទាំងអស់ (All 700)</button>
            <button class="dir-pill" onclick="setDirCategory('GENERAL', this)">🛒 ទីផ្សារទូទៅ (20)</button>
            <button class="dir-pill" onclick="setDirCategory('COMPUTERS', this)">💻 កុំព្យូទ័រ & IT (70)</button>
            <button class="dir-pill" onclick="setDirCategory('PHONES', this)">📱 ទូរស័ព្ទ & Audio (70)</button>
            <button class="dir-pill" onclick="setDirCategory('CARS', this)">🚗 រថយន្ត & ម៉ូតូ (70)</button>
            <button class="dir-pill" onclick="setDirCategory('REAL_ESTATE', this)">🏠 អចលនទ្រព្យ & បុរី (70)</button>
            <button class="dir-pill" onclick="setDirCategory('FASHION', this)">👗 ម៉ូដ & ស្បែកជើង (70)</button>
            <button class="dir-pill" onclick="setDirCategory('BEAUTY', this)">💄 សម្រស់ & សុខភាព (70)</button>
            <button class="dir-pill" onclick="setDirCategory('FURNITURE', this)">🛋️ គ្រឿងសង្ហារិម & ផ្ទះ (70)</button>
            <button class="dir-pill" onclick="setDirCategory('GROCERIES', this)">🥩 ផ្សារទំនើប & អាហារ (70)</button>
            <button class="dir-pill" onclick="setDirCategory('SERVICES', this)">📦 ដឹកជញ្ជូន & សេវាកម្ម (120)</button>
        </div>'''

content = content.replace(pills_old, pills_new)
print("Updated category pills.")

# 3. Update #filter-platform dropdown
with open('scratch/filter_platform_700_html.txt', 'r', encoding='utf-8') as f:
    new_optgroups = f.read().strip()

plat_select_start = content.find('<select class="select-filter" id="filter-platform"')
if plat_select_start == -1:
    raise ValueError("Could not find filter-platform select start")

plat_select_close = content.find('</select>', plat_select_start)
if plat_select_close == -1:
    raise ValueError("Could not find filter-platform select end")

tag_open_end = content.find('>', plat_select_start) + 1

content = content[:tag_open_end] + "\n" + new_optgroups + "\n            " + content[plat_select_close:]
print("Updated #filter-platform dropdown with 700 options.")

# 4. Update CAMBODIA_PLATFORMS_DATA
with open('scratch/platforms_700_js.txt', 'r', encoding='utf-8') as f:
    new_platforms_js = f.read().strip()

js_start = content.find("const CAMBODIA_PLATFORMS_DATA = [")
if js_start == -1:
    raise ValueError("Could not find CAMBODIA_PLATFORMS_DATA start")

js_end = content.find("let currentDirCategory = 'ALL';", js_start)
if js_end == -1:
    raise ValueError("Could not find currentDirCategory anchor")

# find the closing ]; before currentDirCategory
closing_bracket = content.rfind("];", js_start, js_end)
if closing_bracket == -1:
    raise ValueError("Could not find closing bracket for CAMBODIA_PLATFORMS_DATA")

content = content[:js_start] + new_platforms_js + "\n\n    " + content[js_end:]
print("Updated CAMBODIA_PLATFORMS_DATA with 700 items.")

# 5. Update renderPlatformsDirectory for pagination / snappy rendering
old_render = '''    function renderPlatformsDirectory() {
        const container = document.getElementById("platforms-dir-grid");
        if (!container) return;

        const filtered = CAMBODIA_PLATFORMS_DATA.filter(p => {
            const matchCat = (currentDirCategory === 'ALL' || p.category === currentDirCategory);
            const matchQuery = !dirSearchFilter || 
                p.name.toLowerCase().includes(dirSearchFilter) ||
                p.domain.toLowerCase().includes(dirSearchFilter) ||
                p.nameKh.toLowerCase().includes(dirSearchFilter) ||
                p.descKh.toLowerCase().includes(dirSearchFilter);
            return matchCat && matchQuery;
        });

        const badge = document.getElementById("dir-count-badge");
        if (badge) badge.innerText = `បង្ហាញ ${filtered.length} នៃ ២០០ វេទិកា`;'''

new_render = '''    let dirDisplayLimit = 60;

    function renderPlatformsDirectory() {
        const container = document.getElementById("platforms-dir-grid");
        if (!container) return;

        const filtered = CAMBODIA_PLATFORMS_DATA.filter(p => {
            const matchCat = (currentDirCategory === 'ALL' || p.category === currentDirCategory);
            const matchQuery = !dirSearchFilter || 
                p.name.toLowerCase().includes(dirSearchFilter) ||
                p.domain.toLowerCase().includes(dirSearchFilter) ||
                p.nameKh.toLowerCase().includes(dirSearchFilter) ||
                p.descKh.toLowerCase().includes(dirSearchFilter);
            return matchCat && matchQuery;
        });

        const badge = document.getElementById("dir-count-badge");
        if (badge) badge.innerText = `បង្ហាញ ${Math.min(filtered.length, dirDisplayLimit)} នៃ ${filtered.length} (សរុប ៧០០ វេទិកា)`;'''

content = content.replace(old_render, new_render)

# Also update the card rendering to slice up to dirDisplayLimit and add load more button
card_render_old = '''        container.innerHTML = filtered.map(p => {
            return `
                <div class="platform-dir-card">
                    <div>
                        <div class="dir-card-header">
                            <div>
                                <div class="dir-card-name">${p.nameKh}</div>
                                <span class="dir-card-domain">${p.domain}</span>
                            </div>
                            <span class="tag" style="background: rgba(245, 158, 11, 0.18); border: 1px solid rgba(245, 158, 11, 0.4); color: #fde68a; font-size: 0.72rem; font-weight: 700;">
                                ${p.badge}
                            </span>
                        </div>
                        <div class="dir-card-desc">${p.descKh}</div>
                    </div>
                    <div class="dir-card-actions">
                        <button class="dir-search-btn" onclick="launchPlatformSearch('${p.id}', '${p.defaultCategory}', '${p.name}')">
                            🔍 ស្វែងរកក្នុងវិបសាយនេះ
                        </button>
                        <a href="${p.homeUrl}" target="_blank" rel="noopener noreferrer" class="dir-visit-btn">
                            🌐 ចូលវិបសាយ
                        </a>
                    </div>
                </div>
            `;
        }).join('');'''

card_render_new = '''        const toShow = filtered.slice(0, dirDisplayLimit);
        let cardsHtml = toShow.map(p => {
            return `
                <div class="platform-dir-card">
                    <div>
                        <div class="dir-card-header">
                            <div>
                                <div class="dir-card-name">${p.nameKh}</div>
                                <span class="dir-card-domain">${p.domain}</span>
                            </div>
                            <span class="tag" style="background: rgba(245, 158, 11, 0.18); border: 1px solid rgba(245, 158, 11, 0.4); color: #fde68a; font-size: 0.72rem; font-weight: 700;">
                                ${p.badge}
                            </span>
                        </div>
                        <div class="dir-card-desc">${p.descKh}</div>
                    </div>
                    <div class="dir-card-actions">
                        <button class="dir-search-btn" onclick="launchPlatformSearch('${p.id}', '${p.defaultCategory}', '${p.name}')">
                            🔍 ស្វែងរកក្នុងវិបសាយនេះ
                        </button>
                        <a href="${p.homeUrl}" target="_blank" rel="noopener noreferrer" class="dir-visit-btn">
                            🌐 ចូលវិបសាយ
                        </a>
                    </div>
                </div>
            `;
        }).join('');

        if (filtered.length > dirDisplayLimit) {
            cardsHtml += `
                <div style="grid-column: 1 / -1; text-align: center; padding: 20px;">
                    <button onclick="dirDisplayLimit += 60; renderPlatformsDirectory();" 
                            style="background: linear-gradient(135deg, rgba(245, 158, 11, 0.25), rgba(234, 88, 12, 0.25)); border: 1px solid rgba(245, 158, 11, 0.6); color: #fde68a; padding: 12px 28px; border-radius: 12px; cursor: pointer; font-weight: 700; font-family: inherit; font-size: 0.95rem; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                        ⚡ បង្ហាញបន្ថែមទៀត (+60 វិបសាយ) — នៅសល់ ${filtered.length - dirDisplayLimit}
                    </button>
                </div>
            `;
        }

        container.innerHTML = cardsHtml;'''

content = content.replace(card_render_old, card_render_new)

# Reset dirDisplayLimit on category change or search filter
reset_hook = "function setDirCategory(category, pillElem) {\n        dirDisplayLimit = 60;\n"
content = content.replace("function setDirCategory(category, pillElem) {\n", reset_hook)

filter_hook = "function filterPlatformsDirectory() {\n        dirDisplayLimit = 60;\n"
content = content.replace("function filterPlatformsDirectory() {\n", filter_hook)

with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated frontend/index.html with all 700 platforms!")
