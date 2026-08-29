# Stellar Science Club

The official website for **Stellar Science Club**, an Australia-focused science community on Discord with 200+ members.

## What the website is

The site introduces the Stellar Science Club community and gives visitors a clear way to explore what happens inside the server.

It includes:

- **Home** — an overview of the club and its purpose.
- **Features** — homework help, science discussion, study sessions, Kahoot battles, JMSS preparation and YouTube.
- **Study & Events** — information about study sessions and Kahoot battles, including the fact that study-session content is posted on YouTube.
- **Community** — a visual directory of the server's channel categories.
- **JMSS Prep** — specialised channels used by students preparing for JMSS, including interview, Year 10 entry, Year 11 entry and exam-advice spaces.
- **YouTube** — a dedicated page for the Stellar Science Club YouTube channel, including an automatically updated list of the newest uploads.
- **Team** — the founder, co-founder and admin team.

## Automatic YouTube updates

The YouTube page is connected to the public **@StellarScienceClub** channel through a GitHub Actions workflow.

Every 30 minutes, the workflow:

1. Checks the YouTube channel for the newest uploads.
2. Collects the latest video titles, thumbnails, dates and links.
3. Updates `data/videos.json`.
4. Commits the changed data back to the repository.
5. GitHub Pages serves the updated website automatically.

No YouTube API key is stored in the website. The updater uses `yt-dlp` inside GitHub Actions to read the public channel feed.

The workflow can also be run manually from the repository's **Actions** tab using **Update YouTube videos → Run workflow**.

## Links

Discord: https://dsc.gg/stellar-science-club

YouTube: https://www.youtube.com/@StellarScienceClub

## Hosting

This is a static multi-page website designed for GitHub Pages. The website itself does not need a server or database. The only automated backend-like process is the GitHub Actions workflow that refreshes the YouTube data file.

The homepage is `index.html`, and the other pages are regular HTML files in the repository root.
