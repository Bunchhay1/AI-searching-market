# 🇰🇭 Cambodia AI Market Search & Price Aggregator

ប្រព័ន្ធស្ថាបត្យកម្ម AI ស្វែងរកទំនិញ និងប្រៀបធៀបតម្លៃធូរថ្លៃបំផុតសម្រាប់ទីផ្សារប្រទេសកម្ពុជា (ផ្ទះ/បន្ទប់ជួល, ទូរស័ព្ទ, ម៉ូតូ, ឡាន ថ្មី ឬ មួយទឹក) ដោយប្រមូលទិន្នន័យពី **Khmer24, Facebook Marketplace, និង Instagram** តាមរយៈ **Microservices Architecture + Spring Boot + RabbitMQ + PostgreSQL (pgvector) + AI Semantic Search**។

---

## 🏛️ ស្ថាបត្យកម្មប្រព័ន្ធ ៤ ស្រទាប់ (4-Layer System Architecture)

```mermaid
flowchart TD
    subgraph Layer1 [Layer 1: Ingestion & Web Scrapers (Python)]
        K24[Khmer24 Scraper - BS4/Requests] -->|Publish Raw Payload| MQ[RabbitMQ Broker / market.exchange]
        FBM[FB Marketplace Worker - Playwright] -->|Publish Raw Payload| MQ
    end

    subgraph Layer2 [Layer 2: ETL & Normalization (Spring Boot)]
        MQ --> Consumer[ListingQueueConsumer]
        Consumer --> ETL[ListingEtlService]
        ETL --> Currency[CurrencyNormalizer: ៛ KHR -> $ USD]
        ETL --> HTMLClean[JSoup HTML Stripper & Metadata Extractor]
    end

    subgraph Layer3 [Layer 3: AI Vectorization & Vector DB]
        ETL --> Embedder[EmbeddingService / 768-dim Vector]
        Embedder --> PG[(PostgreSQL + pgvector Extension / HNSW Index)]
    end

    subgraph Layer4 [Layer 4: Smart Search API & Frontend UI]
        User([User / Browser]) -->|Khmer Query: ចង់បាន iPhone 13 មួយទឹក ក្រោម $400| WebUI[Frontend Glassmorphism UI]
        WebUI --> API[Spring Boot REST API: /api/v1/search]
        API --> SearchEngine[SearchService / Cosine Similarity '<=>']
        SearchEngine --> PG
        PG --> Results[Ranked Cheapest & Most Relevant Items]
        Results --> User
    end
```

---

## 📂 រចនាសម្ព័ន្ធថតឯកសារ (Project Directory Structure)

```text
AI-searching-market/
├── docker-compose.yml              # PostgreSQL 16 (pgvector) + RabbitMQ Broker
├── backend/                        # Layer 2 & 4: Java Spring Boot 3 Core
│   ├── pom.xml
│   └── src/main/
│       ├── java/com/cambodia/market/
│       │   ├── CambodiaMarketAiApplication.java
│       │   ├── config/             # RabbitMqConfig, WebConfig (CORS)
│       │   ├── consumer/           # ListingQueueConsumer (AMQP Listener)
│       │   ├── controller/         # SearchController, IngestionController
│       │   ├── dto/                # SearchRequest, SearchResponse, RawListingDto
│       │   ├── model/              # ListingItem (JPA Entity with PGvector), Enums
│       │   ├── repository/         # ListingItemRepository (Native pgvector query)
│       │   └── service/            # ListingEtlService, CurrencyNormalizer, EmbeddingService
│       └── resources/
│           ├── application.yml
│           └── schema.sql          # PostgreSQL DDL + pgvector + HNSW index
├── scrapers/                       # Layer 1: Python Scrapers & Ingestion Workers
│   ├── requirements.txt
│   ├── publisher.py                # RabbitMQ Connection & Publisher
│   ├── khmer24_scraper.py          # Khmer24 multi-category scraper
│   └── fb_marketplace_worker.py    # Playwright stealth FB Marketplace worker
└── frontend/                       # Layer 4: Modern Web UI
    └── index.html                  # Interactive Khmer AI Search Dashboard
```

---

## 🚀 របៀបតម្លើង និងដំណើរការប្រព័ន្ធ (How to Run)

### ជំហានទី ១៖ ដំណើរការ PostgreSQL (pgvector) និង RabbitMQ (Docker)
```bash
docker compose up -d
```
- **PostgreSQL**: `localhost:5432` (Database: `market_db`, User: `postgres`, Password: `postgrespassword`)
- **RabbitMQ Management Dashboard**: [http://localhost:15672](http://localhost:15672) (User: `guest`, Password: `guest`)

### ជំហានទី ២៖ ដំណើរការ Spring Boot Backend
ចូលទៅកាន់ថត `backend/` រួចដំណើរការ៖
```bash
cd backend
mvn spring-boot:run
```
- REST API នឹងដំណើរការនៅលើ: `http://localhost:8080`

### ជំហានទី ៣៖ ដំណើរការ Python Scraper (ទាញយកទិន្នន័យចូល RabbitMQ)
ចូលទៅកាន់ថត `scrapers/` រួចតម្លើង dependencies និងដំណើរការ scraper៖
```bash
cd scrapers
pip install -r requirements.txt
python khmer24_scraper.py
```
*សារនឹងត្រូវបញ្ជូនទៅ RabbitMQ ដោយស្វ័យប្រវត្តិ ហើយ Spring Boot ETL Consumer នឹងស្រូបយកមកសម្អាត បម្លែងលុយ និង Vectorize ចូល PostgreSQL។*

### ជំហានទី ៤៖ បើកផ្ទាំងស្វែងរក (Frontend UI)
បើកឯកសារ `frontend/index.html` លើ Browser របស់អ្នក ឬដំណើរការ HTTP Server:
```bash
# ឧទាហរណ៍បើកជាមួយ Python HTTP server
cd frontend
python3 -m http.server 3000
```
ចូលទៅកាន់: [http://localhost:3000](http://localhost:3000)

---

## 🧠 របៀបដែល AI Semantic Search ដំណើរការ

1. **Natural Language Intent Extraction**: ពេល User វាយ `"ចង់បាន iPhone 13 មួយទឹក ក្រោម $400 នៅភ្នំពេញ"` ប្រព័ន្ធនឹងទាញយក:
   - `Intent Condition`: `USED_SECOND_HAND`
   - `Intent Max Price`: `400 USD`
   - `Intent Location`: `Phnom Penh`
2. **Text-to-Vector Embedding**: អត្ថបទត្រូវបានបម្លែងទៅជា 768-dimensional Vector
3. **pgvector Cosine Distance Search (`<=>`)**:
   ```sql
   SELECT id, title, price_usd, (1.0 - (embedding <=> cast(:queryVector as vector))) AS similarity
   FROM listing_items
   WHERE item_condition = 'USED_SECOND_HAND' AND price_usd <= 400
   ORDER BY price_usd ASC, similarity DESC
   LIMIT 20;
   ```
4. **Normalized Currency Comparison**: ប្រព័ន្ធបម្លែងប្រាក់រៀល (KHR) ទៅជាប្រាក់ដុល្លារ (USD) ដោយស្វ័យប្រវត្តិ ធានាការស្វែងរកតម្លៃថោកបំផុតបានយ៉ាងត្រឹមត្រូវ 100%។
