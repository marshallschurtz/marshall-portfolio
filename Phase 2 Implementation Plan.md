# marshallschurtz.com — Phase 2 Development Plan & Data Collection Guide

**Document Purpose:** This is a handoff document for an AI agent to execute Phase 2 of marshallschurtz.com development. It includes context, objectives, style guidelines, and structured prompts to collect required information from the client (Marshall Schurtz).

**Client:** Marshall Schurtz
**Site:** marshallschurtz.com
**Status:** Phase 1 complete (basic structure deployed). Phase 2 addresses style refinements and content population.

---

## Part 1: Context & Background

### 1.1 Who is Marshall Schurtz?

Marshall Schurtz is a Philadelphia-based archaeologist, content creator, and entrepreneur with the following professional identities:

**Academic Credentials:**
- PhD in Mesopotamian Archaeology, University of Pennsylvania (2022)
- Fieldwork/excavation experience at multiple archaeological sites
- Published academic work including dissertation and articles

**Current Ventures:**
- **YouTube Channel (Marshall Schurtz):** Archaeology & travel content. This is his primary long-term career focus — becoming a recognized public archaeologist through accessible content. While also connecting to his company, Merkaiva Travel.
- **Always Sunny Tour:** Walking tour business in Philadelphia based on the TV show "It's Always Sunny in Philadelphia." Has received press coverage including Philadelphia Inquirer.
- **Merakiva Travel:** Archaeological tourism business. Includes travel agent work as well as group trips with an archaeological focus.
- **Sweathead:** Current contract work in strategy/analytics for income while building content career. Highlighting the work he does her

**Core Positioning:** "Exploring the world while understanding its past" - the tagline of the youtube channel but also the central positioning of all of his work.

### 1.2 Site Purpose

marshallschurtz.com is a personal portfolio site that:
1. Synthesizes all of Marshall's professional identities into one cohesive presence
2. Serves as a hub for media, potential collaborators, clients, and audiences
3. Showcases that Marshall is DYNAMIC — not just an archaeologist, but a creator, guide, analyst, and communicator
4. Is visually distinctive with a "stratigraphic" design metaphor (scrolling = excavating deeper)

### 1.3 Current State (Phase 1 Complete)

A basic site structure has been deployed using:
- **Framework:** Astro
- **Styling:** Tailwind CSS
- **Animations:** GSAP + ScrollTrigger
- **CMS:** Sanity.io
- **Hosting:** Vercel

**Issues identified:**
1. Language/copy leans too heavily into "tech/spy/military" aesthetic — feels kitschy
2. Too much relies on CMS — site should be 75% static content about Marshall
3. Missing key sections: full resume, dissertation, publications, comprehensive "what I do" overview
4. Homepage doesn't adequately cover all of Marshall's work areas

---

## Part 2: Phase 2 Objectives

### Objective A: Style & Language Refinement

**Problem:** The visual design is good, but the copywriting went too far into performative "field operative" language that feels like costume rather than identity.

**Goal:** Keep the visual metaphor (depth gauge, grid lines, orange accents, monospace data). Remove the verbal over-performance of it.

**Specific Changes Required:**

| Current (Remove/Revise) | Replacement |
|------------------------|-------------|
| "FIELD OPERATIVE: Marshall Schurtz" | "Marshall Schurtz" or just remove subtitle |
| **Hero tagline** | **"EXPLORING THE WORLD BY UNDERSTANDING ITS PAST"** |
| "CURRENT EXCAVATION:" | "Featured Project" or "Current Project" |
| "[DATA_BLOCK // MONOSPACE]" | Remove label entirely, just show data |
| "LOC:" / "TYPE:" | "Location" / "Type" (spell out) |
| "LIVE TRANSMISSIONS" | "Latest Videos" or "Recent Work" |
| "THE TRENCH (-10m)" | Remove depth labels from section headers (keep visual depth gauge only) |
| "VIEW LATEST SURVEY" | "View Project" |
| "[ARCH_ID: MS_2024]" | Remove entirely |
| "SECTOR" or military-style labels | Remove |

