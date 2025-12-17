from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import os

app = FastAPI(title="AI Retail Arbitrage API", version="0.1.0")

DATABASE_URL = os.getenv("DATABASE_URL", "")
REDIS_URL = os.getenv("REDIS_URL", "")

class StoreCandidate(BaseModel):
    store_id: str
    name: str
    city: str
    state: str

class SelectStoreRequest(BaseModel):
    zip: str
    store_id: str

class Opportunity(BaseModel):
    id: str
    title: str
    buy_price: float
    est_resale: float
    est_fees: float
    est_net_profit: float
    stock_indicator: str  # e.g. HIGH / MED / LOW / UNKNOWN
    confidence: float     # 0..1
    observed_at: str      # ISO timestamp string for now

@app.get("/health")
def health():
    return {
        "status": "ok",
        "env": os.getenv("APP_ENV", "unknown"),
        "database_url_set": bool(DATABASE_URL),
        "redis_url_set": bool(REDIS_URL),
    }

@app.get("/stores/search", response_model=List[StoreCandidate])
def search_stores(zip: str):
    # v1 stub: replace with live store lookup later
    return [
        StoreCandidate(store_id="0001", name="Walmart Supercenter", city="Miami Gardens", state="FL"),
        StoreCandidate(store_id="0002", name="Walmart Neighborhood Market", city="Miami", state="FL"),
    ]

@app.post("/stores/select")
def select_store(req: SelectStoreRequest):
    # v1 stub: later persist selection to DB keyed by user/session
    return {"selected": True, "zip": req.zip, "store_id": req.store_id}

@app.get("/opportunities/top", response_model=List[Opportunity])
def top_opportunities(limit: int = 5):
    # v1 stub: later sourced from live worker pipeline + DB
    sample = [
        Opportunity(
            id="op_001",
            title="SAMPLE ITEM (stub)",
            buy_price=49.00,
            est_resale=129.00,
            est_fees=22.00,
            est_net_profit=58.00,
            stock_indicator="UNKNOWN",
            confidence=0.30,
            observed_at="2025-12-17T00:00:00Z",
        )
    ]
    return sample[:limit]
