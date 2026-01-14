# Marshall Schurtz Portfolio - Multi-Agent Execution Plan

> **Instructions**: Run Agent 0 first, then start Agents 1-4 in parallel. Each agent should check off tasks as completed.

---

## 🚀 AGENT 0: Project Scaffolding (RUN FIRST - BLOCKING)

This must complete before other agents start.

```
/agent-0-scaffolding
```

- [x] Initialize Astro project:
  ```bash
  cd /Users/marshallschurtz/Desktop/MarshallSchurtz_Site
  npm create astro@latest ./ -- --template minimal --typescript strict --install --no-git
  ```
- [x] Add Svelte integration: `npx astro add svelte -y`
- [x] Add Tailwind integration: `npx astro add tailwind -y`
- [x] Install GSAP: `npm install gsap`
- [x] Install Sanity client: `npm install @sanity/client @sanity/image-url`
- [x] Create folder structure:
  - `src/components/global/`
  - `src/components/home/`
  - `src/components/cards/`
  - `src/components/ui/`
  - `src/layouts/`
  - `src/lib/`
  - `src/styles/`
  - `sanity/schemas/`
- [x] Create `src/styles/global.css` with design tokens, fonts, color palette
- [x] Configure `tailwind.config.mjs` with custom theme (colors, fonts)
- [x] Create `src/layouts/BaseLayout.astro` skeleton

---

## 🔶 AGENT 1: Sanity CMS Schemas

```
/agent-1-sanity
```

**No dependencies after Agent 0 completes.**

- [x] Create `sanity/schemas/project.ts` - unified project schema with conditional fields:
  - Base fields: title, slug, projectType, status, images, descriptions, location, date, tags
  - Video fields: youtubeId, duration, infrastructureType
  - Excavation fields: siteName, period, role, institution, seasons
  - Tour fields: tourType, bookingUrl, price, duration
  - Publication fields: publicationType, authors, citation details
- [x] Create `sanity/schemas/fieldNote.ts` - blog post schema
- [x] Create `sanity/schemas/mediaAppearance.ts` - press appearances
- [x] Create `sanity/schemas/siteSettings.ts` - singleton for global settings
- [x] Create `src/lib/sanity.ts` - client configuration and query functions
- [x] Create `src/lib/youtube.ts` - YouTube API integration

---

## 🔷 AGENT 2: Global Components

```
/agent-2-global
```

**No dependencies after Agent 0 completes.**

- [x] Create `src/components/global/Header.astro`:
  - Fixed position, transparent → solid on scroll
  - Left: `MARSHALL SCHURTZ [ARCH_ID: MS_2024]`
  - Right: `01 // WORK  02 // FIELD NOTES  03 // THE METHOD  04 // CONTACT`
  - Mobile hamburger menu
