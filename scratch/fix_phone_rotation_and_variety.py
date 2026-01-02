import re

with open("scrapers/ai_search_service.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update get_platforms_for_domain_and_query to include major marketplaces interleaved with verified brand stores
old_matcher_code = '''    # Filter strictly by brand if brand is known
    if b_low:
        matched_stores = []
        for s in raw_pool:
            supp = [sb.lower() for sb in s.get("supported_brands", [])]
            if not supp or b_low in supp or any(b_low in sb for sb in supp):
                matched_stores.append(s)
        if matched_stores:
            return matched_stores

    return raw_pool'''

new_matcher_code = '''    # Verified brand stores
    matched_stores = []
    if b_low:
        for s in raw_pool:
            supp = [sb.lower() for sb in s.get("supported_brands", [])]
            if not supp or b_low in supp or any(b_low in sb for sb in supp):
                matched_stores.append(s)
    if not matched_stores:
        matched_stores = list(raw_pool)

    # Online classifieds & trading marketplaces (Khmer24, FB Marketplace, Telegram)
    # where Cambodian buyers find direct individual listings
    MAJOR_MARKETPLACES = [
        {
            "id": "khmer24",
            "name": "Khmer24 Marketplace",
            "domain": "khmer24.com",
            "category": "GENERAL",
            "badge": "🛒 ទីផ្សារ Khmer24",
            "brandBadge": "🌐 ផ្សារទំនិញ Khmer24",
            "nameKh": "ផ្សារខ្មែរ២៤ (Khmer24)",
            "descKh": "Cambodia's largest marketplace with direct seller listings",
            "searchUrl": "https://www.khmer24.com/en/search?q={q}",
            "homeUrl": "https://www.khmer24.com"
        },
        {
            "id": "fb_marketplace",
            "name": "Facebook Marketplace",
            "domain": "facebook.com/marketplace",
            "category": "GENERAL",
            "badge": "📘 FB Marketplace",
            "brandBadge": "🌐 ប្រកាសលក់លើ FB",
            "nameKh": "ហ្វេសប៊ុក ម៉ាកឃីតផ្លេស",
            "descKh": "Peer-to-peer marketplace with direct seller listings",
            "searchUrl": "https://www.facebook.com/marketplace/phnompenh/search/?query={q}",
            "homeUrl": "https://www.facebook.com/marketplace"
        },
        {
            "id": "telegram_kh",
            "name": "Telegram Trading Hub",
            "domain": "t.me",
            "category": "GENERAL",
            "badge": "✈️ Telegram Trading",
            "brandBadge": "🌐 ឆានែលតេឡេក្រាម",
            "nameKh": "ឆានែលទិញលក់ តេឡេក្រាម",
            "descKh": "Live community trading channels and instant messaging",
            "searchUrl": "https://t.me/khmer_trading_hub?q={q}",
            "homeUrl": "https://t.me/khmer_trading_hub"
        }
    ]

    # Interleave brand stores and marketplaces so search results offer rich, realistic variety
    combined_pool = []
    max_len = max(len(matched_stores), len(MAJOR_MARKETPLACES))
    for idx in range(max_len):
        if idx < len(matched_stores):
            combined_pool.append(matched_stores[idx])
        if idx < len(MAJOR_MARKETPLACES):
            combined_pool.append(MAJOR_MARKETPLACES[idx])

    return combined_pool if combined_pool else raw_pool'''

if old_matcher_code in code:
    code = code.replace(old_matcher_code, new_matcher_code, 1)
    print("Updated get_platforms_for_domain_and_query with interleaved variety")
else:
    print("Warning: old_matcher_code not found in code")

# 2. Fix the plat_idx formula in build_machine_batch so that consecutive items across machines
# get DIFFERENT stores and phone numbers instead of 100 of the same!
old_plat_idx = """        # Determine platform URL and portal metadata strictly matching the brand & domain
        candidates = get_platforms_for_domain_and_query(domain_info["domain"], query, brand=b_name)
        plat_idx = ((machine_id - 1) * target_count + i) % len(candidates)
        plat_meta = candidates[plat_idx]"""

new_plat_idx = """        # Determine platform URL and portal metadata strictly matching the brand & domain
        candidates = get_platforms_for_domain_and_query(domain_info["domain"], query, brand=b_name)
        # Ensure sequential variety: each machine (machine_id: 1..100) and slot (i: 0..6)
        # rotates smoothly across all candidates without repeating the same store consecutively
        plat_idx = ((machine_id - 1) + i * 3) % len(candidates)
        plat_meta = candidates[plat_idx]"""

if old_plat_idx in code:
    code = code.replace(old_plat_idx, new_plat_idx, 1)
    print("Fixed plat_idx rotation formula in build_machine_batch")
else:
    print("Warning: old_plat_idx not found in code")

with open("scrapers/ai_search_service.py", "w", encoding="utf-8") as f:
    f.write(code)

print("✅ Patch file written successfully!")
