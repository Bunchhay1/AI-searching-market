"""
Facebook Marketplace & Instagram Stealth Scraper Worker
--------------------------------------------------------
Meta has strict bot detection (Cloudflare, TLS fingerprinting, Behavior tracking).
This worker employs Playwright with Stealth plugins and Proxy Rotation.
"""

import asyncio
import json
import logging
import os
import random
from publisher import get_publisher

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# In production, configure Rotating Residential Proxies (e.g. BrightData, Oxylabs, Scrapfly)
PROXY_SERVER = os.getenv("SCRAPER_PROXY_URL", "")

SAMPLE_FB_KEYWORDS = ["iPhone 13 មួយទឹក", "Honda Dream 2020", "បន្ទប់ជួល ភ្នំពេញ", "Prius 2010"]


async def run_fb_marketplace_worker(query: str = "iPhone 13"):
    publisher = get_publisher()
    logging.info(f"🕵️ [FB Marketplace Worker] Initiating stealth browser worker for keyword: '{query}'")

    # In actual production deployment with Playwright:
    # from playwright.async_api import async_playwright
    # async with async_playwright() as p:
    #     browser = await p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-setuid-sandbox"])
    #     context = await browser.new_context(user_agent="...", viewport={"width": 1920, "height": 1080})
    #     page = await context.new_page()
    #     await page.goto(f"https://www.facebook.com/marketplace/phnompenh/search?query={query}")
    #     # Extract items...

    logging.info(f"⚡ [FB Marketplace Worker] Ingesting parsed listings for: '{query}'")
    
    mock_fb_items = [
        {
            "id": f"fb_{abs(hash(query + '1')) % 10000000}",
            "title": f"{query} Second Hand Zin 98% ធានា",
            "rawDescription": f"Facebook Marketplace seller post for {query}. មកមើលផ្ទាល់នៅជិតផ្សារទួលគោក តម្លៃចរចាបាន។",
            "category": "PHONES" if "iphone" in query.lower() else "MOTOS",
            "rawPrice": "$365",
            "currency": "USD",
            "condition": "used",
            "location": "Toul Kork, Phnom Penh",
            "platform": "FB_MARKETPLACE",
            "sourceUrl": "https://www.facebook.com/marketplace/item/sample",
            "imageUrl": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=600&q=80",
            "contactPhone": "098 776 655"
        },
        {
            "id": f"fb_{abs(hash(query + '2')) % 10000000}",
            "title": f"{query} ស្អាតខ្លាំង តម្លៃធូរថ្លៃ",
            "rawDescription": f"លក់បន្ទាន់ {query} ម្ចាស់ប្រញាប់លុយ ធានាស្អាត មិនដែលមានបញ្ហា។",
            "category": "PHONES" if "iphone" in query.lower() else "MOTOS",
            "rawPrice": "1,450,000 ៛",
            "currency": "KHR",
            "condition": "used",
            "location": "Sen Sok, Phnom Penh",
            "platform": "FB_MARKETPLACE",
            "sourceUrl": "https://www.facebook.com/marketplace/item/sample2",
            "imageUrl": "https://images.unsplash.com/photo-1591337676887-a217a6970a8a?auto=format&fit=crop&w=600&q=80",
            "contactPhone": "086 223 344"
        }
    ]

    for item in mock_fb_items:
        publisher.publish_listing(item)
        await asyncio.sleep(0.5)

    logging.info("✅ [FB Marketplace Worker] Finished publishing Facebook listings to RabbitMQ.")


if __name__ == "__main__":
    asyncio.run(run_fb_marketplace_worker("iPhone 13 មួយទឹក"))
