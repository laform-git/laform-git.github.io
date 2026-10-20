/* Library index: builds the cards from sites.json so a new booklet is one small edit. */
(function () {
  function esc(s) { return String(s || "").replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  var st = document.createElement("style"); st.textContent = ".site .l{font:500 11px/1.2 var(--mono,monospace);letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}.sec .banner{display:flex;align-items:center;gap:10px;margin:8px 0 16px;padding:10px 16px;border-radius:10px;background:var(--sc);color:#fff;font:800 15px/1 var(--display,system-ui);letter-spacing:.14em;text-transform:uppercase}.sec .banner small{margin-left:auto;font:500 12px/1 var(--mono,monospace);letter-spacing:.08em;opacity:.85}.sec .site{border-left-color:var(--sc)}.sec .site .u{color:var(--sc)}"; document.head.appendChild(st);
  var COL = { Faith: "#3b6fb6", Health: "#2f8f74", Mindforge: "#8a4fb0", Mirabilia: "#b8487a", Tech: "#c46a1d" };
  var order = ["Faith", "Health", "Mindforge", "Mirabilia", "Tech"];
  fetch("sites.json", { cache: "no-cache" }).then(function (r) { return r.json(); }).then(function (list) {
    var live = list.filter(function (x) { return x.status !== "Pulled"; }), secs = {};
    live.forEach(function (x) { (secs[x.section] = secs[x.section] || []).push(x); });
    var keys = Object.keys(secs).sort(function (a, b) { var i = order.indexOf(a), j = order.indexOf(b); return (i < 0 ? 99 : i) - (j < 0 ? 99 : j) || a.localeCompare(b); });
    document.getElementById("count").textContent = live.length;
    document.getElementById("sections").innerHTML = keys.map(function (k) {
      return '<section class="sec" style="--sc:' + (COL[k] || "#6b6862") + '"><h2 class="banner">' + esc(k) + '<small>' + secs[k].length + '</small></h2><div class="grid">' + secs[k].map(function (x) {
        return '<a class="site" href="' + esc(x.path) + '">' + (x.label ? '<span class="l">' + esc(x.label) + '</span>' : '') + '<span class="t">' + esc(x.name) + "</span>" + (x.blurb ? '<span class="s">' + esc(x.blurb) + "</span>" : "") + '<span class="u">' + esc(x.langs || "Open") + " →</span></a>";
      }).join("") + "</div></section>";
    }).join("");
  });
  if (!document.querySelector(".fsctl")) fetch("reader/reader.html", { cache: "no-cache" }).then(function (r) { return r.text(); }).then(function (h) {
    if (document.querySelector(".fsctl")) return;
    var box = document.createElement("div"); box.innerHTML = h;
    Array.prototype.slice.call(box.childNodes).forEach(function (nd) {
      if (nd.tagName === "SCRIPT") { var s = document.createElement("script"); s.textContent = nd.textContent; document.body.appendChild(s); }
      else document.body.appendChild(nd);
    });
  });
})();
