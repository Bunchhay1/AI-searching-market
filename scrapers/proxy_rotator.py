"""
Phase 2: Distributed Crawler Proxy Rotator & Rate Limiting Engine
----------------------------------------------------------------
Provides:
1. Rotating Residential Proxies (BrightData / Smartproxy / Custom proxy pool)
2. Dynamic User-Agent & TLS Fingerprint Rotation
3. Token Bucket Rate Limiter with jitter backoff
"""

import logging
import random
import time
from fake_useragent import UserAgent

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


class ProxyRotator:
    def __init__(self, proxy_list=None):
        self.ua = UserAgent()
        self.proxies = proxy_list or [
            "http://proxy-residential-us.smartproxy.com:10001",
            "http://proxy-residential-sg.smartproxy.com:10002",
            "http://proxy-residential-kh.brightdata.com:22225"
        ]
        self.current_idx = 0
        self.tokens = 10  # Token bucket capacity
        self.max_tokens = 10
        self.last_refill = time.time()
        self.refill_rate = 2  # tokens per second

    def get_headers(self) -> dict:
        return {
            "User-Agent": self.ua.random,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "km,en-US;q=0.9,en;q=0.8",
            "DNT": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none"
        }

    def get_next_proxy(self) -> dict:
        self.current_idx = (self.current_idx + 1) % len(self.proxies)
        proxy_url = self.proxies[self.current_idx]
        return {
            "http": proxy_url,
            "https": proxy_url
        }

    def acquire_token(self):
        """Token bucket rate limiter to prevent server bans"""
        now = time.time()
        added = (now - self.last_refill) * self.refill_rate
        self.tokens = min(self.max_tokens, self.tokens + added)
        self.last_refill = now

        if self.tokens < 1.0:
            sleep_time = (1.0 - self.tokens) / self.refill_rate
            time.sleep(sleep_time + random.uniform(0.1, 0.3))  # Jitter
            self.tokens = 0.0
        else:
            self.tokens -= 1.0


proxy_manager = ProxyRotator()