**What to Keep:**
- "Field Notes" for blog section (this is natural for an archaeologist)
- Visual depth gauge on right side
- Grid overlay aesthetic
- Orange (#FF4F00) accent color
- Monospace font for metadata (just don't over-label it)
- The stratigraphic scroll concept (background color transition)

**Design Principle:** The site should feel like it was designed by an archaeologist with sophisticated taste, not like it's performing "archaeology" in an on-the-nose way. Think, advanced design studio, not archaeology cosplay.

> [!IMPORTANT]
> **Contact page** also has outdated/kitschy language that needs to be updated to match the refined tone.

---

### Objective B: Content Structure Revision

**Problem:** Site is too CMS-dependent. Should be 75% static content about Marshall with CMS only for incremental additions (new blog posts, new projects to highlight).

**Revised Site Architecture:**

```
HOME (/)
├── Hero (STATIC)
│   └── **"EXPLORING THE WORLD BY UNDERSTANDING ITS PAST"**, name, CTA
├── What I Do (STATIC)
│   └── 5 cards linking to main areas:
│       • Content Creation / YouTube
│       • Always Sunny Tour
│       • Merakiva Travel  
│       • Academic Work
│       • Strategy & Analytics
│   └── **Each card must have engaging copy (2-3 sentences, not just a link)**
├── Featured Project (CMS - **NEEDS RETHINKING - see note below**)
├── Latest Videos (API - YouTube feed, auto-updating, **NO SHORTS**)
│   └── Add "See the channel →" link
├── In The Media (CMS - press mentions)
└── About Preview + CTA (STATIC)

WORK (/work)
├── Static intro/overview
├── Filterable project grid (CMS)
└── Individual project pages (CMS)

ALWAYS SUNNY TOUR (/always-sunny-tour)
├── About the tour (STATIC)
├── Press highlights (CMS)
└── Book CTA → alwayssunnytour.com

MERAKIVA TRAVEL (/merakiva)
├── Services overview (STATIC)
├── Past trips/testimonials (STATIC or CMS)
└── Contact CTA

ACADEMIC (/academic)
├── Overview (STATIC)
├── DISSERTATION (/academic/dissertation)
│   ├── Landing page with abstract (STATIC)
│   └── Individual chapter pages (STATIC - built from provided doc)
├── PUBLICATIONS (/academic/publications)
│   ├── Listing page (CMS for adding new)
│   └── Individual publication pages
│       • PDF attached but text OCR'd for indexing
├── EXCAVATIONS (/academic/excavations)
│   └── Fieldwork listing with details (STATIC)

RESUME (/resume)
├── Dynamic, well-designed CV page (STATIC - built from provided data)
├── Sections: Education, Experience, Skills, Fieldwork, Publications, etc.
└── Downloadable PDF option

FIELD NOTES (/field-notes)
├── Blog listing (CMS)
└── Individual posts (CMS)

ABOUT (/about)
├── Full bio (STATIC)
├── Philosophy/approach (STATIC)
└── Current work mention (STATIC)

CONTACT (/contact)
├── Contact form
├── Social links
├── Booking links
└── **IMPORTANT: Update all copy to match refined tone (remove kitschy language)**
```

> [!WARNING]
> **Featured Project Section** - Current implementation "doesn't make sense." Needs rethinking:
> - What IS a "featured project" for Marshall? A YouTube series? A current focus area?
> - Options: Rename to "Current Focus" / "What I'm Working On", make it highlight a video series, replace with narrative "My Story" section, or remove if redundant
> - **Decision needed from Marshall**

> [!IMPORTANT]
> **Work vs. Resume Clarification:**
> - `/work` = Portfolio of projects (content, tours, consulting work)
> - `/resume` = Formal CV page (education, experience, skills, fieldwork)
> - These are SEPARATE pages serving different purposes

---

## Part 3: Data Collection Prompts

**Instructions for Agent:** Use the following prompts to collect information from Marshall. Each section includes the prompt to ask, the format needed, and how the data will be used.

> [!TIP]
> **Where to find/place files:**
> The user has created a dedicated folder for all raw assets, documents, and answer sheets:
> **`/Users/marshallschurtz/Desktop/MarshallSchurtz_Site/project_assets/`**
>
> *   **Agents:** Check this folder for any files the user says they have provided (CVs, images, markdown answers).
> *   **User:** Drop all huge collections of files, raw high-res images, and markdown answers to prompts here.
> *   **Process:** Copy files from here to `src/assets` or `public` only when actively implementing them. Keep the originals in `project_assets`.

---

### 3.1 Resume / CV Data

**Prompt to Ask Marshall:**

> I need to build your dynamic resume page. Please provide your complete CV/resume information. You can share this in any format — a Word doc, PDF, LinkedIn export, or just paste text. I need:
>
> **Education**
> - Each degree: Institution, degree type, field of study, year completed
> - Dissertation/thesis title if applicable
> - Any honors or distinctions
>
> **Professional Experience**
> For each position:
> - Job title
> - Company/organization name
> - Company website URL (if available)
> - Location
> - Date range (month/year to month/year)
> - 2-4 bullet points describing what you did
> - Any notable achievements or metrics
>
> **Skills**
> - Technical skills (software, tools, programming)
> - Languages (spoken/written, proficiency level)
> - Research methodologies
> - Other relevant skills
>
> **Fieldwork / Excavation Experience**
> For each excavation:
> - Site name
> - Location (country, region)
> - Your role (e.g., Field Director, Surveyor, Student)
> - Sponsoring institution
> - Years/seasons participated
> - Brief description of the project
>
> **Teaching / Speaking / Workshops**
> - Any courses taught
> - Guest lectures
> - Conference presentations
> - Workshops led
>
> **Awards / Grants / Fellowships**
> - Name of award/grant
> - Granting institution
> - Year
> - Brief description if needed
>
> **Professional Memberships**
> - Organizations you belong to
>
> Please include everything — I'll help organize and design it. The more complete, the better the resume page will be.

**Format Needed:** Any format. Agent should parse and structure into JSON or markdown.

**Usage:** Build the /resume page with dynamic, well-designed sections. Also populates parts of /academic/excavations.

---

### 3.2 Dissertation Content

**Prompt to Ask Marshall:**

> I need your full dissertation to create dedicated pages on the site. Each chapter will become its own page, making the content fully indexable by search engines (unlike a PDF).
>
> Please provide:
>
> 1. **The full dissertation document** (Word doc preferred, PDF acceptable)
>
> 2. **Basic metadata:**
>    - Full title
>    - Date completed
>    - Institution
>    - Committee members (names and titles)
>    - Abstract (or I can extract from the doc)
>
> 3. **Chapter breakdown** (if not obvious from the document):
>    - Chapter titles
>    - Any that should be combined or separated differently for web display
>
> 4. **Images/figures:**
>    - Are the images embedded in the doc, or do you have separate high-res files?
>    - Any images that should NOT be included on the public site?
>
> 5. **Related data:**
>    - You mentioned an Airtable database with research data — is this something you want linked/embedded eventually? (Can be Phase 3)
>
> Once I have the document, I'll:
> - Create a dissertation landing page with abstract and navigation
> - Break each chapter into its own page
> - Ensure all text is indexable
> - Properly format figures and citations
> - Link to the full PDF download as an option

**Format Needed:** Word document (.docx) or PDF. Separate image files if available.

**Usage:** Build /academic/dissertation landing page and /academic/dissertation/[chapter-slug] pages.

---

### 3.3 Publications List

**Prompt to Ask Marshall:**

> I need a complete list of your publications to build the publications section. For each publication, please provide:
>
> **For Journal Articles:**
> - Authors (full names, in order)
> - Article title
> - Journal name
> - Year
> - Volume and issue number
> - Page numbers
> - DOI or URL (if available)
> - Abstract (optional but helpful)
> - PDF file (if you can share — I'll OCR for indexing)
>
> **For Book Chapters:**
> - Authors
> - Chapter title
> - Book title
> - Editor(s)
> - Publisher
> - Year
> - Page numbers
> - ISBN or DOI
> - PDF if available
>
> **For Reports / Other:**
> - Full citation in whatever standard format you use
> - PDF if available
> - Public URL if available
>
> **For the Dissertation:**
> - I'll create a separate entry linking to the dissertation pages
>
> If you have a CV or document that already lists these, just share that and I'll extract the information.

**Format Needed:** List, CV section, or bibliography. Any citation format acceptable.

**Usage:** Build /academic/publications page. PDFs will be attached but also OCR'd so text content is searchable.

---

### 3.4 Media Appearances / Press

**Prompt to Ask Marshall:**

> For the "In The Media" section, I need details on press coverage you've received. This includes articles written about you, podcast appearances, TV/radio segments, etc.
>
> For each appearance:
> - Outlet name (e.g., "Philadelphia Inquirer")
> - Title of article/segment
> - Date published
> - URL (full link to the piece)
> - Type: Article, Podcast, TV, Radio, Other
> - A pull quote or brief description (optional — one sentence about what it covers)
> - Image/screenshot (optional)
>
> I know you mentioned the Philadelphia Inquirer article about Always Sunny Tour — please include that and any others you can think of.

**Format Needed:** List with URLs.

**Usage:** Build "In The Media" section on homepage and potentially a dedicated press page.

---

### 3.5 Portfolio / Consulting Examples

**Prompt to Ask Marshall:**

> For the Strategy & Analytics section (your Sweathead-type work), I'd like to showcase examples of consulting or analytical work you've done.
>
> For each example you can share:
> - Client name (can be anonymized like "Major CPG Brand" if needed)
> - Project type (e.g., "Brand Strategy," "Analytics Dashboard," "Market Research")
> - Your role
> - Brief description of the challenge/project
> - What you delivered
> - Results or outcomes (metrics if available)
> - Any visuals you can share (screenshots, sanitized reports)
> - Testimonial quote from client (if available)
>
> If you're not sure what to include or some work is confidential, let me know what you CAN share and I'll help frame it appropriately.
>
> Even 2-3 examples would help demonstrate this side of your work.

**Format Needed:** Descriptions, optional images/screenshots.

**Usage:** Build out the Strategy & Analytics section and/or consulting portfolio items.

---

### 3.6 Always Sunny Tour Details

**Prompt to Ask Marshall:**

> For the Always Sunny Tour section of your personal site, I need:
>
> 1. **Brief description** of the tour (2-3 sentences for the overview card on homepage)
>
> 2. **Longer description** for the dedicated section (1-2 paragraphs about what makes it unique, your connection to it, etc.)
>
> 3. **Key details:**
>    - Tour duration
>    - Price (or "see booking site for current pricing")
>    - How often you run it
>
> 4. **Press mentions** to highlight (URLs)
>
> 5. **Testimonial quotes** from customers (if you have favorites)
>
> 6. **Photos** from tours (if you have good ones that aren't on the main tour site)
>
> 7. **Booking link:** alwayssunnytour.com — confirm this is correct
>
> This section will be brief on your personal site since the tour has its own dedicated site — mainly positioning it within your broader story and linking out.

**Format Needed:** Text descriptions, URLs, optional images.

**Usage:** Build /always-sunny-tour section.

---

### 3.7 Merakiva Travel Details

**Prompt to Ask Marshall:**

> For the Merakiva Travel section, I need:
>
> 1. **Service description:** What do you offer? (archaeological tourism consulting, custom trip planning, etc.)
>
> 2. **Target clients:** Who is this for?
>
> 3. **Example trips or projects** you've planned (anonymized if needed)
>
> 4. **Your approach:** What makes your travel planning different/archaeological?
>
> 5. **Testimonials** if available
>
> 6. **Contact/booking process:** How do people engage you?
>
> 7. **Link:** merakivatravel.com — confirm this is correct

**Format Needed:** Text descriptions.

**Usage:** Build /merakiva section.

---

### 3.8 Bio & Philosophy

**Prompt to Ask Marshall:**

> I need a few versions of your bio and your perspective on your work:
>
> 1. **One-liner:** A single sentence that captures who you are (for meta descriptions, social sharing)
>
> 2. **Short bio (100 words):** For homepage preview, social profiles
>
> 3. **Full bio (300-500 words):** For the About page. Your background, how you got here, what drives you.
>
> 4. **Philosophy / Approach statement:** Why do you do what you do? What's your perspective on public archaeology, infrastructure, content creation? This can be informal — just your thoughts on your work and why it matters.
>
> 5. **Current focus:** What are you working on right now? What's exciting to you?
>
> If you have existing bio text (from your current sites, LinkedIn, etc.), share those and I can help refine/expand.

**Format Needed:** Text.

**Usage:** Homepage hero, /about page, meta descriptions.

---

### 3.9 Social Links & Contact Information

**Prompt to Ask Marshall:**

> Please confirm all your social/professional links:
>
> - YouTube channel URL
> - Instagram URL
> - Bluesky URL
> - LinkedIn URL
> - Twitter/X (if active)
> - Any other platforms
>
> - Contact email (for the contact form to send to)
> - Always Sunny Tour booking URL
> - Merakiva Travel URL or contact method
>
> - Any links that should NOT be included?

**Format Needed:** List of URLs.

**Usage:** Header, footer, contact page, social sharing.

---

### 3.10 Visual Assets

**Prompt to Ask Marshall:**

> I need visual assets to make the site feel personal and engaging. **This is critical — the site currently doesn't have enough photos of you.**
>
> Please provide:
>
> **Required (High Priority):**
> - Professional headshot (highest resolution available)
> - 3-5 photos from excavations/fieldwork (you in action)
> - At least 1 photo from content creation/filming
> - Hero/background image for homepage (or describe what you'd like)
>
> **Helpful if available:**
> - Photos from Always Sunny Tours (you giving the tour)
> - Photos from travels (Merakiva-related destinations)
> - Behind-the-scenes content creation photos
> - Any existing brand assets (logos, etc.)
>
> **For projects:**
> - At least one strong image per project you want featured
>
> For the hero image, the current mockups show infrastructure imagery (dams, trains). Do you want:
> a) A specific infrastructure image
> b) An archaeological site image
> c) A photo of you in the field
> d) Something else
>
> All images should be high resolution (at least 1600px wide for full-width images, 800px for thumbnails).
>
> **Note:** Visual assets will be integrated throughout:
> - Hero section (you or your work)
> - What I Do cards (contextual imagery for each pillar)
> - About section (headshot + fieldwork)
> - Individual project pages

**Format Needed:** Image files (JPG, PNG). Highest resolution available.

**Usage:** Throughout site.

---

## Part 4: Technical Implementation Notes

### 4.1 For the Resume Page

The resume page should be:
- Visually distinctive, not a plain text CV
- Organized by clear sections with the site's design language
- Each job/position as a "card" with expand/collapse for details
- Company logos where available (agent can source from company websites)
- Timeline or visual representation of career progression
- Downloadable PDF version (can be auto-generated or separate upload)
- Skills displayed visually (not just a list)

### 4.2 For the Dissertation Pages

- Landing page: Title, abstract, committee, link to full PDF download
- Chapter navigation: Sidebar or bottom navigation between chapters
- Each chapter: Clean reading layout, properly formatted headings, figures with captions
- Make sure all text is actual HTML text (not images of text)
- Include a "Cite this" section with proper citation format

### 4.3 For Publications

- Each publication should have its own page if PDF is provided
- PDF displayed inline (embedded viewer) AND available for download
- Text extracted from PDF via OCR and included as hidden/visible text for SEO
- Proper citation displayed prominently
- Link to journal/publisher site if available

### 4.4 YouTube Integration

- Already implemented via YouTube Data API v3
- Pulls latest 6 videos automatically
- **IMPORTANT: Filter out YouTube Shorts**
  - Exclude videos with `#Shorts` in title
  - OR exclude videos under 60 seconds duration
- **Add "See the channel →" link** at bottom of section linking to full YouTube channel
- Ensure cache is refreshing appropriately
- Videos should also be embeddable on individual project pages where relevant

### 4.5 Static vs. CMS Content

**Build as STATIC (hardcoded in Astro components):**
- Homepage hero and "What I Do" section
- All content on /about
- Resume page (from provided data)
- Dissertation pages (from provided document)
- Excavations list (from provided CV data)
- Always Sunny Tour section content
- Merakiva Travel section content

**Build with CMS (Sanity):**
- Featured project on homepage (selectable)
- "In The Media" items
- Work/Projects grid items
- Publications (for adding new ones)
- Field Notes / Blog posts

---

## Part 5: Execution Checklist

### Phase 2A: Style Refinement
- [ ] Audit all copy on current site
- [ ] Replace kitschy language per the table in Section 2
- [ ] Test that visual design elements still work after copy changes
- [ ] Ensure consistency across all pages

### Phase 2B: Data Collection
- [ ] Collect resume/CV data from Marshall
- [ ] Collect dissertation document from Marshall
- [ ] Collect publications list from Marshall
- [ ] Collect media appearances from Marshall
- [ ] Collect portfolio examples from Marshall
- [ ] Collect bios and philosophy text from Marshall
- [ ] Collect and organize visual assets

### Phase 2C: Content Build
- [ ] Build /resume page with collected data
- [ ] Build /academic/dissertation landing page
- [ ] Build individual dissertation chapter pages
- [ ] Build /academic/publications structure
- [ ] Build /academic/excavations from CV data
- [ ] Build /always-sunny-tour section
- [ ] Build /merakiva section
- [ ] Update homepage "What I Do" section
- [ ] Update /about with full bio content

### Phase 2D: Final QA
- [ ] All links working
- [ ] All images loading
- [ ] Mobile responsive check
- [ ] Copy proofread (no remaining kitschy language)
- [ ] CMS items displaying correctly
- [ ] YouTube feed working
- [ ] Contact form working
- [ ] Lighthouse score >90

---

## Part 6: Reference Information

### Marshall's Existing Sites
- YouTube: youtube.com/@marshallschurtz
- Always Sunny Tour: alwayssunnytour.com
- Merakiva Travel: merakivatravel.com
- LinkedIn: linkedin.com/in/marshallschurtz
- Instagram: instagram.com/marshallschurtz
- Bluesky: bsky.app/profile/marshallschurtz.com

### Design References
- Mockup images provided show the overall design concept
- Key visual elements: depth gauge, grid overlay, orange accents, monospace metadata, stratigraphic color transition
- Typography: Neo-grotesk headlines (Archivo/Inter), Monospace for data (JetBrains Mono/Space Mono)
- Colors: Surface #F4F1EA, Orange #FF4F00, Bedrock #1A1A1A

### Tech Stack
- Astro (v4.x)
- Tailwind CSS
- GSAP + ScrollTrigger
- Sanity.io CMS
- Vercel hosting
- YouTube Data API v3

