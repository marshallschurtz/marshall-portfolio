# Marshall Schurtz Portfolio

Personal portfolio website for Marshall Schurtz — Founder, Archaeologist, Storyteller, Strategist.

## 🔗 Live URLs

| Service | URL |
|---------|-----|
| **Production Site** | *Deploy to Vercel (see below)* |
| **Sanity Studio** | [marshall-portfolio.sanity.studio](https://marshall-portfolio.sanity.studio/) |
| **GitHub Repo** | [github.com/marshallschurtz/marshall-portfolio](https://github.com/marshallschurtz/marshall-portfolio) |

## 🛠️ Tech Stack

- **Framework**: [Astro](https://astro.build) v5
- **UI Components**: [Svelte](https://svelte.dev) v5
- **Styling**: [TailwindCSS](https://tailwindcss.com) v4
- **CMS**: [Sanity](https://sanity.io)
- **Animations**: [GSAP](https://gsap.com)
- **Hosting**: Vercel (site) + Sanity Studio (CMS)

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- npm or pnpm

### Installation

```bash
# Clone the repository
git clone https://github.com/marshallschurtz/marshall-portfolio.git
cd marshall-portfolio

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

### Development

```bash
# Start the dev server
npm run dev

# Site runs at http://localhost:4321
```

### Sanity Studio (Local)

```bash
cd sanity
npm install
npm run dev

# Studio runs at http://localhost:3333
```

## 📦 Deployment

### Deploy to Vercel

1. Go to [vercel.com/new](https://vercel.com/new)
2. Import the GitHub repo: `marshallschurtz/marshall-portfolio`
3. Add the following **Environment Variables**:

| Variable | Description |
|----------|-------------|
| `PUBLIC_SANITY_PROJECT_ID` | Sanity project ID: `mkro68w7` |
| `PUBLIC_SANITY_DATASET` | Sanity dataset: `production` |
| `PUBLIC_YOUTUBE_API_KEY` | YouTube Data API key |
| `PUBLIC_YOUTUBE_CHANNEL_ID` | YouTube channel ID |

4. Click **Deploy**

### Deploy Sanity Studio

```bash
cd sanity
npx sanity login
npx sanity deploy
```

Studio is deployed to: [marshall-portfolio.sanity.studio](https://marshall-portfolio.sanity.studio/)

### Connect Custom Domain (Cloudflare)

1. In Vercel → Project Settings → Domains
2. Add your domain (e.g., `marshallschurtz.com`)
3. In Cloudflare DNS:
   - Add `CNAME` record pointing to `cname.vercel-dns.com`
   - Set proxy to **OFF** (gray cloud) initially

## 🧞 Commands

| Command | Action |
|---------|--------|
| `npm install` | Install dependencies |
| `npm run dev` | Start dev server at `localhost:4321` |
| `npm run build` | Build production site to `./dist/` |
| `npm run preview` | Preview build locally |

## 📁 Project Structure

```
/
├── public/              # Static assets (images, PDFs, etc.)
├── sanity/              # Sanity CMS Studio
├── src/
│   ├── components/      # Astro & Svelte components
│   ├── layouts/         # Page layouts
│   ├── lib/             # Utilities (Sanity client, animations)
│   ├── pages/           # Routes
│   └── styles/          # Global CSS
├── .env.example         # Environment variable template
└── astro.config.mjs     # Astro configuration
```

## 🔐 Environment Variables

Copy `.env.example` to `.env` and fill in:

```bash
PUBLIC_SANITY_PROJECT_ID=mkro68w7
PUBLIC_SANITY_DATASET=production
PUBLIC_YOUTUBE_API_KEY=your_youtube_api_key
PUBLIC_YOUTUBE_CHANNEL_ID=your_channel_id
```

## 📝 License

Private repository. All rights reserved.
