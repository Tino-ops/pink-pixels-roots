#!/usr/bin/env python3
"""Build data/roots-records.js from per-source raw files.

Each file in data/sources/ keeps a source's OWN field names. data/sources.json
says how those fields map onto the common ROOTS (Dublin Core based) schema.
Nothing is guessed: missing values stay empty/unknown, and every record carries
provenance (which source, how it was collected, which fields were mapped, and
which fields a ROOTS curator added).

Run:  python3 scripts/build_records.py
"""
import json, re, sys, pathlib, urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
PROVINCES = ["Alberta","British Columbia","Manitoba","New Brunswick","Newfoundland and Labrador",
             "Northwest Territories","Nova Scotia","Nunavut","Ontario","Prince Edward Island",
             "Quebec","Saskatchewan","Yukon"]
ACCESS_OK = {"online","on-site only","available by request","partly online","unknown"}
TYPE_MAP = {  # source vocabulary -> ROOTS resource type
 "archival fonds":"Archival collection","archival series":"Archival collection","archival collection":"Archival collection",
 "archival collection (multi-institution)":"Archival collection","archival record":"Archival collection","photograph series":"Archival collection",
 "archival item":"Document","digitized document":"Document","report (library holding)":"Document",
 "online exhibit":"Online exhibit","online presentation":"Online exhibit","oral history":"Oral history","video":"Video",
 "research guide":"Research guide","blog post":"Article","reference article":"Article",
 "newspaper":"Newspaper / magazine","newspaper or magazine":"Newspaper / magazine",
 "digitized microfilm":"Microfilm","microfilm":"Microfilm","crowdsourcing project":"Crowdsourcing project",
 "book":"Book","museum / visitor centre":"Museum / visitor centre"}
YEAR = re.compile(r"(?<!\d)(1[5-9]\d\d|20\d\d)(?!\d)")
DECADE = re.compile(r"(?<!\d)(1[5-9]\d|20\d)0s")

def parse_date(text):
    t = (text or "").strip()
    if not t:
        return {"display": "Date not stated", "start": None, "end": None, "certainty": "unknown"}
    years = [int(y) for y in YEAR.findall(t)]
    dec = DECADE.search(t)
    approx = "?" in t or "c." in t.lower() or "circa" in t.lower() or bool(dec)
    if years:
        start, end = min(years), max(years)
    elif dec:
        start = int(dec.group(1) + "0"); end = start + 9
    else:
        return {"display": t, "start": None, "end": None, "certainty": "unknown"}
    display = t.replace(" to ", "\u2013")
    if approx and "approx" not in display.lower():
        display += " (approximate)"
    return {"display": display, "start": start, "end": end, "certainty": "approximate" if approx else "exact"}

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:48]

def good_url(u):
    try:
        p = urllib.parse.urlparse(u); return p.scheme in ("http", "https") and bool(p.netloc)
    except Exception:
        return False

def main():
    reg = json.loads((DATA / "sources.json").read_text(encoding="utf-8"))
    snap = reg["snapshot_date"]
    records, problems, seen = [], [], set()
    for src in reg["sources"]:
        raw = json.loads((DATA / "sources" / src["raw_file"]).read_text(encoding="utf-8"))
        fmap = src["field_map"]
        for i, row in enumerate(raw):
            mapped = {}
            for native, target in fmap.items():
                v = row.get(native)
                if v not in (None, ""):
                    mapped[target] = v
            cur = row.get("curated", {})
            where = f"{src['id']}[{i}]"
            title = str(mapped.get("title", "")).strip()
            url = str(mapped.get("sourceURL", "")).strip()
            if not title: problems.append(f"{where}: missing title")
            if not good_url(url): problems.append(f"{where}: missing or invalid source URL")
            key = (url, title.lower())
            if key in seen: problems.append(f"{where}: duplicate of an earlier record")
            seen.add(key)
            acc = cur.get("access", "Unknown")
            if acc.lower() not in ACCESS_OK: problems.append(f"{where}: unknown access value {acc!r}")
            d = parse_date(mapped.get("date_text", ""))
            location = str(mapped.get("location") or "Not specified").strip()
            province = next((p for p in PROVINCES if p.lower() in location.lower()), "")
            src_type = str(mapped.get("type") or "").strip()
            rtype = TYPE_MAP.get(src_type.lower(), src_type or "Historical resource")
            if src_type.lower() not in TYPE_MAP: problems.append(f"{where}: type {src_type!r} not in vocabulary map (kept as is)")
            curator_added = [k for k in ("category","people","subjects","access","access_note","coordinates","also_held_by","source_note") if cur.get(k) not in (None, [], "")]
            rec = {
              "id": f"{src['id']}-{slug(title)}", "title": title, "description": str(mapped.get("description", "")).strip(),
              "category": cur.get("category", "Other"), "type": rtype,
              "institution": src["institution"], "sourceURL": url, "original_source": str(mapped.get("original_source", "")).strip(),
              "period": d["display"], "date_text": str(mapped.get("date_text", "")).strip(),
              "date_start": d["start"], "date_end": d["end"], "date_certainty": d["certainty"], "year": d["start"],
              "location": location, "province": province, "coordinates": cur.get("coordinates"),
              "people": cur.get("people", []), "subjects": cur.get("subjects", []), "keywords": [],
              "accessStatus": acc, "accessNote": cur.get("access_note", ""), "restricted": False,
              "rights_statement": src["rights_notice"], "also_held_by": cur.get("also_held_by", []),
              "image": "", "imageAlt": "", "imageCredit": "No image shown: thumbnails need permission from the holding institution.",
              "sourceNote": cur.get("source_note", ""),
              "provenance": {"source_system": src["id"], "source_name": src["institution"], "method": src["method"],
                             "collected_from": src["collected_from"], "retrieved_at": snap,
                             "source_type_term": src_type, "mapped_fields": {k: v for k, v in fmap.items() if k in row and row.get(k) not in (None, "")},
                             "curator_added": curator_added},
            }
            rec["body"] = rec["description"]
            records.append(rec)
    out_sources = [{k: s[k] for k in ("id","institution","kind","website","home","collected_from","source_format","method","rights_notice","field_map")} for s in reg["sources"]]
    build = {"built": snap, "records": len(records), "institutions": len(out_sources)}
    js = ("/* GENERATED by scripts/build_records.py - edit data/sources/*.raw.json or data/sources.json instead. */\n"
          "window.ROOTS_DATA=" + json.dumps(records, ensure_ascii=False, indent=1) + ";\n"
          "window.ROOTS_SOURCES=" + json.dumps(out_sources, ensure_ascii=False, indent=1) + ";\n"
          "window.ROOTS_BUILD=" + json.dumps(build) + ";\n")
    (DATA / "roots-records.js").write_text(js, encoding="utf-8")
    (DATA / "roots-records.json").write_text(json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8")
    by = {}
    for r in records: by[r["institution"]] = by.get(r["institution"], 0) + 1
    print(f"Built {len(records)} records from {len(out_sources)} sources")
    for k, v in sorted(by.items(), key=lambda kv: -kv[1]): print(f"  {v:3d}  {k}")
    unknown = sum(1 for r in records if r["date_certainty"] == "unknown"); approx = sum(1 for r in records if r["date_certainty"] == "approximate")
    print(f"Dates: {unknown} unknown, {approx} approximate")
    if problems:
        print("\nProblems:"); [print("  -", p) for p in problems]; sys.exit(1)

if __name__ == "__main__":
    main()
