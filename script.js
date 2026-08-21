/*
  STELLAR SCIENCE CLUB
  Edit the channel list below to match your actual Discord server.
  Everything else on the site can stay unchanged.
*/

const channels = [
  { name: "announcements", desc: "Server news & updates" },
  { name: "general", desc: "General community chat" },
  { name: "homework-help", desc: "Ask questions & get help" },
  { name: "science-discussion", desc: "Science & new research" },
  { name: "study-sessions", desc: "Study together" },
  { name: "kahoots", desc: "Quizzes & battles" }
];

const grid = document.getElementById("channel-grid");

grid.innerHTML = channels.map(channel => `
  <div class="channel">
    <span class="channel-hash">#</span>
    <div>
      <span class="channel-name">${channel.name}</span>
      <span class="channel-desc">${channel.desc}</span>
    </div>
  </div>
`).join("");

document.getElementById("year").textContent = new Date().getFullYear();
