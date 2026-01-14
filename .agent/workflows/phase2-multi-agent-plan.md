---
description: Phase 2 Multi-Agent Execution Plan for Marshall Schurtz Portfolio
---

# Phase 2: Multi-Agent Execution Plan

> **Last Updated:** 2026-01-13  
> **Status:** 🟡 Planning Complete - Ready for Execution  
> **Platform:** Google Antigravity (parallel agent conversations)

---

## 🚀 How to Launch Agents (READ THIS FIRST)

### Universal Prompt — Copy/Paste This for Each Agent

```
I'm working on Phase 2 of marshallschurtz.com. You are Agent [NUMBER].

Read the full plan here: @[.agent/workflows/phase2-multi-agent-plan.md]

Find your agent section (Agent [NUMBER]), complete your tasks, and prompt me 
for any data or decisions you need. Update the checklist as you go.

Context: This is an Astro site with Svelte, Tailwind, GSAP, and Sanity CMS.
The site is at /Users/marshallschurtz/Desktop/MarshallSchurtz_Site

### 📂 Shared Assets Folder
**Path:** `/Users/marshallschurtz/Desktop/MarshallSchurtz_Site/project_assets/`

All user-provided documents (CV, dissertation, etc.), images, and answers to prompts should be usually placed here.
*   **Do not** put raw assets directly into `public` unless they are final.
*   **Do not** delete files from here after using them; keep them as a source of truth.
*   Look here first for any "missing" data or files mentioned in prompts.
```

### Launch Order

| Phase | Agents | When to Start |
|-------|--------|---------------|
| **Now** | 6, 7, 10 | No dependencies — start immediately |
| **When data arrives** | 8, 9, 11 | After Marshall provides CV/dissertation/bios |
| **Last** | 12 | After all others complete |

### How It Works

1. **Start a new conversation** in Antigravity
2. **Paste the universal prompt** above, replacing `[NUMBER]` with the agent number
3. **The agent reads this doc** and finds its section
4. **The agent will prompt you** for any data/documents it needs
5. **Update this doc** as agents complete (paste conversation IDs, check boxes)

---

## Quick Reference

| Agent | Task | Dependencies | Status | Conversation ID |
|-------|------|--------------|--------|-----------------|
| Agent 6 | Style & Copy Refinement | None | ✅ Complete | _done_ |
| **Agent 6B** | Copy Refinements (Post-Review) | Agent 6 | ✅ Complete | _done_ |
| Agent 7 | Homepage Restructure | None | ✅ Complete | _done_ |
| **Agent 7B** | Homepage Content Improvements | Agent 7 | ✅ Complete | _done_ |
| Agent 8 | Resume/CV Page | Data Collection | ✅ Complete | 8 |
| Agent 9 | Dissertation Section | Data Collection | ✅ Complete | 9 |
| Agent 10 | Publications Section | Agent 1 Schema | ⬜ Not Started | _paste ID here_ |
| Agent 11 | New Site Sections | Data Collection | ⬜ Waiting on Data | _paste ID here_ |
| Agent 12 | Final QA & Polish | All Above | ⬜ Blocked | _paste ID here_ |

**Status Legend:** ⬜ Not Started | 🟡 In Progress | ✅ Complete | ⚠️ Blocked | ⏸️ Waiting on Data

---

## Execution Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PHASE 2A: PARALLEL WORK                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐   │
│   │  AGENT 6         │     │  AGENT 7         │     │  AGENT 10        │   │
│   │  Style Cleanup   │     │  Homepage Rebuild│     │  Publications    │   │
│   │  (No deps)       │     │  (No deps)       │     │  Schema + Page   │   │
│   └────────┬─────────┘     └────────┬─────────┘     └────────┬─────────┘   │
│            │                        │                        │              │
└────────────┼────────────────────────┼────────────────────────┼──────────────┘
             │                        │                        │
             ▼                        ▼                        ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      PHASE 2B: DATA-DEPENDENT WORK                          │
