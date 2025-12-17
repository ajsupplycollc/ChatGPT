# Build Plan (Execution Order)

## Phase 0 — Repo Bootstrap (Day 0)
- Create folders:
  - apps/mobile
  - services/api
  - services/workers
  - packages/shared
  - infra
  - docs
- Add README.md + docs/*.md
- Add .gitignore

## Phase 1 — Backend Skeleton (v1)
- FastAPI app with:
  - /health
  - /stores/search (stub returns sample store)
  - /stores/select (stores selected store in DB)
  - /opportunities/top (stub returns sample opportunities)
- Postgres schema v1
- Redis connected
- Docker compose for api + postgres + redis

## Phase 2 — Live Signal v1 (Walmart-first)
- Implement ONE live price/stock signal path (even limited)
- Store the raw signal with timestamp
- Add freshness rules:
  - TTL
  - retry/backoff
  - confidence scoring

## Phase 3 — Profit Engine v1 (Conservative)
- Fee placeholders + buffers
- Profit model outputs:
  - buy_price
  - est_resale
  - fees
  - net_profit
  - confidence

## Phase 4 — Ranking v1
- Score = net_profit × urgency(low stock) × confidence
- Output Top 5 ranked

## Phase 5 — Mobile v1 (React Native)
- Store selection screen
- Top 5 screen
- Item detail screen

## Phase 6 — Alerts (Stub → Real)
- Stub: log “ALERT” events
- Real: push notification pipeline

## Phase 7 — Validation / Testing
- Simulated tests + one real store test
- Tighten false positives
- Improve freshness/TTL policies

## Definition of v1 Success
From home:
- User selects store
- Gets Top 5 “buy now” recommendations with live data timestamps
In store:
- App helps verify quickly and reduces walking/thinking
