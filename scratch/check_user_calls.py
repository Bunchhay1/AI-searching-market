import sys
sys.path.append("scrapers")
import ai_search_service as s

items_airpods = s.execute_python_ai_search("AirPods Pro 2")
print("=== TOP 10 ITEMS FOR: AirPods Pro 2 ===")
for idx, it in enumerate(items_airpods[:10]):
    t = it.get("title")
    p = it.get("priceUsd")
    seller = it.get("sellerName")
    phone = it.get("contactPhone")
    loc = it.get("location")
    stype = it.get("sellerType")
    print(f"[{idx+1}] {seller} ({stype}) | Phone: '{phone}' | Price: ${p} | Loc: {loc} | Title: {t}")

items_prius = s.execute_python_ai_search("Toyota Prius")
print("\n=== TOP 10 ITEMS FOR: Toyota Prius ===")
for idx, it in enumerate(items_prius[:10]):
    t = it.get("title")
    p = it.get("priceUsd")
    seller = it.get("sellerName")
    phone = it.get("contactPhone")
    loc = it.get("location")
    stype = it.get("sellerType")
    print(f"[{idx+1}] {seller} ({stype}) | Phone: '{phone}' | Price: ${p} | Loc: {loc} | Title: {t}")