- [x] Create `src/components/global/Footer.astro`:
  - Dark bedrock background (#1A1A1A)
  - Navigation links, social icons
  - "Surface ↑" scroll-to-top button
- [x] Create `src/components/global/DepthGauge.svelte`:
  - Fixed right sidebar showing depth (0m → -50m)
  - Orange indicator tracking scroll position
  - Layer labels: SURFACE, THE TRENCH, LIVE TRANSMISSIONS, BEDROCK
- [x] Create `src/components/global/GridOverlay.svelte`:
  - Surveying grid overlay with ON/OFF toggle
- [x] Create `src/lib/animations.ts`:
  - GSAP ScrollTrigger utilities
  - Background color transition function
  - Section reveal animations

---

## 🟢 AGENT 3: Homepage Components

```
/agent-3-homepage
```

**Depends on**: Agent 0 complete, `BaseLayout.astro` exists

- [x] Create `src/components/home/HeroSection.astro`:
  - Full viewport, grayscale infrastructure background
  - Grid overlay toggle (top right)
  - Headline: "DOCUMENTING THE MODERN WORLD THROUGH AN ARCHAEOLOGICAL LENS."
  - Subheadline + CTA button
  - Topographic texture on lower edge
- [x] Create `src/components/home/FeaturedProject.astro`:
  - "CURRENT EXCAVATION" header
  - Two-column layout with technical diagram + data block
- [x] Create `src/components/home/ProjectGrid.astro`:
  - "THE TRENCH (-25m)" section header
  - Filter tabs: ALL | VIDEO | EXCAVATIONS | TOURS | PUBLICATIONS
  - Responsive grid container
- [x] Create `src/components/home/YouTubeFeed.svelte`:
  - "LIVE TRANSMISSIONS" section
  - Fetches latest 6 videos from YouTube API
  - Grid of VideoCards
- [x] Create `src/components/home/MediaSection.astro`:
  - "IN THE MEDIA" section
  - Grid of MediaCards

---

## 🟣 AGENT 4: Card Components & UI

```
/agent-4-cards
```

**No dependencies after Agent 0 completes.**

- [x] Create `src/components/cards/ProjectCard.astro`:
  - Image with gradient overlay
  - Hover: dim image + metadata overlay (LOC, TYPE, STATUS, FIELD DATE)
  - Orange border on hover
- [x] Create `src/components/cards/VideoCard.astro`:
  - YouTube thumbnail, title, date, duration badge
- [x] Create `src/components/cards/MediaCard.astro`:
  - Outlet logo, headline, date, external link icon
- [x] Create `src/components/ui/Button.astro`:
  - Primary style with arrow, hover animation
- [x] Create `src/components/ui/SectionHeader.astro`:
  - Monospace section headers with depth indicator
- [x] Create `src/components/ui/DataBlock.astro`:
  - Orange monospace data overlay component

---

## 🔴 AGENT 5: Pages & Layouts (Run after Agents 1-4)

```
/agent-5-pages
```

**Depends on**: All components from Agents 1-4 complete

- [x] Create `src/pages/index.astro` - orchestrate all homepage sections
- [x] Create `src/pages/work/index.astro` - work listing with filters
- [x] Create `src/pages/work/[slug].astro` - dynamic project detail
- [x] Create `src/layouts/ProjectLayout.astro` - project detail template
- [x] Create `src/pages/field-notes/index.astro` - blog listing
- [x] Create `src/pages/field-notes/[slug].astro` - blog post detail
- [x] Create `src/layouts/PostLayout.astro` - blog post template
- [x] Create `src/pages/method.astro` - About/CV page
- [x] Create `src/pages/contact.astro` - Contact form page

---

## Execution Summary

| Phase | Agents | Mode | Description |
|-------|--------|------|-------------|
| 1 | Agent 0 | Sequential | Project scaffolding (MUST complete first) |
| 2 | Agents 1-4 | **Parallel** | Components, schemas, utilities |
| 3 | Agent 5 | Sequential | Assemble pages using components |

---


---

## 🔵 PHASE 2: Refinement & Content Integration (Current Focus)

**User Feedback Integration**:
- Tone down "spy/operative" jargon (remove "ARCH_ID", "Live Transmissions", etc.).
- Homepage: Shift from 100% dynamic grid to Static Pillar Sections (YouTube, Tours, Strategy, Academic).
- New Pages: Dynamic Resume, Dissertation (Static), Publications (CMS).

### Agent 6: Design & Tone Refinement
- [ ] **Audit & Copy Updates**:
  - [ ] `Header.astro`: Remove "ARCH_ID", simplify navigation labels.
  - [ ] `HeroSection.astro`: Update text to be less "operative", more "academic/explorer".
  - [ ] `DepthGauge.svelte`: Rename labels (e.g., "The Trench" -> "Archive" or "Projects").
  - [ ] `YouTubeFeed.svelte`: Rename "LIVE TRANSMISSIONS" -> "Latest Videos".
- [ ] **Homepage Restructure**:
  - [ ] Create static sections for "The Pillars": YouTube, Always Sunny, Merakiva, Sweathead.
  - [ ] Reduce "Project Grid" prominence (move to /work or bottom of home).

### Agent 7: New Content Sections
- [ ] **Resume/CV Page**:
  - [ ] Create `src/pages/cv.astro`.
  - [ ] Design print-friendly layout.
  - [ ] Integrate user data (Waiting for input).
- [ ] **Dissertation Section**:
  - [ ] Create `src/pages/dissertation/index.astro` (Overview).
  - [ ] Create `src/pages/dissertation/[chapter].astro` (or individual static pages).
  - [ ] Layout for long-form academic text.
- [ ] **Publications Section**:
  - [ ] Create/Update `publication` schema in Sanity (ensure PDF/Link fields are robust).
  - [ ] Create `src/pages/publications.astro` listing.

