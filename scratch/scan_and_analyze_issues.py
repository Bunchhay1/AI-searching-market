import sys
import os

sys.path.append("scrapers")
import ai_search_service as s

print("=" * 70)
print("🔍 SCANNING AI SEARCH SERVICE FOR PHONE COLLISIONS & LOCATION ISSUES")
print("=" * 70)

test_queries = [
    "airpods",
    "ipod",
    "iphone 15",
    "samsung s24",
    "prius 2010",
    "scoopy 2023",
    "macbook pro m3",
    "dell xps",
    "borey villa"
]

all_anomalies = []

for q in test_queries:
    domain_info = s.classify_intent_and_specs(q)
    print(f"\n--- Testing Query: '{q}' (Domain: {domain_info['domain']}, Brand: {domain_info['brand']}) ---")
    
    # Run 10 machines directly without external duckduckgo network lag
    items = []
    for mid in range(1, 15):
        plat = "KHMER24" if mid % 2 == 0 else "FACEBOOK"
        batch = s.build_machine_batch(mid, q, plat, real_crawled=[], target_count=7)
        items.extend(batch)

    # Analyze items
    phone_to_stores = {}
    store_to_locs = {}
    
    for it in items:
        p = it.get("contactPhone", "").strip()
        seller = it.get("seller_name") or it.get("platform")
        loc = it.get("location", "")
        title = it.get("title", "")
        pid = it.get("platform_id", "")
        price = it.get("priceUsd", 0)

        if seller:
            store_to_locs.setdefault(seller, set()).add(loc)

        if p:
            phone_to_stores.setdefault(p, []).append({
                "seller": seller,
                "pid": pid,
                "loc": loc,
                "title": title,
                "price": price
            })

    # 1. Detect Cross-Store Collisions
    for p, records in phone_to_stores.items():
        unique_sellers = set(r["seller"] for r in records)
        if len(unique_sellers) > 1:
            msg = f"❌ COLLISION: Phone '{p}' is shared by multiple DIFFERENT stores: {unique_sellers}"
            print(msg)
            for r in records[:4]:
                print(f"     -> Store: {r['seller']} | Loc: {r['loc']} | Title: {r['title'][:35]} | Price: ${r['price']}")
            all_anomalies.append(msg)

    # 2. Detect Store Location Inconsistencies
    for store, locs in store_to_locs.items():
        if len(locs) > 1 and not any(k in store.lower() for k in ["khmer24", "facebook", "fb_marketplace", "telegram"]):
            msg = f"⚠️ LOCATION JUMP: Store '{store}' appears in {len(locs)} different locations: {locs}"
            print(msg)
            all_anomalies.append(msg)

    # 3. Detect Landline Area Code Mismatches
    for p, records in phone_to_stores.items():
        if p.startswith("023"): # Phnom Penh landline
            non_pp_locs = [r["loc"] for r in records if "phnom penh" not in r["loc"].lower()]
            if non_pp_locs:
                store_names = set(r["seller"] for r in records)
                msg = f"⚠️ AREA CODE MISMATCH: Phone '{p}' (Phnom Penh 023 landline) used for non-Phnom Penh locations: {set(non_pp_locs)} by {store_names}"
                print(msg)
                all_anomalies.append(msg)

print("\n" + "=" * 70)
print(f"TOTAL ANOMALIES DETECTED: {len(all_anomalies)}")
print("=" * 70)
