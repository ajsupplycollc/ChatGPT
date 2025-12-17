# AI Retail Arbitrage App (Walmart-first)

## Goal
Build a mobile (iOS + Android) AI-powered retail arbitrage app that recommends what to buy **right now** using **real-time inventory + pricing** and ranks opportunities by profitability + urgency.

## Non-Negotiables
- Mobile-first delivery (iOS + Android)
- Real-time data only (freshness validated)
- Walmart-first (expandable to Target/BestBuy/Home Depot/Lowe’s)
- Minimize user effort and decision fatigue
- Exploit every possible edge (speed, inventory collapse, pricing latency)
- No “background work” claims — only count explicit, testable artifacts

## Research Status (LOCKED)
Retail arbitrage research is considered COMPLETE and binding:
- Paid Slack arbitrage groups = speed + aggregation, not magic data
- Walmart app/back-end tends to expose richer store-level inventory than the public site
- Clearance/rollback/shelf/app mismatches propagate with latency
- Low inventory + high resale velocity is a top ROI indicator
- Do not re-research unless invalidated by evidence

## Current Phase
**BUILD PHASE ACTIVE**

## System Architecture (Modules)
A. Data Acquisition Layer
- Store + ZIP selection
- UPC/EAN, Walmart item ID/SKU
- Live price + availability polling
- Change detector (diff-based)

B. Validation Layer
- Cross-check allowed sources
- Freshness rules (timestamps/TTL/retries)
- Confidence scoring

C. Profit Engine
- Amazon / eBay / pawn-local resale models
- Fees/shipping/taxes/risk buffers (conservative)

D. Ranking & Urgency Engine
- Score = profit × probability × urgency(low stock) × confidence
- Low-inventory indicators + “act now” thresholds

E. Alerts
- Push notifications
- Top 5 “right now”
- Watchlists + thresholds

F. Mobile App UI
- Chat-style input + structured results
- Dashboard of ranked opportunities

G. Learning Loop (later, not blocking v1)
- Outcomes + personalization + false-positive suppression

## Tech Stack (Recommended)
- Mobile: React Native + TypeScript
- Backend API: FastAPI (Python)
- Workers/Jobs: Python workers (RQ/Celery or asyncio)
- Queue/Cache: Redis
- DB: Postgres
- Dev: Docker Compose

## Repo Structure (Target)
arbitrage-app/
  apps/mobile/
  services/api/
  services/workers/
  packages/shared/
  infra/
  docs/

## v1 Milestone (First Executable Demo)
- Store selection (ZIP/store ID)
- One **live** price/stock signal (even if limited)
- Profit engine v1 (conservative)
- Ranking v1
- Mobile “Top 5 right now” screen + push notification stub

## How to Resume This Project in a New Chat
Paste this repo link and say:
“Read the repo state and continue the build from the current phase.”

Repo: https://github.com/ajsupplycollc/ChatGPT

## Next Task (Do This Next)
1) Create repo skeleton folders
2) Add docs/architecture.md, docs/build_plan.md, docs/data_sources.md
3) Start backend API skeleton (FastAPI)
4) Implement first live inventory/price signal + diff-based polling worker
