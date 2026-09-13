#!/usr/bin/env python3
"""Refresh the public Stellar Science Club upload feed.

No YouTube API key is required. yt-dlp reads the public channel upload page and
writes a small JSON file consumed by the static GitHub Pages site.
"""
import json, os, subprocess
from datetime import datetime, timezone

CHANNEL = "https://www.youtube.com/@StellarScienceClub/videos"
OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "videos.json"))

cmd = [
    "yt-dlp", "--dump-json", "--playlist-end", "12", "--no-warnings",
    "--ignore-errors", "--skip-download", CHANNEL,
]
result = subprocess.run(cmd, check=False, capture_output=True, text=True, timeout=180)
entries=[]
for line in result.stdout.splitlines():
    try: item=json.loads(line)
    except json.JSONDecodeError: continue
    if item.get("id"): entries.append(item)

if not entries:
    print("No videos returned; preserving the existing feed.")
    raise SystemExit(0)

videos=[]
for item in entries:
    vid=item["id"]
    upload_date=item.get("upload_date") or ""
    published=f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}" if len(upload_date)==8 else ""
    videos.append({
        "id":vid,
        "title":item.get("title") or "Untitled video",
        "url":f"https://www.youtube.com/watch?v={vid}",
        "thumbnail":f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
        "published":published,
        "duration":item.get("duration_string") or "",
    })

payload={"updated":datetime.now(timezone.utc).isoformat(),"channel":"https://www.youtube.com/@StellarScienceClub","videos":videos}
os.makedirs(os.path.dirname(OUTPUT),exist_ok=True)
with open(OUTPUT,"w",encoding="utf-8") as f: json.dump(payload,f,ensure_ascii=False,indent=2); f.write("\n")
print(f"Updated {OUTPUT} with {len(videos)} uploads.")
