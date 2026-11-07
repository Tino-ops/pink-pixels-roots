"""ROOTS manual metadata entry tool. Python 3, no external dependencies.
Run: python metadata_entry.py
The exported JSON can be imported from ROOTS > Search > Import institution metadata.
Records are unverified until a reviewer checks their original source URLs.
"""
import json
from pathlib import Path
from urllib.parse import urlparse

records = []
while True:
    title = input("Record title (blank to finish): ").strip()
    if not title:
        break
    institution = input("Holding/source institution: ").strip()
    source = input("Original source URL (https://...): ").strip()
    parsed = urlparse(source)
    if not institution or parsed.scheme not in ("https", "http") or not parsed.netloc:
        print("Institution and a valid http(s) source URL are required. Entry skipped.")
        continue
    date = input("Historical year or period (optional): ").strip()
    location = input("Location (optional): ").strip()
    resource_type = input("Resource type (optional): ").strip()
    description = input("Description (optional): ").strip()
    records.append({
        "title": title,
        "institution": institution,
        "sourceURL": source,
        "date": date,
        "location": location,
        "type": resource_type or "Historical resource",
        "description": description,
    })
    print("Entry added.\n")

out = Path("roots_metadata.json")
out.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved {len(records)} records to {out.resolve()}")
