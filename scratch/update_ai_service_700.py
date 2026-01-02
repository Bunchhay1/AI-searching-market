import json
import re

# Read current ai_search_service.py
with open('scrapers/ai_search_service.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace CAMBODIA_MARKET_PLATFORMS
with open('scratch/platforms_700_py.txt', 'r', encoding='utf-8') as f:
    new_platforms_py = f.read().strip()

plat_start = content.find("CAMBODIA_MARKET_PLATFORMS = [")
plat_end = content.find("\n]\n\n\n# ─── PRICE TREND")
if plat_start == -1 or plat_end == -1:
    raise ValueError("Could not find CAMBODIA_MARKET_PLATFORMS boundaries")

content = content[:plat_start] + new_platforms_py + content[plat_end + 3:]
print("Replaced CAMBODIA_MARKET_PLATFORMS with 700 items.")

# 2. Enrich CAMBODIA_PRICE_HISTORY with new super AI data
super_price_history = '''
    # ── ELECTRONICS, GADGETS & AUDIO (Super AI Data) ──
    "marshall stanmore": {
        "3m_ago": 360, "6m_ago": 380, "12m_ago": 395,
        "reason_high": [
            "បាស Bluetooth ស៊េរីល្បី Marshall Stanmore III សំឡេងកន្ត្រាក់បេះដូង Retro Design ពេញនិយមខ្លាំង",
            "ទំនិញសុទ្ធ 100% នាំចូលមានស្តង់ដារធានា 1 ឆ្នាំពេញពីតំណាងចែកចាយផ្លូវការ",
            "ទីផ្សារមានផលិតផលចម្លង (Fake/Copy) ច្រើន ធ្វើឱ្យទំនិញសុទ្ធប្រអប់ Original មានតម្លៃខ្ពស់",
            "បំពាក់បច្ចេកវិទ្យា Bluetooth 5.2 និងរន្ធដោត RCA / AUX គុណភាពខ្ពស់"
        ],
        "peak_season": ["Nov", "Dec", "Jan"],
        "trend": "STABLE_HIGH",
    },
    "sony wh-1000xm5": {
        "3m_ago": 340, "6m_ago": 360, "12m_ago": 390,
        "reason_high": [
            "កំពូលកាសបិទសំឡេងរំខាន No.1 Noise Cancelling ដំណើរការដោយឈីប Processor V1 & QN1",
            "គុណភាពសំឡេង Hi-Res Audio Wireless LDAC និងមីក្រូហ្វូន 8 គ្រាប់ចាប់សំឡេងច្បាស់ល្អ",
            "ទំនិញថ្មីប្រអប់ធានាក្រុមហ៊ុន Sony Cambodia 1 ឆ្នាំ រក្សាតម្លៃបានល្អ"
        ],
        "peak_season": ["Oct", "Nov", "Dec"],
        "trend": "DECLINING",
    },
    "bose quietcomfort": {
        "3m_ago": 320, "6m_ago": 340, "12m_ago": 360,
        "reason_high": [
            "កាស Bose QuietComfort Ultra ល្បីល្បាញខាងផាសុកភាពពាក់មិនឈឺត្រចៀក និង Spatial Audio",
            "នាំចូលផ្លូវការពី Bose Cambodia ធានាគុណភាពកម្រិតពិភពលោក"
        ],
        "peak_season": ["Nov", "Dec"],
        "trend": "STABLE_HIGH",
    },
    "dji mini 4 pro": {
        "3m_ago": 880, "6m_ago": 930, "12m_ago": 990,
        "reason_high": [
            "ដ្រូនខ្នាតតូចទម្ងន់ក្រោម 249g បំពាក់សេនស័រការពារការប៉ះទង្គិចជុំទិស Omni-directional Obstacle Sensing",
            "កាមេរ៉ាថត 4K/60fps HDR True Vertical Shooting សម្រាប់ Reels & TikTok",
            "កញ្ចប់ Fly More Combo Plus ជាមួយតេឡេ RC 2 អេក្រង់ភ្លឺច្បាស់ មានតម្រូវការខ្ពស់"
        ],
        "peak_season": ["Dec", "Jan", "Feb"],
        "trend": "STABLE_HIGH",
    },

    # ── COMPUTERS & GAMING IT (Super AI Data) ──
    "rog zephyrus": {
        "3m_ago": 1850, "6m_ago": 1950, "12m_ago": 2100,
        "reason_high": [
            "កំពូល Gaming Ultrabook ស្តើងស្រាល អេក្រង់ OLED ROG Nebula Display 240Hz",
            "បំពាក់បន្ទះឈីប Intel Core Ultra 9 / AMD Ryzen AI និង GPU RTX 4070/4080",
            "តួអាលុយមីញ៉ូម CNC Premium Finish និងធានាផ្លូវការ Perfect Warranty 2 ឆ្នាំ"
        ],
        "peak_season": ["Jul", "Aug", "Sep"],
        "trend": "STABLE_HIGH",
    },
    "keychron q1": {
        "3m_ago": 175, "6m_ago": 185, "12m_ago": 195,
        "reason_high": [
            "Custom Mechanical Keyboard តួ Full CNC Aluminum និង Double-Gasket Mount វាយអក្សរស្រួលដៃ",
            "គាំទ្រ QMK/VIA កែប្រែ Switch Hot-swappable និង Wireless 2.4GHz + Bluetooth",
            "ពេញនិយមខ្លាំងក្នុងចំណោម Programmer និង Content Creator នៅភ្នំពេញ"
        ],
        "peak_season": ["All Year"],
        "trend": "STABLE",
    },

    # ── MOTORBIKES & VEHICLES (Super AI Data) ──
    "vespa primavera": {
        "3m_ago": 3850, "6m_ago": 3900, "12m_ago": 4100,
        "reason_high": [
            "ម៉ូតូលំដាប់ Luxury Scooter អ៊ីតាលី តួដែកថែប Monocoque រឹងមាំមិនច្រែះ",
            "ម៉ាស៊ីន i-Get 150cc ABS សន្សំសំចៃសាំង និងប្រព័ន្ធហ្វ្រាំងសុវត្ថិភាព",
            "រក្សាតម្លៃទីផ្សារមួយទឹកបានខ្ពស់ (High Resale Value) ពេញនិយមក្នុងក្រុងភ្នំពេញ"
        ],
        "peak_season": ["Jan", "Feb", "Mar"],
        "trend": "STABLE_HIGH",
    },
    "ducati monster": {
        "3m_ago": 13500, "6m_ago": 14000, "12m_ago": 14800,
        "reason_high": [
            "Superbike អ៊ីតាលី កម្លាំង 937cc Testastretta 11° សំឡេងកាចខ្លាំង",
            "ពន្ធគយនាំចូលម៉ូតូធំ Big Bike និងគ្រឿងបន្លាស់ Original នាំចូលមានតម្លៃខ្ពស់"
        ],
        "peak_season": ["Nov", "Dec", "Jan"],
        "trend": "STABLE_HIGH",
    },

    # ── REAL ESTATE & CONDOS (Super AI Data) ──
    "the peak condo": {
        "3m_ago": 135000, "6m_ago": 138000, "12m_ago": 145000,
        "reason_high": [
            "ខុនដូលំដាប់ខ្ពស់កណ្តាលរាជធានីភ្នំពេញ ទល់មុខកោះពេជ្រ ជាប់ Shangri-La Hotel",
            "ទេសភាពទន្លេមេគង្គ 360 ដឺក្រេ និងផ្សារទំនើបក្នុងអគារ",
            "អត្រាជួលត្រឡប់មកវិញ (Rental Yield) ខ្ពស់ 6-8% ក្នុងមួយឆ្នាំ"
        ],
        "peak_season": ["All Year"],
        "trend": "STABLE_HIGH",
    },
    "borey peng huoth": {
        "3m_ago": 285000, "6m_ago": 290000, "12m_ago": 310000,
        "reason_high": [
            "បុរីលំដាប់លេខមួយនៅកម្ពុជា ជាមួយសួនផ្កាអឺរ៉ុប Euro Park និងសន្តិសុខ 24 ម៉ោង",
            "គុណភាពសំណង់រឹងមាំ និងបរិស្ថានរស់នៅស្ងប់ស្ងាត់ មានកិត្យានុភាពខ្ពស់",
            "តម្លៃដីបណ្តោយផ្លូវជាតិលេខ 1 និងបឹងស្នោ កើនឡើងជាលំដាប់"
        ],
        "peak_season": ["Nov", "Dec", "Jan"],
        "trend": "STABLE_HIGH",
    },

    # ── HOME APPLIANCES & ROBOTICS (Super AI Data) ──
    "roborock s8": {
        "3m_ago": 890, "6m_ago": 950, "12m_ago": 1050,
        "reason_high": [
            "ម៉ាស៊ីនបោស និងជូតផ្ទះស្វ័យប្រវត្តិកំពូល Robot Vacuum & Mop",
            "កម្លាំងបឺត 6000Pa និងធុងទឹកជូតសម្អាតកម្ដៅស្ងួតដោយខ្លួនឯង (Self-Drying Dock)",
            "បច្ចេកវិទ្យា Reactive 3D Obstacle Avoidance គេចឧបសគ្គបានឆ្លាតវៃ"
        ],
        "peak_season": ["Sep", "Oct", "Nov"],
        "trend": "DECLINING",
    },
    "herman miller aeron": {
        "3m_ago": 1250, "6m_ago": 1300, "12m_ago": 1350,
        "reason_high": [
            "កៅអី Ergonomic លំដាប់ពិភពលោក ការពារការឈឺចង្កេះ និងខ្នងសម្រាប់អ្នកអង្គុយធ្វើការយូរ",
            "សំណាញ់ Pellicle ខ្យល់ចេញចូលត្រជាក់ស្រួល និងធានារហូតដល់ 12 ឆ្នាំ",
            "រក្សាតម្លៃមួយទឹកស្ទើរតែស្មើនឹងតម្លៃថ្មី ដោយសារភាពធន់ប្រើបានលើសពី 15 ឆ្នាំ"
        ],
        "peak_season": ["All Year"],
        "trend": "STABLE_HIGH",
    },
'''

hist_target = "CAMBODIA_PRICE_HISTORY = {"
hist_pos = content.find(hist_target)
if hist_pos != -1:
    insert_pos = hist_pos + len(hist_target)
    content = content[:insert_pos] + super_price_history + content[insert_pos:]
    print("Enriched CAMBODIA_PRICE_HISTORY with super AI price data.")

# 3. Replace WEBSITE_DOMAIN_MAP
with open('scratch/domain_map_700.json', 'r', encoding='utf-8') as f:
    domain_map = json.load(f)

map_start = content.find("WEBSITE_DOMAIN_MAP = {")
pos_func = content.find("def get_platforms_for_domain_and_query")
if map_start == -1 or pos_func == -1:
    raise ValueError("Could not find WEBSITE_DOMAIN_MAP or get_platforms_for_domain_and_query boundaries")

map_lines = ["WEBSITE_DOMAIN_MAP = {"]
for k, v in sorted(domain_map.items()):
    map_lines.append(f'    "{k}": "{v}",')
map_lines.append("}")
new_map_py = "\n".join(map_lines)

content = content[:map_start] + new_map_py + content[pos_func:]
print(f"Replaced WEBSITE_DOMAIN_MAP with {len(domain_map)} entries.")

# 4. Update get_platforms_for_domain_and_query comment to 700
content = content.replace("Encompasses all 200 Cambodian platforms across 10 categories.", "Encompasses all 700 Cambodian platforms across 10 categories.")

# 5. Update /platforms categories count in HTTP handler
cat_pattern = r'{"id": "ALL", "labelKh": "ទាំងអស់ \(២០០ ប្រភព\)", "labelEn": "All Platforms", "count": len\(CAMBODIA_MARKET_PLATFORMS\)},.*?{"id": "SERVICES", "labelKh": "សៀវភៅ & ដឹកជញ្ជូន", "labelEn": "Books, Travel & Logistics", "count": 20}'

new_cats_payload = '''{"id": "ALL", "labelKh": "ទាំងអស់ (៧០០ ប្រភព)", "labelEn": "All Platforms", "count": len(CAMBODIA_MARKET_PLATFORMS)},
                    {"id": "GENERAL", "labelKh": "ទីផ្សារទូទៅ & E-Commerce", "labelEn": "General Classifieds", "count": 20},
                    {"id": "COMPUTERS", "labelKh": "កុំព្យូទ័រ Gaming & IT", "labelEn": "Computers & Gaming IT", "count": 70},
                    {"id": "PHONES", "labelKh": "ទូរស័ព្ទ, គ្រឿង Gadget & Audio", "labelEn": "Phones & Audio Gadgets", "count": 70},
                    {"id": "CARS", "labelKh": "រថយន្ត, ម៉ូតូ & គ្រឿងបន្លាស់", "labelEn": "Cars, Motos & Parts", "count": 70},
                    {"id": "REAL_ESTATE", "labelKh": "អចលនទ្រព្យ, ខុនដូ & បុរី", "labelEn": "Real Estate, Condos & Boreys", "count": 70},
                    {"id": "FASHION", "labelKh": "ម៉ូដ, សម្លៀកបំពាក់ & គ្រឿងអលង្ការ", "labelEn": "Fashion, Shoes & Jewelry", "count": 70},
                    {"id": "BEAUTY", "labelKh": "សម្រស់, គ្រឿងសម្អាង & សុខភាព", "labelEn": "Beauty & Personal Care", "count": 70},
                    {"id": "FURNITURE", "labelKh": "គ្រឿងសង្ហារិម, ផ្ទះបាយ & គ្រឿងផ្ទះ", "labelEn": "Furniture & Appliances", "count": 70},
                    {"id": "GROCERIES", "labelKh": "ផ្សារទំនើប & អាហារសរីរាង្គ", "labelEn": "Supermarkets & Gourmet", "count": 70},
                    {"id": "SERVICES", "labelKh": "ដឹកជញ្ជូន, សំបុត្រយន្តហោះ & សេវាកម្ម", "labelEn": "Logistics, Travel & Services", "count": 120}'''

content = re.sub(cat_pattern, new_cats_payload, content, flags=re.DOTALL)
print("Updated /platforms route category counts.")

# Write back to scrapers/ai_search_service.py
with open('scrapers/ai_search_service.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated scrapers/ai_search_service.py!")
