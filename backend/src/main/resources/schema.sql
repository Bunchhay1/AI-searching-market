-- Enable the pgvector extension for AI Semantic Embeddings
CREATE EXTENSION IF NOT EXISTS vector;

-- Create table for aggregated Cambodian Market Listings
CREATE TABLE IF NOT EXISTS listing_items (
    id VARCHAR(64) PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    category VARCHAR(50) NOT NULL,           -- PHONES, MOTOS, REAL_ESTATE, CARS, ELECTRONICS
    item_condition VARCHAR(20) NOT NULL,     -- NEW, USED_SECOND_HAND
    price_usd NUMERIC(12, 2) NOT NULL,       -- Normalized price in USD for comparison
    original_price NUMERIC(14, 2) NOT NULL,  -- Original parsed price
    original_currency VARCHAR(10) NOT NULL,  -- USD or KHR
    location VARCHAR(100),                   -- e.g., Phnom Penh, Siem Reap, Toul Kork, Sen Sok
    platform VARCHAR(50) NOT NULL,           -- KHMER24, FB_MARKETPLACE, INSTAGRAM
    source_url TEXT,
    image_url TEXT,
    contact_phone VARCHAR(50),
    embedding vector(768),                   -- 768-dim vector embedding for semantic search (Gemini/BERT/OpenAI)
    raw_payload JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create standard indexes for rapid filtering
CREATE INDEX IF NOT EXISTS idx_listing_category ON listing_items(category);
CREATE INDEX IF NOT EXISTS idx_listing_condition ON listing_items(item_condition);
CREATE INDEX IF NOT EXISTS idx_listing_price_usd ON listing_items(price_usd);
CREATE INDEX IF NOT EXISTS idx_listing_location ON listing_items(location);
CREATE INDEX IF NOT EXISTS idx_listing_platform ON listing_items(platform);

-- Create HNSW (Hierarchical Navigable Small World) Index on vector column for ultra-fast Cosine Distance searches
CREATE INDEX IF NOT EXISTS idx_listing_embedding_hnsw 
ON listing_items USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);
