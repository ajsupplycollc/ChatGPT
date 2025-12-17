# Architecture (Build-Ready)

## Purpose
Mobile-first AI retail arbitrage system (Walmart-first) using real-time inventory + pricing and ranking opportunities by profit + urgency + confidence.

## High-Level Components
1) Mobile App (React Native)
- Store selection (ZIP/store)
- “Top 5 right now” dashboard
- Item detail view (price/stock/profit/confidence)
- Push notifications
- Optional chat-style query interface

2) Backend API (FastAPI)
- Auth (later)
- Store management (ZIP → store)
- Opportunity feed endpoint (ranked items)
- Watchlists + thresholds (later)
- Health/freshness reporting

3) Workers (Polling + Diff + Rank)
- Poll inventory/price signals
- Compute diffs and emit events only on change
- Validate freshness + confidence
- Run profit calc and ranking
- Trigger alerts when thresholds met

4) Data Stores
- Redis (cache, queues, TTL freshness)
- Postgres (stores, items, signals, opportunities, history)

## Data Flow (Core Loop)
Poll → Validate → Diff → Score → Rank → Notify → Serve to Mobile

## Non-Negotiables
- Real-time only: every signal must have timestamp + TTL + retry policy
- No background “pretend” progress: only explicit artifacts count
- Modular connectors: Walmart first, others later

## APIs (Initial)
GET /health
GET /stores/search?zip=XXXXX
POST /stores/select
GET /opportunities/top?limit=5
GET /opportunities/{id}

## Workers (Initial)
- poller: fetch live price/stock signals
- differ: compare to last seen; emit change events
- scorer: profit + urgency + confidence
- notifier: stub (logs now; push later)

## “v1 Done” Definition
- A user selects a store
- Backend produces Top 5 ranked opportunities using at least one live signal
- Mobile displays Top 5 and refreshes
