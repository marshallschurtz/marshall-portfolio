# Media Kit Page: Development Document
## Marshall Schurtz — Brand Partnership Page

**Project:** Single-page media kit for marshallschurtz.com  
**Purpose:** Enable brand partnerships, product-for-coverage exchanges, and professional outreach  
**Business Entity:** Merakiva Travel Inc (Delaware Corporation)  
**Contact:** marshall@merakivatravel.com

---

## 1. Project Overview

### What This Page Does
- Positions Marshall as an archaeologist-creator with credibility and engaged audience
- Provides private metrics brands need for internal decisions
- Makes partnership structure immediately clear
- Enables frictionless outreach (one link = everything they need)
- Functions as both live webpage AND printable PDF

### Key Differentiator
This isn't a vanity page. It provides information brands *can't* get from looking at the channel: demographic breakdowns, engagement rates, geographic distribution, and clear partnership structures.

---

## 2. Technical Requirements

### Core Functionality
- **Single scrolling page** (no navigation, no subpages)
- **Print-to-PDF button** — Generates clean PDF of page content
- **YouTube API integration** — Pulls live view counts for featured videos
- **Analytics timestamp** — Shows when demographic/private data was last updated
- **Mobile-first responsive design**
- **Fast load times** (compress all images, lazy load videos)

### API Integration Specs
```
YouTube Data API v3
- Pull: viewCount, likeCount, subscriberCount
- Videos to embed: 
  1. Riyadh Metro (1ispFw7z-jY)
  2. Iberia Business Class (D2ixseA9C4Q)
  3. Carthage Harbor (cEvHUw2DgkA)
- Refresh: On page load (cached for 1 hour)
- Display: Live view count badge on each video thumbnail
```

### Print-to-PDF Requirements
- Clean formatting (hide navigation elements, print button)
- Include "Generated from marshallschurtz.com on [DATE]" footer
- Maintain brand colors and typography
- Single continuous document (no page breaks mid-section)

---

## 3. Design Direction


Follow the overall site's design principles, as laid out in the global CSS.

### Aesthetic Concept: "Academic Explorer"
Editorial feel meets field journal. Premium but not pretentious. The vibe of a high-end travel magazine meets an archaeological field report.


---

## 4. Page Structure & Copy

### Section 1: Hero (Above the Fold)

**Layout:** 
- Left: Headline + subhead + proof points
- Right: Hero image (Marshall in field/travel context). Utlize from  project_assets/images/marshall

**Copy:**

```
[H1] PhD Archaeologist. Travel Creator. First to the Story.

[Subhead] I create infrastructure and travel documentaries 
with genuine expertise — and audiences who take action.

[Three proof badges in a row:]
🎓 PhD Archaeology (University of Pennsylvania, 2022)
📺 130,000+ views on breakout video
🚀 First creator to cover the complete Riyadh Metro system
```

---

### Section 2: The Positioning (2-3 sentences)

**Copy:**

```
Most travel creators show you places. I show you why they matter.

As a working archaeologist with exclusive access to sites like the 
Lagash excavation in Iraq, I bring credibility that transfers to 
brand partners. My content lives at the intersection of infrastructure, 
archaeology, and exploration travel — and reaches an audience of 
well-spending travelers and documentary enthusiasts who click, 
engage, and convert.
```

---

### Section 3: Audience Data (Private Metrics)

**Layout:** 
- Three-column grid on desktop
- Stacked cards on mobile
- "Last updated: [TIMESTAMP]" below section

**Data to display:**


SAMPLE DATA - replace with up-to date data, shared in screenshots
```
DEMOGRAPHICS
├── Gender: 90% Male / 10% Female
├── Age Range: 25-44 (primary), 18-24 (secondary)
└── [Visual: Simple horizontal bars]

GEOGRAPHY (Top 5)
├── United States: 20%
├── Saudi Arabia: 12%
├── United Kingdom: 3%
├── [Other countries from analytics]
└── [Visual: Horizontal bar chart]

AUDIENCE INTERESTS
├── Documentary & Nonfiction
├── Travel Enthusiasts  
├── Tech-Forward Professionals
├── Transit & Infrastructure
└── History & Archaeology

ENGAGEMENT
├── Subscriber Count: [LIVE VIA API]
├── Engagement Rate: [CALCULATED]
├── Avg. Watch Time: [FROM ANALYTICS]
└── Link Click Rate: 500+ clicks on breakout video
```

