import urllib.request
import urllib.parse
import json

queries = [
    "airpods",
    "apple watch series 4",
    "iphone 16 pro max",
    "keychron q1 max",
    "highlander 2022",
    "vespa primavera 150",
    "macbook pro m3"
]

total_tested = 0
total_missing_phone = 0

print("=" * 70)
print("COMPREHENSIVE AUDIT: CORRECT PRODUCT & REAL TELEPHONE VERIFICATION")
print("=" * 70)

for q in queries:
    encoded_q = urllib.parse.quote(q)
    url = f"http://localhost:5001/ai-search?q={encoded_q}"
    req = urllib.request.urlopen(url)
    res = json.loads(req.read().decode())
    items = res.get("items", [])
    print(f"\n🔍 Query: '{q}' -> Returned {len(items)} items")
    for idx, item in enumerate(items[:3]):
        total_tested += 1
        phone = item.get("contactPhone")
        if not phone:
            total_missing_phone += 1
        print(f"  #{idx+1} {item.get('title')}")
        print(f"     💵 Price: ${item.get('priceUsd')} (Tier: {item.get('priceTier')})")
        print(f"     📞 Phone: {phone} (Verified: {item.get('hasVerifiedPhone')})")
        print(f"     🏪 Store: {item.get('platformSiteName')}")

print("\n" + "=" * 70)
print(f"TOTAL AUDITED ITEMS: {total_tested}")
print(f"ITEMS MISSING PHONE: {total_missing_phone} (MUST BE 0)")
print("=" * 70)
