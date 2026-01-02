# Dedicated restoration script
import sys

restored_platforms_chunk = """        "id": "ips_cambodia", "name": "IPS Cambodia", "domain": "ips-cambodia.com",
        "category": "REAL_ESTATE", "badge": "🏠 Real Estate", "nameKh": "IPS Cambodia",
        "descKh": "ទីភ្នាក់ងារអចលនទ្រព្យអន្តរជាតិឈានមុខគេក្នុងប្រទេសកម្ពុជា (Expat & Local)",
        "searchUrl": "https://ips-cambodia.com/properties/?keyword={q}",
        "homeUrl": "https://ips-cambodia.com"
    },
    {
        "id": "cbre_kh", "name": "CBRE Cambodia", "domain": "cbre.com.kh",
        "category": "REAL_ESTATE", "badge": "🏠 Real Estate", "nameKh": "CBRE Cambodia",
        "descKh": "ក្រុមហ៊ុនប្រឹក្សា និងគ្រប់គ្រងអចលនទ្រព្យពាណិជ្ជកម្ម និងលំនៅដ្ឋានស្តង់ដារសកល",
        "searchUrl": "https://www.cbre.com.kh/properties?search={q}",
        "homeUrl": "https://www.cbre.com.kh"
    },
    {
        "id": "century21_kh", "name": "Century 21 Cambodia", "domain": "century21.com.kh",
        "category": "REAL_ESTATE", "badge": "🏠 Real Estate", "nameKh": "Century 21 Cambodia",
        "descKh": "បណ្តាញភ្នាក់ងារអចលនទ្រព្យសកលប្រចាំកម្ពុជា ជាមួយការិយាល័យទូទាំងប្រទេស",
        "searchUrl": "https://www.century21.com.kh/search?q={q}",
        "homeUrl": "https://www.century21.com.kh"
    },
    {
        "id": "mapletree_kh", "name": "Mapletree Realty", "domain": "mapletreer.com",
        "category": "REAL_ESTATE", "badge": "🏠 Real Estate", "nameKh": "Mapletree Realty",
        "descKh": "សេវាកម្មទិញ-លក់ និងជួលអចលនទ្រព្យប្រកបដោយទំនុកចិត្ត និងតម្លាភាព",
        "searchUrl": "https://www.mapletreer.com/search?q={q}",
        "homeUrl": "https://www.mapletreer.com"
    },
    {
        "id": "towncity_kh", "name": "TownCity Real Estate", "domain": "towncity.com",
        "category": "REAL_ESTATE", "badge": "🏠 Real Estate", "nameKh": "TownCity Real Estate",
        "descKh": "ភ្នាក់ងារអចលនទ្រព្យជំនាញលើការជួលខុនដូ វីឡា និងដីសម្រាប់វិនិយោគ",
        "searchUrl": "https://towncity.com/property-search/?keyword={q}",
        "homeUrl": "https://towncity.com"
    },
    {
        "id": "fazwaz_kh", "name": "FazWaz Cambodia", "domain": "fazwaz.com.kh",
        "category": "REAL_ESTATE", "badge": "🏠 Real Estate", "nameKh": "FazWaz Cambodia",
        "descKh": "វេទិកាស្វែងរកផ្ទះ និងគម្រោងខុនដូថ្មីៗជាមួយទិន្នន័យ 3D និងតម្លៃច្បាស់លាស់",
        "searchUrl": "https://www.fazwaz.com.kh/property-sales/cambodia?q={q}",
        "homeUrl": "https://www.fazwaz.com.kh"
    },
    {
        "id": "knightfrank_kh", "name": "Knight Frank Cambodia", "domain": "knightfrank.com.kh",
        "category": "REAL_ESTATE", "badge": "🏠 Real Estate", "nameKh": "Knight Frank Cambodia",
        "descKh": "អ្នកជំនាញទីផ្សារអចលនទ្រព្យកម្រិតប្រណិត និងការវាយតម្លៃអចលនទ្រព្យផ្លូវការ",
        "searchUrl": "https://www.knightfrank.com.kh/properties?keyword={q}",
        "homeUrl": "https://www.knightfrank.com.kh"
    },

    # ── 5. FASHION, BEAUTY & ACCESSORIES (5) ─────────────────────────────────
    {
        "id": "zando", "name": "Zando", "domain": "zando.com.kh",
        "category": "FASHION", "badge": "👗 Fashion", "nameKh": "Zando Cambodia",
        "descKh": "បណ្តាញហាងលក់សម្លៀកបំពាក់ និងម៉ូដទាន់សម័យធំជាងគេនៅកម្ពុជា ជាមួយម៉ាកល្បីៗជាច្រើន",
        "searchUrl": "https://zando.com.kh/search?q={q}",
        "homeUrl": "https://zando.com.kh"
    },
    {
        "id": "l192", "name": "L192", "domain": "l192.com",
        "category": "FASHION", "badge": "👗 Fashion", "nameKh": "L192 Cambodia",
        "descKh": "កម្មវិធីទិញទំនិញសម្លៀកបំពាក់ គ្រឿងតុបតែង និង Lifestyle ពេញនិយមបំផុតសម្រាប់យុវវ័យ",
        "searchUrl": "https://l192.com/search?q={q}",
        "homeUrl": "https://l192.com"
    },
    {
        "id": "ten11", "name": "Ten11", "domain": "ten11.com.kh",
        "category": "FASHION", "badge": "👗 Fashion", "nameKh": "Ten11 Clothing",
        "descKh": "ម៉ាកសម្លៀកបំពាក់ទាន់សម័យក្នុងស្រុក គុណភាពខ្ពស់ រចនាយ៉ាងពិសេសសម្រាប់ប្រជាជនកម្ពុជា",
        "searchUrl": "https://ten11.com.kh/search?q={q}",
        "homeUrl": "https://ten11.com.kh"
    },
    {
        "id": "pedro_kh", "name": "Pedro Cambodia", "domain": "pedroshoes.com/kh",
        "category": "FASHION", "badge": "👠 Luxury Shoes & Bags", "nameKh": "Pedro Cambodia",
        "descKh": "ហាងស្បែកជើង កាបូប និងគ្រឿងលម្អម៉ាកល្បីកម្រិតអន្តរជាតិ ស្តង់ដារប្រណិត",
"""

with open("scrapers/ai_search_service.py", "r", encoding="utf-8") as f:
    content = f.read()

# Locate the bad start
start_marker = '    {\n        "id": "ips_cambodiaCAMBODIA_PRICE_HISTORY = {\n'
# Locate the bad end
end_marker = '}្រឿងលម្អម៉ាកល្បីកម្រិតអន្តរជាតិ ស្តង់ដារប្រណិត",\n'

if start_marker in content and end_marker in content:
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker) + len(end_marker)
    
    clean_replacement = "    {\n" + restored_platforms_chunk
    content = content[:start_idx] + clean_replacement + content[end_idx:]
    with open("scrapers/ai_search_service.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("REPLACEMENT SUCCESSFUL!")
else:
    print("MARKERS NOT FOUND!")
    print("start_marker in content:", start_marker in content)
    print("end_marker in content:", end_marker in content)
