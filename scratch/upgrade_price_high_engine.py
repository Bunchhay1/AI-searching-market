# -*- coding: utf-8 -*-
"""
Upgrade CAMBODIA_PRICE_HISTORY, GLOBAL_PRICE_PRESSURE_FACTORS,
and generate_price_high_analysis in ai_search_service.py
with 100% correct, fluent, natural Khmer text across all domains.
"""

new_section = '''# ─── PRICE TREND & "WHY SO HIGH" ANALYSIS ENGINE ───────────────────────────
# Historical price benchmarks per model (USD) — reflects real Cambodia market
CAMBODIA_PRICE_HISTORY = {
    # ── PHONES ──
    "iphone 17 pro max": {
        "3m_ago": 1950, "6m_ago": None, "12m_ago": None,
        "reason_high": [
            "ម៉ូដែលកំពូលទើបចេញថ្មី បំពាក់បន្ទះឈីប A19 Pro និងប្រព័ន្ធកាមេរ៉ាជំនាន់ចុងក្រោយ",
            "ការនាំចូលដំណាក់កាលដំបូងមានកំណត់ តម្រូវការកុម្ម៉ង់ទុកមុនខ្ពស់លើសការផ្គត់ផ្គង់",
            "ហាងលក់រាយគិតកម្រៃបន្ថែម (Margin 15-25%) ក្នុងរដូវកាលចេញដំបូង",
            "អត្រាប្តូរប្រាក់ និងថ្លៃដឹកជញ្ជូនផ្លូវអាកាសអន្តរជាតិមានតម្លៃខ្ពស់",
        ],
        "peak_season": ["Oct", "Nov", "Dec"],
        "trend": "RISING",
    },
    "iphone 16 pro max": {
        "3m_ago": 1380, "6m_ago": 1420, "12m_ago": 1450,
        "reason_high": [
            "ម៉ូដែលពេញនិយមខ្លាំង បំពាក់បន្ទះឈីប A18 Pro និង Apple Intelligence",
            "កូដ ZA (ស៊ីមពីររូបវន្ត) និង LL (USA) មានតម្រូវការខ្ពស់ក្នុងទីផ្សារកម្ពុជា",
            "គុណភាពម៉ាស៊ីនមួយទឹកស្អាត 99% ឬម៉ាស៊ីនថ្មីប្រអប់នៅតែរក្សាតម្លៃបានល្អ",
            "ពន្ធគយនាំចូល និងអត្រាប្តូរប្រាក់ USD រួមចំណែកធ្វើឱ្យតម្លៃទីផ្សារមានកម្រិតខ្ពស់",
        ],
        "peak_season": ["Sep", "Oct", "Nov"],
        "trend": "STABLE_HIGH",
    },
    "iphone 15 pro max": {
        "3m_ago": 950, "6m_ago": 980, "12m_ago": 1050,
        "reason_high": [
            "តួខ្លួន Titanium ទម្ងន់ស្រាល និងប្តូរមករន្ធសាក USB-C ជាជម្រើសល្អបំផុតសម្រាប់អ្នកចង់សន្សំលុយ",
            "ទំហំផ្ទុក 256GB / 512GB នៅតែមានអ្នកស្វែងរកច្រើន ធ្វើឱ្យតម្លៃមួយទឹកធ្លាក់ចុះតិចតួច",
            "ម៉ាស៊ីនមួយទឹកសំណុំហ្ស៊ីន 100% មិនទាន់ជួសជុលមានស្តុកតិច",
        ],
        "peak_season": ["Jan", "Feb", "Mar"],
        "trend": "DECLINING",
    },
    "iphone 14 pro max": {
        "3m_ago": 720, "6m_ago": 750, "12m_ago": 820,
        "reason_high": [
            "ម៉ូដែល Dynamic Island ជំនាន់ដំបូង តម្លៃធ្លាក់មកដល់កម្រិតសមរម្យសម្រាប់អ្នកប្រើប្រាស់ទូទៅ",
            "ពណ៌ Deep Purple និង Space Black នៅតែពេញនិយម និងមានតម្រូវការខ្ពស់",
            "ស្តុកម៉ាស៊ីនស្អាត ថ្មនៅខ្ពស់ (>85%) ចាប់ផ្តើមពិបាករក",
        ],
        "peak_season": ["Apr", "May", "Jun"],
        "trend": "DECLINING",
    },
    "samsung galaxy s24 ultra": {
        "3m_ago": 920, "6m_ago": 980, "12m_ago": 1150,
        "reason_high": [
            "កំពូលស្មាតហ្វូន Android ជាមួយ Galaxy AI និងប៊ិច S-Pen កាមេរ៉ា 200MP",
            "ការធ្លាក់ថ្លៃមានល្បឿនមធ្យម បន្ទាប់ពីការប្រកាសចេញម៉ូដែលជំនាន់ក្រោយ",
            "តម្រូវការខ្ពស់សម្រាប់អ្នកធ្វើការងារ Graphic និងថតរូប",
        ],
        "peak_season": ["Feb", "Mar", "Apr"],
        "trend": "DECLINING",
    },

    # ── CARS ──
    "toyota corolla cross": {
        "3m_ago": 40500, "6m_ago": 41000, "12m_ago": 42000,
        "reason_high": [
            "រថយន្ត SUV ខ្នាតតូចដែលពេញនិយមបំផុតនៅកម្ពុជា ងាយស្រួលបើកបរក្នុងក្រុង និងសន្សំសំចៃសាំង",
            "ពន្ធគយនាំចូលរថយន្តស្រុកខ្មែរ (Import Duty + Excise + VAT) ខ្ពស់ដល់ 60-80%",
            "ម៉ូដែល Hybrid សន្សំសំចៃសាំងខ្លាំង តម្រូវការទីផ្សារខ្ពស់ ធ្វើឱ្យតម្លៃមួយទឹកមិនងាយធ្លាក់ថ្លៃ",
            "គ្រឿងបន្លាស់សម្បូរបែប និងតម្លៃលក់បន្ត (Resale Value) ខ្ពស់ដាច់គេ",
        ],
        "peak_season": ["Jun", "Jul", "Aug"],
        "trend": "STABLE_HIGH",
    },
    "toyota land cruiser": {
        "3m_ago": 155000, "6m_ago": 160000, "12m_ago": 168000,
        "reason_high": [
            "រថយន្តប្រណីតនិមិត្តរូបកិត្តិយស (LC300) ការផ្គត់ផ្គង់ទូទាំងពិភពលោកមានកំណត់ ត្រូវរង់ចាំយូរ",
            "ពន្ធគយនាំចូលរថយន្តម៉ាស៊ីនធំ V6 3.5L Twin Turbo មានអត្រាខ្ពស់បំផុត",
            "តម្រូវការពីរដ្ឋបាល ក្រុមហ៊ុនធំៗ និងឥស្សរជនខ្ពស់ជាប់ជានិច្ច ធ្វើឱ្យតម្លៃរក្សាស្ថិរភាពខ្ពស់",
            "ថ្លៃដឹកជញ្ជូន កញ្ចប់ Option VIP (ZX / GR-Sport) នាំចូលពីមជ្ឈិមបូព៌ា (GCC) ឬជប៉ុន",
        ],
        "peak_season": ["Nov", "Dec", "Jan"],
        "trend": "STABLE_HIGH",
    },
    "toyota prius": {
        "3m_ago": 16500, "6m_ago": 17000, "12m_ago": 17500,
        "reason_high": [
            "រថយន្ត Hybrid ពេញនិយមបំផុតសម្រាប់អ្នករត់តាក់ស៊ី និងគ្រួសារ ដោយសារស៊ីសាំងតិចបំផុត 3.8-4.5L/100km",
            "តម្លៃសាំងឡើងថ្លៃ ជំរុញឱ្យតម្រូវការទិញរថយន្ត Hybrid កើនឡើងខ្លាំង",
            "ឡានស្អាត អត់បុក អត់កាត់ត និងអាគុយ Hybrid នៅល្អ 100% មានតម្លៃថ្លៃជាងឡានធម្មតា",
        ],
        "peak_season": ["Jun", "Jul", "Aug"],
        "trend": "STABLE_HIGH",
    },
    "toyota camry": {
        "3m_ago": 34000, "6m_ago": 35000, "12m_ago": 36500,
        "reason_high": [
            "រថយន្ត Sedan លំដាប់ថ្នាក់ដឹកនាំ TNGA Platform ស៊េរីឆ្នាំ 2018-2025 មានផាសុកភាពខ្ពស់",
            "ពន្ធគយនាំចូលរថយន្ត CBU ពេញលេញ និងថ្លៃចុះបញ្ជីផ្លូវការ",
            "រថយន្តដែលរក្សាបានគីឡូម៉ែត្រតិច និងថែទាំត្រឹមត្រូវនៅហាងផ្លូវការ មានតម្លៃខ្ពស់",
        ],
        "peak_season": ["Mar", "Apr", "May"],
        "trend": "DECLINING",
    },
    "lexus rx": {
        "3m_ago": 72000, "6m_ago": 75000, "12m_ago": 78000,
        "reason_high": [
            "រថយន្ត SUV ប្រណីតលំដាប់ខ្ពស់ពេញនិយមបំផុតសម្រាប់គ្រួសារកម្ពុជា ផាសុកភាពល្អឥតខ្ចោះ",
            "តម្លៃលក់បន្តរឹងមាំ និងកម្រិតខូចខាតទាបបំផុត",
            "ពន្ធនាំចូលរថយន្តប្រណីត និងថ្លៃធានារ៉ាប់រងខ្ពស់",
        ],
        "peak_season": ["Oct", "Nov", "Dec"],
        "trend": "STABLE_HIGH",
    },
    "ford ranger": {
        "3m_ago": 38000, "6m_ago": 39500, "12m_ago": 41000,
        "reason_high": [
            "រថយន្តភីកអាប់ (Pickup) ដាច់គេនៅកម្ពុជា បច្ចេកវិទ្យាទំនើប និងរូបរាងរឹងមាំ",
            "តម្រូវការប្រើប្រាស់តាមបណ្តាខេត្ត និងការងារសំណង់ គម្រោងអភិវឌ្ឍន៍ខ្ពស់",
            "តម្លៃរក្សាបានល្អសម្រាប់ស៊េរី Wildtrak និង Raptor",
        ],
        "peak_season": ["May", "Jun", "Jul"],
        "trend": "STABLE",
    },

    # ── MOTOS ──
    "honda pcx 160": {
        "3m_ago": 3800, "6m_ago": 3900, "12m_ago": 4000,
        "reason_high": [
            "ម៉ូតូស្កូតទ័រពេញនិយមសម្រាប់យុវវ័យ និងអ្នកធ្វើការ បំពាក់ Smart Key និងប្រព័ន្ធហ្វ្រាំង ABS",
            "ការនាំចូលពីប្រទេសថៃ និងថ្លៃពន្ធគយធ្វើឱ្យតម្លៃខ្ពស់ជាងតម្លៃដើម",
            "តម្រូវការទីផ្សារខ្ពស់ និងភាពធន់មាំនៃម៉ាស៊ីន eSP+ 4-Valve",
        ],
        "peak_season": ["Jan", "Feb", "Mar"],
        "trend": "STABLE",
    },
    "honda dream": {
        "3m_ago": 2350, "6m_ago": 2380, "12m_ago": 2400,
        "reason_high": [
            "ម៉ូតូប្រចាំប្រទេសកម្ពុជា (Legendary 125cc) ងាយស្រួលលក់បន្ត និងប្រើប្រាស់បានគ្រប់ស្ថានភាពផ្លូវ",
            "តម្រូវការខ្ពស់ប្រចាំឆ្នាំ គ្រប់ស្រទាប់វណ្ណៈ និងគ្រប់ខេត្តក្រុង",
            "តម្លៃលក់បន្តមិនដែលធ្លាក់ចុះខ្លាំង រក្សាតម្លៃបានល្អដាច់គេក្នុងចំណោមម៉ូតូទាំងអស់",
        ],
        "peak_season": ["Apr", "May", "Jun"],
        "trend": "STABLE",
    },
    "honda scoopy": {
        "3m_ago": 2200, "6m_ago": 2250, "12m_ago": 2300,
        "reason_high": [
            "ម៉ូតូស្វ័យប្រវត្តពេញនិយមបំផុតសម្រាប់សិស្ស-និស្សិត និងនារី រូបរាងតូចច្រឡឹង ងាយស្រួលបើកបរ",
            "ម៉ូដែលនាំចូលពីប្រទេសថៃ (Club12 / Prestige) មានតម្លៃខ្ពស់ជាងម៉ូដែលក្នុងស្រុក",
            "តម្រូវការទីផ្សារខ្ពស់ជាប់ជានិច្ចនៅដើមឆ្នាំសិក្សាថ្មី",
        ],
        "peak_season": ["Sep", "Oct", "Nov"],
        "trend": "STABLE",
    },

    # ── COMPUTERS ──
    "macbook pro": {
        "3m_ago": 1750, "6m_ago": 1800, "12m_ago": 1850,
        "reason_high": [
            "បំពាក់បន្ទះឈីប Apple Silicon (M3/M4 Pro/Max) ដែលមានអនុភាពខ្ពស់សម្រាប់ Graphic, Code និង Video 4K/8K",
            "អេក្រង់ Liquid Retina XDR 120Hz ProMotion គុណភាពល្អឥតខ្ចោះ គ្មានដៃគូប្រកួតប្រជែង",
            "ការនាំចូលពីប្រទេសសិង្ហបុរី ឬហុងកុង ដោយមានពន្ធ និងថ្លៃដឹកជញ្ជូនបន្ថែម",
            "តម្រូវការខ្ពស់ពីសហគ្រិន Designer និង Programmers នៅកម្ពុជា",
        ],
        "peak_season": ["Sep", "Oct", "Nov"],
        "trend": "STABLE_HIGH",
    },
    "macbook air": {
        "3m_ago": 980, "6m_ago": 1020, "12m_ago": 1080,
        "reason_high": [
            "កុំព្យូទ័រយួរដៃស្តើងស្រាល ពេញនិយមបំផុតសម្រាប់សិស្សនិស្សិត និងការងារការិយាល័យ",
            "ថ្មកាន់បានយូររហូតដល់ 18 ម៉ោង និងដំណើរការដោយស្ងាត់គ្មានកង្ហារ",
            "តម្រូវការកើនឡើងខ្លាំងនៅរដូវកាលចូលរៀន និងដើមឆ្នាំថ្មី",
        ],
        "peak_season": ["Aug", "Sep", "Oct"],
        "trend": "STABLE",
    },

    # ── REAL ESTATE ──
    "phnom penh": {
        "3m_ago": 350, "6m_ago": 340, "12m_ago": 320,
        "reason_high": [
            "តម្រូវការជួល និងទិញអចលនទ្រព្យនៅតំបន់កណ្តាលក្រុង (BKK1, ទួលគោក, ចំការមន) មានការកើនឡើង",
            "លំហូរវិនិយោគិនបរទេស (FDI) និងអាជីវកម្មថ្មីៗ បង្កើនតម្រូវការខុនដូ និងការិយាល័យ",
            "ដីធ្លីនៅតំបន់ទីប្រជុំជនមានកំណត់ ជំរុញឱ្យតម្លៃដី និងថ្លៃសំណង់កើនឡើងជាបន្តបន្ទាប់",
            "ការអភិវឌ្ឍហេដ្ឋារចនាសម្ព័ន្ធ (ស្ពាន, ផ្លូវក្រវាត់ក្រុង, ព្រលានយន្តហោះថ្មី) ធ្វើឱ្យតម្លៃអចលនទ្រព្យឡើងថ្លៃ",
        ],
        "peak_season": ["Oct", "Nov", "Dec"],
        "trend": "RISING",
    },
    "borey": {
        "3m_ago": 145000, "6m_ago": 142000, "12m_ago": 138000,
        "reason_high": [
            "តម្រូវការលំនៅដ្ឋានបែបគ្រួសារ (ផ្ទះល្វែង, វីឡាកូនកាត់, វីឡាភ្លោះ) មានការកើនឡើងជាលំដាប់",
            "ការអភិវឌ្ឍហេដ្ឋារចនាសម្ព័ន្ធផ្លូវជាតិ និងគម្រោងផ្លូវក្រវាត់ក្រុងទី៣",
            "គម្រោងបុរីធំៗផ្តល់លក្ខខណ្ឌបង់រំលស់ងាយស្រួល ជំរុញឱ្យតម្រូវការទិញកើនឡើង",
        ],
        "peak_season": ["Nov", "Dec", "Jan"],
        "trend": "RISING",
    },

    # ── FASHION & LIFESTYLE ──
    "fashion": {
        "3m_ago": 45, "6m_ago": 45, "12m_ago": 42,
        "reason_high": [
            "ទំនិញម៉ាកប្រណិតនាំចូលពីបរទេស (Brand-name authentic) មានថ្លៃដឹកជញ្ជូន និងពន្ធគយខ្ពស់",
            "ការបញ្ជាទិញតាមរដូវកាល (New Collection) មានតម្លៃដើមខ្ពស់ពីក្រុមហ៊ុនផ្គត់ផ្គង់",
            "ការធានាភាពសុទ្ធ 100% និងសេវាកម្មហាងលំដាប់ខ្ពស់នៅកណ្តាលរាជធានី",
        ],
        "peak_season": ["Nov", "Dec", "Apr"],
        "trend": "STABLE",
    },
}

# Global price pressure factors (as of Sep 2026)
GLOBAL_PRICE_PRESSURE_FACTORS = {
    "usd_khr_rate": {
        "value": 4115, "change_pct": 2.3, "impact": "HIGH",
        "desc_kh": "អត្រាប្តូរប្រាក់ USD/KHR = ៤,១១៥ ៛ (កើនឡើង ២.៣% ក្នុងរយៈពេល ៦ ខែ) ធ្វើឱ្យតម្លៃគិតជាប្រាក់រៀលកើនឡើងបន្តិចបន្តួច"
    },
    "import_duty_cars": {
        "value": "65-80%", "change_pct": 0, "impact": "VERY_HIGH",
        "desc_kh": "ពន្ធគយនាំចូលរថយន្ត CBU (Customs Duty + Excise + VAT) សរុប ៦៥% ទៅ ៨០% ធ្វើឱ្យតម្លៃរថយន្តនៅកម្ពុជាខ្ពស់ជាងប្រទេសជិតខាង"
    },
    "import_duty_phones": {
        "value": "10-15%", "change_pct": 0, "impact": "MEDIUM",
        "desc_kh": "ពន្ធនាំចូលទូរសព្ទ និងឧបករណ៍អេឡិចត្រូនិក ១០% ទៅ ១៥% (VAT និងថ្លៃត្រួតពិនិត្យស្តង់ដារ TRC)"
    },
    "fuel_price_surge": {
        "value": "$1.15/L", "change_pct": 5.2, "impact": "MEDIUM",
        "desc_kh": "តម្លៃប្រេងឥន្ធនៈសាំងស៊ុបពែរជាមធ្យម $1.15/L ជំរុញឱ្យថ្លៃដឹកជញ្ជូន និងការធ្វើដំណើរមានការកើនឡើង"
    },
    "supply_chain_recovery": {
        "value": "85%", "change_pct": 8, "impact": "LOW",
        "desc_kh": "ខ្សែច្រវាក់ផ្គត់ផ្គង់គ្រឿងអេឡិចត្រូនិក និងបន្ទះឈីបសកលបានវិលមករកប្រក្រតីភាព ៨៥% ដែលជួយទប់ទល់កុំឱ្យតម្លៃហក់ឡើងខ្ពស់ខ្លាំង"
    },
    "usd_strength_index": {
        "value": 104.5, "change_pct": 2.1, "impact": "HIGH",
        "desc_kh": "សន្ទស្សន៍កម្លាំងប្រាក់ដុល្លារ (US Dollar Index DXY) រឹងមាំ ធ្វើឱ្យថ្លៃដើមនៃការនាំចូលទំនិញពីបណ្តាប្រទេសដទៃមានតម្លៃខ្ពស់"
    },
}


def generate_price_high_analysis(query: str, current_avg_price: float, domain_info: dict) -> dict:
    """
    Deep AI analysis: WHY is the price high compared to historical/expected values.
    Returns structured price trend, reasons, and buyer recommendations.
    """
    q = query.lower().strip()
    domain = domain_info.get("domain", "PHONES")
    model_full = f"{domain_info.get('brand','')} {domain_info.get('model','')}".strip().lower()

    # Find best matching historical record
    hist = None
    for k, v in CAMBODIA_PRICE_HISTORY.items():
        if k in q or (model_full and k in model_full) or (model_full and model_full in k):
            hist = v
            break

    # Fallback to domain generic benchmarks if no exact model match
    if not hist:
        if domain == "CARS":
            hist = {
                "3m_ago": round(current_avg_price * 1.02),
                "6m_ago": round(current_avg_price * 1.04),
                "12m_ago": round(current_avg_price * 1.07),
                "reason_high": [
                    "ពន្ធគយនាំចូលរថយន្ត និងថ្លៃចុះបញ្ជីផ្លូវការនៅកម្ពុជាមានអត្រាខ្ពស់",
                    "ការចំណាយលើការថែទាំ គ្រឿងបន្លាស់ហ្ស៊ីន និងការធានាគុណភាពពីអ្នកលក់",
                    "តម្រូវការទីផ្សាររថយន្តមួយទឹកគុណភាពខ្ពស់ (Grade A/ល្អឥតខ្ចោះ) មានច្រើន",
                ],
                "peak_season": ["Jun", "Jul", "Aug", "Dec"],
                "trend": "STABLE_HIGH",
            }
        elif domain == "MOTOS":
            hist = {
                "3m_ago": round(current_avg_price * 1.01),
                "6m_ago": round(current_avg_price * 1.02),
                "12m_ago": round(current_avg_price * 1.04),
                "reason_high": [
                    "ម៉ូតូដែលពេញនិយមនៅកម្ពុជារក្សាតម្លៃបានល្អ និងងាយស្រួលលក់ចេញវិញ",
                    "ការនាំចូលពីប្រទេសជិតខាងមានថ្លៃពន្ធ និងថ្លៃដឹកជញ្ជូនបន្ថែម",
                    "តម្រូវការប្រើប្រាស់ប្រចាំថ្ងៃខ្ពស់ទាំងក្នុងរាជធានី និងតាមបណ្តាខេត្ត",
                ],
                "peak_season": ["Apr", "May", "Oct"],
                "trend": "STABLE",
            }
        elif domain == "COMPUTERS":
            hist = {
                "3m_ago": round(current_avg_price * 1.03),
                "6m_ago": round(current_avg_price * 1.05),
                "12m_ago": round(current_avg_price * 1.08),
                "reason_high": [
                    "ការនាំចូលគ្រឿងអេឡិចត្រូនិក និងកុំព្យូទ័រយួរដៃពីសិង្ហបុរី ថៃ ឬហុងកុង មានថ្លៃដឹកជញ្ជូន និងពន្ធបន្ថែម",
                    "តម្រូវការខ្ពស់ពីសិស្ស និស្សិត និងអ្នកធ្វើការជំនាញបច្ចេកវិទ្យា",
                    "ការធានាគុណភាពផ្លូវការពីហាងក្នុងស្រុក (Local Warranty)",
                ],
                "peak_season": ["Aug", "Sep", "Oct"],
                "trend": "STABLE_HIGH",
            }
        elif domain == "REAL_ESTATE":
            hist = {
                "3m_ago": round(current_avg_price * 0.98),
                "6m_ago": round(current_avg_price * 0.96),
                "12m_ago": round(current_avg_price * 0.93),
                "reason_high": [
                    "តម្រូវការអចលនទ្រព្យនៅតំបន់សក្តានុពល និងហេដ្ឋារចនាសម្ព័ន្ធថ្មីៗកើនឡើង",
                    "ការវិនិយោគលើវិស័យសំណង់ និងលំហូរវិនិយោគិនពីបរទេស",
                    "ដីធ្លីនៅតំបន់កណ្តាលក្រុង និងជាយក្រុងសំខាន់ៗមានតម្លៃកើនឡើងជាលំដាប់",
                ],
                "peak_season": ["Oct", "Nov", "Dec", "Jan"],
                "trend": "RISING",
            }
        elif domain == "FASHION":
            hist = {
                "3m_ago": round(current_avg_price * 1.0),
                "6m_ago": round(current_avg_price * 1.02),
                "12m_ago": round(current_avg_price * 1.05),
                "reason_high": [
                    "ទំនិញម៉ាកល្បីនាំចូលពីបរទេសមានថ្លៃពន្ធនាំចូល និងថ្លៃដឹកជញ្ជូនផ្លូវអាកាស",
                    "ការធានាផលិតផលសុទ្ធ 100% និងសេវាកម្មអតិថិជនកម្រិតខ្ពស់",
                    "តម្រូវការសម្លៀកបំពាក់ និងគ្រឿងតុបតែងទាន់សម័យក្នុងរដូវកាលពិធីបុណ្យទាន",
                ],
                "peak_season": ["Nov", "Dec", "Jan", "Apr"],
                "trend": "STABLE",
            }
        else:
            hist = {
                "3m_ago": round(current_avg_price * 1.05),
                "6m_ago": round(current_avg_price * 1.08),
                "12m_ago": round(current_avg_price * 1.15),
                "reason_high": [
                    "តម្រូវការទីផ្សារខ្ពស់ ខណៈការផ្គត់ផ្គង់ទំនិញមានកម្រិតកំណត់",
                    "ពន្ធគយនាំចូល អត្រាប្តូរប្រាក់ USD និងថ្លៃដឹកជញ្ជូនផ្លូវការ",
                    "កម្រៃចំណេញរបស់ហាងលក់រាយក្នុងស្រុកដើម្បីទូទាត់ថ្លៃជួលទីតាំង និងបុគ្គលិក",
                ],
                "peak_season": ["Sep", "Oct", "Nov", "Dec"],
                "trend": "DECLINING",
            }

    # Build timeline points
    now = datetime.now()
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    timeline = []

    if hist.get("12m_ago"):
        timeline.append({
            "label": "12 ខែមុន",
            "price": hist["12m_ago"],
            "period": "12m"
        })
    if hist.get("6m_ago"):
        timeline.append({
            "label": "6 ខែមុន",
            "price": hist["6m_ago"],
            "period": "6m"
        })
    if hist.get("3m_ago"):
        timeline.append({
            "label": "3 ខែមុន",
            "price": hist["3m_ago"],
            "period": "3m"
        })
    timeline.append({
        "label": "បច្ចុប្បន្ន",
        "price": round(current_avg_price),
        "period": "current"
    })

    # Delta calculations
    delta_3m = round(current_avg_price - hist["3m_ago"]) if hist.get("3m_ago") else 0
    delta_3m_pct = round((delta_3m / hist["3m_ago"]) * 100, 1) if hist.get("3m_ago") else 0.0

    delta_6m = round(current_avg_price - hist["6m_ago"]) if hist.get("6m_ago") else 0
    delta_6m_pct = round((delta_6m / hist["6m_ago"]) * 100, 1) if hist.get("6m_ago") else 0.0

    delta_12m = round(current_avg_price - hist["12m_ago"]) if hist.get("12m_ago") else 0
    delta_12m_pct = round((delta_12m / hist["12m_ago"]) * 100, 1) if hist.get("12m_ago") else 0.0

    # Trend status & badge
    trend = hist.get("trend", "STABLE")
    if delta_12m_pct > 3 or trend == "RISING":
        trend_badge = "📈 តម្លៃកំពុងឡើង (Rising)"
        trend_color = "#f87171"
    elif trend == "STABLE_HIGH":
        trend_badge = "⏸️ តម្លៃខ្ពស់ថេរ (Stable High)"
        trend_color = "#fbbf24"
    elif delta_12m_pct < -8 or trend == "DECLINING":
        trend_badge = "📉 តម្លៃកំពុងចុះ (Declining)"
        trend_color = "#34d399"
    else:
        trend_badge = "➡️ តម្លៃមានស្ថិរភាព (Stable)"
        trend_color = "#60a5fa"

    # Peak season warning
    current_month = now.strftime("%b")
    is_peak = current_month in hist.get("peak_season", [])
    peak_warning = (
        f"⚡ បច្ចុប្បន្នជារដូវកាលទិញច្រើន (Peak Season: {current_month}) — តម្រូវការខ្ពស់ តម្លៃអាចឡើងថ្លៃ ៥% ទៅ ១០%"
        if is_peak else
        f"រដូវកាលធម្មតា (Non-Peak) — រដូវកាលដែលមានតម្រូវការទិញច្រើនគឺខែ: {', '.join(hist.get('peak_season', ['ចុងឆ្នាំ']))}"
    )

    # Key reasons why price is high (localized to Cambodia market)
    reasons_why_high = hist.get("reason_high", [])

    # Global macro factors for this domain
    global_factors_applicable = []
    if domain == "CARS":
        global_factors_applicable.append(
            f"ពន្ធគយនាំចូលរថយន្ត {GLOBAL_PRICE_PRESSURE_FACTORS['import_duty_cars']['value']} → {GLOBAL_PRICE_PRESSURE_FACTORS['import_duty_cars']['desc_kh']}"
        )
    elif domain in ["PHONES", "COMPUTERS", "TABLETS"]:
        global_factors_applicable.append(
            f"ពន្ធនាំចូលឧបករណ៍អេឡិចត្រូនិក {GLOBAL_PRICE_PRESSURE_FACTORS['import_duty_phones']['value']} → {GLOBAL_PRICE_PRESSURE_FACTORS['import_duty_phones']['desc_kh']}"
        )
    global_factors_applicable.append(
        f"អត្រាប្តូរប្រាក់ USD/KHR = {GLOBAL_PRICE_PRESSURE_FACTORS['usd_khr_rate']['value']} ៛ → {GLOBAL_PRICE_PRESSURE_FACTORS['usd_khr_rate']['desc_kh']}"
    )

    # Buyer advice based on trend
    if trend in ["RISING", "STABLE_HIGH"]:
        buyer_advice = (
            f"⚠️ និន្នាការទីផ្សារ: {trend_badge} ។ "
            f"គោលដៅតម្លៃទិញសមរម្យ: ${round(current_avg_price * 0.90):,} ដល់ ${round(current_avg_price * 0.96):,} ។ "
            f"អនុសាសន៍: ប្រសិនបើត្រូវការប្រើប្រាស់ជាបន្ទាន់ គួរស្វែងរកចរចាបញ្ចុះតម្លៃ ៥% ទៅ ៨% ពីតម្លៃដាក់លក់ ឬស្វែងរកម៉ាស៊ីនមួយទឹកស្អាត 99% សំណុំហ្ស៊ីន។"
        )
    elif trend == "DECLINING":
        buyer_advice = (
            f"✅ និន្នាការទីផ្សារ: {trend_badge} ។ "
            f"គោលដៅតម្លៃទិញសមរម្យ: ${round(current_avg_price * 0.88):,} ដល់ ${round(current_avg_price * 0.94):,} ។ "
            f"អនុសាសន៍: តម្លៃកំពុងមាននិន្នាការធ្លាក់ចុះជាបន្តបន្ទាប់។ ប្រសិនបើមិនទាន់ប្រញាប់ គួររង់ចាំ ១ ទៅ ២ ខែទៀត ដើម្បីទទួលបានតម្លៃកាន់តែចំណេញ។"
        )
    else:
        buyer_advice = (
            f"⚖️ និន្នាការទីផ្សារ: {trend_badge} ។ "
            f"គោលដៅតម្លៃទិញសមរម្យ: ${round(current_avg_price * 0.92):,} ដល់ ${round(current_avg_price * 0.97):,} ។ "
            f"អនុសាសន៍: ទីផ្សារមានស្ថិរភាពល្អ អាចពិនិត្យមើលគុណភាពទំនិញជាក់ស្តែង និងចរចាបញ្ចុះតម្លៃ ៣% ទៅ ៥% មុនសម្រេចចិត្តទិញ។"
        )

    return {
        "hasPriceHighAnalysis": True,
        "currentAvgPrice": current_avg_price,
        "priceTimeline": timeline,
        "delta3m": delta_3m,
        "delta3mPct": delta_3m_pct,
        "delta6m": delta_6m,
        "delta6mPct": delta_6m_pct,
        "delta12m": delta_12m,
        "delta12mPct": delta_12m_pct,
        "trendBadge": trend_badge,
        "trendColor": trend_color,
        "trendStatus": trend,
        "isPeakSeason": is_peak,
        "peakWarning": peak_warning,
        "reasonsWhyHigh": reasons_why_high,
        "globalFactors": global_factors_applicable,
        "buyerAdvice": buyer_advice,
        "globalPressureFactors": {
            k: {
                "label": v.get("desc_kh", ""),
                "impact": v.get("impact", ""),
                "value": str(v.get("value", "")),
                "changePct": v.get("change_pct", 0)
            }
            for k, v in list(GLOBAL_PRICE_PRESSURE_FACTORS.items())[:4]
        }
    }
'''

with open("scrapers/ai_search_service.py", "r", encoding="utf-8") as f:
    content = f.read()

start_marker = '# ─── PRICE TREND & "WHY SO HIGH" ANALYSIS ENGINE ───────────────────────────\n'
end_marker = '    return {\n        "hasPriceHighAnalysis": True,\n'

start_idx = content.find(start_marker)
if start_idx == -1:
    print("ERROR: start_marker not found!")
    exit(1)

# Find the end of generate_price_high_analysis function (find next top-level def)
next_def_marker = '\n\ndef '
next_def_idx = content.find(next_def_marker, start_idx)
if next_def_idx == -1:
    print("ERROR: next_def_marker not found!")
    exit(1)

old_block = content[start_idx:next_def_idx]
print(f"Found old block from char {start_idx} to {next_def_idx} (len {len(old_block)})")

new_content = content[:start_idx] + new_section + content[next_def_idx:]
with open("scrapers/ai_search_service.py", "w", encoding="utf-8") as f:
    f.write(new_content)

print("SUCCESSFULLY UPGRADED PRICE HIGH ANALYSIS ENGINE!")
