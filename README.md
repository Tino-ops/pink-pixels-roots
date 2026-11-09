# ROOTS — National Black History Knowledge Hub 🌱

**Every story has roots. Find yours.**

ROOTS is a Black Canadian history discovery hub created by **Pink Pixels** for **RBC HubHacks 2026**, responding to the challenge from the **Black Cultural Centre for Nova Scotia (BCCNS)**.

Historical resources are spread across archives, libraries, museums, universities and community organizations. ROOTS helps people discover those resources through a shared search experience **without copying or taking ownership of the original collections**. Each indexed record points back to its source.

**[Open the ROOTS demo](https://tino-ops.github.io/pink-pixels-roots/)** · **[Source code](https://github.com/Tino-ops/pink-pixels-roots)**

> **Prototype, not a production archive.** The initial index contains **46 hand-collected metadata records from seven source organizations**, assembled on **November 8, 2026**. These organizations are data sources, **not claimed institutional partners**. Live harvesting, institutional approval, and server-side publication are not implemented.

## Try the demo

1. Open the [live demo](https://tino-ops.github.io/pink-pixels-roots/) or open `index.html` locally in a modern browser.
2. Use **Search** to find people, places, subjects, institutions and resource types. Try **Mary Ann Shadd Cary**.
3. Open a record to inspect the holding/source institution, access information, original URL and provenance.
4. Explore the **Institutions**, **Timeline**, **Map**, and **Data model** views where records have suitable metadata.
5. Try **Ask ROOTS** with a historical question. It searches the indexed records rather than generating unsupported historical narratives.

The site is a static HTML/CSS/JavaScript application. There is **no npm installation or build step** for the interface. The map may require internet access for external mapping services.

## What is implemented

| Feature | Prototype behavior |
| --- | --- |
| Search and filters | Keyword search and filters for province, institution, people, places, subjects, resource type, access and years |
| Ask ROOTS | Rule-based, index-grounded search; reports when matching records are absent; **not a generative AI model** |
| Record details | Source/holder, original link, access instructions, provenance, reference information where available, and related records |
| Institutions | Overview of represented sources and their indexed records |
| Timeline and map | Explore records with usable dates or coordinates |
| Data model | Common metadata fields and source-specific mappings |
| Import/contributions | Prototype metadata import and contribution interactions; browser-local behavior is **not shared publication** |

The index contains descriptive metadata and links, **not copies of entire historical collections**. Index summaries may be authored for ROOTS rather than supplied verbatim by source institutions. Original sources remain authoritative.

## Data sources

| Source organization | Indexed records |
| --- | ---: |
| Nova Scotia Archives | 17 |
| Archives of Ontario | 12 |
| Library and Archives Canada | 11 |
| Canadiana | 3 |
| Black Cultural Centre for Nova Scotia | 1 |
| University of Calgary Libraries | 1 |
| The Canadian Encyclopedia | 1 |
| **Total** | **46** |

These counts describe the **sample snapshot**, not live synchronized catalogues or formal partnerships. Records may have incomplete dates, rights or geographic metadata; ROOTS should not infer missing facts.

## Repository structure

```text
index.html                    Static landing page and application
data/
  roots-records.js            Generated index loaded by the browser
  roots-records.json          JSON version of the index
  sources.json                Source-specific mappings to common fields
  sources/*.raw.json          Sample source metadata in source-specific formats
scripts/
  build_records.py            Python 3 metadata normalization/validation script
add_items.py                  Optional CLI helper for generating import JSON
test_records.json             Synthetic sample for testing imports (not history)
README.md                     Project guide
.gitignore                    Local/generated file exclusions
.nojekyll                     GitHub Pages compatibility
```

## Rebuild the index

Python 3 is required; the build script uses the standard library.

```bash
python scripts/build_records.py
```

The pipeline reads `data/sources/*.raw.json` using mappings in `data/sources.json`, normalizes fields into a Dublin Core-based structure, validates records and generates `data/roots-records.js` and `data/roots-records.json`.

To add another source, provide its raw metadata file and mapping, then rerun the script. Validation checks include missing titles, invalid URLs, unsupported access values and duplicates. The source provenance is retained in the resulting index.

For a **synthetic import example**, see `test_records.json`. Do not mistake its test institution or `example.org` URL for a real historical source. `add_items.py` is an optional command-line helper for preparing browser-import JSON.

## Important limitations

- The 46-record dataset is a **manually collected snapshot**, not automated API or OAI-PMH harvesting.
- The application is a **static browser prototype**, without a shared backend or authenticated institutional review workflow.
- Browser-imported records are **not automatically published to other users**. Client-side access labels and hidden previews do **not** enforce security.
- Source links and metadata may become outdated; production use would require link monitoring, refresh schedules and institutional review.
- Historical coverage is limited to the sample records. A missing search result does **not** mean the history does not exist.
- Production priorities include shared storage, permissions and rights review, accessibility testing, automated ingestion, stronger entity matching and French-language support.

**Do not upload private, restricted or sensitive assets to the public dataset.**

## Team Pink Pixels

| Member | Responsibility |
| --- | --- |
| Tinotenda | Product lead, presentation, integration and testing |
| Shanella | Frontend, landing page and UI |
| Benita | Metadata, search and import validation |
| Ale | Explore, timeline, heritage map and recommendations |
| Ashlee | Institutional contributions, research and user experience |

## Development and credits

`main` is the final integrated demo branch. Earlier feature and integration branches document team development. Changes to the demo should be tested before updating `main`.

ROOTS draws product inspiration from interest-based discovery experiences, cultural heritage aggregators and place-based history projects. It is a hackathon proof of concept built with HTML, CSS, JavaScript, Python and AI-assisted coding tools.

**Built by Pink Pixels for RBC HubHacks 2026.**
