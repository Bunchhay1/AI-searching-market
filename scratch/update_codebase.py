# scratch/update_codebase.py
import re
import json

with open("scratch/generate_platforms.py", "r", encoding="utf-8") as f:
    gen_code = f.read()

# Let's import raw_categories from generate_platforms.py
import sys
sys.path.append("scratch")
from generate_platforms import raw_categories

# ── 1. GENERATE PYTHON CODE FOR ai_search_service.py ──
py_platforms_lines = []
for c in raw_categories:
    py_platforms_lines.append(f"    # ── {c['cat_name_en'].upper()} ({len(c['items'])}) ──")
    for item in c["items"]:
        p_dict = {
            "id": item[0],
            "name": item[1],
            "domain": item[2],
            "category": c["cat_id"],
            "badge": item[3],
            "nameKh": item[4],
            "descKh": item[5],
            "searchUrl": item[6],
            "homeUrl": item[7]
        }
        py_platforms_lines.append(f"    {json.dumps(p_dict, ensure_ascii=False)},")

py_platforms_str = "CAMBODIA_MARKET_PLATFORMS = [\n" + "\n".join(py_platforms_lines) + "\n]"

# Generate WEBSITE_DOMAIN_MAP extensions
domain_map_lines = []
for c in raw_categories:
    cat = c["cat_id"]
    domain_map_lines.append(f"    # ── {c['cat_name_en']} ──")
    for item in c["items"]:
        p_id, p_name, p_dom = item[0], item[1], item[2]
        clean_dom = p_dom.replace("https://", "").replace("http://", "").split("/")[0].lower()
        clean_name = p_name.lower().strip()
        domain_map_lines.append(f'    "{clean_dom}": "{cat}", "{clean_name}": "{cat}",')
        if p_id != clean_name:
            domain_map_lines.append(f'    "{p_id}": "{cat}",')

py_domain_map_str = "WEBSITE_DOMAIN_MAP = {\n" + "\n".join(domain_map_lines) + "\n}"

# Read ai_search_service.py
with open("scrapers/ai_search_service.py", "r", encoding="utf-8") as f:
    ai_content = f.read()

# Replace CAMBODIA_MARKET_PLATFORMS
# Find start: CAMBODIA_MARKET_PLATFORMS = [
# Find end: CAMBODIA_PRICE_HISTORY = {
pattern = r"CAMBODIA_MARKET_PLATFORMS = \[.*?\]\n\n\n# ─── PRICE TREND"
match = re.search(pattern, ai_content, flags=re.DOTALL)
if not match:
    print("ERROR: Could not find CAMBODIA_MARKET_PLATFORMS in ai_search_service.py")
    sys.exit(1)

new_ai_content = ai_content[:match.start()] + py_platforms_str + "\n\n\n# ─── PRICE TREND" + ai_content[match.end():]

# Now update get_platforms_for_domain_and_query and categories in ai_search_service.py
# Let's inspect where get_platforms_for_domain_and_query is defined
func_old = """def get_platforms_for_domain_and_query(domain: str, query: str):
    \"\"\"
    Returns candidate platforms tailored to the search domain and specific website name in query.
    \"\"\"
    q_low = query.lower().strip()
    exact_matches = []
    for p in CAMBODIA_MARKET_PLATFORMS:
        p_name = p["name"].lower()
        p_dom = p["domain"].lower()
        p_id = p["id"].lower()
        if p_dom in q_low or p_name in q_low or p_id in q_low:
            exact_matches.append(p)
            
    if domain == "REAL_ESTATE":
        base = [p for p in CAMBODIA_MARKET_PLATFORMS if p["category"] == "REAL_ESTATE"]
        extra = [p for p in CAMBODIA_MARKET_PLATFORMS if p["id"] in ["khmer24", "sabaylok"]]
        pool = base + extra
    elif domain == "CARS":
        base = [p for p in CAMBODIA_MARKET_PLATFORMS if p["category"] == "CARS"]
        extra = [p for p in CAMBODIA_MARKET_PLATFORMS if p["id"] in ["khmer24", "sabaylok"]]
        pool = base + extra
    elif domain in ["ELECTRONICS", "COMPUTERS", "PHONES", "TABLETS"]:
        base = [p for p in CAMBODIA_MARKET_PLATFORMS if p["category"] == "ELECTRONICS"]
        extra = [p for p in CAMBODIA_MARKET_PLATFORMS if p["id"] in ["khmer24", "sabaylok"]]
        pool = base + extra
    elif domain == "FASHION":
        base = [p for p in CAMBODIA_MARKET_PLATFORMS if p["category"] == "FASHION"]
        extra = [p for p in CAMBODIA_MARKET_PLATFORMS if p["id"] in ["khmer24", "larue"]]
        pool = base + extra
    else: # GENERAL
        pool = [p for p in CAMBODIA_MARKET_PLATFORMS if p["category"] == "GENERAL"]

    if exact_matches:
        # Prioritize exact matching platform so it appears heavily in listings
        return exact_matches * 3 + pool
    return pool"""

