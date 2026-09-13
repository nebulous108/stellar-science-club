
(() => {
  const targets = [document.getElementById('home-videos'), document.getElementById('youtube-videos')].filter(Boolean);
  if (!targets.length) return;
  const esc = v => String(v ?? '').replace(/[&<>'"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));
  const date = v => { if(!v) return ''; const d=new Date(v); return Number.isNaN(d.getTime())?'':d.toLocaleDateString('en-AU',{day:'numeric',month:'short',year:'numeric'}); };
  fetch('data/videos.json?ts='+Date.now(), {cache:'no-store'})
    .then(r => { if(!r.ok) throw new Error('feed'); return r.json(); })
    .then(data => {
      const videos=(data.videos||[]).filter(v=>v && v.id).slice(0,12);
      if(!videos.length) throw new Error('empty');
      targets.forEach(target=>{
        const count=target.id==='home-videos'?3:12;
        target.innerHTML=videos.slice(0,count).map(v=>`<article class="video"><a class="thumb" href="${esc(v.url)}" target="_blank" rel="noopener"><img src="${esc(v.thumbnail || `https://i.ytimg.com/vi/${encodeURIComponent(v.id)}/hqdefault.jpg`)}" alt="${esc(v.title)}" loading="lazy"><span class="play-badge">▶</span></a><div class="video-body"><h3>${esc(v.title||'Untitled video')}</h3><div class="meta">${esc(date(v.published))}${v.duration?` · ${esc(v.duration)}`:''}</div><a class="watch" href="${esc(v.url)}" target="_blank" rel="noopener">Watch on YouTube →</a></div></article>`).join('');
      });
    })
    .catch(()=>targets.forEach(target=>target.innerHTML='<div class="loading">The latest upload feed is temporarily unavailable. <a class="watch" href="https://www.youtube.com/@StellarScienceClub" target="_blank" rel="noopener">Open the YouTube channel →</a></div>'));
})();
