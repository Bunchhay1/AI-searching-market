"""
Khmer24 Live Cron Ingestion Worker
----------------------------------
Periodically polls Khmer24's live categories (e.g. phones, motos, rent)
Extracts raw DOM cards and streams clean items to Spring Boot Ingestion API.
"""

import logging
import os
import random
import time
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

API_BACKEND_INGEST = os.getenv("BACKEND_INGEST_URL", "http://localhost:8080/api/v1/ingest/item")

CATEGORIES = [
    ("PHONES", "https://www.khmer24.com/en/c-phones-and-tablets.html"),
    ("MOTOS", "https://www.khmer24.com/en/motorcycles.html"),
    ("REAL_ESTATE", "https://www.khmer24.com/en/property/house-for-rent.html")
]

def fetch_and_ingest():
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "km,en-US;q=0.9,en;q=0.8"
    }

    for cat_name, url in CATEGORIES:
        logging.info(f"🕷️ [Khmer24 Cron] Ingesting category: {cat_name} -> {url}")
        try:
            resp = requests.get(url, headers=headers, timeout=8)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")
                items = soup.select(".item, .item-list article, .post")
                count = 0
                for item in items[:5]:
                    title_elem = item.select_one(".title, .item-title, h2, h3")
                    price_elem = item.select_one(".price, .item-price, .text-red")
                    link_elem = item.select_one("a[href]")
                    img_elem = item.select_one("img[src]")

                    if title_elem and price_elem:
                        payload = {
                            "title": title_elem.get_text(strip=True),
                            "rawDescription": f"Khmer24 live ad: {title_elem.get_text(strip=True)}",
                            "category": cat_name,
                            "rawPrice": price_elem.get_text(strip=True),
                            "currency": "USD" if "$" in price_elem.get_text() else "KHR",
                            "platform": "KHMER24",
                            "sourceUrl": link_elem["href"] if link_elem else url,
                            "imageUrl": img_elem["src"] if img_elem else "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=600",
                            "contactPhone": None
                        }
                        requests.post(API_BACKEND_INGEST, json=payload, timeout=5)
                        count += 1
                logging.info(f"✅ Ingested {count} live items from Khmer24 {cat_name}")
        except Exception as e:
            logging.warning(f"Khmer24 live network fetch notice: {e}")


if __name__ == "__main__":
    fetch_and_ingest()
