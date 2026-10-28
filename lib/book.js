/* Study booklet viewer. Each booklet folder has book.json and notes/<lang>/*.md.
   Pages are the notes word for word (already stripped of personal details before publishing). */
(function () {
  var B = null, LANGS = [], idx = {}, order = {};
  var UI = {
    en: { contents: "Contents", prev: "← Previous", next: "Next →", index: "↑ Index", start: "Start here", other: "Español", loading: "Loading…", of: "of", section: "Section" },
    es: { contents: "Contenido", prev: "← Anterior", next: "Siguiente →", index: "↑ Índice", start: "Empieza aquí", other: "English", loading: "Cargando…", of: "de", section: "Sección" }
  };
  function norm(s) { return String(s || "").toLowerCase().replace(/[^a-z0-9áéíóúñü]/g, ""); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function t(o, l) { return typeof o === "string" ? o : (o && (o[l] || o.en)) || ""; }
  function el(id) { return document.getElementById(id); }

  function route() {
    var h = (location.hash || "").replace(/^#/, "").split("/");
    if (h.length === 1 && h[0] && LANGS.indexOf(h[0]) < 0 && order[LANGS[0]] && order[LANGS[0]].some(function (n) { return n.id === h[0]; })) h = [LANGS[0], h[0]];
    var l = LANGS.indexOf(h[0]) > -1 ? h[0] : (localStorage_get("lang") || LANGS[0]);
    if (LANGS.indexOf(l) < 0) l = LANGS[0];
    return { lang: l, id: h[1] || "", sec: h[2] || "" };
  }
  function localStorage_get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function localStorage_set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  function langLink(r) {
    if (LANGS.length < 2) return "";
    var NAME = { en: "English", es: "Español" };
    return '<span class="langs" role="group" aria-label="Language">' + LANGS.map(function (l) {
      return l === r.lang ? '<span class="on" aria-current="true">' + NAME[l] + "</span>"
        : '<a href="#' + l + "/" + r.id + '" lang="' + l + '">' + NAME[l] + "</a>";
    }).join("") + "</span>";
  }

  function home(r) {
    var l = r.lang, first = order[l][0];
    var cards = B.sections.map(function (s, i) {
      var lis = s.notes.filter(function (n) { return n[l]; }).map(function (n) {
        return '<li><a href="#' + l + "/" + n.id + '">' + esc(n[l].title) + "</a></li>";
      }).join("");
      return '<section class="seccard c' + (i % 4) + '"><div class="eyebrow">' + UI[l].section + " " + (i + 1) + "</div><h2>" + esc(t(s.title, l)) + "</h2><ol>" + lis + "</ol></section>";
    }).join("");
    document.title = t(B.title, l);
    return '<div class="crumbs"><a href="../">↑ Library</a>' + langLink(r) + '</div>' +
      '<header class="hero"><div class="eyebrow">' + esc(t(B.eyebrow, l)) + "</div><h1>" + t(B.titleHtml || B.title, l) + '</h1><p class="lede">' + esc(t(B.lede, l)) + "</p>" +
      (first ? '<p style="margin-top:18px"><a href="#' + l + "/" + first.id + '"><b>' + UI[l].start + ": " + esc(first[l].title) + " →</b></a></p>" : "") + "</header>" +
      '<div class="secgrid">' + cards + "</div>";
  }

  function render(md, l) {
    md = md.replace(/^---\n[\s\S]*?\n---\n/, "");
    md = md.replace(/^# .*\n/m, "");
    md = md.replace(/\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]+))?\]\]/g, function (m, target, alias) {
      var id = idx[l][norm(target)], label = alias || target;
      return id ? "[" + label + "](#" + l + "/" + id + ")" : label;
    });
    var html = window.marked.parse(md, { gfm: true, breaks: true });
    var parts = html.split(/(?=<h2[\s>])/), out = "";
    parts.forEach(function (p, i) {
      p = p.replace(/<hr\s*\/?>\s*$/, "");
      if (!p.trim() || /^(\s*<hr\s*\/?>\s*)*$/.test(p)) return;
      if (i === 0 && !/^<h2/.test(p)) out += '<section class="card intro">' + p + "</section>";
      else out += '<section class="card c' + ((i - (/^<h2/.test(parts[0]) ? 0 : 1)) % 4) + '">' + p + "</section>";
    });
    return out;
  }

  function page(r) {
    var l = r.lang, list = order[l], k = list.findIndex(function (n) { return n.id === r.id; });
    if (k < 0) return null;
    var n = list[k], sec = n._sec, s = B.sections[sec];
    var inSec = s.notes.filter(function (x) { return x[l]; }), pos = inSec.indexOf(n) + 1;
    var prev = k ? list[k - 1] : null, next = list[k + 1] || null;
    function a(x, cls, key) { return x ? '<a class="' + cls + '" href="#' + l + "/" + x.id + '"><span class="k">' + key + '</span><span class="t">' + esc(x[l].title) + "</span></a>" : '<span class="empty"></span>'; }
    document.title = n[l].title + " · " + t(B.title, l);
    var shell = '<div class="crumbs sticky"><i class="prog" id="prog"></i><a href="#' + l + '/">↑ ' + esc(t(B.title, l)) + '</a><span class="sep">/</span><span class="here">' + esc(t(s.title, l)) + " · " + pos + " " + UI[l].of + " " + inSec.length + "</span>" + '<button class="tocbtn" id="tocbtn" type="button" aria-label="' + UI[l].contents + '">☰<span class="lbl"> ' + UI[l].contents + "</span></button>" + langLink(r) + "</div>" +
      '<div class="layout"><aside class="toc" id="toc"></aside><article class="note"><div class="eyebrow">' + esc(t(B.title, l)) + " · " + esc(n.id.toUpperCase()) + " · " + esc(t(s.title, l)) + '</div><h1 class="nt">' + esc(n[l].title) + '</h1><div id="body" class="loading">' + UI[l].loading + "</div></article></div>" +
      '<nav class="pager">' + (prev ? a(prev, "", UI[l].prev) : '<a href="#' + l + '/"><span class="k">' + UI[l].prev + '</span><span class="t">' + UI[l].contents + "</span></a>") +
      '<a class="idx" href="#' + l + '/"><span class="k">' + UI[l].index + '</span><span class="t">' + UI[l].contents + "</span></a>" + a(next, "next", UI[l].next) + "</nav>";
    setTimeout(function () {
      fetch("notes/" + n[l].file, { cache: "no-cache" }).then(function (x) { return x.text(); }).then(function (md) {
        var b = el("body"); if (!b) return; b.className = ""; b.innerHTML = render(md, l); buildToc(l, r); if (r.sec) goSec(r.sec);
      }).catch(function () { var b = el("body"); if (b) b.textContent = "Could not load this note."; });
    }, 0);
    return shell;
  }

  /* section links: every section heading gets an address (#lang/note/section) and a share button */
  var SHARE = { en: { label: "Share this section", copied: "Link copied" }, es: { label: "Compartir esta sección", copied: "Enlace copiado" } };
  var ICON = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M10 14a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1M14 10a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/></svg>';
  function slug(s) { return String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 60) || "s"; }
  function goSec(s) {
    var t = el("sec-" + s); if (!t) return;
    window.scrollTo({ top: t.getBoundingClientRect().top + scrollY - 90 });
    var c = t.closest(".card"); if (c) { c.classList.add("flash"); setTimeout(function () { c.classList.remove("flash"); }, 1600); }
  }
  function toast(msg) {
    var d = document.createElement("div"); d.className = "toast"; d.textContent = msg; document.body.appendChild(d);
    setTimeout(function () { d.remove(); }, 1800);
  }
  function buildToc(l, r) {
    var toc = el("toc"), hs = document.querySelectorAll("#body h2"); if (!toc) return;
    var html = '<div class="eyebrow">' + UI[l].contents + "</div><ol>", used = {};
    var S = SHARE[l] || SHARE.en;
    hs.forEach(function (h) {
      var txt = h.textContent, id = slug(txt), k = id, j = 2;
      while (used[k]) k = id + "-" + j++;
      used[k] = 1; h.id = "sec-" + k;
      html += '<li><a href="#' + l + "/" + r.id + "/" + k + '" data-s="' + k + '">' + esc(txt) + "</a></li>";
      h.insertAdjacentHTML("beforeend", '<button class="shr" type="button" data-s="' + k + '" aria-label="' + S.label + '" title="' + S.label + '">' + ICON + "</button>");
    });
    toc.innerHTML = html + "</ol>";
    toc.onclick = function (e) { var a = e.target.closest("a"); if (!a) return; e.preventDefault(); history.replaceState(null, "", a.getAttribute("href")); goSec(a.dataset.s); toc.classList.remove("open"); };
    el("body").onclick = function (e) {
      var b = e.target.closest(".shr"); if (!b) return;
      var url = location.href.split("#")[0] + "#" + l + "/" + r.id + "/" + b.dataset.s;
      var h = el("sec-" + b.dataset.s), title = (h ? h.textContent : "") + " · " + document.title;
      history.replaceState(null, "", "#" + l + "/" + r.id + "/" + b.dataset.s);
      if (navigator.share) navigator.share({ title: title, url: url }).catch(function () {});
      else if (navigator.clipboard) navigator.clipboard.writeText(url).then(function () { toast(S.copied); }, function () { prompt("", url); });
      else prompt("", url);
    };
    var btn = el("tocbtn"); if (btn) btn.onclick = function () { toc.classList.toggle("open"); };
    var links = toc.querySelectorAll("a");
    function spy() {
      var cur = 0; hs.forEach(function (h, i) { if (h.getBoundingClientRect().top < 140) cur = i; });
      links.forEach(function (a, i) { a.classList.toggle("on", i === cur); });
      var p = el("prog"), d = document.documentElement; if (p) p.style.width = Math.min(100, scrollY / Math.max(1, d.scrollHeight - innerHeight) * 100) + "%";
    }
    window.onscroll = spy; spy();
  }

  function show() {
    var r = route();
    if (show.cur && r.id && show.cur.lang === r.lang && show.cur.id === r.id) { show.cur = r; if (r.sec) goSec(r.sec); return; }
    show.cur = r; localStorage_set("lang", r.lang);
    document.documentElement.lang = r.lang;
    var v = el("view"), h = (r.id && page(r)) || home(r);
    v.innerHTML = h; window.scrollTo(0, 0);
  }

  function addReader() {
    if (document.querySelector(".fsctl")) return;
    fetch("../reader/reader.html", { cache: "no-cache" }).then(function (x) { return x.text(); }).then(function (h) {
      var box = document.createElement("div"); box.innerHTML = h;
      Array.prototype.slice.call(box.childNodes).forEach(function (nd) {
        if (nd.tagName === "SCRIPT") { var s = document.createElement("script"); s.textContent = nd.textContent; document.body.appendChild(s); }
        else document.body.appendChild(nd);
      });
    }).catch(function () {});
  }

  fetch("book.json", { cache: "no-cache" }).then(function (x) { return x.json(); }).then(function (b) {
    B = b; LANGS = b.langs || ["en"];
    LANGS.forEach(function (l) { idx[l] = {}; order[l] = []; });
    b.sections.forEach(function (s, si) {
      s.notes.forEach(function (n) {
        n._sec = si;
        LANGS.forEach(function (l) {
          if (!n[l]) return;
          order[l].push(n);
          [n[l].title, n[l].h1, n[l].file.replace(/^.*\//, "").replace(/\.md$/, "")].concat(n[l].aka || []).forEach(function (k) { if (k) idx[l][norm(k)] = n.id; });
        });
      });
    });
    show(); addReader();
    window.addEventListener("hashchange", show);
  });
})();
