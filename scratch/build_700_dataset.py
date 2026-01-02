import json
import sys
import os

sys.path.append('scrapers')
import ai_search_service

# 1. Load initial 200 platforms
initial_200 = ai_search_service.CAMBODIA_MARKET_PLATFORMS
print(f"Loaded {len(initial_200)} initial platforms.")

# 2. Load 500 parsed platforms
with open('scratch/parsed_500.json') as f:
    parsed_500 = json.load(f)
print(f"Loaded {len(parsed_500)} parsed platforms (201-700).")

# 3. Standardize and merge
all_700 = []

for idx, p in enumerate(initial_200):
    item = dict(p)
    if 'defaultCategory' not in item:
        item['defaultCategory'] = item.get('category', 'GENERAL')
    item['num'] = idx + 1
    all_700.append(item)

for p in parsed_500:
    item = dict(p)
    if 'defaultCategory' not in item:
        item['defaultCategory'] = item.get('category', 'GENERAL')
    all_700.append(item)

print(f"Total merged platforms: {len(all_700)}")

# Verify uniqueness of ids and domains
ids = set()
for p in all_700:
    if p['id'] in ids:
        print(f"Warning duplicate ID: {p['id']}")
    ids.add(p['id'])

print(f"Unique IDs: {len(ids)} / {len(all_700)}")

# Save master JSON
with open('scratch/all_700_platforms.json', 'w', encoding='utf-8') as f:
    json.dump(all_700, f, ensure_ascii=False, indent=2)

# 4. Generate Python snippet for CAMBODIA_MARKET_PLATFORMS
py_lines = ["CAMBODIA_MARKET_PLATFORMS = ["]
category_headers = {
    1: "── GENERAL CLASSIFIEDS & E-COMMERCE (20) ──",
    21: "── COMPUTERS, LAPTOPS & IT HARDWARE (20) ──",
    41: "── SMARTPHONES, TABLETS & MOBILE TECH (20) ──",
    61: "── VEHICLES, CARS & MOTORCYCLES (20) ──",
    81: "── REAL ESTATE, BOREYS & PROPERTY (20) ──",
    101: "── FASHION, CLOTHING & SHOES (20) ──",
    121: "── BEAUTY, SKINCARE & HEALTH (20) ──",
    141: "── FURNITURE, HOME DECOR & LIVING (20) ──",
    161: "── SUPERMARKETS, GROCERIES & FOOD (20) ──",
    181: "── BOOKS, LOGISTICS & GENERAL SERVICES (20) ──",
    201: "── ELECTRONICS, GADGETS & AUDIO (50) ──",
    251: "── COMPUTER SYSTEMS, GAMING & IT EQUIPMENT (50) ──",
    301: "── AUTOMOTIVE, BIKES, SPARE PARTS & RENTAL (50) ──",
    351: "── REAL ESTATE, CONDOS, BOREYS & COMMERCIAL (50) ──",
    401: "── FASHION, FOOTWEAR & JEWELRY (50) ──",
    451: "── BEAUTY, COSMETICS & PERSONAL CARE (50) ──",
    501: "── HOME & KITCHEN APPLIANCES, FURNITURE & LIGHTING (50) ──",
    551: "── SUPERMARKETS, ORGANIC STORES & GOURMET FOOD (50) ──",
    601: "── LOGISTICS, DELIVERY & EXPRESS FREIGHT (50) ──",
    651: "── BOOKS, TRAVEL, TICKETING & BUSINESS SERVICES (50) ──"
}

for i, p in enumerate(all_700):
    num = i + 1
    if num in category_headers:
        py_lines.append(f"    # {category_headers[num]}")
    clean_p = {
        "id": p["id"],
        "name": p["name"],
        "domain": p["domain"],
        "category": p["category"],
        "badge": p["badge"],
        "nameKh": p["nameKh"],
        "descKh": p["descKh"],
        "searchUrl": p["searchUrl"],
        "homeUrl": p["homeUrl"]
    }
    py_lines.append(f"    {json.dumps(clean_p, ensure_ascii=False)},")

