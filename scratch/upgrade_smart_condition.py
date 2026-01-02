# -*- coding: utf-8 -*-
"""
Upgrade scrapers/ai_search_service.py:
1. Condition grading: NEW_100, LIKE_NEW_99, USED_GOOD
2. Realistic condition pricing with savings vs new
3. Smart Cheap Deal tagging
4. Detailed entity extraction: detailedModelName, modelYear, modelSeries, seriesTrim
5. smartConditionPricing in AI Agent insights
"""

with open("scrapers/ai_search_service.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update build_machine_batch pricing and condition
old_price_calc = '''        # Intentional scam bait for specific edge machine test (machine 7, item 1)
        if machine_id % 33 == 0 and i == 1:
            item_price = int(trim_price * 0.28) # Under 30% price (Deposit Scam Bait)
        else:
            variation = ((idx * 17) % 13) - 6
            item_price = int(trim_price * (1 + variation / 100.0))
            if item_price < 10:
                item_price = 50'''

new_price_calc = '''        # Condition Grading: NEW_100 (~30%), LIKE_NEW_99 (~50%), USED_GOOD (~20%)
        cond_mod = idx % 10
        if cond_mod in [0, 1, 2]:
            cond_code = "NEW_100"
            cond_badge = "🌟 ថ្មីកេះ 100%"
            cond_tag = "ថ្មីកេះ 100% ប្រអប់"
            cond_mult = 1.0 + (((idx * 7) % 5) / 100.0) # 100% - 104%
        elif cond_mod in [3, 4, 5, 6, 7]:
            cond_code = "LIKE_NEW_99"
            cond_badge = "✨ ស្អាត 99% (Like New)"
            cond_tag = "ស្អាត 99% សំណុំហ្ស៊ីន"
            cond_mult = 0.81 + (((idx * 7) % 6) / 100.0) # 81% - 86% (Save 14-19%!)
        else:
            cond_code = "USED_GOOD"
            cond_badge = "👍 មួយទឹកស្អាត 95%"
            cond_tag = "មួយទឹកស្អាត 95%"
            cond_mult = 0.70 + (((idx * 7) % 6) / 100.0) # 70% - 75%

        brand_new_base = trim_price
        if machine_id % 33 == 0 and i == 1:
            item_price = int(trim_price * 0.28) # Deposit Scam Bait for Sentinel testing
        else:
            item_price = int(trim_price * cond_mult)
            if item_price < 10:
                item_price = 50

        savings_vs_new = max(0, brand_new_base - item_price)
        is_smart_cheap = (cond_code == "LIKE_NEW_99" or (cond_code == "NEW_100" and item_price <= brand_new_base * 0.96)) and item_price >= brand_new_base * 0.55'''

if old_price_calc in code:
    code = code.replace(old_price_calc, new_price_calc)
    print("1. Replaced price and condition calculation in build_machine_batch!")

# 2. Update title templates to reflect cond_tag
old_car_title = '''            title = f"{car_core} ឆ្នាំ {year} {trim_name} ({color})"
            desc = f"លក់រថយន្ត {car_core} ឆ្នាំ {year} ម៉ាស៊ីន {trim_name} ពណ៌ {color} ឡានស្អាត អត់បុក អត់ច្រេះ ធានាទឹកថ្នាំហ្ស៊ីន ទីតាំង {loc}។ Call/Chat ឥឡូវនេះ!"'''

new_car_title = '''            title = f"{car_core} ឆ្នាំ {year} {trim_name} {cond_tag} ({color})"
            desc = f"លក់រថយន្ត {car_core} ឆ្នាំ {year} ម៉ាស៊ីន {trim_name} {cond_tag} ពណ៌ {color} ឡានស្អាត អត់បុក អត់ច្រេះ ធានាទឹកថ្នាំហ្ស៊ីន ទីតាំង {loc}។ Call/Chat ឥឡូវនេះ!"'''

if old_car_title in code:
    code = code.replace(old_car_title, new_car_title)
    print("2. Updated car title with cond_tag!")

old_default_title = '''            title = f"{item_full_name} {year} {color} ស្អាត 99% សំណុំហ្ស៊ីន ({platform})"
            desc = f"លក់បន្ទាន់ {item_full_name} សភាពស្អាត 99% ទំហំ {year} ពណ៌ {color} គ្រឿងហ្ស៊ីនទាំងអស់ ទីតាំង {loc}។ Call/Chat ឥឡូវនេះ!"'''

new_default_title = '''            title = f"{item_full_name} ({year}) {cond_tag} {trim_name} ({color})"
            desc = f"លក់ {item_full_name} សភាព {cond_tag} {trim_name} ពណ៌ {color} គ្រឿងហ្ស៊ីន ទីតាំង {loc}។ Call/Chat ឥឡូវនេះ!"'''

if old_default_title in code:
    code = code.replace(old_default_title, new_default_title)
    print("3. Updated default title with cond_tag!")

# 3. Update batch item dictionary fields
old_batch_dict = '''            "condition": "USED_SECOND_HAND" if ("មួយទឹក" in title or "20" in str(year) and int(year) < 2024 if str(year).isdigit() else True) else "NEW",
            "priceUsd": item_price,'''

new_batch_dict = '''            "condition": cond_code,
            "conditionGrade": cond_code,
            "conditionBadge": cond_badge,
            "conditionKhmer": cond_badge,
            "isSmartCheap": is_smart_cheap,
            "savingsVsNewUsd": savings_vs_new,
            "priceUsd": item_price,'''

if old_batch_dict in code:
    code = code.replace(old_batch_dict, new_batch_dict)
    print("4. Updated batch dictionary with conditionGrade, savingsVsNewUsd, isSmartCheap!")

# 4. Add detailedModelName, modelSeries
old_model_fields = '''            "modelName": domain_info["model"],
            "modelYear": str(year),
            "isYearVerified": domain_info.get("is_year_verified", False),
            "verifiedYear": domain_info.get("verified_year"),
            "storageCapacity": spec_display,'''

new_model_fields = '''            "modelName": domain_info["model"],
            "detailedModelName": domain_info["model"],
            "modelYear": str(year),
            "modelSeries": trim_name,
            "seriesTrim": trim_name,
            "isYearVerified": domain_info.get("is_year_verified", False),
            "verifiedYear": domain_info.get("verified_year"),
            "storageCapacity": spec_display,'''

if old_model_fields in code:
    code = code.replace(old_model_fields, new_model_fields)
    print("5. Added detailedModelName, modelSeries, seriesTrim to item dictionary!")

# 5. Add smartConditionPricing calculation in generate_ai_agent_insights
old_insights_return = '''        "timeframeAnalysis": calculate_timeframe_analysis(items, timeframe_filter),
        "priceHighAnalysis": generate_price_high_analysis(query, domain_info, avg_p)'''

new_insights_return = '''        "timeframeAnalysis": calculate_timeframe_analysis(items, timeframe_filter),
        "smartConditionPricing": calculate_smart_condition_pricing(items, avg_p),
        "priceHighAnalysis": generate_price_high_analysis(query, domain_info, avg_p)'''

calculate_smart_condition_pricing_fn = '''def calculate_smart_condition_pricing(items: list, avg_p: float):
    """
    Analyzes price disparity between Brand New 100% vs Like New 99% vs Used 95%
    and highlights smart cheap bargain deals.
    """
    new_items = [it for it in items if it.get("condition") == "NEW_100" and it.get("priceUsd", 0) > 0]
    likenew_items = [it for it in items if it.get("condition") == "LIKE_NEW_99" and it.get("priceUsd", 0) > 0]
    used_items = [it for it in items if it.get("condition") == "USED_GOOD" and it.get("priceUsd", 0) > 0]

    avg_new = int(sum(it["priceUsd"] for it in new_items) / len(new_items)) if new_items else int(avg_p * 1.05)
    avg_99 = int(sum(it["priceUsd"] for it in likenew_items) / len(likenew_items)) if likenew_items else int(avg_p * 0.84)
    avg_used = int(sum(it["priceUsd"] for it in used_items) / len(used_items)) if used_items else int(avg_p * 0.72)

    savings_diff = max(0, avg_new - avg_99)
    savings_pct = round((savings_diff / max(1, avg_new)) * 100, 1)

    smart_deals = [it for it in items if it.get("isSmartCheap") and it.get("scamRiskLevel") == "LOW"]
    smart_deals.sort(key=lambda x: -x.get("savingsVsNewUsd", 0))

    return {
        "brandNew": {
            "count": len(new_items),
            "avgPrice": avg_new,
            "badgeKhmer": "🌟 ថ្មីកេះ 100% (Brand New)",
            "descKhmer": "ទំនិញថ្មីកេះ ប្រអប់ហ្ស៊ីន ធានាក្រុមហ៊ុនផ្លូវការ"
        },
        "likeNew99": {
            "count": len(likenew_items),
            "avgPrice": avg_99,
            "badgeKhmer": "✨ ស្អាត 99% សំណុំហ្ស៊ីន (Like New)",
            "descKhmer": "មួយទឹកដូចថ្មី គ្មានស្នាម គ្រឿងហ្ស៊ីន 100%"
        },
        "usedGood": {
            "count": len(used_items),
            "avgPrice": avg_used,
            "badgeKhmer": "👍 មួយទឹកស្អាត 95% (Used Good)",
            "descKhmer": "តម្លៃធូរថ្លៃ សន្សំសំចៃខ្ពស់"
        },
        "savingsDiffUsd": savings_diff,
        "savingsPercent": savings_pct,
        "smartAdviceKhmer": f"💡 ការប្រៀបធៀបឆ្លាតវៃ (Smart Comparison): ការជ្រើសរើសទិញ 'ស្អាត 99% សំណុំហ្ស៊ីន' ជួយអ្នកសន្សំបាន ${savings_diff:,} ({savings_pct}%) ធៀបនឹងទិញថ្មីកេះ 100% ដោយគុណភាព សោភ័ណភាព និងគ្រឿងហ្ស៊ីនស្ទើរតែដូចគ្នាទាំងស្រុង!",
        "topSmartDealsCount": len(smart_deals)
    }
'''

if "def calculate_smart_condition_pricing(" not in code:
    idx_insights = code.find("def generate_ai_agent_insights(")
    if idx_insights != -1:
        code = code[:idx_insights] + calculate_smart_condition_pricing_fn + "\n\n" + code[idx_insights:]
        print("6. Injected calculate_smart_condition_pricing function!")

if old_insights_return in code:
    code = code.replace(old_insights_return, new_insights_return)
    print("7. Connected smartConditionPricing in generate_ai_agent_insights!")

with open("scrapers/ai_search_service.py", "w", encoding="utf-8") as f:
    f.write(code)

print("AI SEARCH SERVICE SMART CHEAP & CONDITION UPGRADE COMPLETE!")
