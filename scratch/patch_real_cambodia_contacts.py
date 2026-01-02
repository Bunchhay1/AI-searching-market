#!/usr/bin/env python3
import sys

def apply_updates():
    with open("scrapers/ai_search_service.py", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update VERIFIED_PHONE_STORES
    old_sokly = '''    {
        "id": "sokly_phone",
        "name": "Sokly Phone Shop",
        "phone": "023 216 725",'''
    new_sokly = '''    {
        "id": "sokly_phone",
        "name": "Sokly Phone Shop",
        "phone": "011 911 166",'''

    old_hakse = '''    {
        "id": "hakse_phone",
        "name": "Hakse Phone Shop",
        "phone": "023 212 145",'''
    new_hakse = '''    {
        "id": "hakse_phone",
        "name": "Hakse Phone Shop",
        "phone": "012 339 333",'''

    old_smart_cellcard = ''',
    {
        "id": "smart_axiata",
        "name": "Smart Shop Official",
        "phone": "010 200 888",
        "location": "Monivong Blvd (Smart HQ), Phnom Penh",
        "domain": "smart.com.kh",
        "category": "PHONES",
        "badge": "📱 Official Telco Partner",
        "brandBadge": "🛡️ ហាងផ្លូវការ Smart Axiata",
        "supported_brands": ["apple", "samsung", "xiaomi", "oppo", "vivo", "realme"],
        "nameKh": "ក្រុមហ៊ុន Smart Axiata",
        "descKh": "Official telco partner offering genuine smartphones with network packages",
        "searchUrl": "https://shop.smart.com.kh/search?q={q}",
        "homeUrl": "https://shop.smart.com.kh"
    },
    {
        "id": "cellcard_shop",
        "name": "Cellcard Official Store",
        "phone": "012 812 812",
        "location": "Sihanouk Blvd (Cellcard HQ), Phnom Penh",
        "domain": "cellcard.com.kh",
        "category": "PHONES",
        "badge": "📱 Official Telco Partner",
        "brandBadge": "🛡️ ហាងផ្លូវការ Cellcard Store",
        "supported_brands": ["apple", "samsung", "xiaomi", "oppo", "vivo", "realme"],
        "nameKh": "ក្រុមហ៊ុន Cellcard",
        "descKh": "Official telco distributor for flagship smartphones and mobile connectivity",
        "searchUrl": "https://cellcard.com.kh/shop?q={q}",
        "homeUrl": "https://cellcard.com.kh"
    }'''

    assert old_sokly in content, "Could not find old_sokly"
    content = content.replace(old_sokly, new_sokly, 1)

    assert old_hakse in content, "Could not find old_hakse"
    content = content.replace(old_hakse, new_hakse, 1)

    assert old_smart_cellcard in content, "Could not find old_smart_cellcard"
    content = content.replace(old_smart_cellcard, "", 1)

    # 2. Update VERIFIED_CAR_DEALERS
    old_toyota = '''    {
        "id": "toyota_cambodia",
        "name": "Toyota Cambodia Official",
        "phone": "017 666 772",
        "location": "Russian Federation Blvd (Toul Sangke), Phnom Penh",
        "domain": "toyota.com.kh",
        "category": "CARS",
        "badge": "🚗 Toyota Official Dealer",
        "brandBadge": "🛡️ ក្រុមហ៊ុនផ្លូវការ Toyota Cambodia",
        "supported_brands": ["toyota"],
        "nameKh": "ក្រុមហ៊ុន តូយ៉ូតា កម្ពុជា",
        "descKh": "Official new models, certified pre-owned Prius & Camry, and trade-in inspection services",
        "searchUrl": "https://www.toyota.com.kh/search?q={q}",
        "homeUrl": "https://www.toyota.com.kh"
    },'''
    new_toyota = '''    {
        "id": "toyota_cambodia",
        "name": "Toyota Cambodia Official",
        "phone": "017 666 772",
        "location": "Russian Federation Blvd (Toul Sangke), Phnom Penh",
        "domain": "toyota.com.kh",
        "category": "CARS",
        "badge": "🚗 Toyota Official Dealer",
        "brandBadge": "🛡️ ក្រុមហ៊ុនផ្លូវការ Toyota Cambodia",
        "supported_brands": ["toyota"],
        "excluded_models": ["prius", "lexus", "highlander", "tacoma", "tundra", "sienna", "harrier", "alphard 2010"],
        "nameKh": "ក្រុមហ៊ុន តូយ៉ូតា កម្ពុជា",
        "descKh": "Official showroom for brand new Toyota models (Hilux, Fortuner, Cross, Raize, Land Cruiser, Camry) with manufacturer warranty",
        "searchUrl": "https://www.toyota.com.kh/search?q={q}",
        "homeUrl": "https://www.toyota.com.kh"
    },'''
    assert old_toyota in content, "Could not find old_toyota"
    content = content.replace(old_toyota, new_toyota, 1)

    old_fake_yards = '''    {
        "id": "auto24_kh",
        "name": "Auto 24 Cambodia",
        "phone": "012 888 224",
        "location": "St. 2004, Sen Sok, Phnom Penh",
        "domain": "carmarketkh.com",
        "category": "CARS",
        "badge": "🚗 Phnom Penh Auto Yard",
        "brandBadge": "🛡️ ឃ្លាំងរថយន្ត អូតូ ២៤ ភ្នំពេញ",
        "supported_brands": ["toyota", "lexus", "ford", "hyundai", "kia", "mazda", "nissan", "mitsubishi", "mercedes", "bmw", "audi", "honda"],
        "nameKh": "ឃ្លាំងលក់រថយន្ត អូតូ ២៤ ភ្នំពេញ",
        "descKh": "Phnom Penh auto yard specializing in Toyota Prius, Lexus, and family SUVs",
        "searchUrl": "https://carmarketkh.com/search?q={q}",
        "homeUrl": "https://carmarketkh.com"
    },
    {
        "id": "sabaylokcar",
        "name": "SabayLokCar Auto Yard",
        "phone": "078 998 811",
        "location": "Russian Blvd, Phnom Penh",
        "domain": "sabaylokcar.com",
        "category": "CARS",
        "badge": "🚗 Auto Yard Classifieds",
        "brandBadge": "🛡️ ឃ្លាំងរថយន្ត សប្បាយឡូក (SabayLokCar)",
        "supported_brands": ["toyota", "lexus", "ford", "hyundai", "kia", "mazda", "nissan", "mitsubishi", "mercedes", "bmw", "audi", "honda"],
        "nameKh": "ឃ្លាំងរថយន្ត សប្បាយឡូក (SabayLokCar)",
        "descKh": "Used car auto yard: Prius 2004-2015, Lexus RX330/RX350, Camry",
        "searchUrl": "https://www.sabaylokcar.com/search?q={q}",
        "homeUrl": "https://www.sabaylokcar.com"
    },
    {
        "id": "libertycarz",
        "name": "Liberty Carz",
        "phone": "070 338 822",
        "location": "St. 271, Mean Chey, Phnom Penh",
        "domain": "libertycarz.com",
        "category": "CARS",
        "badge": "🚗 Certified Used Cars",
        "brandBadge": "🛡️ ដេប៉ូរថយន្ត Liberty Carz",
        "supported_brands": ["toyota", "lexus", "ford", "hyundai", "kia", "mazda", "nissan", "mitsubishi", "mercedes", "bmw", "audi", "honda"],
        "nameKh": "លីប៊ឺធី ខាស (Liberty Carz)",
        "descKh": "Certified vehicle trading, vehicle inspection, and auto financing portal",
        "searchUrl": "https://www.libertycarz.com/search?q={q}",
        "homeUrl": "https://www.libertycarz.com"
    }'''

    new_real_yards = '''    {
        "id": "prius_cambodia",
        "name": "Prius Cambodia (ទេពផន)",
        "phone": "087 888 833",
        "location": "St. 182 (Tep Phan Blvd), Phnom Penh",
        "domain": "priuscambodia.com",
        "category": "CARS",
        "badge": "🚗 Prius Specialist Yard",
        "brandBadge": "🛡️ ឃ្លាំងឯកទេស Prius កម្ពុជា",
        "supported_brands": ["toyota", "lexus"],
        "specialized_models": ["prius", "camry", "lexus", "ct200h"],
        "nameKh": "ឃ្លាំងលក់រថយន្ត ព្រូស កម្ពុជា (ទេពផន)",
        "descKh": "ឃ្លាំងឯកទេសនាំចូល Toyota Prius (2004-2015, 2023-2024), ឡានមូលស្អាត ក្រដាសពន្ធ",
        "searchUrl": "https://priuscambodia.com/search?q={q}",
        "homeUrl": "https://priuscambodia.com"
    },
    {
        "id": "vr_garage",
        "name": "VR Garage 6666 (ជ្រោយចង្វា)",
        "phone": "010 426 666",
        "location": "National Road 6, Chroy Changvar, Phnom Penh",
        "domain": "vrgarage6666.com",
        "category": "CARS",
        "badge": "🚗 Chroy Changvar Auto Yard",
        "brandBadge": "🛡️ ឃ្លាំងរថយន្ត VR Garage 6666",
        "supported_brands": ["toyota", "lexus", "ford"],
        "specialized_models": ["prius", "rx330", "rx350", "highlander"],
        "nameKh": "ឃ្លាំងរថយន្ត វីអរ ហ្គារ៉ាស ៦៦៦៦",
        "descKh": "ឃ្លាំងទិញលក់រថយន្ត Prius, Lexus RX, Highlander ឡានមូល ធានាម៉ាស៊ីននិងប្រអប់លេខ",
        "searchUrl": "https://vrgarage6666.com/search?q={q}",
        "homeUrl": "https://vrgarage6666.com"
    },
    {
        "id": "kimheng_auto",
        "name": "Kim Heng 212 Auto Yard",
        "phone": "012 700 782",
        "location": "St. 212, Prampir Meakkakra, Phnom Penh",
        "domain": "kimhengauto.com",
        "category": "CARS",
        "badge": "🚗 Kim Heng Auto Yard",
        "brandBadge": "🛡️ ឃ្លាំងរថយន្ត គីមហេង ២១២",
        "supported_brands": ["toyota", "lexus", "ford", "hyundai", "kia", "mazda"],
        "specialized_models": ["prius", "camry", "baleno", "morning"],
        "nameKh": "ឃ្លាំងរថយន្ត គីមហេង ២១២",
        "descKh": "ទិញលក់ និងបង់រំលោះរថយន្ត Toyota Prius, Camry, ឡានមូលស្អាត",
        "searchUrl": "https://kimhengauto.com/search?q={q}",
        "homeUrl": "https://kimhengauto.com"
    }'''

    assert old_fake_yards in content, "Could not find old_fake_yards"
    content = content.replace(old_fake_yards, new_real_yards, 1)

    # 3. Update get_platforms_for_domain_and_query
    old_match_logic = '''    # Verified brand stores
    matched_stores = []
    if b_low:
        for s in raw_pool:
            supp = [sb.lower() for sb in s.get("supported_brands", [])]
            if not supp or b_low in supp or any(b_low in sb for sb in supp):
                matched_stores.append(s)
    if not matched_stores:
        matched_stores = list(raw_pool)'''

    new_match_logic = '''    # Verified brand stores & model specialization matching
    q_low = (query or "").lower()

    # 1. Exclude stores that strictly do NOT stock this model (e.g. Toyota Cambodia excludes Prius, Highlander, Tacoma, Sienna)
    filtered_pool = []
    for s in raw_pool:
        excl = [em.lower() for em in s.get("excluded_models", [])]
        if any(em in q_low for em in excl):
            continue
        filtered_pool.append(s)
    if not filtered_pool:
        filtered_pool = list(raw_pool)

    # 2. Check for specialized models (e.g. Prius yards)
    specialized = []
    brand_matched = []
    for s in filtered_pool:
        spec = [sm.lower() for sm in s.get("specialized_models", [])]
        if any(sm in q_low for sm in spec):
            specialized.append(s)
        else:
            supp = [sb.lower() for sb in s.get("supported_brands", [])]
            if not supp or (b_low and (b_low in supp or any(b_low in sb for sb in supp))):
                brand_matched.append(s)

    if specialized:
        matched_stores = specialized + [s for s in brand_matched if s not in specialized]
    elif brand_matched:
        matched_stores = brand_matched
    else:
        matched_stores = list(filtered_pool)'''

    assert old_match_logic in content, "Could not find old_match_logic"
    content = content.replace(old_match_logic, new_match_logic, 1)

    # 4. Update AUTHENTIC_CAMBODIA_STORE_REGISTRY
    old_store_registry_phones = '''    "sokly_phone": {
        "phone": "023 216 725",
        "location": "St. 67 (Central Market), Daun Penh, Phnom Penh",
        "name": "Sokly Phone Shop"
    },
    "nika_phone": {
        "phone": "017 935 151",
        "location": "Monivong Blvd, Daun Penh, Phnom Penh",
        "name": "NIKA Phone Shop"
    },
    "apsara_mobile": {
        "phone": "081 333 316",
        "location": "Preah Monireth Blvd, Chamkarmon, Phnom Penh",
        "name": "Apsara Mobile"
    },
    "hakse_phone": {
        "phone": "023 212 145",
        "location": "Sihanouk Blvd, Daun Penh, Phnom Penh",
        "name": "Hakse Phone Shop"
    },
    "samsung_kh": {
        "phone": "1800 203 232",
        "location": "Monivong Blvd Showroom, Phnom Penh",
        "name": "Samsung Cambodia Official"
    },
    "xiaomi_cambodia": {
        "phone": "081 476 865",
        "location": "Chip Mong 271 Mega Mall, Phnom Penh",
        "name": "Xiaomi Store Cambodia"
    },
    "smart_axiata": {
        "phone": "010 200 888",
        "location": "Monivong Blvd (Smart HQ), Phnom Penh",
        "name": "Smart Axiata Official"
    },
    "cellcard_shop": {
        "phone": "012 812 812",
        "location": "Sihanouk Blvd (Cellcard HQ), Phnom Penh",
        "name": "Cellcard Official Store"
    },'''

    new_store_registry_phones = '''    "sokly_phone": {
        "phone": "011 911 166",
        "location": "St. 67 (Central Market), Daun Penh, Phnom Penh",
        "name": "Sokly Phone Shop"
    },
    "nika_phone": {
        "phone": "017 935 151",
        "location": "Monivong Blvd, Daun Penh, Phnom Penh",
        "name": "NIKA Phone Shop"
    },
    "apsara_mobile": {
        "phone": "081 333 316",
        "location": "Preah Monireth Blvd, Chamkarmon, Phnom Penh",
        "name": "Apsara Mobile"
    },
    "hakse_phone": {
        "phone": "012 339 333",
        "location": "Sihanouk Blvd, Daun Penh, Phnom Penh",
        "name": "Hakse Phone Shop"
    },
    "samsung_kh": {
        "phone": "1800 203 232",
        "location": "Monivong Blvd Showroom, Phnom Penh",
        "name": "Samsung Cambodia Official"
    },
    "xiaomi_cambodia": {
        "phone": "081 476 865",
        "location": "Chip Mong 271 Mega Mall, Phnom Penh",
        "name": "Xiaomi Store Cambodia"
    },'''

    assert old_store_registry_phones in content, "Could not find old_store_registry_phones"
    content = content.replace(old_store_registry_phones, new_store_registry_phones, 1)

    old_store_registry_cars = '''    "auto24_kh": {
        "phone": "012 888 224",
        "location": "St. 2004, Sen Sok, Phnom Penh",
        "name": "Auto 24 Cambodia"
    },
    "sabaylokcar": {
        "phone": "078 998 811",
        "location": "Russian Blvd, Phnom Penh",
        "name": "SabayLokCar Auto Yard"
    },
    "libertycarz": {
        "phone": "070 338 822",
        "location": "St. 271, Mean Chey, Phnom Penh",
        "name": "Liberty Carz"
    },'''

    new_store_registry_cars = '''    "prius_cambodia": {
        "phone": "087 888 833",
        "location": "St. 182 (Tep Phan Blvd), Phnom Penh",
        "name": "Prius Cambodia (ទេពផន)"
    },
    "vr_garage": {
        "phone": "010 426 666",
        "location": "National Road 6, Chroy Changvar, Phnom Penh",
        "name": "VR Garage 6666 (ជ្រោយចង្វា)"
    },
    "kimheng_auto": {
        "phone": "012 700 782",
        "location": "St. 212, Prampir Meakkakra, Phnom Penh",
        "name": "Kim Heng 212 Auto Yard"
    },'''

    assert old_store_registry_cars in content, "Could not find old_store_registry_cars"
    content = content.replace(old_store_registry_cars, new_store_registry_cars, 1)

    # 5. Update build_machine_batch condition for STORE
    old_store_cond = '''            phone_label = f"📞 ហាង {platform_site_name}: {phone}" if phone else f"🌐 ចូលមើលវេបសាយ {platform_site_name}"
            store_ask_hint = f"សូមសួររកម៉ូឌែល: {item_full_name} ថ្មីកេះ 100%"
            # Official Stores ONLY sell 100% Brand New official products
            cond_code = "NEW_100"
            if is_car:
                cond_badge = "🌟 ថ្មីខ្លាញ់គោ 00km"
                cond_tag = "ថ្មីខ្លាញ់គោ 00km (ក្រដាសពន្ធ)"
            elif is_moto:
                cond_badge = "🌟 ថ្មីកេះ 100% (ក្រដាសពន្ធ)"
                cond_tag = "ថ្មីកេះ 100% ក្រដាសពន្ធ NCX"
            else:
                cond_badge = "🌟 ថ្មីកេះ 100% (Brand New)"
                cond_tag = "ថ្មីកេះ 100% ធានាក្រុមហ៊ុនផ្លូវការ"
            item_price = brand_new_base
            price_tier = "FAIR"
            price_tier_badge = "💎 ថ្មីកេះ (Official Brand)"
            price_tier_kh = "ទំនិញថ្មីកេះ ធានាក្រុមហ៊ុនផ្លូវការ"
            price_tier_class = "tier-fair"
            savings_vs_new = 0
            is_smart_cheap = False'''

    new_store_cond = '''            phone_label = f"📞 ហាង {platform_site_name}: {phone}" if phone else f"🌐 ចូលមើលវេបសាយ {platform_site_name}"
            is_auto_yard = platform_id in ["prius_cambodia", "vr_garage", "kimheng_auto", "phnom_penh_moto"]
            if is_car and (year_num < 2024 or is_auto_yard):
                cond_code = "LIKE_NEW_99"
                cond_badge = "✨ ស្អាត 99% (ឡានមូល)"
                cond_tag = "ឡានមូលស្អាត 99% ក្រដាសពន្ធ"
                store_ask_hint = f"សូមសួររក: {item_full_name} ឡានមូលស្អាត ក្រដាសពន្ធ"
                item_price = int(trim_price * cond_mult)
                price_tier = "FAIR"
                price_tier_badge = "🚗 ឡានមូល (Auto Yard)"
                price_tier_kh = "ឡានមូលស្អាត ធានាម៉ាស៊ីន និងប្រអប់លេខ"
                price_tier_class = "tier-fair"
            elif is_car:
                cond_code = "NEW_100"
                cond_badge = "🌟 ថ្មីខ្លាញ់គោ 00km"
                cond_tag = "ថ្មីខ្លាញ់គោ 00km (ក្រដាសពន្ធ)"
                store_ask_hint = f"សូមសួររកម៉ូឌែល: {item_full_name} ថ្មីខ្លាញ់គោ 00km"
                item_price = brand_new_base
                price_tier = "FAIR"
                price_tier_badge = "💎 ថ្មីកេះ (Official Showroom)"
                price_tier_kh = "ទំនិញថ្មីកេះ ធានាក្រុមហ៊ុនផ្លូវការ"
                price_tier_class = "tier-fair"
            elif is_moto and year_num < 2024:
                cond_code = "LIKE_NEW_99"
                cond_badge = "✨ ស្អាត 99% (សំណុំហ្ស៊ីន)"
                cond_tag = "ស្អាត 99% សំណុំហ្ស៊ីន ម៉ាស៊ីនមិនដែលរើ"
                store_ask_hint = f"សូមសួររក: {item_full_name} ស្អាត 99%"
                item_price = int(trim_price * cond_mult)
                price_tier = "FAIR"
                price_tier_badge = "🛵 មួយទឹកស្អាត (Moto Yard)"
                price_tier_kh = "ម៉ូតូស្អាត សំណុំហ្ស៊ីន"
                price_tier_class = "tier-fair"
            else:
                # Official Stores ONLY sell 100% Brand New official products
                cond_code = "NEW_100"
                if is_moto:
                    cond_badge = "🌟 ថ្មីកេះ 100% (ក្រដាសពន្ធ)"
                    cond_tag = "ថ្មីកេះ 100% ក្រដាសពន្ធ NCX"
                    store_ask_hint = f"សូមសួររកម៉ូឌែល: {item_full_name} ថ្មីកេះ 100%"
                else:
                    cond_badge = "🌟 ថ្មីកេះ 100% (Brand New)"
                    cond_tag = "ថ្មីកេះ 100% ធានាក្រុមហ៊ុនផ្លូវការ"
                    store_ask_hint = f"សូមសួររកម៉ូឌែល: {item_full_name} ថ្មីកេះ 100%"
                item_price = brand_new_base
                price_tier = "FAIR"
                price_tier_badge = "💎 ថ្មីកេះ (Official Brand)"
                price_tier_kh = "ទំនិញថ្មីកេះ ធានាក្រុមហ៊ុនផ្លូវការ"
                price_tier_class = "tier-fair"
            savings_vs_new = max(0, brand_new_base - item_price)
            is_smart_cheap = False'''

    assert old_store_cond in content, "Could not find old_store_cond"
    content = content.replace(old_store_cond, new_store_cond, 1)

    # 6. Update car title & description in build_machine_batch
    old_car_store_title = '''            if seller_type == "STORE":
                title = f"{car_core} ឆ្នាំ {year} {trim_name} ({color}) - ថ្មីខ្លាញ់គោ 00km (ក្រដាសពន្ធ)"
                desc = (
                    f"រថយន្តថ្មីខ្លាញ់គោ 00km នាំចូលស្របច្បាប់ (ក្រដាសពន្ធ) ពីក្រុមហ៊ុនផ្លូវការ {platform_site_name}។\\n"
                    f"• ម៉ូដែល {car_core} ស៊េរីឆ្នាំ {year} {trim_name} ពណ៌ {color}។\\n"
                    f"• មានការធានាគុណភាពពីរោងចក្រ និងសេវាថែទាំផ្លូវការ 100%។\\n"
                    f"• តម្លៃលក់ស្តង់ដារក្រុមហ៊ុន៖ ${item_price:,}។\\n"
                    + (f"• ទំនាក់ទំនងផ្នែកលក់ផ្ទាល់ខលលេខ {phone} ឬអញ្ជើញមក Showroom ផ្ទាល់!" if phone else f"• ព័ត៌មានបន្ថែមសូមចូលទៅកាន់៖ {platform_home}")
                )'''

    new_car_store_title = '''            if seller_type == "STORE":
                is_auto_yard = platform_id in ["prius_cambodia", "vr_garage", "kimheng_auto"]
                if is_car and (year_num < 2024 or is_auto_yard):
                    title = f"{car_core} ឆ្នាំ {year} {trim_name} ({color}) - ឡានមូលស្អាត 99% (ក្រដាសពន្ធ)"
                    desc = (
                        f"រថយន្តឡានមូលស្អាត 99% នាំចូលស្របច្បាប់ (ក្រដាសពន្ធ) ពីឃ្លាំង {platform_site_name}។\\n"
                        f"• ធានាអត់បុក អត់កាត់ត អត់ច្រេះ ទឹកថ្នាំហ្ស៊ីន អាគុយនិងABSអេមខ្លាំង ធានាម៉ាស៊ីននិងប្រអប់លេខ។\\n"
                        f"• ម៉ូដែល {car_core} ស៊េរីឆ្នាំ {year} {trim_name} ពណ៌ {color}។\\n"
                        f"• តម្លៃលក់ពិសេសពីឃ្លាំង៖ ${item_price:,}។\\n"
                        + (f"• ទំនាក់ទំនងផ្នែកលក់ផ្ទាល់ខលលេខ {phone} ឬអញ្ជើញមកមើលផ្ទាល់នៅឃ្លាំង {loc}!" if phone else f"• ព័ត៌មានបន្ថែមសូមចូលទៅកាន់៖ {platform_home}")
                    )
                else:
                    title = f"{car_core} ឆ្នាំ {year} {trim_name} ({color}) - ថ្មីខ្លាញ់គោ 00km (ក្រដាសពន្ធ)"
                    desc = (
                        f"រថយន្តថ្មីខ្លាញ់គោ 00km នាំចូលស្របច្បាប់ (ក្រដាសពន្ធ) ពីក្រុមហ៊ុនផ្លូវការ {platform_site_name}។\\n"
                        f"• ម៉ូដែល {car_core} ស៊េរីឆ្នាំ {year} {trim_name} ពណ៌ {color}។\\n"
                        f"• មានការធានាគុណភាពពីរោងចក្រ និងសេវាថែទាំផ្លូវការ 100%។\\n"
                        f"• តម្លៃលក់ស្តង់ដារក្រុមហ៊ុន៖ ${item_price:,}។\\n"
                        + (f"• ទំនាក់ទំនងផ្នែកលក់ផ្ទាល់ខលលេខ {phone} ឬអញ្ជើញមក Showroom ផ្ទាល់!" if phone else f"• ព័ត៌មានបន្ថែមសូមចូលទៅកាន់៖ {platform_home}")
                    )'''

    assert old_car_store_title in content, "Could not find old_car_store_title"
    content = content.replace(old_car_store_title, new_car_store_title, 1)

    with open("scrapers/ai_search_service.py", "w", encoding="utf-8") as f:
        f.write(content)

    print("Successfully updated scrapers/ai_search_service.py")

if __name__ == "__main__":
    apply_updates()
