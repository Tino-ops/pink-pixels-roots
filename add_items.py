"""Create ROOTS-compatible JSON records and search them locally.

Run: python add_items.py
Import item_records.json from ROOTS > Search > Import historical metadata (JSON).
Only add records with an original, verifiable institutional source URL.
"""
import json
from pathlib import Path
from urllib.parse import urlparse

OUTPUT = Path("item_records.json")
records = []

def valid_url(value):
    parsed = urlparse(value)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)

while True:
    title = input("Record title (blank to finish): ").strip()
    if not title:
        break
    institution = input("Holding/source institution: ").strip()
    source_url = input("Original institutional record URL: ").strip()
    if not institution or not valid_url(source_url):
        print("Institution and a valid http(s) source URL are required. Please try again.")
        continue
    date = input("Date or historical period (optional): ").strip()
    description = input("Short description (optional): ").strip()
    location = input("Location (optional): ").strip()
    resource_type = input("Resource type (optional): ").strip()
    access_status = input("Access status (Online / Available by request / On-site only / Unknown): ").strip() or "Unknown"

    record = {
        "title": title,
        "institution": institution,
        "sourceURL": source_url,
        "date": date,
        "description": description,
        "location": location,
        "type": resource_type or "Historical resource",
        "accessStatus": access_status,
    }
    records.append(record)
    print("Record added.\n")
    more = input("Add another record? (yes/no): ").strip().lower()
    if more != "yes":
        break

OUTPUT.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved {len(records)} record(s) to {OUTPUT.resolve()}")
print("Import this JSON file in ROOTS > Search > Import historical metadata (JSON).")

while records:
    keyword = input("Search descriptions/titles (or 'done' to finish): ").strip().lower()
    if keyword == "done":
        break
    if not keyword:
        continue
    matches = [r for r in records if keyword in (r["title"] + " " + r["description"]).lower()]
    for r in matches:
        print(f"{r['title']} | {r['institution']} | {r['sourceURL']}")
    if not matches:
        print("No matching records found.")
