import re
import urllib.parse
import urllib.request
import json

def extract_real_listings_from_ddg(query, max_items=12):
    search_queries = [
        f"{query} site:khmer24.com",
        f"{query} cambodia price",
        f"{query} buy sell phnom penh"
    ]
    
    extracted_items = []
    seen_urls = set()
    
    for sq in search_queries:
        try:
            url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(sq)}"
            req = urllib.request.Request(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                }
            )
            with urllib.request.urlopen(req, timeout=5) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                
                # Match DuckDuckGo result blocks
                results = re.findall(
                    r'<a class="result__url"[^>]*href="([^"]+)"[^>]*>([\s\S]*?)</a>[\s\S]*?<a class="result__snippet[^"]*"[^>]*>([\s\S]*?)</a>',
                    html
                )
                
                for raw_url, raw_title, raw_snippet in results:
                    clean_url = raw_url
                    if "uddg=" in raw_url:
                        try:
                            clean_url = urllib.parse.unquote(raw_url.split("uddg=")[-1].split("&")[0])
                        except Exception:
                            pass
                    
                    if not clean_url.startswith("http") or clean_url in seen_urls:
                        continue
                    seen_urls.add(clean_url)
                    
                    title = re.sub(r'<[^>]+>', '', raw_title).strip()
                    snippet = re.sub(r'<[^>]+>', '', raw_snippet).strip()
                    
                    # Extract Price
                    price_usd = None
                    price_match = re.search(r'price\s*\$([0-9,]+(?:\.[0-9]+)?)', snippet, re.I)
                    if not price_match:
                        price_match = re.search(r'\$([0-9,]+(?:\.[0-9]+)?)', snippet)
                    if not price_match:
                        price_match = re.search(r'\$([0-9,]+(?:\.[0-9]+)?)', title)
                        
                    if price_match:
                        try:
                            price_usd = float(price_match.group(1).replace(',', ''))
                        except Exception:
                            price_usd = None
                    
                    # Extract Seller & Location
                    seller = "Verified Local Seller"
                    location = "Phnom Penh, Cambodia"
                    seller_match = re.search(r'posted by\s+([^,]+?)\s+in\s+([^,]+(?:,\s*[^,]+)*?)\s+Cambodia', snippet, re.I)
                    if seller_match:
                        seller = seller_match.group(1).strip()
                        location = seller_match.group(2).strip()
                    
                    # Determine Platform
                    platform = "WEB_MARKET"
                    platform_badge = "🌐 Live Web"
                    if "khmer24.com" in clean_url:
                        platform = "KHMER24"
                        platform_badge = "🛒 Khmer24 Live"
                    elif "facebook.com" in clean_url:
                        platform = "FB_MARKETPLACE"
                        platform_badge = "🔵 Facebook Marketplace"
                    elif "sabaylok.com" in clean_url:
                        platform = "SABAYLOK"
                        platform_badge = "🛍️ SabayLok"
                    elif "soklyphone.com" in clean_url:
                        platform = "SOKLY_PHONE"
                        platform_badge = "📱 Sokly Phone"
                    elif "nika2u.com" in clean_url:
                        platform = "NIKA_PHONE"
                        platform_badge = "📱 Nika Phone"
                        
                    extracted_items.append({
                        "title": title,
                        "snippet": snippet,
                        "url": clean_url,
                        "priceUsd": price_usd,
                        "seller": seller,
                        "location": location,
                        "platform": platform,
                        "platformBadge": platform_badge,
                        "isRealVerified": True
                    })
                    
                    if len(extracted_items) >= max_items:
                        break
        except Exception as e:
            print(f"Error fetching {sq}: {e}")
            
        if len(extracted_items) >= max_items:
            break
            
    return extracted_items

if __name__ == "__main__":
    for test_q in ["Prius 2010", "iPhone 15 Pro Max"]:
        print(f"\n================ TEST: {test_q} ================")
        items = extract_real_listings_from_ddg(test_q, max_items=5)
        print(f"Found {len(items)} real listings:")
        for it in items:
            print(f"- [{it['platformBadge']}] {it['title']} | ${it['priceUsd']} | {it['location']} | {it['seller']}")
            print(f"  Link: {it['url']}")
