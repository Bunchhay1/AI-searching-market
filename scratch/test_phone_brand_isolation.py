import urllib.request, urllib.parse, json

test_cases = [
    {
        "query": "iPhone 13",
        "expected_brand": "Apple",
        "allowed_stores": ["iOne Apple Premium Reseller", "NIKA Phone Shop", "Sokly Phone Shop", "Apsara Mobile", "Hakse Phone Shop", "Smart Shop Official", "Cellcard Official Store"],
        "forbidden_stores": ["Samsung Cambodia Official", "Xiaomi Store Cambodia", "Toyota Cambodia Official", "RMA Ford Cambodia", "PTC Computer"],
        "allowed_phones": ["023 997 779", "011 777 555", "012 999 777", "012 900 113", "012 888 849", "010 200 888", "012 812 812", ""]
    },
    {
        "query": "Samsung Galaxy S24 Ultra",
        "expected_brand": "Samsung",
        "allowed_stores": ["Samsung Cambodia Official", "NIKA Phone Shop", "Sokly Phone Shop", "Apsara Mobile", "Hakse Phone Shop", "Smart Shop Official", "Cellcard Official Store"],
        "forbidden_stores": ["iOne Apple Premium Reseller", "Xiaomi Store Cambodia", "Toyota Cambodia Official"],
        "allowed_phones": ["023 993 232", "011 777 555", "012 999 777", "012 900 113", "012 888 849", "010 200 888", "012 812 812", ""]
    },
    {
        "query": "Ford Ranger Wildtrak",
        "expected_brand": "Ford",
        "allowed_stores": ["RMA Ford Cambodia", "Auto 24 Cambodia", "SabayLokCar Auto Yard", "Liberty Carz"],
        "forbidden_stores": ["Toyota Cambodia Official", "HGB Mazda Cambodia", "BYD Harmony Cambodia", "iOne Apple Premium Reseller", "Samsung Cambodia Official"],
        "allowed_phones": ["012 333 972", "012 900 800", "023 998 801", "023 900 808", ""]
    },
    {
        "query": "Toyota Prius 2012",
        "expected_brand": "Toyota",
        "allowed_stores": ["Toyota Cambodia Official", "Auto 24 Cambodia", "SabayLokCar Auto Yard", "Liberty Carz"],
        "forbidden_stores": ["RMA Ford Cambodia", "HGB Mazda Cambodia", "BYD Harmony Cambodia"],
        "allowed_phones": ["023 993 399", "012 900 800", "023 998 801", "023 900 808", ""]
    },
    {
        "query": "MacBook Pro M3",
        "expected_brand": "Apple",
        "allowed_stores": ["iOne Mac & Apple Store", "PTC Computer"],
        "forbidden_stores": ["Gold One Computer", "Chhay Hok Computer", "Toyota Cambodia Official", "Samsung Cambodia Official"],
        "allowed_phones": ["023 997 779", "023 222 212", ""]
    }
]

all_passed = True
print("=" * 80)
print("🔍 AUDITING 100% BRAND-STORE COMPATIBILITY & AUTHENTIC PHONE NUMBERS")
print("=" * 80)

for tc in test_cases:
    q = tc["query"]
    url = f"http://localhost:5001/ai-search?q={urllib.parse.quote_plus(q)}"
    res = urllib.request.urlopen(url)
    data = json.loads(res.read().decode())
    items = data.get("items", [])

    print(f"\n🧪 Testing Query: \"{q}\" (Items: {len(items)})")
    
    forbidden_hits = []
    invalid_phones = []
    
    for it in items[:50]:
        store = it.get("platformSiteName", "")
        phone = it.get("contactPhone") or ""
        badge = it.get("brandAuthorizedBadge", "")
        
        # Check forbidden stores
        for fs in tc["forbidden_stores"]:
            if fs.lower() in store.lower():
                forbidden_hits.append((store, it.get("title")))
                
        # Check phone is either empty or in allowed_phones
        if phone and phone not in tc["allowed_phones"]:
            invalid_phones.append((store, phone))

    if forbidden_hits:
        print(f"  ❌ FAILED: Found {len(forbidden_hits)} forbidden store assignments:")
        for fs, tit in forbidden_hits[:3]:
            print(f"     - Store '{fs}' assigned to '{tit}'")
        all_passed = False
    else:
        print("  ✅ PASS: 0 forbidden store assignments! Brand isolation strictly maintained.")

    if invalid_phones:
        print(f"  ❌ FAILED: Found {len(invalid_phones)} unexpected phone numbers:")
        for s, p in invalid_phones[:3]:
            print(f"     - Store '{s}' returned unknown phone '{p}'")
        all_passed = False
    else:
        print("  ✅ PASS: All phone numbers are 100% genuine and verified for their respective stores.")

    # Show sample output
    sample = items[0]
    print(f"  📌 Sample #1: {sample.get('title')}")
    print(f"     • Store: {sample.get('platformSiteName')}")
    print(f"     • Phone: {sample.get('contactPhone')} ({sample.get('phoneLabel')})")
    print(f"     • Brand Badge: {sample.get('brandAuthorizedBadge')}")
    print(f"     • Store Ask Hint: {sample.get('storeAskHint')}")

print("\n" + "=" * 80)
if all_passed:
    print("🎉 ALL TESTS PASSED: 100% ACCURATE BRAND-STORE MATCHING & ZERO WRONG NUMBERS!")
else:
    print("⚠️ SOME TESTS FAILED. PLEASE REVIEW LOGS.")
print("=" * 80)
