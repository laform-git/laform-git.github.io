/* Library index: builds the cards from sites.json so a new booklet is one small edit. */
(function () {
  function esc(s) { return String(s || "").replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  var st = document.createElement("style"); st.textContent = ".site .l{font:500 11px/1.2 var(--mono,monospace);letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}.sec .banner{display:flex;align-items:center;gap:10px;margin:8px 0 16px;padding:10px 16px;border-radius:10px;background:var(--sc);color:#fff;font:800 15px/1 var(--display,system-ui);letter-spacing:.14em;text-transform:uppercase}.sec .banner small{margin-left:auto;font:500 12px/1 var(--mono,monospace);letter-spacing:.08em;opacity:.85}.sec .site{border-left-color:var(--sc)}.sec .site .u{color:var(--sc)}.sec .banner .secname{color:inherit;text-decoration:none}.sec .banner .shr{display:inline-flex;align-items:center;justify-content:center;width:30px;height:30px;margin-left:6px;padding:0;border:0;border-radius:50%;background:transparent;color:#fff;opacity:.8;cursor:pointer}.sec .banner .shr:hover{opacity:1;background:rgba(255,255,255,.18)}.sec[hidden]{display:none}#allsec{margin:0 0 14px;font:600 15px/1.2 var(--display,system-ui)}#allsec a{color:var(--accent);text-decoration:none}#allsec[hidden]{display:none}"; document.head.appendChild(st);
st.textContent += [
 ".brand h1 span{background:linear-gradient(90deg,#c0812a,#2f9a7a,#9256bd,#3f74c0);-webkit-background-clip:text;background-clip:text;color:transparent}",
 ".brand .wel{margin:10px 0 0;font:500 clamp(17px,2.4vw,20px)/1.4 var(--display,system-ui);color:var(--muted)}",
 "#libtools{margin:22px 0 6px}",
 "#libq{width:100%;font:500 17px/1.2 var(--display,system-ui);color:var(--ink);background:var(--surface);border:1.5px solid var(--rule);border-radius:14px;padding:14px 16px 14px 44px;outline:none;-webkit-appearance:none;appearance:none;background-image:url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23999' stroke-width='2.4' stroke-linecap='round'%3E%3Ccircle cx='11' cy='11' r='7'/%3E%3Cpath d='M20 20l-3.5-3.5'/%3E%3C/svg%3E\");background-repeat:no-repeat;background-position:15px center}",
 "#libq:focus{border-color:var(--accent)}",
 ".chips{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0 4px}",
 ".chips a{display:inline-flex;align-items:center;gap:7px;font:700 14px/1 var(--display,system-ui);padding:10px 15px;min-height:40px;border-radius:999px;background:var(--surface);border:1.5px solid var(--rule);color:var(--ink);text-decoration:none}",
 ".chips a i{width:9px;height:9px;border-radius:50%;background:var(--c)}",
 ".chips a.on{background:var(--ink);border-color:var(--ink);color:var(--bg)}",
 ".sec .banner{background:none!important;color:var(--ink)!important;padding:0!important;margin:10px 0 14px!important;font:800 14px/1 var(--display,system-ui)!important;letter-spacing:.14em}",
 ".sec .banner:before{content:'';width:11px;height:11px;border-radius:3px;background:var(--sc);flex:none}",
 ".sec .banner small{margin-left:0!important;color:var(--muted);opacity:1!important}",
 ".sec .banner .shr{color:var(--muted)!important;margin-left:auto!important}",
 ".sec .site{flex-direction:row!important;align-items:flex-start;gap:14px!important;border:1.5px solid var(--rule)!important;border-radius:16px!important;padding:14px!important;box-shadow:0 1px 2px rgba(0,0,0,.04)}",
 ".sec .site:hover,.sec .site:focus-visible{border-color:var(--sc)!important}",
 ".sec .site .tx{display:flex;flex-direction:column;gap:4px;min-width:0}",
 ".sec .site .s{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}",
 ".etile{position:relative;flex:none;width:64px;height:64px;border-radius:12px;color:#fff;background:linear-gradient(180deg,var(--ta),var(--tb));box-shadow:0 1px 3px rgba(0,0,0,.18)}",
 ".etile i{position:absolute;inset:6px;border:2px solid #fff}",
 ".etile b{position:absolute;left:12px;bottom:13px;font:700 26px/1 -apple-system,'Helvetica Neue',Arial,sans-serif;letter-spacing:-.8px}",
 ".etile em{position:absolute;top:10px;right:11px;font:600 10px/1 -apple-system,'Helvetica Neue',Arial,sans-serif;font-style:normal}",
 ".sec .site[hidden],#noresult[hidden]{display:none!important}",
 "#noresult{color:var(--muted);font:500 16px/1.4 var(--display,system-ui);padding:16px 0}"
].join("");
  var ICON = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M10 14a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1M14 10a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/></svg>';
  function slug(x) { return String(x).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, ""); }
  function toast(m) { var d = document.createElement("div"); d.textContent = m; d.style.cssText = "position:fixed;left:50%;bottom:90px;transform:translateX(-50%);background:#222;color:#fff;font:600 14px/1 system-ui,sans-serif;padding:10px 16px;border-radius:999px;z-index:99"; document.body.appendChild(d); setTimeout(function () { d.remove(); }, 1800); }
  var COL = { Faith: "#b8741a", Health: "#2f8f74", Mindforge: "#8a4fb0", Mirabilia: "#b8487a", Tech: "#3b6fb6" };
  var order = ["Faith", "Health", "Mindforge", "Mirabilia", "Tech"];
  var TILE = { Faith: ["#d39a48", "#8a5512"], Health: ["#4fb393", "#1f6b55"], Mindforge: ["#a873cc", "#62307f"], Mirabilia: ["#d77aa3", "#8f3561"], Tech: ["#6a95d4", "#28508a"] };
  function tile(x) { var c = TILE[x.section] || ["#8a8f98", "#4b5059"]; return x.sym ? '<span class="etile" style="--ta:' + c[0] + ";--tb:" + c[1] + '" aria-hidden="true"><i></i>' + (x.num ? "<em>" + (x.num < 10 ? "0" : "") + x.num + "</em>" : "") + "<b>" + esc(x.sym) + "</b></span>" : ""; }
  /* English / Español switch: also sets the language every booklet opens in */
  var SEC_ES = { Faith: "Fe", Health: "Salud", Mindforge: "Ideas y cultura", Mirabilia: "Mirabilia", Tech: "Tecnología" };
  var TXT = { en: { dir: "Directory", pub: "published", h1: 'Study <span>Library</span>', foot: "Study notes, published from a personal library.", wel: "Welcome to my personal notes, kept short.", q: "Search every series…", allc: "All", none: "Nothing found.", all: "← All sections", copied: "Link copied", share: "Share this section", open: "Open" },
              es: { dir: "Directorio", pub: "publicados", h1: 'Notas <span>de estudio</span>', foot: "Notas de estudio, publicadas desde una colección personal.", wel: "¡Bienvenido! Colección de notas personales en forma breve.", q: "Buscar en todas las series…", allc: "Todas", none: "No se encontró nada.", all: "← Todas las secciones", copied: "Enlace copiado", share: "Compartir esta sección", open: "Abrir" } };
  var LANG = "en"; try { LANG = localStorage.getItem("lang") === "es" ? "es" : "en"; } catch (e) {}
  var LIST = null;
  var sw = document.createElement("div"); sw.id = "libsw"; sw.setAttribute("role", "group"); sw.setAttribute("aria-label", "Language");
  st.textContent += "#libsw{display:inline-flex;border:2px solid var(--accent,#a8620f);border-radius:999px;overflow:hidden;margin:0 0 14px;font:700 15px/1 var(--display,system-ui)}#libsw button{font:inherit;border:0;padding:9px 18px;min-height:40px;cursor:pointer;background:var(--surface,#fff);color:var(--accent,#a8620f)}#libsw button[aria-pressed=true]{background:var(--accent,#a8620f);color:var(--surface,#fff)}";
  [["en", "English"], ["es", "Español"]].forEach(function (o) { var b = document.createElement("button"); b.type = "button"; b.textContent = o[1]; b.lang = o[0]; b.onclick = function () { setLang(o[0]); }; sw.appendChild(b); });
  var secEl = document.getElementById("sections"); secEl.parentNode.insertBefore(sw, secEl);
  function setLang(l) { LANG = l; try { localStorage.setItem("lang", l); } catch (e) {} render(); }
  function T(x, k) { return LANG === "es" && x[k + "_es"] ? x[k + "_es"] : x[k]; }
  function href(x) { if (LANG === "es") return x.path_es || x.path; return x.path_es && /#es\/$/.test(x.path_es) ? x.path + "#en/" : x.path; }
  fetch("sites.json", { cache: "no-cache" }).then(function (r) { return r.json(); }).then(function (list) { LIST = list; render(); });
  function render() {
    var list = LIST; if (!list) return; var tx = TXT[LANG];
    document.documentElement.lang = LANG;
    sw.querySelectorAll("button").forEach(function (b) { b.setAttribute("aria-pressed", String(b.lang === LANG)); });
    var h1 = document.querySelector(".brand h1"); if (h1) h1.innerHTML = tx.h1;
    var ey = document.querySelector(".brand .eyebrow"); if (ey) ey.innerHTML = tx.dir + ' · <span id="count"></span> ' + tx.pub;
    var ft = document.querySelector("footer"); if (ft) ft.textContent = tx.foot;
    var ab = document.getElementById("allsec"); if (ab) ab.innerHTML = '<a href="#">' + tx.all + "</a>";
    var live = list.filter(function (x) { return x.status !== "Pulled"; }), secs = {};
    live.forEach(function (x) { (secs[x.section] = secs[x.section] || []).push(x); });
    var keys = Object.keys(secs).sort(function (a, b) { var i = order.indexOf(a), j = order.indexOf(b); return (i < 0 ? 99 : i) - (j < 0 ? 99 : j) || a.localeCompare(b); });
    document.getElementById("count").textContent = live.length;
    document.getElementById("sections").innerHTML = keys.map(function (k) {
      var sl = slug(k);
      var kn = LANG === "es" ? (SEC_ES[k] || k) : k;
      return '<section class="sec" id="' + sl + '" style="--sc:' + (COL[k] || "#6b6862") + '"><h2 class="banner"><a class="secname" href="#' + sl + '">' + esc(kn) + '</a><button class="shr" type="button" data-s="' + sl + '" aria-label="' + esc(tx.share) + '" title="' + esc(tx.share) + '">' + ICON + '</button><small>' + secs[k].length + '</small></h2><div class="grid">' + secs[k].map(function (x) {
        var lab = T(x, "label"), bl = T(x, "blurb");
        var hay = [x.name, x.name_es, x.blurb, x.blurb_es, x.label, x.label_es, x.section, SEC_ES[x.section]].join(" ").toLowerCase();
        return '<a class="site" href="' + esc(href(x)) + '" data-q="' + esc(hay) + '">' + tile(x) + '<span class="tx">' + (lab ? '<span class="l">' + esc(lab) + '</span>' : '') + '<span class="t">' + esc(T(x, "name")) + "</span>" + (bl ? '<span class="s">' + esc(bl) + "</span>" : "") + '<span class="u">' + esc(x.langs || tx.open) + " →</span></span></a>";
      }).join("") + "</div></section>";
    }).join("");
    tools(keys, tx);
    filter();
  }
  function tools(keys, tx) {
    var h1 = document.querySelector(".brand h1");
    if (h1) { var w = document.querySelector(".brand .wel"); if (!w) { w = document.createElement("p"); w.className = "wel"; h1.parentNode.insertBefore(w, h1.nextSibling); } w.textContent = tx.wel; }
    var box = document.getElementById("libtools");
    if (!box) { box = document.createElement("div"); box.id = "libtools"; secEl.parentNode.insertBefore(box, secEl); box.innerHTML = '<input id="libq" type="search" autocomplete="off" enterkeyhint="search"><nav class="chips"></nav>'; el("libq").addEventListener("input", search); }
    var q = el("libq"); q.placeholder = tx.q; q.setAttribute("aria-label", tx.q);
    box.querySelector(".chips").innerHTML = '<a href="#" data-s="">' + esc(tx.allc) + "</a>" + keys.map(function (k) { return '<a href="#' + slug(k) + '" data-s="' + slug(k) + '" style="--c:' + (COL[k] || "#888") + '"><i></i>' + esc(LANG === "es" ? (SEC_ES[k] || k) : k) + "</a>"; }).join("");
    if (q.value) search();
  }
  function el(id) { return document.getElementById(id); }
  function search() {
    var v = (el("libq").value || "").trim().toLowerCase(), any = false;
    if (v && location.hash) history.replaceState(null, "", location.pathname + location.search);
    document.querySelectorAll("#sections .sec").forEach(function (sec) {
      var n = 0; sec.querySelectorAll(".site").forEach(function (a) { var ok = !v || a.dataset.q.indexOf(v) > -1; a.hidden = !ok; if (ok) n++; });
      sec.hidden = v ? n === 0 : false; if (n) any = true;
    });
    var nr = el("noresult"); if (!nr) { nr = document.createElement("p"); nr.id = "noresult"; secEl.parentNode.insertBefore(nr, secEl); }
    nr.textContent = TXT[LANG].none; nr.hidden = !v || any;
    if (!v) filter(); else markChips("");
  }
  function markChips(h) { document.querySelectorAll(".chips a").forEach(function (a) { a.classList.toggle("on", a.dataset.s === h); }); }
  window.addEventListener("hashchange", filter);
  document.getElementById("sections").onclick = function (e) {
      var bt = e.target.closest(".shr"); if (!bt) return;
      var url = location.href.split("#")[0] + "#" + bt.dataset.s, name = bt.parentNode.firstChild.textContent;
      if (navigator.share) navigator.share({ title: name + (LANG === "es" ? " · Notas de estudio" : " · Study Library"), url: url }).catch(function () {});
      else if (navigator.clipboard) navigator.clipboard.writeText(url).then(function () { toast(TXT[LANG].copied); }, function () { prompt("", url); });
      else prompt("", url);
    };
  /* a section link (#faith, #health…) shows only that section, with a way back to everything */
  function filter() {
    if (!LIST) return;
    var h = decodeURIComponent((location.hash || "").slice(1)), all = document.querySelectorAll("#sections .sec"), hit = false;
    all.forEach(function (s) { if (s.id === h) hit = true; });
    all.forEach(function (s) { s.hidden = hit && s.id !== h; });
    var back = document.getElementById("allsec");
    if (hit && !back) {
      back = document.createElement("p"); back.id = "allsec";
      back.innerHTML = '<a href="#">' + TXT[LANG].all + '</a>';
      document.getElementById("sections").before(back);
    }
    if (back) back.hidden = !hit;
    markChips(hit ? h : "");
    if (back) back.hidden = true;
    if (hit) { var tb = el("libtools"); if (tb) window.scrollTo(0, tb.getBoundingClientRect().top + scrollY - 12); }
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