func_new = """def get_platforms_for_domain_and_query(domain: str, query: str):
    \"\"\"
    Returns candidate platforms tailored to the search domain and specific website name in query.
    Encompasses all 200 Cambodian platforms across 10 categories.
    \"\"\"
    q_low = query.lower().strip()
    exact_matches = []
    for p in CAMBODIA_MARKET_PLATFORMS:
        p_name = p["name"].lower()
        p_dom = p["domain"].lower()
        p_id = p["id"].lower()
        if p_dom in q_low or p_name in q_low or p_id in q_low:
            exact_matches.append(p)
            
    if domain == "REAL_ESTATE":
        base = [p for p in CAMBODIA_MARKET_PLATFORMS if p["category"] == "REAL_ESTATE"]
        extra = [p for p in CAMBODIA_MARKET_PLATFORMS if p["id"] in ["khmer24", "sabaylok"]]
        pool = base + extra
    elif domain in ["CARS", "MOTORS", "MOTOS"]:
        base = [p for p in CAMBODIA_MARKET_PLATFORMS if p["category"] == "CARS"]
        extra = [p for p in CAMBODIA_MARKET_PLATFORMS if p["id"] in ["khmer24", "sabaylok"]]
        pool = base + extra
    elif domain == "COMPUTERS":
        base = [p for p in CAMBODIA_MARKET_PLATFORMS if p["category"] == "COMPUTERS"]
        extra = [p for p in CAMBODIA_MARKET_PLATFORMS if p["id"] in ["khmer24", "sabaylok"]]
        pool = base + extra
    elif domain in ["PHONES", "SMARTPHONES", "TABLETS"]:
        base = [p for p in CAMBODIA_MARKET_PLATFORMS if p["category"] == "PHONES"]
        extra = [p for p in CAMBODIA_MARKET_PLATFORMS if p["id"] in ["khmer24", "sabaylok"]]
        pool = base + extra
    elif domain == "ELECTRONICS":
        base = [p for p in CAMBODIA_MARKET_PLATFORMS if p["category"] in ["COMPUTERS", "PHONES", "FURNITURE"]]
        extra = [p for p in CAMBODIA_MARKET_PLATFORMS if p["id"] in ["khmer24", "sabaylok"]]
        pool = base + extra
    elif domain == "FASHION":
        base = [p for p in CAMBODIA_MARKET_PLATFORMS if p["category"] == "FASHION"]
        extra = [p for p in CAMBODIA_MARKET_PLATFORMS if p["id"] in ["khmer24", "l192_fashion"]]
        pool = base + extra
    elif domain in ["BEAUTY", "COSMETICS"]:
        base = [p for p in CAMBODIA_MARKET_PLATFORMS if p["category"] == "BEAUTY"]
        extra = [p for p in CAMBODIA_MARKET_PLATFORMS if p["id"] in ["khmer24", "l192_beauty", "larue"]]
        pool = base + extra
    elif domain in ["FURNITURE", "HOME"]:
        base = [p for p in CAMBODIA_MARKET_PLATFORMS if p["category"] == "FURNITURE"]
        extra = [p for p in CAMBODIA_MARKET_PLATFORMS if p["id"] in ["khmer24", "sabaylok"]]
        pool = base + extra
    elif domain in ["GROCERIES", "SUPERMARKET"]:
        base = [p for p in CAMBODIA_MARKET_PLATFORMS if p["category"] == "GROCERIES"]
        extra = [p for p in CAMBODIA_MARKET_PLATFORMS if p["id"] in ["nham24", "wownow", "aeon_online", "lucky_supermarket"]]
        pool = base + extra
    elif domain in ["SERVICES", "TRAVEL", "LOGISTICS"]:
        base = [p for p in CAMBODIA_MARKET_PLATFORMS if p["category"] == "SERVICES"]
        extra = [p for p in CAMBODIA_MARKET_PLATFORMS if p["id"] in ["khmer24", "camboquick", "bookmebus", "vireak_buntham"]]
        pool = base + extra
    else: # GENERAL
        pool = [p for p in CAMBODIA_MARKET_PLATFORMS if p["category"] == "GENERAL"]

    if exact_matches:
        # Prioritize exact matching platform so it appears heavily in listings
        return exact_matches * 3 + pool
    return pool"""

if func_old in new_ai_content:
    new_ai_content = new_ai_content.replace(func_old, func_new)
else:
    print("WARNING: Could not do exact replace of get_platforms_for_domain_and_query, using regex")
    pattern_func = r"def get_platforms_for_domain_and_query\(domain: str, query: str\):.*?return pool"
    new_ai_content = re.sub(pattern_func, func_new, new_ai_content, flags=re.DOTALL)

