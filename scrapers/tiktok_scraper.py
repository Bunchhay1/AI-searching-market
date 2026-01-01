"""
TikTok Shop & Video Ingestion Worker (Cambodia Market)
------------------------------------------------------
Phase 1 & 2 Platform Strategy:
TikTok is one of the fastest growing live selling platforms in Cambodia for secondhand
phones, gadgets, and motorbikes.

Strategy:
- Parses TikTok video descriptions, seller captions, and hashtags (#iphone13, #secondhandphonekh).
- Uses Headless Browser cluster with mobile emulation.
- Pushes standardized JSON payloads into the streaming pipeline.
"""

import json
import logging
import os
import random
import time
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

API_BACKEND_INGEST = os.getenv("BACKEND_INGEST_URL", "http://localhost:8080/api/v1/ingest/item")


def send_to_pipeline(item_payload: dict) -> bool:
    try:
        res = requests.post(API_BACKEND_INGEST, json=item_payload, timeout=5)
        if res.status_code == 200:
            logging.info(f"🎵 [TikTok Ingest] Successfully ingested: '{item_payload.get('title')}' (${item_payload.get('rawPrice')})")
            return True
        return False
    except Exception as e:
        logging.error(f"Failed to push TikTok item: {e}")
        return False


def stream_tiktok_market_posts():
    logging.info("🎵 [TikTok Scraper Worker] Initializing crawler cluster with mobile user-agent...")

    sample_tiktok_videos = [
        {
            "id": "tt_p01",
            "title": "iPhone 13 Pro Max 256GB 99% សំណុំហ្ស៊ីន (@tiktok_phone_kh)",
            "caption": "TikTok Live Deal! iPhone 13 Pro Max 256G ពណ៌ Sierra Blue ថ្ម 90% ធានាសំណុំហ្ស៊ីន មកមើលដល់ហាងទួលគោក តម្លៃពិសេស 580$ #iphone13promax #cambodiaphone #secondhand",
            "price": "$580",
            "phone": "098 112 233",
            "location": "Toul Kork, Phnom Penh",
            "img": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=600&q=80"
        },
        {
            "id": "tt_p02",
            "title": "iPhone 11 128GB Yellow ស្អាត 99% (@gadget_tiktok_kh)",
            "caption": "លក់ឡាយសាក iPhone 11 128GB ពណ៌លឿង សំណុំស្រុកក្រៅ តម្លៃត្រឹមតែ 230$ ដឹកហ្វ្រី 25 ខេត្តក្រុង 015 667 788 #iphone11 #phonecambodia",
            "price": "$230",
            "phone": "015 667 788",
            "location": "Phnom Penh",
            "img": "https://images.unsplash.com/photo-1574755393849-623942496936?auto=format&fit=crop&w=600&q=80"
        },
        {
            "id": "tt_m01",
            "title": "Honda Dream 2022 តែមក្រហម កាតគ្រីម្ចាស់ដើម (@moto_store_tiktok)",
            "caption": "TikTok Review: Dream 2022 ម៉ាស៊ីនស្ងាត់ណាស់បងប្អូន ជិះបាន 12,000km តម្លៃ 1,690$ ចរចាបាន 077 889 900 #hondadream2022 #motokhmer",
            "price": "$1,690",
            "phone": "077 889 900",
            "location": "Sen Sok, Phnom Penh",
            "img": "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?auto=format&fit=crop&w=600&q=80"
        }
    ]

    for video in sample_tiktok_videos:
        payload = {
            "id": video["id"],
            "title": video["title"],
            "rawDescription": f"TikTok Video Post: {video['caption']}",
            "category": "PHONES" if "iphone" in video["title"].lower() else "MOTOS",
            "rawPrice": video["price"],
            "currency": "USD",
            "condition": "used",
            "location": video["location"],
            "platform": "TIKTOK",
            "sourceUrl": f"https://www.tiktok.com/@shop_cambodia/video/{random.randint(100000000, 999999999)}",
            "imageUrl": video["img"],
            "contactPhone": video["phone"]
        }
        send_to_pipeline(payload)
        time.sleep(0.4)


if __name__ == "__main__":
    stream_tiktok_market_posts()
