/* Light/Dark option for Tech-section pages that were designed light-only.
   Shares the saved choice with Claude Tips (ct-theme) and the Library (skin).
   Usage: <script src="../lib/tech-theme.js" data-toggle="top|bottom|none" data-lang="es|en"></script> */
(function(){
  var s=document.currentScript,pos=(s&&s.dataset.toggle)||"top",es=((s&&s.dataset.lang)||document.documentElement.lang||"").indexOf("es")===0;
  var r=document.documentElement,K="ct-theme";
  function saved(){try{var sk=localStorage.getItem("skin");var v=localStorage.getItem(K);if(v)return v;if(sk==="thingsdark")return "dark"}catch(e){}return "light"}
  function meta(n,v){var m=document.querySelector('meta[name="'+n+'"]');if(!m){m=document.createElement("meta");m.name=n;document.head.appendChild(m)}m.content=v}
  var css=document.createElement("style");
  css.textContent='html{background:#fff}html.tt-dark{background:#151617}'+
   '@media (prefers-color-scheme:dark){html:not(.tt-dark){background:#fff}}'+
   'html.tt-dark body{filter:invert(.9) hue-rotate(180deg)}'+
   'html.tt-dark img,html.tt-dark video,html.tt-dark picture,html.tt-dark canvas{filter:invert(1) hue-rotate(180deg)}'+
   '.tt-bar{display:flex;justify-content:flex-end;gap:6px;margin:10px 0;font:600 14px/1 system-ui,sans-serif}'+
   '.tt-bar.bottom{justify-content:center;margin:28px 0 18px}'+
   '.tt-bar button{white-space:nowrap;cursor:pointer;border:1.5px solid #cbd5e1;background:#fff;color:#1f2937;border-radius:999px;padding:8px 14px;min-height:36px;font:inherit}'+
   '.tt-bar button[aria-pressed="true"]{display:none}.tt-bar button{border-color:#F97316;color:#c2410c;font-weight:800}';
  document.head.appendChild(css);
  function apply(d){r.classList.toggle("tt-dark",d);meta("color-scheme","light dark");r.style.colorScheme="light";meta("darkreader-lock","");meta("theme-color",d?"#151617":"#ffffff")}
  apply(saved()==="dark");
  function bar(){
    if(pos==="none"||document.querySelector(".tt-bar"))return;
    var d=document.createElement("div");d.className="tt-bar "+pos;d.setAttribute("role","group");d.setAttribute("aria-label",es?"Tema":"Theme");
    [["light",es?"☀ Claro":"☀ Light"],["dark",es?"☾ Oscuro":"☾ Dark"]].forEach(function(o){
      var b=document.createElement("button");b.type="button";b.textContent=o[1];b.setAttribute("aria-pressed",String(r.classList.contains("tt-dark")===(o[0]==="dark")));
      b.onclick=function(){apply(o[0]==="dark");try{localStorage.setItem(K,o[0]);localStorage.setItem("skin",o[0]==="dark"?"thingsdark":"things")}catch(e){}d.querySelectorAll("button").forEach(function(x){x.setAttribute("aria-pressed",String(x===b))})};
      d.appendChild(b)});
    var w=document.querySelector(".wrap")||document.querySelector("main")||document.body;
    var hb=document.querySelector(".homebar");if(pos!=="bottom"&&hb){d.style.margin="0 0 0 auto";hb.style.display="flex";hb.style.alignItems="center";hb.appendChild(d)}else if(pos==="bottom")w.appendChild(d);else w.insertBefore(d,w.firstChild);
  }
  if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",bar);else bar();
  window.addEventListener("pageshow",function(){var dk=saved()==="dark";apply(dk);document.querySelectorAll(".tt-bar button").forEach(function(x,i){x.setAttribute("aria-pressed",String((i===1)===dk))})});
})();
