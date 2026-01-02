import sys
import os

sys.path.append("scrapers")
import ai_search_service as s

print("=" * 80)
print("🚀 COMPREHENSIVE 50-QUERY FULL-CLUSTER AUDIT ACROSS ALL DOMAINS")
print("=" * 80)

test_queries = [
    # Audio / iPods / AirPods
    "airpods", "airpods pro", "airpods max", "airpods 4", "ipod", "ipod touch", "galaxy buds", "earbuds",
    # Phones
    "iphone 15 pro max", "iphone 13", "iphone 11", "samsung galaxy s24 ultra", "samsung z fold 6",
    "xiaomi 14 ultra", "redmi note 13", "oppo reno 11", "vivo v30", "realme 12",
    # Computers & Laptops
    "macbook pro m3", "macbook air m2", "dell xps 15", "thinkpad x1 carbon", "asus rog zephyrus",
    "gaming pc rtx 4080", "hp pavilion", "acer nitro 5",
    # Vehicles & Cars
    "toyota prius 2008", "toyota prius 2012", "lexus rx330", "lexus rx350 2010", "toyota camry 2007",
    "ford ranger wildtrak", "toyota land cruiser 2020", "byd atto 3", "mazda cx-5",
    # Motos
    "honda dream 2024", "honda scoopy 2023", "honda click 160", "vespa sprint 150",
    # Watches
    "apple watch ultra 2", "apple watch series 9", "apple watch series 10",
    # Real Estate
    "borey peng huoth", "condo bkk1", "twin villa sen sok", "shophouse daun penh", "land chroy changvar"
]

total_items_checked = 0
phone_to_store_map = {}
store_to_location_map = {}
banned_vip_numbers = ["012 999 777", "011 777 555", "012 900 113", "012 888 849"]
detected_vip_violations = []
detected_collisions = []
detected_location_jumps = []
detected_area_code_mismatches = []

for q in test_queries:
    domain_info = s.classify_intent_and_specs(q)
    # Generate 5 machines (35 items) per query across diverse categories
    items = []
    for mid in range(1, 6):
        plat = "KHMER24" if mid % 2 == 0 else "FACEBOOK"
        batch = s.build_machine_batch(mid, q, plat, real_crawled=[], target_count=7)
        items.extend(batch)

    total_items_checked += len(items)

    for it in items:
        p = (it.get("contactPhone") or "").strip()
        seller = it.get("sellerName") or it.get("platform")
        loc = it.get("location") or ""
        stype = it.get("sellerType")

        # Check banned fake VIP numbers
        if p in banned_vip_numbers:
            detected_vip_violations.append(f"Query: '{q}', Store: '{seller}', Fake VIP Phone: '{p}'")

        # Check cross-store phone collisions
        if p:
            phone_to_store_map.setdefault(p, set()).add(seller)

        # Check store location stability
        if stype == "STORE":
            store_to_location_map.setdefault(seller, set()).add(loc)

            # Check area code coherence
            if p.startswith("023") and "phnom penh" not in loc.lower():
                detected_area_code_mismatches.append(f"Store '{seller}' has 023 Phnom Penh landline '{p}' but non-PP location '{loc}'")

print(f"\nAudit completed. Total listings analyzed: {total_items_checked}")

# Evaluate results
print("\n--- 1. Banned Fake VIP Phone Check ---")
if detected_vip_violations:
    print(f"❌ FAIL: Found {len(detected_vip_violations)} fake VIP phone numbers:")
    for v in detected_vip_violations:
        print(f"   -> {v}")
else:
    print("✅ PASS: 0 fake VIP numbers detected across all queries!")

print("\n--- 2. Cross-Store Phone Collision Check ---")
collision_count = 0
for p, stores in phone_to_store_map.items():
    if len(stores) > 1:
        # Check if they are just branches of the same brand (e.g. iOne)
        norm_names = set(s.split()[0].lower() for s in stores)
        if len(norm_names) > 1:
            collision_count += 1
            detected_collisions.append(f"Phone '{p}' shared by distinct stores: {stores}")

if collision_count > 0:
    print(f"❌ FAIL: Found {collision_count} cross-store collisions:")
    for c in detected_collisions:
        print(f"   -> {c}")
else:
    print("✅ PASS: 0 cross-store phone collisions! Every store has a unique phone number.")

print("\n--- 3. Store Location Stability & Area Code Coherence ---")
jump_count = 0
for store, locs in store_to_location_map.items():
    if len(locs) > 1:
        jump_count += 1
        detected_location_jumps.append(f"Store '{store}' moved across {len(locs)} locations: {locs}")

if jump_count > 0:
    print(f"❌ FAIL: Found {jump_count} location jump anomalies:")
    for j in detected_location_jumps:
        print(f"   -> {j}")
else:
    print("✅ PASS: 0 location jump anomalies! Every verified store is anchored to its real address.")

if detected_area_code_mismatches:
    print(f"❌ FAIL: Found {len(detected_area_code_mismatches)} area code mismatches:")
    for a in detected_area_code_mismatches:
        print(f"   -> {a}")
else:
    print("✅ PASS: 0 area code mismatches! (All 023 landlines belong to Phnom Penh addresses).")

print("\n" + "=" * 80)
total_errors = len(detected_vip_violations) + collision_count + jump_count + len(detected_area_code_mismatches)
print(f"🎯 FINAL AUDIT SCORE: {'100% PERFECT (0 ERRORS)' if total_errors == 0 else f'FAILED WITH {total_errors} ISSUES'}")
print("=" * 80)
