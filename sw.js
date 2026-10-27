/* Study Library offline support: pages come from the network when online (and are saved),
   from the saved copy when offline. The "Save for offline" button fills the cache with everything. */
var CACHE = "study-library";
self.addEventListener("install", function () { self.skipWaiting(); });
self.addEventListener("activate", function (e) { e.waitUntil(self.clients.claim()); });
function key(req) { var u = new URL(req.url); u.hash = ""; u.search = ""; return u.href; }
self.addEventListener("fetch", function (e) {
  var r = e.request;
  if (r.method !== "GET") return;
  var u = new URL(r.url);
  if (u.origin === self.location.origin) {
    e.respondWith(
      fetch(r).then(function (res) {
        if (res && res.ok) { var c = res.clone(); caches.open(CACHE).then(function (ca) { ca.put(key(r), c); }); }
        return res;
      }).catch(function () {
        return caches.open(CACHE).then(function (ca) {
          return ca.match(key(r)).then(function (m) {
            if (m) return m;
            if (r.mode === "navigate") return ca.match(new URL(u.pathname.replace(/[^/]*$/, ""), u).href).then(function (d) { return d || ca.match(new URL("./", self.registration.scope).href); });
            return Response.error();
          });
        });
      })
    );
  } else if (/fonts\.googleapis\.com|fonts\.gstatic\.com|cdn\.jsdelivr\.net/.test(u.host)) {
    e.respondWith(
      caches.open(CACHE).then(function (ca) {
        return ca.match(r.url).then(function (m) {
          var net = fetch(r).then(function (res) { if (res && (res.ok || res.type === "opaque")) ca.put(r.url, res.clone()); return res; });
          return m || net;
        });
      })
    );
  }
});