├─────────────────────────────────────────────────────────────────────────────┤
│  (Start these once Marshall provides the required data)                     │
│                                                                              │
│   ┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐   │
│   │  AGENT 8         │     │  AGENT 9         │     │  AGENT 11        │   │
│   │  Resume/CV       │     │  Dissertation    │     │  New Sections    │   │
│   │  (Needs CV data) │     │  (Needs doc)     │     │  (Needs bios)    │   │
│   └────────┬─────────┘     └────────┬─────────┘     └────────┬─────────┘   │
│            │                        │                        │              │
└────────────┼────────────────────────┼────────────────────────┼──────────────┘
             │                        │                        │
             └────────────────────────┼────────────────────────┘
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          PHASE 2C: FINAL QA                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                           ┌──────────────────┐                              │
│                           │  AGENT 12        │                              │
│                           │  QA & Polish     │                              │
│                           │  (All complete)  │                              │
│                           └──────────────────┘                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Agent Assignments

### ✅ Agent 6: Style & Copy Refinement

**Status: COMPLETE (with refinements needed)**

**Objective:** Remove "spy/operative" language, keep archaeological aesthetic

**Files modified:**
- `src/components/global/Header.astro` — Remove "ARCH_ID", simplify nav labels
- `src/components/global/DepthGauge.svelte` — Rename layer labels
- `src/components/home/HeroSection.astro` — Soften language
- `src/components/home/FeaturedProject.astro` — "CURRENT EXCAVATION" → "Featured Project"
- `src/components/home/YouTubeFeed.svelte` — "LIVE TRANSMISSIONS" → "Latest Videos"
- `src/components/home/ProjectGrid.astro` — Remove depth labels from headers

**Completed checklist:**
- [x] Audit all component copy
- [x] Update `Header.astro`
- [x] Update `DepthGauge.svelte`
- [x] Update `HeroSection.astro`
- [x] Update `FeaturedProject.astro`
- [x] Update `YouTubeFeed.svelte`
- [x] Update `ProjectGrid.astro`
- [x] Verify site still renders correctly

> [!WARNING]
> **User Feedback — Refinements Required (see Agent 6B below)**

---

### ⬜ Agent 6B: Copy Refinements (Post-Review)

**Can run immediately - no dependencies**

**Objective:** Address specific copy/functionality issues flagged by Marshall

> [!TIP]
> **Placeholder Approach:** Use compelling placeholder copy now. Real specific content will be swapped in by later agents (8, 9, 11) when Marshall provides documents and assets.

**Issues to fix:**

1. **Header tagline** — Change main hero text to: **"EXPLORING THE WORLD BY UNDERSTANDING ITS PAST"**
   - File: `src/components/home/HeroSection.astro`

2. **YouTube feed — exclude Shorts**
   - File: `src/components/home/YouTubeFeed.svelte` and/or `src/lib/youtube.ts`
   - Filter out videos with `#Shorts` in title OR videos under 60 seconds
   - Add "See the channel →" link at bottom of section linking to YouTube channel

3. **Contact page outdated language**
   - File: `src/pages/contact.astro`
   - Audit and update copy to match refined tone
   - Use professional but approachable placeholder text

**Checklist:**
- [x] Update HeroSection.astro tagline to "EXPLORING THE WORLD BY UNDERSTANDING ITS PAST"
- [x] Filter Shorts from YouTube feed (by title or duration)
- [x] Add "See the channel →" link to YouTubeFeed.svelte
- [x] Audit and fix Contact page copy
- [x] Test YouTube feed still works after changes

---

### ✅ Agent 7: Homepage Restructure

**Status: COMPLETE (with refinements needed)**

**Objective:** Add static "What I Do" pillar sections to homepage

**Files created/modified:**
- `src/components/home/WhatIDo.astro` — New static section with 5 cards
- `src/pages/index.astro` — Integrated new section

**Completed checklist:**
- [x] Create `src/components/home/WhatIDo.astro`
- [x] Design card component for each pillar
- [x] Update `src/pages/index.astro` section order
- [x] Ensure responsive layout
- [x] Add hover animations consistent with existing cards

> [!WARNING]
> **User Feedback — Refinements Required (see Agent 7B below)**

---

### ✅ Agent 7B: Homepage Content Improvements (Post-Review)

**Status: COMPLETE**

**Objective:** Make "What I Do" section more engaging; rethink Featured Project

> [!TIP]
> **Placeholder Approach:** Write compelling placeholder copy for all cards and sections now. Use engaging language that captures the spirit of each area. Real specific details (testimonials, metrics, case studies) will be swapped in by later agents when Marshall provides data.

**Issues to fix:**

