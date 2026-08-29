#!/usr/bin/env python3
"""Update data/videos.json from the Stellar Science Club YouTube channel.

This script is run by GitHub Actions. It uses yt-dlp to resolve the public
YouTube handle, so no YouTube API key is required.
"""
import json
import os
import subprocess
from datetime import datetime, timezone

CHANNEL = "https://www.youtube.com/@StellarScienceClub/videos"
OUTPUT = os.path.join(os.path.dirname(__file__), "..", "data", "videos.json")

cmd = [
    "yt-dlp",
    "--flat-playlist",
    "--dump-single-json",
    "--playlist-end", "12",
    "--no-warnings",
    CHANNEL,
]

result = subprocess.run(cmd, check=True, capture_output=True, text=True)
info = json.loads(result.stdout)
entries = info.get("entries") or []

videos = []
for item in entries:
    if not item or not item.get("id"):
        continue
    vid = item["id"]
    title = item.get("title") or "Untitled video"
    upload_date = item.get("upload_date") or ""
    published = ""
    if len(upload_date) == 8:
        published = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"
    videos.append({
        "id": vid,
        "title": title,
        "url": f"https://www.youtube.com/watch?v={vid}",
        "thumbnail": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
        "published": published,
        "duration": item.get("duration_string") or "",
    })

payload = {
    "updated": datetime.now(timezone.utc).isoformat(),
    "channel": "https://www.youtube.com/@StellarScienceClub",
    "videos": videos,
}

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"Updated {OUTPUT} with {len(videos)} videos.")