# Update /platforms endpoint
old_platforms_ep = """            payload = {
                "totalPlatforms": len(CAMBODIA_MARKET_PLATFORMS),
                "platforms": CAMBODIA_MARKET_PLATFORMS,
                "categories": [
                    {"id": "ALL", "labelKh": "ទាំងអស់ (៤៦ ប្រភព)", "labelEn": "All Platforms", "count": len(CAMBODIA_MARKET_PLATFORMS)},
                    {"id": "REAL_ESTATE", "labelKh": "អចលនទ្រព្យ & ផ្ទះជួល", "labelEn": "Real Estate & Property", "count": 10},
                    {"id": "CARS", "labelKh": "ទីផ្សាររថយន្ត & យានយន្ត", "labelEn": "Cars & Vehicles", "count": 6},
                    {"id": "GENERAL", "labelKh": "ទីផ្សារទូទៅ & ទំនិញមួយទឹក", "labelEn": "General Classifieds & E-Commerce", "count": 10},
                    {"id": "ELECTRONICS", "labelKh": "ទូរស័ព្ទ កុំព្យូទ័រ & អេឡិចត្រូនិក", "labelEn": "Electronics & Computers", "count": 15},
                    {"id": "FASHION", "labelKh": "សម្លៀកបំពាក់ & គ្រឿងលម្អ", "labelEn": "Fashion & Accessories", "count": 5}
                ]
            }"""

new_platforms_ep = """            payload = {
                "totalPlatforms": len(CAMBODIA_MARKET_PLATFORMS),
                "platforms": CAMBODIA_MARKET_PLATFORMS,
                "categories": [
                    {"id": "ALL", "labelKh": "ទាំងអស់ (២០០ ប្រភព)", "labelEn": "All Platforms", "count": len(CAMBODIA_MARKET_PLATFORMS)},
                    {"id": "GENERAL", "labelKh": "ទីផ្សារទូទៅ & E-Commerce", "labelEn": "General Classifieds", "count": 20},
                    {"id": "COMPUTERS", "labelKh": "កុំព្យូទ័រ Gaming & IT", "labelEn": "Computers & Gaming IT", "count": 20},
                    {"id": "PHONES", "labelKh": "ទូរស័ព្ទ & ថេបប្លេត", "labelEn": "Phones & Tablets", "count": 20},
                    {"id": "CARS", "labelKh": "រថយន្ត & គ្រឿងយន្ត", "labelEn": "Cars & Vehicles", "count": 20},
                    {"id": "REAL_ESTATE", "labelKh": "អចលនទ្រព្យ & បុរី", "labelEn": "Real Estate & Housing", "count": 20},
                    {"id": "FASHION", "labelKh": "ម៉ូដ & សម្លៀកបំពាក់", "labelEn": "Fashion & Apparel", "count": 20},
                    {"id": "BEAUTY", "labelKh": "សម្រស់ & សុខភាព", "labelEn": "Beauty & Health", "count": 20},
                    {"id": "FURNITURE", "labelKh": "គ្រឿងសង្ហារិម & គ្រឿងផ្ទះ", "labelEn": "Furniture & Appliances", "count": 20},
                    {"id": "GROCERIES", "labelKh": "ផ្សារទំនើប & គ្រឿងទេស", "labelEn": "Supermarkets & Groceries", "count": 20},
                    {"id": "SERVICES", "labelKh": "សៀវភៅ & ដឹកជញ្ជូន", "labelEn": "Books, Travel & Logistics", "count": 20}
                ]
            }"""

if old_platforms_ep in new_ai_content:
    new_ai_content = new_ai_content.replace(old_platforms_ep, new_platforms_ep)
else:
    print("Updating /platforms endpoint via regex...")
    pattern_ep = r"payload = \{\s*\"totalPlatforms\":.*?\n            \}"
    new_ai_content = re.sub(pattern_ep, new_platforms_ep.strip(), new_ai_content, flags=re.DOTALL)

with open("scrapers/ai_search_service.py", "w", encoding="utf-8") as f:
    f.write(new_ai_content)

print("scrapers/ai_search_service.py updated successfully!")

# ── 2. GENERATE FRONTEND UPDATES FOR index.html ──
with open("frontend/index.html", "r", encoding="utf-8") as f:
    fe_content = f.read()

# Update top button
fe_content = fe_content.replace("៥២ វេទិកាទីផ្សារកម្ពុជា (52 Portals)", "២០០ វេទិកាទីផ្សារកម្ពុជា (200 Portals)")
fe_content = fe_content.replace("៤៨ វេទិកាទីផ្សារកម្ពុជា (48 Portals)", "២០០ វេទិកាទីផ្សារកម្ពុជា (200 Portals)")
fe_content = fe_content.replace("៤៦ វេទិកាទីផ្សារកម្ពុជា (46 Portals)", "២០០ វេទិកាទីផ្សារកម្ពុជា (200 Portals)")

