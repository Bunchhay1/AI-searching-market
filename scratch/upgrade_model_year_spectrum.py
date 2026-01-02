import re

with open('scrapers/ai_search_service.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update classify_intent_and_specs to enrich trims & years when no year is specified for popular models
# Let's inspect generic Highlander without ext_year
highlander_old = '''        elif "highlander" in q:
            brand = "Toyota"
            if (ext_year and ext_year <= 2007) or any(y in q for y in ["2001", "2002", "2003", "2004", "2005", "2006", "2007"]):
                y_str = str(ext_year) if ext_year else "2003"
                model_name = f"Highlander {y_str}"
                trims = [("V6 3.0L / 3.3L Limited 4WD ប៉ុង 2 បើកដំបូល", 12800), ("2.4L Base Option ប៉ុង 1 ស្លាកលេខភ្នំពេញ", 10200)]
                years = [str(ext_year)] if ext_year else ["2001", "2002", "2003", "2004", "2005"]
                core_specs = ["ម៉ាស៊ីន V6 3.0L / 3.3L / 2.4L 4WD", "ប៉ុង 1 ឬ ប៉ុង 2 ដំបូលបើក", "ពូកស្បែក កៅអី 2-3 ជួរ", "ស៊េរីឆ្នាំ 2001-2007"]
            elif (ext_year and 2008 <= ext_year <= 2013) or any(y in q for y in ["2008", "2009", "2010", "2011", "2012", "2013"]):
                model_name = "Highlander (2008-2013)"
                trims = [("2.7L Base Option កៅអី 3 ជួរ ស្លាកលេខ 2x", 19500), ("3.5L V6 Limited Full Option ដំបូលបើក JBL", 24500)]
                years = [str(ext_year)] if ext_year else ["2008", "2010", "2012"]
                core_specs = ["ម៉ាស៊ីន 2.7L / 3.5L V6 កៅអី 3 ជួរ", "ដំបូលបើក Sunroof & Smart Key", "JBL Premium Audio", "ស៊េរីឆ្នាំ 2008-2013"]
            else:
                model_name = "Highlander (New Gen)"
                trims = [("3.5L V6 XLE Captain Seats 7-Seats", 33500), ("2.5L Hybrid Platinum / Limited AWD", 58000)]
                years = ["2024", "2023", "2021", "2018"]
                core_specs = ["ម៉ាស៊ីន V6 / 2.5L Hybrid 7-Seats", "Captain Chairs & Panoramic Roof", "Toyota Safety Sense (TSS)", "ស៊េរីឆ្នាំ 2018-2024"]'''

highlander_new = '''        elif "highlander" in q:
            brand = "Toyota"
            if (ext_year and ext_year <= 2007) or any(y in q for y in ["2001", "2002", "2003", "2004", "2005", "2006", "2007"]):
                y_str = str(ext_year) if ext_year else "2003"
                model_name = f"Highlander {y_str}"
                trims = [("2.4L Base Option ប៉ុង 1 ស្លាកលេខភ្នំពេញ", 10200), ("V6 3.0L / 3.3L Limited 4WD ប៉ុង 2 បើកដំបូល", 12800)]
                years = [str(ext_year)] if ext_year else ["2001", "2003", "2005"]
                core_specs = ["ម៉ាស៊ីន V6 3.0L / 3.3L / 2.4L 4WD", "ប៉ុង 1 ឬ ប៉ុង 2 ដំបូលបើក", "ពូកស្បែក កៅអី 2-3 ជួរ", "ស៊េរីឆ្នាំ 2001-2007"]
            elif (ext_year and 2008 <= ext_year <= 2013) or any(y in q for y in ["2008", "2009", "2010", "2011", "2012", "2013"]):
                model_name = "Highlander (2008-2013)"
                trims = [("2.7L Base Option កៅអី 3 ជួរ ស្លាកលេខ 2x", 19500), ("3.5L V6 Limited Full Option ដំបូលបើក JBL", 24500)]
                years = [str(ext_year)] if ext_year else ["2008", "2010", "2012"]
                core_specs = ["ម៉ាស៊ីន 2.7L / 3.5L V6 កៅអី 3 ជួរ", "ដំបូលបើក Sunroof & Smart Key", "JBL Premium Audio", "ស៊េរីឆ្នាំ 2008-2013"]
            elif ext_year and ext_year >= 2014:
                model_name = f"Highlander ({ext_year})"
                trims = [("3.5L V6 XLE Captain Seats 7-Seats", 33500), ("2.5L Hybrid Platinum / Limited AWD", 58000)]
                years = [str(ext_year)]
                core_specs = ["ម៉ាស៊ីន V6 / 2.5L Hybrid 7-Seats", "Captain Chairs & Panoramic Roof", "Toyota Safety Sense (TSS)", f"ស៊េរីឆ្នាំ {ext_year}"]
            else:
                # Generic Highlander: True Cambodian market spectrum (Cheap 2003 -> Fair 2010 -> Expensive 2024)
                model_name = "Highlander"
                trims = [
                    ("2.4L Base Option ប៉ុង 1 (ស៊េរីចាស់ធូរថ្លៃ)", 10500),
                    ("V6 3.0L / 3.3L Limited 4WD ប៉ុង 2 បើកដំបូល", 12800),
                    ("2.7L Base Option កៅអី 3 ជួរ (ស៊េរីមធ្យម)", 19500),
                    ("3.5L V6 Limited Full Option JBL (ស៊េរីមធ្យម)", 24500),
                    ("3.5L V6 XLE Captain Seats (ស៊េរីថ្មី)", 34500),
                    ("2.5L Hybrid Platinum AWD ថ្មីខ្លាញ់គោ", 58000)
                ]
                years = ["2003", "2005", "2010", "2012", "2020", "2024"]
                core_specs = ["ជម្រើសចម្រុះគ្រប់ស៊េរីឆ្នាំ 2003 ដល់ 2024", "ម៉ាស៊ីន 2.4L / 3.3L / 3.5L V6 / 2.5L Hybrid", "ជម្រើសធូរថ្លៃ ដល់ជម្រើសកម្រិតខ្ពស់"]'''

content = content.replace(highlander_old, highlander_new)

# Update RX350 generic search
rx350_old = '''                else:
                    trims = [("2.4L Turbo AWD F-Sport Performance 2023+", 115000), ("350h Hybrid Luxury 2024", 125000)]
                    years = ["2024", "2023"]
                    core_specs = ["ម៉ាស៊ីន 2.4L Turbo / 2.5L Hybrid F-Sport", "អេក្រង់ 14-inch Touchscreen", "ស៊េរីឆ្នាំ 2023-2024"]'''

rx350_new = '''                elif ext_year and ext_year >= 2023:
                    trims = [("2.4L Turbo AWD F-Sport Performance 2023+", 115000), ("350h Hybrid Luxury 2024", 125000)]
                    years = ["2024", "2023"]
                    core_specs = ["ម៉ាស៊ីន 2.4L Turbo / 2.5L Hybrid F-Sport", "អេក្រង់ 14-inch Touchscreen", "ស៊េរីឆ្នាំ 2023-2024"]
                else:
                    # Generic RX350: True Cambodian market spectrum (Cheap 2008 -> Fair 2012/2017 -> Expensive 2024)
                    model_name = "RX350"
                    trims = [
                        ("3.5L V6 Touring ស្លាកលេខភ្នំពេញ (ស៊េរីចាស់ធូរថ្លៃ)", 21500),
                        ("3.5L V6 AWD Full Option បើកដំបូល (ស៊េរីចាស់)", 23500),
                        ("3.5L V6 AWD F-Sport Mouse Control (ស៊េរីមធ្យម)", 34500),
                        ("3.5L V6 AWD Premium ក្រដាសពន្ធថ្មី (ស៊េរីមធ្យម)", 62000),
                        ("3.5L V6 F-Sport Triple Beam LED (កម្រិតខ្ពស់)", 68000),
                        ("2.4L Turbo AWD F-Sport Performance ថ្មីខ្លាញ់គោ", 115000)
                    ]
                    years = ["2008", "2010", "2012", "2017", "2020", "2024"]
                    core_specs = ["ជម្រើសចម្រុះគ្រប់ជំនាន់ RX350 (2008 ដល់ 2024)", "ម៉ាស៊ីន 3.5L V6 / 2.4L Turbo F-Sport AWD", "ជម្រើសធូរថ្លៃ $21k ដល់កម្រិតខ្ពស់ $115k"]'''

content = content.replace(rx350_old, rx350_new)

# Update build_machine_batch in scrapers/ai_search_service.py to inject Tier partitioning
target_batch_setup = '''    for i in range(target_count):
        idx = machine_id * 3 + i
        recency = generate_recency_timestamp(idx)
        loc = LOCATIONS[idx % len(LOCATIONS)]

        color = domain_info["colors"][idx % len(domain_info["colors"])]
        year = domain_info.get("verified_year") if domain_info.get("verified_year") else domain_info["years"][idx % len(domain_info["years"])]
        trim_name, trim_price = domain_info["trims"][idx % len(domain_info["trims"])]'''

replacement_batch_setup = '''    for i in range(target_count):
        idx = machine_id * 3 + i
        recency = generate_recency_timestamp(idx)
        loc = LOCATIONS[idx % len(LOCATIONS)]

        color = domain_info["colors"][idx % len(domain_info["colors"])]

        # ─── SMART AI PRICE & MODEL MIX ENGINE (CHEAP vs FAIR vs EXPENSIVE) ───
        sorted_trims = sorted(domain_info["trims"], key=lambda x: x[1])
        num_trims = len(sorted_trims)
        avail_years = domain_info.get("years", ["2022"])
        num_years = len(avail_years)

        tier_mod = idx % 10  # 30% CHEAP (0,1,2), 50% FAIR (3,4,5,6,7), 20% EXPENSIVE (8,9)

        if tier_mod in [0, 1, 2]:
            # CHEAP TIER (Budget / Bargain Deal)
            price_tier = "CHEAP"
            price_tier_badge = "⚡ ធូរថ្លៃ (Budget Deal)"
            price_tier_kh = "ជម្រើសតម្លៃធូរថ្លៃ (ចំណេញថវិកា)"
            price_tier_class = "tier-cheap"
            # Lower priced trim & earlier year
            trim_idx = 0 if num_trims == 1 else (idx % max(1, num_trims // 2))
            trim_name, trim_price = sorted_trims[trim_idx]
            year = domain_info.get("verified_year") or (avail_years[-1] if num_years > 1 else avail_years[0])
        elif tier_mod in [8, 9]:
            # EXPENSIVE TIER (Premium / Flagship Spec)
            price_tier = "EXPENSIVE"
            price_tier_badge = "💎 កម្រិតខ្ពស់ (Premium Flagship)"
            price_tier_kh = "ជម្រើសកម្រិតខ្ពស់ (ថ្មីកេះ/Full Option)"
            price_tier_class = "tier-expensive"
            # Highest priced trim & latest year
            trim_name, trim_price = sorted_trims[-1]
            year = domain_info.get("verified_year") or avail_years[0]
        else:
            # FAIR TIER (Fair Market Sweet Spot)
            price_tier = "FAIR"
            price_tier_badge = "⚖️ តម្លៃទីផ្សារ (Fair Market)"
            price_tier_kh = "តម្លៃទីផ្សារសមរម្យ (ស្តង់ដារ)"
            price_tier_class = "tier-fair"
            # Median trim & mid year
            mid_trim_idx = num_trims // 2 if num_trims > 1 else 0
            trim_name, trim_price = sorted_trims[mid_trim_idx]
            mid_year_idx = num_years // 2 if num_years > 1 else 0
            year = domain_info.get("verified_year") or avail_years[mid_year_idx]'''

content = content.replace(target_batch_setup, replacement_batch_setup)

# Inject priceTier fields into batch.append dict
target_dict_entry = '''            "conditionKhmer": cond_badge,
            "isSmartCheap": is_smart_cheap,
            "savingsVsNewUsd": savings_vs_new,
            "priceUsd": item_price,'''

replacement_dict_entry = '''            "conditionKhmer": cond_badge,
            "priceTier": price_tier,
            "priceTierBadge": price_tier_badge,
            "priceTierKhmer": price_tier_kh,
            "priceTierClass": price_tier_class,
            "isSmartCheap": is_smart_cheap or (price_tier == "CHEAP"),
            "savingsVsNewUsd": savings_vs_new,
            "priceUsd": item_price,'''

content = content.replace(target_dict_entry, replacement_dict_entry)

# Inject priceModelSpectrum into generate_ai_agent_insights return dict
target_insights_end = '''    return {
        "query": query,
        "category": domain_info.get("category", "OTHER"),
        "domain": domain_type,
        "totalAnalyzed": len(items),
        "clusterMachinesCount": 100,'''

spectrum_computation = '''    # ─── SMART AI PRICE & MODEL SPECTRUM ENGINE ─────────────────────────────
    cheap_items = [it for it in items if it.get("priceTier") == "CHEAP"]
    fair_items = [it for it in items if it.get("priceTier") == "FAIR"]
    exp_items = [it for it in items if it.get("priceTier") == "EXPENSIVE"]

    cheap_prices = [it["priceUsd"] for it in cheap_items if it.get("priceUsd", 0) > 0] or [min_p]
    fair_prices = [it["priceUsd"] for it in fair_items if it.get("priceUsd", 0) > 0] or [avg_p]
    exp_prices = [it["priceUsd"] for it in exp_items if it.get("priceUsd", 0) > 0] or [max_p]

    def _get_unique_tags(it_list, k, limit=4):
        res = []
        for x in it_list:
            v = x.get(k)
            if v and v not in res:
                res.append(str(v))
            if len(res) >= limit:
                break
        return res

    price_model_spectrum = {
        "hasSpectrum": True,
        "totalCount": len(items),
        "cheapTier": {
            "tierId": "CHEAP",
            "badge": "⚡ ធូរថ្លៃ / Budget Deal",
            "titleKhmer": "ជម្រើសធូរថ្លៃ & ចំណេញថវិកា (Budget Deals)",
            "count": len(cheap_items),
            "percentage": round(len(cheap_items) / len(items) * 100) if items else 30,
            "minPrice": min(cheap_prices),
            "maxPrice": max(cheap_prices),
            "avgPrice": round(sum(cheap_prices) / len(cheap_prices)),
            "typicalYears": _get_unique_tags(cheap_items, "modelYear"),
            "typicalTrims": _get_unique_tags(cheap_items, "seriesTrim"),
            "whyCheapKhmer": "តម្លៃធូរថ្លៃដោយសារជាស៊េរីឆ្នាំទាបបន្តិច ឬ Option មធ្យម (ស្អាត 95%-99%) សន្សំប្រាក់បានច្រើនបំផុត",
            "targetBuyerKhmer": "ស័ក្តិសមសម្រាប់អ្នកចង់សន្សំថវិកា និងចង់បានតម្លៃទាបបំផុតក្នុងទីផ្សារ"
        },
        "fairTier": {
            "tierId": "FAIR",
            "badge": "⚖️ តម្លៃទីផ្សារ / Fair Market",
            "titleKhmer": "ជម្រើសតម្លៃទីផ្សារសមរម្យ (Fair Market Sweet Spot)",
            "count": len(fair_items),
            "percentage": round(len(fair_items) / len(items) * 100) if items else 50,
            "minPrice": min(fair_prices),
            "maxPrice": max(fair_prices),
            "avgPrice": round(sum(fair_prices) / len(fair_prices)),
            "typicalYears": _get_unique_tags(fair_items, "modelYear"),
            "typicalTrims": _get_unique_tags(fair_items, "seriesTrim"),
            "whyFairKhmer": "តម្លៃស្តង់ដារពេញនិយម៖ ទទួលបានគុណភាពម៉ាស៊ីនស្អាត 99% សំណុំហ្ស៊ីន 100% និងតម្លៃសមរម្យតាមទីផ្សារទូទៅ",
            "targetBuyerKhmer": "ស័ក្តិសមសម្រាប់អ្នកទិញទូទៅដែលចង់បានតុល្យភាពល្អរវាងតម្លៃ និងគុណភាព"
        },
        "expensiveTier": {
            "tierId": "EXPENSIVE",
            "badge": "💎 កម្រិតខ្ពស់ / Flagship Spec",
            "titleKhmer": "ជម្រើសកម្រិតខ្ពស់ & ថ្មីកេះ (Premium & Flagship Specs)",
            "count": len(exp_items),
            "percentage": round(len(exp_items) / len(items) * 100) if items else 20,
            "minPrice": min(exp_prices),
            "maxPrice": max(exp_prices),
            "avgPrice": round(sum(exp_prices) / len(exp_prices)),
            "typicalYears": _get_unique_tags(exp_items, "modelYear"),
            "typicalTrims": _get_unique_tags(exp_items, "seriesTrim"),
            "whyExpensiveKhmer": "តម្លៃខ្ពស់ដោយសារជាស៊េរីឆ្នាំចុងក្រោយបង្អស់ (2024-2025) ថ្មីកេះ 100% Option ពេញ និងមានការធានាផ្លូវការ",
            "targetBuyerKhmer": "ស័ក្តិសមសម្រាប់អ្នកចង់បានភាពល្អឥតខ្ចោះ ថ្មីកេះ និងបច្ចេកវិទ្យាចុងក្រោយ"
        },
        "summaryKhmer": f"ទីផ្សារមានចម្រុះតាំងពីជម្រើសធូរថ្លៃ (${min(cheap_prices):,} - ${max(cheap_prices):,}) ដល់ជម្រើសកម្រិតខ្ពស់ (${min(exp_prices):,} - ${max(exp_prices):,})។"
    }

    return {
        "query": query,
        "category": domain_info.get("category", "OTHER"),
        "domain": domain_type,
        "totalAnalyzed": len(items),
        "clusterMachinesCount": 100,
        "priceModelSpectrum": price_model_spectrum,'''

content = content.replace(target_insights_end, spectrum_computation)

with open('scrapers/ai_search_service.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated scrapers/ai_search_service.py with Smart AI Price & Model Spectrum successfully!")
