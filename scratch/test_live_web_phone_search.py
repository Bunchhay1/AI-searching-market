import urllib.request
import urllib.parse
import re
import html

CAMBODIA_PHONE_REGEX = re.compile(
    r'(?:\+?855|0)(?:[1-9]\d{1,2})[\s.-]?\d{3}[\s.-]?\d{3,4}\b'
)

CAMBODIA_VALID_PREFIXES = {
    # Smart
    "010", "016", "069", "070", "081", "086", "087", "093", "096", "098",
    # Cellcard
    "011", "012", "014", "017", "061", "076", "077", "078", "085", "089", "092", "095", "099",
    # Metfone
    "031", "060", "066", "067", "068", "071", "088", "090", "097",
    # Landlines
    "023", "024", "025", "026", "032", "033", "034", "035", "036", "042", "043", "044", "052", "053", "054", "055", "062", "063", "072", "073", "074", "075"
}

def clean_and_validate_cambodia_phone(raw_phone: str) -> str:
    if not raw_phone:
        return ""
    digits = re.sub(r'[^\d]', '', raw_phone)
    if digits.startswith("855"):
        digits = "0" + digits[3:]
    if not digits.startswith("0"):
        digits = "0" + digits
    
    if len(digits) not in [9, 10]:
        return ""
    
    prefix = digits[:3]
    if prefix not in CAMBODIA_VALID_PREFIXES:
        return ""
    
    if len(digits) == 9:
        return f"{digits[:3]} {digits[3:6]} {digits[6:]}"
    else:
        return f"{digits[:3]} {digits[3:6]} {digits[6:]}"

def search_duckduckgo_lite(query: str, max_results: int = 5):
    url = "https://lite.duckduckgo.com/lite/"
    data = urllib.parse.urlencode({'q': query}).encode('utf-8')
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://lite.duckduckgo.com/'
        }
    )
    results = []
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            
            # Simple regex parser for DuckDuckGo Lite results
            # Result links: <a rel="nofollow" class='result-link' href="...">Title</a>
            # Snippets: <td class='result-snippet'>...</td>
            link_pattern = re.compile(r"<a[^>]+class=['\"]result-link['\"][^>]*href=['\"]([^'\"]+)['\"][^>]*>(.*?)</a>", re.DOTALL | re.IGNORECASE)
            snippet_pattern = re.compile(r"<td[^>]+class=['\"]result-snippet['\"][^>]*>(.*?)</td>", re.DOTALL | re.IGNORECASE)
            
            links = link_pattern.findall(content)
            snippets = snippet_pattern.findall(content)
            
            for i in range(min(len(links), len(snippets), max_results)):
                href, raw_title = links[i]
                title = html.unescape(re.sub(r'<[^>]+>', '', raw_title)).strip()
                snippet = html.unescape(re.sub(r'<[^>]+>', '', snippets[i])).strip()
                
                combined_text = title + " " + snippet
                raw_phones = CAMBODIA_PHONE_REGEX.findall(combined_text)
                valid_phone = ""
                for p in raw_phones:
                    val = clean_and_validate_cambodia_phone(p)
                    if val:
                        valid_phone = val
                        break
                
                results.append({
                    "title": title,
                    "url": href,
                    "snippet": snippet,
                    "phone": valid_phone
                })
    except Exception as e:
        print(f"Error: {e}")
    return results

if __name__ == "__main__":
    queries = [
        'site:facebook.com "Toyota Prius" phnom penh (012 OR 010 OR 087 OR 017)',
        'site:facebook.com "MacBook Pro M3" phnom penh phone',
        'site:khmer24.com "iPhone 16 Pro Max"'
    ]
    for q in queries:
        print(f"\n==================== SEARCH: {q} ====================")
        res = search_duckduckgo_lite(q, max_results=3)
        print(f"Results found: {len(res)}")
        for r in res:
            print(f"Title: {r['title']}")
            print(f"Phone: {r['phone'] or 'None found'}")
            print(f"URL: {r['url']}")
            print(f"Snippet: {r['snippet'][:120]}...")
            print("-" * 50)