1. **"What I Do" cards need more than a sentence and a link**
   - File: `src/components/home/WhatIDo.astro`
   - Each card should have 2-3 sentences of engaging placeholder copy:
     - **YouTube/Content:** Describe the archaeological storytelling angle
     - **Always Sunny Tour:** Capture the fun, unique experience
     - **Merakiva Travel:** Archaeological tourism appeal
     - **Academic Work:** Scholarly expertise and fieldwork
     - **Strategy & Analytics:** Analytical/consulting capabilities
   - Use placeholder images (generate or use stock) — real photos added later

2. **Featured Project → rename to "Current Focus"**
   - File: `src/components/home/FeaturedProject.astro`
   - Rename section header to "Current Focus" or "What I'm Working On"
   - Use placeholder content about building the YouTube channel / content creation
   - Structure it to be easily updated via CMS later

3. **Placeholder for visual assets**
   - Use generated/stock images for now
   - Add clear `<!-- TODO: Replace with real photo -->` comments
   - Later agents will swap in real assets when provided

**Checklist:**
- [x] Rewrite all 5 "What I Do" card descriptions with engaging placeholder copy
- [x] Rename Featured Project to "Current Focus"
- [x] Update FeaturedProject content with placeholder about current work
- [x] Add placeholder images where needed with TODO comments
- [x] Ensure homepage flows coherently even with placeholders

---

### ⬜ Agent 8: Resume/CV Page

**Blocked until Marshall provides CV data**

**Objective:** Create dynamic, visually distinctive resume page

**Create:**
- `src/pages/resume.astro` or `src/pages/cv.astro`
- `src/components/resume/` — Component folder for resume sections

**Design Requirements:**
- Visually distinctive, not a plain text CV
- Each section as expandable cards
- Timeline or visual career progression
- Skills displayed visually (bars, tags, etc.)
- Downloadable PDF option
- Print-friendly CSS

**Sections to include:**
1. Education (with honors, dissertation title)
2. Professional Experience (with company logos)
3. Fieldwork / Excavations
4. Publications (link to full publications page)
5. Teaching / Speaking
6. Awards / Grants / Fellowships
7. Skills (technical, languages, methodologies)
8. Professional Memberships

**Will Prompt You For:**
- Resume/CV document (PDF, Word, or LinkedIn export)
- Any additional fieldwork or excavation details
- Whether you want a downloadable PDF generated

**Checklist:**
- [ ] ⏸️ Waiting for CV data from Marshall
- [x] Create page structure
- [x] Build section components
- [x] Implement expand/collapse interactions
- [x] Add timeline visualization
- [x] Style for print
- [ ] Add PDF download button (Future Phase)

---

### ⬜ Agent 9: Dissertation Section

**Blocked until Marshall provides dissertation document**

**Objective:** Create dissertation landing page + chapter pages

**Create:**
- `src/pages/academic/dissertation/index.astro` — Landing page
- `src/pages/academic/dissertation/[chapter].astro` — Dynamic chapter pages
- `src/layouts/DissertationLayout.astro` — Long-form reading layout

**Landing Page Content:**
- Title, abstract, committee members
- Chapter navigation
- Full PDF download link
- "Cite this" section with proper citation format

**Chapter Pages:**
- Clean reading layout
- Proper heading hierarchy
- Figures with captions
- Chapter navigation (prev/next)
- Progress indicator

**Will Prompt You For:**
- Dissertation document (Word preferred, PDF works)
- Committee member names and titles
- Any figures that should be excluded from public site
- Whether to link Airtable research database (can be Phase 3)

**Checklist:**
- [x] ⏸️ Data received - files located in project_assets
- [x] Parse dissertation structure (7 chapters identified)
- [x] Create landing page with abstract
- [x] Build chapter page template (DissertationLayout.astro)
- [x] Create reading-optimized layout
- [x] Add chapter navigation (prev/next)
- [x] Add "Cite this" section
- [x] Link to PDF download
- [x] Add "ACADEMIC" to main navigation
- [x] Extract full chapter content from Word document (111,080 words extracted)
- [x] Integrate extracted content into Astro chapter pages
- [x] Fix Tailwind v4 compatibility issues in layout

---

### ⬜ Agent 10: Publications Section

**Can run immediately - builds on existing Sanity schema**

**Objective:** Create publications listing page with CMS integration

**Modify/Create:**
- Verify `sanity/schemas/project.ts` has publication type with PDF fields
- `src/pages/academic/publications.astro` — Listing page
- `src/pages/academic/publications/[slug].astro` — Individual publication page

