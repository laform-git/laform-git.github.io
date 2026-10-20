/* Library index: builds the cards from sites.json so a new booklet is one small edit. */
(function () {
  function esc(s) { return String(s || "").replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  var order = ["Faith", "Health", "Mindforge", "Mirabilia", "Tech"];
  fetch("sites.json", { cache: "no-cache" }).then(function (r) { return r.json(); }).then(function (list) {
    var live = list.filter(function (x) { return x.status !== "Pulled"; }), secs = {};
    live.forEach(function (x) { (secs[x.section] = secs[x.section] || []).push(x); });
    var keys = Object.keys(secs).sort(function (a, b) { var i = order.indexOf(a), j = order.indexOf(b); return (i < 0 ? 99 : i) - (j < 0 ? 99 : j) || a.localeCompare(b); });
    document.getElementById("count").textContent = live.length;
    document.getElementById("sections").innerHTML = keys.map(function (k) {
      return '<section class="sec"><h2>' + esc(k) + '</h2><div class="grid">' + secs[k].map(function (x) {
        return '<a class="site" href="' + esc(x.path) + '"><span class="t">' + esc(x.name) + "</span>" + (x.blurb ? '<span class="s">' + esc(x.blurb) + "</span>" : "") + '<span class="u">' + esc(x.langs || "Open") + " →</span></a>";
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
