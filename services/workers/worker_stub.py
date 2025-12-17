"""
Worker stub for v1.

Next steps:
- Implement a poller that fetches ONE live signal (price/availability)
- Store result with observed_at + ttl + confidence
- Diff against last seen
- Trigger scoring/ranking
"""

def main():
    print("worker_stub: running (no-op)")

if __name__ == "__main__":
    main()
