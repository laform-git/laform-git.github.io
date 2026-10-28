/* Library index: builds the cards from sites.json so a new booklet is one small edit. */
(function () {
  function esc(s) { return String(s || "").replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  var st = document.createElement("style"); st.textContent = ".site .l{font:500 11px/1.2 var(--mono,monospace);letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}.sec .banner{display:flex;align-items:center;gap:10px;margin:8px 0 16px;padding:10px 16px;border-radius:10px;background:var(--sc);color:#fff;font:800 15px/1 var(--display,system-ui);letter-spacing:.14em;text-transform:uppercase}.sec .banner small{margin-left:auto;font:500 12px/1 var(--mono,monospace);letter-spacing:.08em;opacity:.85}.sec .site{border-left-color:var(--sc)}.sec .site .u{color:var(--sc)}.sec .banner .shr{display:inline-flex;align-items:center;justify-content:center;width:30px;height:30px;margin-left:6px;padding:0;border:0;border-radius:50%;background:transparent;color:#fff;opacity:.8;cursor:pointer}.sec .banner .shr:hover{opacity:1;background:rgba(255,255,255,.18)}.sec[hidden]{display:none}#allsec{margin:0 0 14px;font:600 15px/1.2 var(--display,system-ui)}#allsec a{color:var(--accent);text-decoration:none}#allsec[hidden]{display:none}"; document.head.appendChild(st);
  var ICON = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M10 14a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1M14 10a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/></svg>';
  function slug(x) { return String(x).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, ""); }
  function toast(m) { var d = document.createElement("div"); d.textContent = m; d.style.cssText = "position:fixed;left:50%;bottom:90px;transform:translateX(-50%);background:#222;color:#fff;font:600 14px/1 system-ui,sans-serif;padding:10px 16px;border-radius:999px;z-index:99"; document.body.appendChild(d); setTimeout(function () { d.remove(); }, 1800); }
  var COL = { Faith: "#b8741a", Health: "#2f8f74", Mindforge: "#8a4fb0", Mirabilia: "#b8487a", Tech: "#3b6fb6" };
  var order = ["Faith", "Health", "Mindforge", "Mirabilia", "Tech"];
  fetch("sites.json", { cache: "no-cache" }).then(function (r) { return r.json(); }).then(function (list) {
    var live = list.filter(function (x) { return x.status !== "Pulled"; }), secs = {};
    live.forEach(function (x) { (secs[x.section] = secs[x.section] || []).push(x); });
    var keys = Object.keys(secs).sort(function (a, b) { var i = order.indexOf(a), j = order.indexOf(b); return (i < 0 ? 99 : i) - (j < 0 ? 99 : j) || a.localeCompare(b); });
    document.getElementById("count").textContent = live.length;
    document.getElementById("sections").innerHTML = keys.map(function (k) {
      var sl = slug(k);
      return '<section class="sec" id="' + sl + '" style="--sc:' + (COL[k] || "#6b6862") + '"><h2 class="banner">' + esc(k) + '<button class="shr" type="button" data-s="' + sl + '" aria-label="Share the ' + esc(k) + ' section" title="Share this section">' + ICON + '</button><small>' + secs[k].length + '</small></h2><div class="grid">' + secs[k].map(function (x) {
        return '<a class="site" href="' + esc(x.path) + '">' + (x.label ? '<span class="l">' + esc(x.label) + '</span>' : '') + '<span class="t">' + esc(x.name) + "</span>" + (x.blurb ? '<span class="s">' + esc(x.blurb) + "</span>" : "") + '<span class="u">' + esc(x.langs || "Open") + " →</span></a>";
      }).join("") + "</div></section>";
    }).join("");
    filter();
    window.addEventListener("hashchange", filter);
    document.getElementById("sections").onclick = function (e) {
      var bt = e.target.closest(".shr"); if (!bt) return;
      var url = location.href.split("#")[0] + "#" + bt.dataset.s, name = bt.parentNode.firstChild.textContent;
      if (navigator.share) navigator.share({ title: name + " · Study Library", url: url }).catch(function () {});
      else if (navigator.clipboard) navigator.clipboard.writeText(url).then(function () { toast("Link copied"); }, function () { prompt("", url); });
      else prompt("", url);
    };
  });
  /* a section link (#faith, #health…) shows only that section, with a way back to everything */
  function filter() {
    var h = decodeURIComponent((location.hash || "").slice(1)), all = document.querySelectorAll("#sections .sec"), hit = false;
    all.forEach(function (s) { if (s.id === h) hit = true; });
    all.forEach(function (s) { s.hidden = hit && s.id !== h; });
    var back = document.getElementById("allsec");
    if (hit && !back) {
      back = document.createElement("p"); back.id = "allsec";
      back.innerHTML = '<a href="#">← All sections</a>';
      document.getElementById("sections").before(back);
    }
    if (back) back.hidden = !hit;
    if (hit) window.scrollTo(0, back.getBoundingClientRect().top + scrollY - 16);
  }
  if (!document.querySelector(".fsctl")) fetch("reader/reader.html", { cache: "no-cache" }).then(function (r) { return r.text(); }).then(function (h) {
    if (document.querySelector(".fsctl")) return;
    var box = document.createElement("div"); box.innerHTML = h;
    Array.prototype.slice.call(box.childNodes).forEach(function (nd) {
      if (nd.tagName === "SCRIPT") { var s = document.createElement("script"); s.textContent = nd.textContent; document.body.appendChild(s); }
      else document.body.appendChild(nd);
    });
  });
})();
(function () { var s = document.createElement("script"); s.src = "lib/offline.js"; document.body.appendChild(s); })();