**Features:**
- Each publication has its own page
- PDF embedded inline AND downloadable
- Proper citation displayed prominently
- DOI/journal links
- Filter by publication type

**Will Prompt You For:** Nothing — this sets up the structure. Content added via Sanity CMS later.

**Checklist:**
- [ ] Verify/update Sanity publication schema
- [ ] Create `src/pages/academic/publications.astro`
- [ ] Create `src/pages/academic/publications/[slug].astro`
- [ ] Implement PDF embed + download
- [ ] Add citation display
- [ ] Add filter by publication type

---

### ⬜ Agent 11: New Site Sections

**Blocked until Marshall provides content**

**Objective:** Build new static content sections

**Create:**
- `src/pages/always-sunny-tour.astro`
- `src/pages/merakiva.astro`
- `src/pages/academic/index.astro` — Academic overview
- `src/pages/academic/excavations.astro`
- Update `src/pages/about.astro` with full bio

**Content needed from Marshall (see Phase 2 Implementation Plan sections 3.6-3.8):**
- Always Sunny Tour details + photos
- Merakiva Travel service descriptions
- Bio versions (one-liner, short, full)
- Philosophy/approach statement
- Excavation details from CV

**Will Prompt You For:**
- Always Sunny Tour: description, press highlights, testimonials, photos
- Merakiva Travel: services, target clients, example trips, approach
- Bio: one-liner, short (100 words), full (300-500 words)
- Philosophy/approach statement
- Social links confirmation

**Checklist:**
- [ ] ⏸️ Waiting for content from Marshall
- [ ] Create Always Sunny Tour page
- [ ] Create Merakiva Travel page
- [ ] Create Academic overview page
- [ ] Create Excavations page
- [ ] Update About page with full bio
- [ ] Ensure consistent navigation

---

### ⬜ Agent 12: Final QA & Polish

**Blocked until all above agents complete**

**Objective:** Comprehensive QA and final polish

**Checklist:**
- [ ] All internal links working
- [ ] All images loading
- [ ] Mobile responsive check (all breakpoints)
- [ ] Copy proofread (no remaining kitschy language)
- [ ] CMS items displaying correctly
- [ ] YouTube feed working
- [ ] Contact form working
- [ ] Lighthouse score > 90 (performance, accessibility, SEO)
- [ ] Cross-browser testing (Chrome, Safari, Firefox)
- [ ] Meta tags and OG images correct
- [ ] Favicon displaying

**Will Prompt You For:** Nothing — this agent tests what other agents built.

---

## Data Collection Status

Track which data has been received from Marshall:

| Data Type | Status | Notes |
|-----------|--------|-------|
| Resume/CV Page | ✅ Received | Found in project_assets |
| Dissertation | ⬜ Not Received | **Required for Agent 9** |
| Publications List | ⬜ Not Received | |
| Media Appearances | ⬜ Not Received | |
| Portfolio Examples | ⬜ Not Received | |
| Always Sunny Tour Details | ⬜ Not Received | |
| Merakiva Details | ⬜ Not Received | |
| Bios (short/long) | ⬜ Not Received | |
| Social Links | ⬜ Not Received | |
| Visual Assets | ⚠️ **NEEDED** | Headshots, fieldwork photos, travel photos |

---

## Notes & Communication Log

_Use this section to track cross-agent coordination and important decisions._

| Date | Agent | Note |
|------|-------|------|
| 2026-01-13 | Setup | Initial plan created |
| 2026-01-13 | 6, 7 | Completed basic implementation |
| 2026-01-13 | Review | User identified 8 issues: YouTube shorts, header copy, What I Do engagement, Featured Project clarity, visual assets, contact page, overall explanation |
| | | Created Agent 6B and 7B to address refinements |

---

## How to Use This Document

1. **Start a new Antigravity conversation** for each agent
2. **Paste the agent's prompt** from the relevant section above
3. **Attach any required documents** mentioned in the prompt
4. **Update the "Conversation ID" column** in the Quick Reference table
5. **Update status** as agents complete their work
6. **Check off items** in each agent's checklist as they complete

**Parallel Execution Guide:**
- Start Agents 6, 7, and 10 immediately (no dependencies)
- Start Agents 8, 9, and 11 once Marshall provides required data
- Start Agent 12 only after all others complete