**Small print below:**
```
Analytics updated [DATE]. Live subscriber count via YouTube API.
```

---

### Section 4: Featured Content

**Layout:**
- Three video cards in a row (desktop)
- Each card: Thumbnail + title + live view count badge
- Stacked on mobile

**Videos to Feature:**

```
[VIDEO CARD 1]
Thumbnail: Riyadh Metro
Title: "[LIVE TITLE FROM YOUTUBE]""
Badge: [LIVE VIEW COUNT] views
Subtext: Infrastructure + Transit

[VIDEO CARD 2]
Thumbnail: Iberia Business Class
Title: "[LIVE TITLE FROM YOUTUBE]"
Badge: [LIVE VIEW COUNT] views
Subtext: Premium Travel

[VIDEO CARD 3]
Thumbnail: Carthage Harbor
Title: "[LIVE TITLE FROM YOUTUBE]""
Badge: [LIVE VIEW COUNT] views
Subtext: Archaeological Exploration
```

**Below cards:**
```
My videos are evergreen — they rank in search and continue 
generating views for years. The Riyadh Metro video gained 
46,000 views in its first week and continues growing. Combining sensationalist content with infrastructure means that viewers keep discovering videos, as my take rises above typical travel vlog explainers.
```

---

### Section 5: Content Formats

**Layout:** Simple two-column list or icon grid

**Copy:**

```
WHAT I CREATE

Challenge Documentaries
└── Complete system rides, multi-day routes, first-to-cover projects
    Example: "Every line on the Riyadh Metro"

Infrastructure + Culture
└── Transit systems, megaprojects, development stories
    Example: "7 Things About Riyadh That Changed My Perception"

Premium Travel
└── Business class reviews, hotel features, gear deep-dives
    Example: "[live title of iberia video]"

Archaeological Exploration  
└── Site visits with expert commentary, historical storytelling
    Example: "[live title of carthage video]"
```

---

### Section 6: Partnership Options

**Layout:** Two cards side by side

**Copy:**

```
HOW WE CAN WORK TOGETHER

─────────────────────────────────────────────────────────────

INTEGRATED MENTION + LINK
Natural mention within video narrative. Your product or 
service appears as part of the story, not an interruption.
Includes: On-screen mention, link in description, pin in comments.
Best for: Gear, travel tech, services I authentically use.

─────────────────────────────────────────────────────────────

AD-BREAK SPONSORSHIP  
Dedicated 30-60 second segment within the video. 
Similar to the sponsor breaks you see on established channels.
Includes: Custom script, on-screen graphics, description link.
Best for: Apps, insurance, travel services, larger brand campaigns.

─────────────────────────────────────────────────────────────

HOTELS & TOURS: COVERAGE EXCHANGE
Complimentary stay or experience in exchange for video feature.
Includes: On-camera highlight, description link, raw footage/
photos for your marketing use (UGC).
Best for: Properties and operators along my planned routes.

─────────────────────────────────────────────────────────────

Contact for rates and availability.
```

---

### Section 7: What You Get

**Layout:** Simple list with icons

**Copy:**

```
WHAT I BRING TO PARTNERSHIPS

✓ PhD-Level Credibility
  Your brand associated with expertise, not influencer fluff.

✓ High Production Value  
  4K footage, professional audio, narrative storytelling.

✓ Evergreen Content
  Videos rank in search and stay relevant for years.

✓ Action-Oriented Audience
  Viewers click links and convert — even on products 
  unrelated to the video content.

✓ UGC Assets (for hotels/tours)
  Raw footage and photos available for your marketing use.
```

---

### Section 8: Upcoming Projects

**Layout:** Simple timeline or list

**Copy:**

