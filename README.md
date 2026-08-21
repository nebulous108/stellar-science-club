# Stellar Science Club Website

A static, GitHub Pages-ready website for the Stellar Science Club Discord server.

## Files

- `index.html` — page structure/content
- `styles.css` — visual design
- `script.js` — channel list + small page behaviour
- `assets/stellar-qr.png` — supplied Discord QR code

## Before publishing

Open `script.js` and change the `channels` array so the names/descriptions exactly match your real Discord channels.

The following details are already included:

- 200+ members
- @Nebulous — Founder
- @Joe — Co-Founder
- Discord: https://dsc.gg/stellar-science-club
- YouTube: https://www.youtube.com/@StellarScienceClub
- Australia-focused science community
- Homework help
- Study sessions
- Kahoot battles
- Science discussion / new research

The old design elements you asked to remove are NOT included:
- No giveaways
- No twice-daily news
- No website science-fact section

## GitHub Pages

For a simple static site, GitHub Pages can publish directly from your `main` branch and the repository root.

1. Create/open your GitHub repository.
2. Upload all files and the `assets` folder.
3. Commit the changes.
4. Go to **Settings → Pages**.
5. Under **Build and deployment**, choose **Deploy from a branch**.
6. Select `main` and `/(root)`.
7. Click **Save**.

GitHub will build and publish the site automatically after changes are pushed.

If you later want a custom domain, configure it from the same Pages settings area.

## Design

The design is intentionally based on the screenshots you supplied:
- dark space background
- purple/blue gradient accents
- rounded glass-like cards
- large centred hero
- feature cards
- event cards
- team section
- QR join card
- YouTube promotion
- responsive mobile layout

No framework or build step is required.
