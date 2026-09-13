# Stellar Science Club — Website Revamp

A multi-page static website for Stellar Science Club, designed for GitHub Pages.

## Pages
- `index.html` — homepage, community identity, latest uploads
- `features.html` — what members can do
- `study-events.html` — study sessions and weekly events
- `community.html` — channel structure
- `jmss.html` — John Monash Science School hub
- `youtube.html` — newest YouTube uploads
- `team.html` — leadership and staff structure

## Automatic YouTube uploads
The site uses a small generated data file at `data/videos.json` rather than trying to expose a YouTube API key in browser JavaScript.

`.github/workflows/update-youtube.yml` runs every 30 minutes and can also be started manually from **Actions → Refresh YouTube uploads → Run workflow**. It installs the latest `yt-dlp`, reads the public `@StellarScienceClub/videos` page, and updates `data/videos.json` with the newest uploads. The page itself remains plain static HTML/CSS/JS, so it works on GitHub Pages.

### Important
- The site shows the **newest uploads from Stellar Science Club's channel**. It does not access a visitor's personal YouTube "For You" recommendations.
- The fallback `data/videos.json` contains two known Stellar Science Club videos so the site is not blank before the first workflow run.
- If GitHub Actions is disabled, you can still edit `data/videos.json` manually.

## GitHub Pages
Publish the repository from the root of the default branch, or use a GitHub Pages Actions deployment. GitHub Pages supports static HTML/CSS/JS files directly.

## Customisation
- Main styling: `assets/style.css`
- Site behaviour: `assets/site.js`
- YouTube rendering: `assets/video-feed.js`
- Upload feed data: `data/videos.json`
- YouTube updater: `scripts/update_youtube.py`
