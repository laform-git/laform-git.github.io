/* "Save for offline" for the whole Study Library (library home page). */
(function () {
  if (!("serviceWorker" in navigator) || !window.caches) return;
  navigator.serviceWorker.register("sw.js").catch(function () {});
  /* home-screen app: manifest, icon and app-mode tags */
  [["link", { rel: "manifest", href: "manifest.webmanifest" }],
   ["link", { rel: "apple-touch-icon", href: "data:image/png;base64,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" }],
   ["meta", { name: "apple-mobile-web-app-capable", content: "yes" }],
   ["meta", { name: "mobile-web-app-capable", content: "yes" }],
   ["meta", { name: "apple-mobile-web-app-title", content: "Library" }],
   ["meta", { name: "theme-color", content: "#f7ead3" }]].forEach(function (t) {
    var el = document.createElement(t[0]); for (var k in t[1]) el.setAttribute(k, t[1][k]); document.head.appendChild(el);
  });
  var CACHE = "study-library";
  var st = document.createElement("style");
  st.textContent = ".offbar{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin:6px 0 22px}.offbar button{font:700 15px/1 var(--display,system-ui);cursor:pointer;border:1.5px solid var(--accent);background:var(--accent);color:var(--surface);border-radius:999px;padding:11px 18px;min-height:44px}.offbar button[disabled]{opacity:.6;cursor:default}.offbar .msg{font:500 13px/1.3 var(--mono,monospace);color:var(--muted)}";
  document.head.appendChild(st);
  var bar = document.createElement("div"); bar.className = "offbar";
  bar.innerHTML = '<button type="button">⬇ Save library for offline</button><span class="msg" aria-live="polite"></span>';
  var btn = bar.querySelector("button"), msg = bar.querySelector(".msg");
  var anchor = document.getElementById("sections");
  if (!anchor) return;
  anchor.parentNode.insertBefore(bar, anchor);
  function fmt(b) { return b > 1048576 ? (b / 1048576).toFixed(1) + " MB" : Math.max(1, Math.round(b / 1024)) + " KB"; }
  function show() {
    var s = null; try { s = JSON.parse(localStorage.getItem("offlineSaved") || "null"); } catch (e) {}
    if (s) { btn.textContent = "↻ Update offline copy"; msg.textContent = "✓ Saved for offline · " + s.d + " · " + fmt(s.b) + " · " + s.n + " files"; }
    else msg.textContent = "Saves every booklet (English and Spanish) on this device.";
  }
  show();
  var base = new URL("./", location.href);
  function abs(p, from) { try { var u = new URL(p, from || base); u.hash = ""; return u.href; } catch (e) { return null; } }
  function sameOrigin(u) { return u && u.indexOf(base.origin) === 0; }
  function refs(html, from) {
    var out = [], re = /(?:href|src)\s*=\s*["']([^"'#]+)["']/g, m;
    while ((m = re.exec(html))) {
      var v = m[1];
      if (/^(data:|mailto:|javascript:)/.test(v)) continue;
      var u = abs(v, from); if (!u) continue;
      if (sameOrigin(u) || (/fonts\.googleapis\.com\/css|cdn\.jsdelivr\.net\/npm/.test(u))) out.push(u);
    }
    return out;
  }
  function getText(u) { return fetch(u, { cache: "no-cache" }).then(function (r) { return r.ok ? r.text() : ""; }).catch(function () { return ""; }); }
  btn.addEventListener("click", function () {
    btn.disabled = true; msg.textContent = "Finding files…";
    if (navigator.storage && navigator.storage.persist) navigator.storage.persist().catch(function () {});
    var urls = {};
    function add(u) { if (u) urls[u] = 1; }
    ["./", "index.html", "sites.json", "manifest.webmanifest", "lib/library.js", "lib/offline.js", "lib/icon.svg", "lib/book.js", "lib/book.css", "lib/themes.css", "lib/themes.js", "reader/reader.html"].forEach(function (p) { add(abs(p)); });
    getText(abs("index.html")).then(function (h) { refs(h, base).forEach(add); return fetch(abs("sites.json"), { cache: "no-cache" }); })
      .then(function (r) { return r.json(); })
      .then(function (list) {
        return Promise.all(list.filter(function (x) { return x.status !== "Pulled"; }).map(function (x) {
          var dir = abs(x.path); add(dir);
          return getText(dir).then(function (h) {
            var rs = refs(h, dir); rs.forEach(add);
            return fetch(abs("book.json", dir), { cache: "no-cache" }).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; }).then(function (b) {
              if (b) {
                add(abs("book.json", dir));
                b.sections.forEach(function (s) { s.notes.forEach(function (n) { (b.langs || ["en"]).forEach(function (l) { if (n[l] && n[l].file) add(abs("notes/" + n[l].file, dir)); }); }); });
                return;
              }
              /* plain HTML site (Claude Tips): its pages and what they load */
              var pages = rs.filter(function (u) { return sameOrigin(u) && /\.html$/.test(u) && u.indexOf(dir) === 0; });
              return Promise.all(pages.map(function (p) { return getText(p).then(function (t) { refs(t, p).forEach(add); }); }));
            });
          });
        }));
      })
      .then(function () {
        var css = Object.keys(urls).filter(function (u) { return /fonts\.googleapis\.com\/css/.test(u); });
        return Promise.all(css.map(function (u) { return getText(u).then(function (t) { var re = /url\((https:\/\/fonts\.gstatic\.com[^)]+)\)/g, m; while ((m = re.exec(t))) add(m[1]); }); }));
      })
      .then(function () {
        var all = Object.keys(urls), done = 0, bytes = 0, fail = 0, i = 0;
        return caches.open(CACHE).then(function (ca) {
          function next() {
            if (i >= all.length) return Promise.resolve();
            var u = all[i++];
            var opts = sameOrigin(u) ? { cache: "no-cache" } : { mode: "cors" };
            return fetch(u, opts).then(function (res) {
              if (!res.ok) { fail++; return; }
              return res.clone().blob().then(function (b) { bytes += b.size; return ca.put(u, res); });
            }).catch(function () { fail++; }).then(function () { done++; msg.textContent = "Saving " + done + " of " + all.length + "…"; return next(); });
          }
          return Promise.all([next(), next(), next(), next(), next(), next()]).then(function () { return { n: all.length - fail, b: bytes, fail: fail }; });
        });
      })
      .then(function (r) {
        var d = new Date().toLocaleDateString(undefined, { month: "short", day: "numeric" });
        try { localStorage.setItem("offlineSaved", JSON.stringify({ d: d, b: r.b, n: r.n })); } catch (e) {}
        btn.disabled = false; show();
        if (r.fail) msg.textContent += " (" + r.fail + " could not be saved — try again online)";
      })
      .catch(function () { btn.disabled = false; msg.textContent = "Could not save — check the connection and try again."; });
  });
})();
