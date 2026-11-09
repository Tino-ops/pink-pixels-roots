
# ROOTS — Black Canadian History Discovery Hub 🌱

**Team:** Pink Pixels  
**Hackathon:** RBC HubHacks 2026  
**Challenge Partner:** Black Cultural Centre for Nova Scotia (BCCNS)

**Every story has roots. Find yours.**

## About ROOTS

ROOTS is a digital discovery platform designed to make Black Canadian history easier to find, explore, and connect with.

Historical resources are often spread across museums, archives, libraries, universities, and community organizations. This can make it difficult for the public to discover important stories, especially when visitors do not know which institution holds the information they need.

ROOTS aims to bring these resources together through a **single, accessible, searchable discovery platform**.

Rather than taking ownership of historical collections, ROOTS connects users to resources held by their original institutions while preserving attribution, provenance, rights information, and source links.

Our goal is to make discovering Black Canadian history **as intuitive as exploring food, music, or places on familiar digital platforms**.

## Our Product Vision

We want ROOTS to feel like a discovery experience, not a complicated archival database.

A visitor shouldn't need to know the exact name of a historical figure, event, document, or institution to begin exploring.

Instead, users should be able to select something they're interested in and discover related historical resources naturally.

**For example:**

A user on Uber Eats might know they're interested in chicken but not know which dish or restaurant they want.

Similarly, a visitor on ROOTS might know they're interested in **Music** but not know exactly what to search for.

ROOTS could guide them toward jazz, gospel, musicians, performances, historical events, and related archival records.

This interest-based approach encourages curiosity and makes historical exploration more approachable.

## What Inspired ROOTS?

Our concept combines four complementary approaches to digital discovery.

### 1. Uber Eats — Discovery Experience

**Inspiration:** Helping users discover options based on their interests.

On Uber Eats, someone interested in chicken can explore different restaurants, dishes, and recommendations without knowing exactly what they want.

**ROOTS Equivalent:** A visitor selects Music and discovers jazz, gospel, artists, performances, and related historical records.

We want users to explore Black Canadian history through familiar interests rather than needing specialized historical knowledge.

### 2. Google Arts & Culture — Visual Exploration

**Inspiration:** Visually engaging collections, thematic browsing, and curated cultural experiences.

**ROOTS Equivalent:** Beautiful discovery pages, historical themes, related records, and engaging pathways that encourage visitors to continue exploring.

Our goal is to make historical discovery visually inviting and enjoyable.

### 3. Europeana — Data Infrastructure

**Inspiration:** Bringing cultural heritage metadata from multiple institutions into one searchable discovery system.

**ROOTS Equivalent:** A unified catalogue that uses standardized metadata to connect historical resources across institutions.

Each record preserves its source institution, attribution, rights information, and original collection link.

ROOTS is intended to complement existing archives, not replace them.

### 4. Historypin — Community Participation

**Inspiration:** Place-based historical exploration and community contributions.

**ROOTS Equivalent:** Smaller cultural organizations can contribute historical metadata, while visitors can explore Black Canadian heritage through locations and community stories.

We want both large institutions and smaller community organizations to have opportunities to make their collections discoverable.

## Our Minimum Viable Product (MVP)

Our MVP prioritizes **ease of use, accessibility, and searchability**.

We want visitors of different ages, backgrounds, and technical abilities to navigate ROOTS without difficulty.

### Core MVP Priorities

**1. Easy to Use**
- Simple, intuitive navigation.
- Clear categories and understandable labels.
- Minimal steps to find historical resources.
- A consistent and responsive interface.

**2. Accessible**
- Readable text and clear visual contrast.
- Mobile-friendly layouts.
- Keyboard-accessible navigation and controls.
- Descriptive labels and accessible form inputs.

**3. Searchable**
- Keyword search across historical records.
- Filtering by topics, institutions, and resource types.
- Relevant search results with clear descriptions.
- Direct links to original historical sources.

**4. Exploration-Based Discovery**
- Browse categories such as Music, People, Communities, and Civil Rights.
- Discover related historical resources.
- Explore historical events through a timeline.
- Discover heritage locations through an interactive map.

**5. Trustworthy Historical Information**
- Clear labelling of what has and has not been checked: every record is marked as institution-supplied metadata until a reviewer confirms it against the original source.
- Clear institutional attribution.
- Original source links.
- Preservation of available rights and access information.

**6. Inclusive Institutional Contributions**
- A simple metadata submission form for smaller organizations.
- A planned CSV import option for larger institutions.
- A shared metadata structure for records from different sources.
- A review process before submitted records become publicly discoverable.

## Key Platform Features

### Search Historical Records

Visitors can search for historical people, places, events, subjects, and resources using everyday language.

### Explore by Interest

Visitors can begin with a broad interest and discover related historical topics and records.

### Interactive Historical Timeline

Users can explore Black Canadian history chronologically through historical events and connected resources, each linked to its source institution.

### Explore Near Me — Heritage Map

Users can discover Black Canadian heritage sites, historical locations, and cultural institutions through an interactive map.

### Historical Record Details

Each record is designed to include:
- Title and description.
- Historical date or period, where available.
- Relevant people, places, and subjects.
- Holding or source institution.
- Resource type.
- Available rights and access information.
- Original source URL.

### Institutional Contributions

ROOTS aims to support two contribution pathways:

**Smaller Institutions:** Manual metadata submission through a straightforward form.

**Larger Institutions:** Bulk metadata imports using standardized CSV files, with potential API-based integration in future development.

Submitted metadata would follow a common structure and be reviewed before publication.

## Data Sources and Proof of Concept

ROOTS indexes metadata from **7 institutions** and links every record back to the holder. No collection is copied.

