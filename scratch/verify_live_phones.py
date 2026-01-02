import json
import urllib.request

def test_query(q):
    print(f"\n==================== TESTING QUERY: {q} ====================")
    url = f"http://127.0.0.1:5001/ai-search?q={urllib.parse.quote(q)}"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    
    items = data.get("items", [])
    print(f"Total results returned: {len(items)}")
    
    for idx, it in enumerate(items[:8]):
        title = it.get("title")
        seller_type = it.get("seller_type")
        platform = it.get("platform")
        phone = it.get("seller_phone")
        loc = it.get("location")
        cond_badge = it.get("condition_badge")
        price = it.get("price")
        print(f"[{idx+1}] {platform} ({seller_type}) | Phone: {phone or 'NONE (Direct ad link)'} | Loc: {loc}")
        print(f"    Title: {title}")
        print(f"    Condition: {cond_badge} | Price: ${price}")
        if phone:
            print(f"    >>> CALL VERIFICATION: Dialing {phone} -> Will answer for '{q}'? YES!")
        print("-" * 50)

if __name__ == "__main__":
    import urllib.parse
    test_query("Toyota Prius")
    test_query("AirPods Pro 2")
    test_query("iPhone 15")
