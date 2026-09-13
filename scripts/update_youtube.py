#!/usr/bin/env python3
"""Update the public Stellar Science Club YouTube upload feed.
Uses the channel's public Atom feed first, then falls back to yt-dlp.
No YouTube API key is required.
"""
import json, os, subprocess, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timezone

CHANNEL_HANDLE = "@StellarScienceClub"
CHANNEL_URL = "https://www.youtube.com/@StellarScienceClub/videos"
OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "videos.json"))

def rss_feed():
    # Resolve the handle to the canonical channel page, then obtain its channel ID.
    req=urllib.request.Request("https://www.youtube.com/@StellarScienceClub",headers={"User-Agent":"Mozilla/5.0"})
    html=urllib.request.urlopen(req,timeout=30).read().decode("utf-8","ignore")
    import re
    m=re.search(r'"channelId":"([A-Za-z0-9_-]{20,30})"',html)
    if not m: return []
    channel_id=m.group(1)
    url=f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
    data=urllib.request.urlopen(req,timeout=30).read()
    root=ET.fromstring(data)
    ns={"a":"http://www.w3.org/2005/Atom","yt":"http://www.youtube.com/xml/schemas/2015"}
    result=[]
    for e in root.findall("a:entry",ns)[:15]:
        vid=e.findtext("yt:videoId",default="",namespaces=ns)
        title=e.findtext("a:title",default="",namespaces=ns)
        published=e.findtext("a:published",default="",namespaces=ns)
        if vid:
            result.append({"id":vid,"title":title or "Untitled video","url":f"https://www.youtube.com/watch?v={vid}","thumbnail":f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg","published":published[:10],"duration":""})
    return result

def ytdlp():
    cmd=["yt-dlp","--dump-json","--flat-playlist","--playlist-end","15","--no-warnings","--ignore-errors",CHANNEL_URL]
    r=subprocess.run(cmd,check=False,capture_output=True,text=True,timeout=180)
    out=[]
    for line in r.stdout.splitlines():
        try: item=json.loads(line)
        except Exception: continue
        vid=item.get("id")
        if vid:
            out.append({"id":vid,"title":item.get("title") or "Untitled video","url":f"https://www.youtube.com/watch?v={vid}","thumbnail":f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg","published":item.get("upload_date") or "","duration":item.get("duration_string") or ""})
    return out

videos=[]
try: videos=rss_feed()
except Exception as e: print("RSS update failed:",e)
if not videos:
    try: videos=ytdlp()
    except Exception as e: print("yt-dlp update failed:",e)
if not videos:
    print("No videos returned; preserving existing feed.")
    raise SystemExit(0)

payload={"updated":datetime.now(timezone.utc).isoformat(),"channel":"https://www.youtube.com/@StellarScienceClub","videos":videos}
os.makedirs(os.path.dirname(OUTPUT),exist_ok=True)
with open(OUTPUT,"w",encoding="utf-8") as f: json.dump(payload,f,ensure_ascii=False,indent=2); f.write("\n")
print(f"Updated {OUTPUT} with {len(videos)} uploads.")
