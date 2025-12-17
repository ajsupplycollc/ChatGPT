# Data Sources (Walmart-first)

## Guiding Rules
- Real-time only (timestamped + TTL)
- Use only publicly accessible or user-authorized data
- If a source is unreliable, mark confidence low and do not recommend

## Signal Types
1) Price signal
- Current buy price (store-level if possible)

2) Availability signal
- In-stock / limited stock / out-of-stock
- Quantity if available
- “Pickup available” as proxy if quantity not available

3) Identifier mapping
- UPC/EAN ↔ Walmart item ID ↔ SKU
- Later: UPC/EAN ↔ Amazon ASIN ↔ eBay listing comps

## Walmart-first Approaches (Ordered)
A) Official/Allowed
- Public product pages (price/availability)
- Pickup/delivery availability endpoints when accessible

B) App-level / Semi-public
- Data exposed by Walmart mobile flows (requires careful validation and compliance)
- Use only if accessible without violating access controls

C) User-assisted (Fallback that keeps us compliant and live)
- User scans barcode in Walmart app / scanner and inputs:
  - price
  - store availability status
- App uses that as “ground truth” when automation fails

## Freshness & Confidence
- Each signal stored with:
  - observed_at (timestamp)
  - source
  - ttl_seconds
  - confidence (0–1)
- Recommendations require:
  - observed_at within TTL
  - confidence above threshold

## Resale Data (Later)
- Amazon/eBay comps require:
  - stable product matching
  - fee model
  - avoid restricted categories
