#!/usr/bin/env python3
"""Validate that the documented scraper integration contract stays explicit."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
doc = ROOT / "docs" / "REALTIME_DATA_10_SCRAPERS.md"
readme = ROOT / "README.md"

def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)

if not doc.exists():
    fail("Missing docs/REALTIME_DATA_10_SCRAPERS.md")
text = doc.read_text(encoding="utf-8")
required = [
    "Ten independent scraper adapters",
    "These are adapter roles, not ten sources that are already connected",
    "stale",
    "signature-verified payment webhooks",
    "server-side endpoint",
    "Release checklist",
]
for phrase in required:
    if phrase.lower() not in text.lower():
        fail(f"Missing required integration safeguard: {phrase}")
if not readme.exists():
    fail("Missing README.md")
readme_text = readme.read_text(encoding="utf-8")
if "REALTIME_DATA_10_SCRAPERS.md" not in readme_text:
    fail("README must link the scraper integration contract")
print("PASS: real-time data integration contract and safety disclosures are present.")
