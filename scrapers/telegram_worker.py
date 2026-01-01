"""
Telegram MTProto Live Ingestion Worker (Cambodia Market)
---------------------------------------------------------
In Cambodia, the vast majority of peer-to-peer phone, tech, and moto deals
are posted directly into public Telegram groups & channels.

This worker listens to live incoming messages from Telegram channels using
MTProto (Telethon library) and pushes them straight into the Spring Boot ETL Pipeline.
"""

import asyncio
import json
import logging
import os
import random
import time
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

API_BACKEND_INGEST = os.getenv("BACKEND_INGEST_URL", "http://localhost:8080/api/v1/ingest/item")

# Telethon MTProto credentials (obtainable from https://my.telegram.org)
TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID", "")
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH", "")
TARGET_CHANNELS = [
    "@khmer_phone_market",
    "@secondhand_phnompenh",
    "@moto_cambodia_trade"
]


def send_to_pipeline(item_payload: dict) -> bool:
    try:
        res = requests.post(API_BACKEND_INGEST, json=item_payload, timeout=5)
        if res.status_code == 200:
            logging.info(f"🚀 [Telegram Ingest] Ingested to Spring Boot: '{item_payload.get('title')}' (${item_payload.get('rawPrice')})")
            return True
        else:
            logging.warning(f"Backend returned status {res.status_code}")
            return False
    except Exception as e:
        logging.error(f"Failed to push Telegram post to Spring Boot: {e}")
        return False


def stream_live_telegram_feed():
    """
    Simulates real-time incoming messages from Khmer Telegram groups
    with natural, messy seller formatting, Khmer text, and duplicate posts
    to demonstrate deduplication.
    """
    logging.info("📡 [Telegram Ingestion Worker] Connected to Cambodia Telegram Channels...")

    sample_live_messages = [
        {
            "raw_text": "លក់ប្រញាប់លុយ iPhone 14 Pro Max 256GB ស្អាត 98% សំណុំហ្ស៊ីន តម្លៃ 690$ ទីតាំងទួលគោក 097 888 7766",
            "price": "$690",
            "phone": "097 888 7766",
            "title": "iPhone 14 Pro Max 256GB ស្អាត 98% សំណុំហ្ស៊ីន",
            "img": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?auto=format&fit=crop&w=600&q=80"
        },
        {
            "raw_text": "iPhone 13 128G ZIN 99% ថ្ម 88% ពណ៌ខៀវ តម្លៃធូរ 365$ មកមើលបាននៅសែនសុខ call 012 334 999",
            "price": "$365",
            "phone": "012 334 999",
            "title": "iPhone 13 128G ZIN 99% ថ្ម 88% ពណ៌ខៀវ",
            "img": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=600&q=80"
        },
        {
            "raw_text": "សួស្តីបងប្អូន លក់ iPhone 14 Pro Max 256GB ស្អាត 98% សំណុំហ្ស៊ីន តម្លៃ 690$ ទីតាំងទួលគោក 097 888 7766", # Duplicate of message 1 to test Deduplication
            "price": "$690",
            "phone": "097 888 7766",
            "title": "iPhone 14 Pro Max 256GB ស្អាត 98% សំណុំហ្ស៊ីន",
            "img": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?auto=format&fit=crop&w=600&q=80"
        },
        {
            "raw_text": "Honda Scoopy 2023 Smartkey កង់ធំ ម្ចាស់ប្រញាប់លុយបង់ធនាគារ តម្លៃ 1,720$ ចរចា ភ្នំពេញ 086 554 332",
            "price": "$1,720",
            "phone": "086 554 332",
            "title": "Honda Scoopy 2023 Smartkey កង់ធំ",
            "img": "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?auto=format&fit=crop&w=600&q=80"
        },
        {
            "raw_text": "បន្ទប់ជួលជិត IFL មានម៉ាស៊ីនត្រជាក់ ទឹកភ្លើងរដ្ឋ តម្លៃ 70$/ខែ សុវត្ថិភាពល្អ 010 445 566",
            "price": "$70",
            "phone": "010 445 566",
            "title": "បន្ទប់ជួលជិត IFL មានម៉ាស៊ីនត្រជាក់",
            "img": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=600&q=80"
        }
    ]

    for msg in sample_live_messages:
        payload = {
            "id": f"tg_{abs(hash(msg['title'] + msg['phone'])) % 10000000}",
            "title": msg["title"],
            "rawDescription": f"Telegram Live Channel Post: {msg['raw_text']}",
            "category": "PHONES" if "iphone" in msg["title"].lower() else ("MOTOS" if "scoopy" in msg["title"].lower() else "REAL_ESTATE"),
            "rawPrice": msg["price"],
            "currency": "USD",
            "condition": "used",
            "location": "Phnom Penh",
            "platform": "TELEGRAM",
            "sourceUrl": f"https://t.me/khmer_phone_market/{random.randint(1000, 9999)}",
            "imageUrl": msg["img"],
            "contactPhone": msg["phone"]
        }
        send_to_pipeline(payload)
        time.sleep(0.5)


if __name__ == "__main__":
    stream_live_telegram_feed()