| Institution | Records | How it was collected |
|---|---|---|
| Nova Scotia Archives | 17 | Public item and collection pages (the pages publish Dublin Core meta tags) |
| Archives of Ontario | 12 | A PDF research guide (finding aid), extracted by hand |
| Library and Archives Canada | 11 | Public genealogy guide and blog pages |
| Canadiana | 3 | Viewer links cited by the LAC guide |
| Black Cultural Centre for Nova Scotia | 1 | Public "Visit Us" page |
| University of Calgary Libraries | 1 | Public digital-collection record |
| The Canadian Encyclopedia | 1 | Public article |

**What is real and what is not.** These 46 records are a **hand-collected snapshot taken on 2026-11-08**, not a live harvest. Descriptions are short summaries written for the index; they are not the institutions' own descriptions. Live harvesting through APIs or OAI-PMH is the next step wherever an institution offers it, and has not been built. Where a source states no date, ROOTS shows "Date not stated"; where a date is uncertain it is marked approximate.

### How the data pipeline works

```
data/sources/<source>.raw.json   each source in its OWN field names
data/sources.json                per-source mapping: source field -> ROOTS (Dublin Core based) field
scripts/build_records.py         maps, parses dates, normalizes resource types, validates, adds provenance
data/roots-records.js            the generated index the app loads (data/roots-records.json is a copy)
```

To add a source, add a raw file and an entry in `data/sources.json`, then run `python3 scripts/build_records.py`. The build fails on a missing title, an invalid source URL, an unknown access value or a duplicate. Every record carries provenance: the source system, how and when it was collected, which source fields were mapped, and which fields a ROOTS curator added (category, people, subjects, access notes). The mapping is shown in the app on the **Data model** page.

## Team Responsibilities

| Team Member | Responsibility |
|---|---|
| Tinotenda | Product Lead, Presentation, Integration & Testing |
| Shanella | Frontend Development, Landing Page & User Interface |
| Benita | Backend Development, Metadata & Search |
| Ale | Explore, Timeline, Heritage Map & Recommendations |
| Ashlee | Institutional Contributions, Research & User Experience |

## Current Project Status

ROOTS is currently in active development for RBC HubHacks 2026.

### Working in the prototype today

- **Search and filters:** free text plus filters for province, institution, people, places, subjects, resource type, access and a year range.
- **Ask ROOTS (grounded search):** plain-language questions answered only from indexed records. Each answer names the holding institution, date and access for every record, shows how the question was interpreted, and says so when nothing matches. It uses no outside knowledge and no language model, so it cannot invent information.
- **Institutions view:** who holds what, the access mix, how each source was collected, and co-holders named by the sources.
- **Record pages:** held by, reference number, access instructions, link to the authoritative record, provenance, and cross-institution connections (shared people, subjects, places).
- **Data model page:** Dublin Core mapping and the per-source field mapping.
- **Timeline and map:** records with a stated year or valid coordinates only.

### Not built yet

Live API or OAI-PMH harvesting, thumbnails (they need permission from each holder), review by the institutions, French-language search, and a server-side API. Browser imports on the Contribute page are stored only in that browser.

## How to Run the Current Prototype

1. Download or clone this GitHub repository.
2. Open `index.html` in a modern web browser.
3. To rebuild the index after editing a source file, run `python3 scripts/build_records.py` (Python 3, no extra packages). The app reads `data/roots-records.js`, so it works offline from a file.
4. On the Search page, expand **Import historical metadata (JSON)** to import a JSON array of records with `title`, `institution`, and `sourceURL`. The importer rejects incomplete or invalid-URL rows and reports skipped duplicates.
5. Imported records can include `accessStatus` (`Public`, `Educational`, `By request`, `Online`, `Available by request`, `On-site only`, or `Unknown`) and `contactEmail`. Restricted record-detail pages hide previews and show an email request link when a contact address is provided.
6. This is a browser-only prototype: imported records are not persisted or verified; access labels and preview hiding are **not server-enforced security**. Do not upload sensitive or restricted assets into the public dataset.

Additional instructions will be provided as new components and backend functionality are integrated.

## GitHub Development Workflow

The team uses separate branches to develop features collaboratively.

| Branch | Responsibility |
|---|---|
| `main` | Stable integrated project |
| `feature/frontend` | Landing page and frontend development |
| `feature/backend-search` | Metadata, backend and search |
| `feature/discovery` | Explore, timeline, map and recommendations |
| `feature/contributions` | Institutional submission and contribution features |

Developers work on their assigned branches and submit pull requests.

Changes are reviewed and tested before being merged into `main`.

## Helper script

`add_items.py` is a dependency-free command-line tool for creating ROOTS-compatible JSON records for the browser import (title, institution, source URL, date, location, type, access status). Import its `item_records.json` output from **Search > Import historical metadata (JSON)**.

## Future Scalability

Beyond the hackathon, ROOTS could expand to support:

- Additional museums, archives, libraries, universities, and community organizations across Canada.
- Institutional metadata imports and authorized API integrations.
- More advanced cross-institution search.
- Expanded historical timelines and geographic discovery.
- Community-led storytelling and contributions.
- Educational discovery experiences.
- Optional personalized recommendations.

Our long-term vision is a scalable national discovery layer for Black Canadian historical resources.

## Our Mission

**ROOTS is not just about storing history. It's about making history easier to find, explore, understand, and connect with.**

By combining intuitive discovery, engaging exploration, standardized metadata, and community participation, we hope to make Black Canadian history more accessible to everyone.

**Every story has roots. Find yours. 🌱**

Developed by **Team Pink Pixels** for **RBC HubHacks 2026**.