py_lines.append("]\n")

with open('scratch/platforms_700_py.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(py_lines))

print("Saved scratch/platforms_700_py.txt")

# 5. Generate JS snippet for CAMBODIA_PLATFORMS_DATA
js_lines = ["const CAMBODIA_PLATFORMS_DATA = ["]
for i, p in enumerate(all_700):
    num = i + 1
    if num in category_headers:
        js_lines.append(f"    // {category_headers[num]}")
    clean_p = {
        "id": p["id"],
        "name": p["name"],
        "domain": p["domain"],
        "category": p["category"],
        "badge": p["badge"],
        "nameKh": p["nameKh"],
        "descKh": p["descKh"],
        "searchUrl": p["searchUrl"],
        "homeUrl": p["homeUrl"],
        "defaultCategory": p["category"]
    }
    js_lines.append(f"    {json.dumps(clean_p, ensure_ascii=False)},")
js_lines.append("];\n")

with open('scratch/platforms_700_js.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(js_lines))

print("Saved scratch/platforms_700_js.txt")

# 6. Generate Optgroups for HTML select
categories_meta = [
    ("GENERAL", "🛒 ទីផ្សារទូទៅ & E-Commerce", 20),
    ("COMPUTERS", "💻 កុំព្យូទ័រ & ឧបករណ៍ IT", 70),
    ("PHONES", "📱 ទូរស័ព្ទ, គ្រឿង Gadget & Audio", 70),
    ("CARS", "🚗 រថយន្ត, ម៉ូតូ & គ្រឿងបន្លាស់", 70),
    ("REAL_ESTATE", "🏢 អចលនទ្រព្យ, ខុនដូ & បុរី", 70),
    ("FASHION", "👕 សម្លៀកបំពាក់, ស្បែកជើង & គ្រឿងអលង្ការ", 70),
    ("BEAUTY", "💄 សម្រស់, គ្រឿងសម្អាង & សុខភាព", 70),
    ("FURNITURE", "🛋️ គ្រឿងសង្ហារិម, សម្ភារៈផ្ទះបាយ & បន្ទប់គេង", 70),
    ("GROCERIES", "🥩 ផ្សារទំនើប, អាហារសរីរាង្គ & ភេសជ្ជៈ", 70),
    ("SERVICES", "📦 ដឹកជញ្ជូន, សំបុត្រយន្តហោះ, សណ្ឋាគារ & សេវាកម្ម", 120),
]

html_optgroups = ['<option value="">🌐 គ្រប់វិបសាយទាំង ៧០០ (All 700 Marketplaces & Brands)</option>']
for cat_id, cat_title, expected_count in categories_meta:
    cat_platforms = [p for p in all_700 if p['category'] == cat_id]
    html_optgroups.append(f'                <optgroup label="{cat_title} ({len(cat_platforms)})">')
    for p in cat_platforms:
        display_name = p['name']
        html_optgroups.append(f'                    <option value="{p["id"]}">{display_name}</option>')
    html_optgroups.append('                </optgroup>')

with open('scratch/filter_platform_700_html.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(html_optgroups))

print("Saved scratch/filter_platform_700_html.txt")

# 7. Generate Domain Map updates
domain_map = dict(ai_search_service.WEBSITE_DOMAIN_MAP)
for p in all_700:
    d = p['domain'].lower()
    c = p['category']
    domain_map[d] = c
    clean_d = d.replace('www.', '')
    domain_map[clean_d] = c
    # host root
    host_root = clean_d.split('/')[0]
    domain_map[host_root] = c
    # brand id
    domain_map[p['id'].lower()] = c

print(f"Enriched WEBSITE_DOMAIN_MAP size: {len(domain_map)}")
with open('scratch/domain_map_700.json', 'w', encoding='utf-8') as f:
    json.dump(domain_map, f, ensure_ascii=False, indent=2)

print("All 700 dataset artifacts created successfully!")
