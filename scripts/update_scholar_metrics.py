#!/usr/bin/env python3
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen


SCHOLAR_USER_ID = "-DlGT8IAAAAJ"
SCHOLAR_URL = f"https://scholar.google.com/citations?user={SCHOLAR_USER_ID}&hl=en"
OUTPUT_PATH = Path("_data/scholar_metrics.json")


def fetch_html(url: str) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            )
        },
    )
    with urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", "ignore")


def parse_metrics(html: str) -> tuple[int, int]:
    values = re.findall(r'<td class="gsc_rsb_std">([^<]+)</td>', html)
    cleaned = [value.replace(",", "").strip() for value in values]
    if len(cleaned) >= 4 and cleaned[0].isdigit() and cleaned[2].isdigit():
        return int(cleaned[0]), int(cleaned[2])

    cited_by_match = re.search(r"Cited by ([0-9,]+)", html)
    h_index_match = re.search(r'h-index</a></td><td class="gsc_rsb_std">([0-9,]+)</td>', html)
    if cited_by_match and h_index_match:
        citations = int(cited_by_match.group(1).replace(",", ""))
        h_index = int(h_index_match.group(1).replace(",", ""))
        return citations, h_index

    raise ValueError("Could not parse Google Scholar metrics")


def load_existing(path: Path) -> dict | None:
    if not path.exists():
        return None
    return json.loads(path.read_text())


def main() -> int:
    existing = load_existing(OUTPUT_PATH)
    try:
        html = fetch_html(SCHOLAR_URL)
        citations, h_index = parse_metrics(html)
    except Exception as exc:
        if existing:
            print(
                f"Warning: failed to refresh Google Scholar metrics ({exc}); using cached data.",
                file=sys.stderr,
            )
            return 0
        raise

    next_data = {
        "citations": citations,
        "h_index": h_index,
        "user_id": SCHOLAR_USER_ID,
        "source_url": SCHOLAR_URL,
        "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }

    if existing:
        unchanged = (
            existing.get("citations") == citations
            and existing.get("h_index") == h_index
            and existing.get("user_id") == SCHOLAR_USER_ID
            and existing.get("source_url") == SCHOLAR_URL
        )
        if unchanged:
            print(f"Metrics unchanged: citations={citations}, h_index={h_index}")
            return 0

    OUTPUT_PATH.write_text(json.dumps(next_data, indent=2, ensure_ascii=False) + "\n")
    print(f"Updated metrics: citations={citations}, h_index={h_index}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