```
ON THE HORIZON

February 2026 — TREN MAYA DOCUMENTARY
First expert-led documentary of Mexico's complete Tren Maya loop.
1,500km of rail through the Yucatan, visiting every UNESCO 
archaeological site on the route. Partnership opportunities available.

March 2026 — LAGASH ARCHAEOLOGICAL DIG
Exclusive content from active excavation in Iraq. 
First public video featuring newly discovered city walls 

April 2026 — RETRACED WILLIAM THE CONQUERER BY BIKE
A two week trip where I bike from William the Conquerer's birthplace to France to Westminster Abbey in London, exploring the entirey of his conquest of England while pushing myself through physical and logistical challenges of this nearly 500 mile journey.

```

---

### Section 9: Footer / Contact

**Layout:** Centered, simple

**Copy:**

```
─────────────────────────────────────────────────────────────

LET'S TALK

marshall@merakivatravel.com

YouTube: youtube.com/@marshallschurtz
Instagram: @marshallschurtz

Partnerships managed through my company, Merakiva Travel Inc.

─────────────────────────────────────────────────────────────

[PRINT AS PDF BUTTON]

─────────────────────────────────────────────────────────────
```

---

## 5. Assets Required From Marshall

### Images
| Asset | Specs | Purpose |
|-------|-------|---------|
| Hero photo | 1200x800px min, landscape | Section 1 hero |
| Action shot 1 | 800x600px min | Optional secondary |
| Headshot | 400x400px, square | Footer or about |

### Data (from YouTube Analytics export)
| Metric | Where It Goes |
|--------|---------------|
| Gender breakdown % | Demographics card |
| Age range breakdown % | Demographics card |
| Top 5 countries + % | Geography chart |
| Subscriber count | Hero + Audience section |
| Average watch time | Audience section |
| Engagement rate calculation | Audience section |
| 28-day or 365-day views | Optional |

### Video IDs for API
| Video | YouTube ID |
|-------|------------|


### Brand Assets
| Asset | Purpose |
|-------|---------|
| Merakiva Travel logo (if exists) | Footer |

### Access
| Item | Purpose |
|------|---------|
| YouTube API key | Live view counts |


---

## 6. Developer Notes

### Print-to-PDF Implementation
Use browser's native print functionality with CSS @media print rules:
```css
@media print {
  .print-button, .nav-elements { display: none; }
  .page-container { max-width: 100%; }
  /* Add footer with generation date */
}
```

Or use a library like html2pdf.js for more control over PDF output.

### YouTube API Integration
(already implemented on site - look for existing documentaiton)
```javascript
// Pseudocode structure
const YOUTUBE_API_KEY = 'YOUR_KEY';
const VIDEO_IDS = ['1ispFw7z-jY', 'VIDEO_ID_2', 'VIDEO_ID_3'];

async function fetchVideoStats(videoId) {
  const response = await fetch(
    `https://www.googleapis.com/youtube/v3/videos?part=statistics&id=${videoId}&key=${YOUTUBE_API_KEY}`
  );
  const data = await response.json();
  return data.items[0].statistics;
}

// Cache results for 1 hour to avoid rate limits
```

### Analytics Timestamp
Store the date when Marshall last updated the demographic data in a config file or CMS. Display as:
```
"Audience analytics as of December 2025. Subscriber count live."
```

### Responsive Breakpoints
```css
/* Mobile first */
@media (min-width: 768px) { /* Tablet */ }
@media (min-width: 1024px) { /* Desktop */ }
```

---

## 7. Success Criteria

The page is successful if:
1. A brand can understand Marshall's value prop in < 10 seconds
2. They can find demographic data without scrolling far
3. Partnership options are immediately clear
4. They can generate a PDF to share internally
5. Page loads in < 3 seconds
6. Works perfectly on mobile (brands forward these on phones)

---

## 8. Questions for Marshall Before Build


2. **Hero photo:** Do you have a high-res action shot you want to use?
3. **Merakiva logo:** Does one exist, or should we skip it?
---> IN FOLDER ---> /project_assets/images/merakiva/ merakiva logo
4. **Analytics export:** 3 images included with up-to-date analystics


---

## 9. Output

Output the requisite files and verify their functionality.

Then, verify the correct information with me, Marshall.

---

*Document created: January 2026*  
*For: AI Developer implementation*