# Update helper text
fe_content = fe_content.replace("ស្វែងរកទំនិញ ពិនិត្យតម្លៃ និងទិញលក់លើ ៥២ វេទិកាឈានមុខគេនៅកម្ពុជា", "ស្វែងរកទំនិញ ពិនិត្យតម្លៃ និងទិញលក់លើ ២០០ វេទិកាឈានមុខគេនៅកម្ពុជា (១០ ប្រភេទធំៗ)")
fe_content = fe_content.replace("៥២ វេទិកាផ្លូវការ", "២០០ វេទិកាផ្លូវការ")
fe_content = fe_content.replace("៤៦ វេទិកាផ្លូវការ", "២០០ វេទិកាផ្លូវការ")
fe_content = fe_content.replace("៥២ វេទិកាទីផ្សារកម្ពុជាផ្លូវការ (52 Verified Cambodian Portals)", "២០០ វេទិកាទីផ្សារកម្ពុជាផ្លូវការ (200 Verified Cambodian Portals)")

# Update filter-category
new_filter_cat = """            <select class="select-filter" id="filter-category" onchange="performSearch()">
                <option value="">គ្រប់ប្រភេទ (All Categories)</option>
                <option value="GENERAL">🛒 ទីផ្សារទូទៅ (General Classifieds)</option>
                <option value="COMPUTERS">💻 កុំព្យូទ័រ & Gaming (Computers & IT)</option>
                <option value="PHONES">📱 ទូរស័ព្ទ & Tablets (Smartphones)</option>
                <option value="CARS">🚗 រថយន្ត & ម៉ូតូ (Cars & Motors)</option>
                <option value="REAL_ESTATE">🏠 អចលនទ្រព្យ & ផ្ទះ (Real Estate)</option>
                <option value="FASHION">👗 សម្លៀកបំពាក់ & ម៉ូដ (Fashion)</option>
                <option value="BEAUTY">💄 សម្រស់ & សុខភាព (Beauty & Health)</option>
                <option value="FURNITURE">🛋️ គ្រឿងសង្ហារិម & ផ្ទះ (Furniture & Decor)</option>
                <option value="GROCERIES">🥩 ផ្សារទំនើប & គ្រឿងទេស (Supermarkets)</option>
                <option value="SERVICES">📦 សៀវភៅ & ដឹកជញ្ជូន (Books & Logistics)</option>
            </select>"""

old_filter_cat_regex = r'<select class="select-filter" id="filter-category" onchange="performSearch\(\)">.*?</select>'
fe_content = re.sub(old_filter_cat_regex, new_filter_cat, fe_content, flags=re.DOTALL)

# Update filter-platform select
# Build 10 optgroups for filter-platform
optgroups = []
optgroups.append('            <select class="select-filter" id="filter-platform" onchange="performSearch()" style="border-color: rgba(245, 158, 11, 0.4); background: rgba(15, 23, 42, 0.85); color: #fde68a; font-weight: 600;">')
optgroups.append('                <option value="">🌐 គ្រប់វិបសាយទាំង ២០០ (All 200 Marketplaces)</option>')
for c in raw_categories:
    optgroups.append(f'                <optgroup label="{c["icon"]} {c["cat_name_kh"]} ({len(c["items"])})">')
    for item in c["items"]:
        optgroups.append(f'                    <option value="{item[0]}">{item[1]}</option>')
    optgroups.append('                </optgroup>')
optgroups.append('            </select>')
new_filter_plat = "\n".join(optgroups)

old_filter_plat_regex = r'<select class="select-filter" id="filter-platform".*?</select>'
fe_content = re.sub(old_filter_plat_regex, new_filter_plat, fe_content, flags=re.DOTALL)

# Update Category Filter Pills in Directory Modal
new_pills = """        <!-- Category Filter Pills -->
        <div class="dir-category-pills">
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
        </div>"""

old_pills_regex = r'<!-- Category Filter Pills -->\s*<div class="dir-category-pills">.*?</div>'
fe_content = re.sub(old_pills_regex, new_pills, fe_content, flags=re.DOTALL)

# Update CAMBODIA_PLATFORMS_DATA
with open("scratch/platforms_js.txt", "r", encoding="utf-8") as f:
    new_js_platforms = f.read().strip()

old_js_platforms_regex = r'const CAMBODIA_PLATFORMS_DATA = \[.*?\];'
fe_content = re.sub(old_js_platforms_regex, new_js_platforms, fe_content, flags=re.DOTALL)

with open("frontend/index.html", "w", encoding="utf-8") as f:
    f.write(fe_content)

print("frontend/index.html updated successfully!")
