/* Reading themes trial — remembers choice in localStorage "theme2" / "theme2obs" */
(function(){
 var r=document.documentElement,T={sepia:"Sepia",dark:"Dark",clean:"Clean",obs:"Obsidian"},K="theme2";
 function get(k,d){try{return localStorage.getItem(k)||d}catch(e){return d}}function put(k,v){try{localStorage.setItem(k,v)}catch(e){}}
 var bar=document.createElement("div");bar.className="skinbar thembar";bar.setAttribute("role","group");bar.setAttribute("aria-label","Theme");
 bar.innerHTML='<span class="seg">'+Object.keys(T).map(function(k){return '<button type="button" data-k="'+k+'" aria-pressed="false">'+T[k]+"</button>"}).join("")+'</span><button type="button" class="mode" aria-label="Obsidian light or dark" hidden></button>';
 var mode=bar.querySelector(".mode");
 function set(k){if(!T[k])k="sepia";r.setAttribute("data-skin",k);var od=get(K+"obs","light");r.setAttribute("data-obs",od);
  r.setAttribute("data-theme",k==="dark"||(k==="obs"&&od==="dark")?"dark":"light");
  bar.querySelectorAll(".seg button").forEach(function(b){b.setAttribute("aria-pressed",String(b.dataset.k===k))});
  mode.hidden=k!=="obs";mode.textContent=od==="dark"?"☾ Dark":"☀ Light";put(K,k);vault()}
 bar.addEventListener("click",function(e){var b=e.target.closest("button");if(!b)return;if(b===mode){put(K+"obs",get(K+"obs","light")==="dark"?"light":"dark");set("obs")}else set(b.dataset.k)});
 var w=document.querySelector(".wrap");(w?w.parentNode:document.body).insertBefore(bar,w||document.body.firstChild);
 /* Obsidian-style file explorer: every note in the book, grouped by section */
 var B=null,side=document.createElement("nav");side.className="vault";side.setAttribute("aria-label","Notes");document.body.appendChild(side);
 function t(o,l){return typeof o==="string"?o:(o&&(o[l]||o.en))||""}
 function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
 function vault(){if(!B||r.getAttribute("data-skin")!=="obs")return;var h=(location.hash||"").replace(/^#/,"").split("/"),l=(B.langs||["en"]).indexOf(h[0])>-1?h[0]:(get("lang","en")),id=h[1]||"";
  side.innerHTML='<div class="vh">'+esc(t(B.title,l))+"</div>"+B.sections.map(function(s){return "<details open><summary>"+esc(t(s.title,l))+"</summary>"+s.notes.filter(function(n){return n[l]}).map(function(n){return '<a href="#'+l+"/"+n.id+'"'+(n.id===id?' class="on"':"")+">"+esc(n[l].title)+"</a>"}).join("")+"</details>"}).join("")}
 fetch("book.json",{cache:"no-cache"}).then(function(x){return x.json()}).then(function(b){B=b;vault()}).catch(function(){});
 window.addEventListener("hashchange",vault);
 set(get(K,"sepia"));
})();
