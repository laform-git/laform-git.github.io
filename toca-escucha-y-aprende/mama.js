/* Toca, escucha y aprende: voz para las notas de mamá (una bocina por sección, Escuchar todo, menú de voces). */
(function(){
  var SPK='<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M3 9v6h4l5 4V5L7 9H3zm13.5 3A4.5 4.5 0 0 0 14 8v8a4.5 4.5 0 0 0 2.5-4zM14 3.2v2.1a7 7 0 0 1 0 13.4v2.1a9 9 0 0 0 0-17.6z"/></svg>';
  var synth=window.speechSynthesis, voices=[], chosen='', queue=[], playingAll=false, current=null;
  var calm=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var sel=document.getElementById('voz');
  try{chosen=localStorage.getItem('emva-voz')||''}catch(e){}
  function fill(){ if(!synth) return; var all=synth.getVoices(); if(!all.length) return;
    var es=all.filter(function(v){return /^es/i.test(v.lang)}), r=function(v){return /MX/i.test(v.lang)?0:/US/i.test(v.lang)?1:2};
    es.sort(function(a,b){return r(a)-r(b)||a.name.localeCompare(b.name)}); voices=es.length?es:all;
    sel.innerHTML='<option value="">Automática</option>';
    voices.forEach(function(v){var o=document.createElement('option');o.value=v.voiceURI;o.textContent=v.name+' ('+v.lang+')';sel.appendChild(o)});
    if(chosen&&voices.some(function(v){return v.voiceURI===chosen})) sel.value=chosen; }
  if(synth){ fill(); if('onvoiceschanged' in synth) synth.onvoiceschanged=fill; setTimeout(fill,500); }
  sel.addEventListener('change',function(){ chosen=sel.value; try{localStorage.setItem('emva-voz',chosen)}catch(e){} });
  function voice(){ if(chosen){var c=voices.find(function(v){return v.voiceURI===chosen}); if(c) return c;} return voices.find(function(v){return /es[-_]MX/i.test(v.lang)})||voices.find(function(v){return /^es/i.test(v.lang)})||null; }
  function text(el){ return Array.prototype.map.call(el.querySelectorAll('h2,p,li,dt,dd'),function(n){var t=n.textContent.replace(/\s+/g,' ').trim(); return /[.!?:]$/.test(t)?t:t+'.'}).join(' '); }
  function marks(){ document.querySelectorAll('.reading').forEach(function(e){e.classList.remove('reading')}); document.querySelectorAll('.spk.on').forEach(function(b){b.classList.remove('on')}); }
  function setAll(on){ document.getElementById('all').classList.toggle('playing',on); document.getElementById('all-i').textContent=on?'■':'▶'; document.getElementById('all-t').textContent=on?'Detener':'Escuchar todo'; }
  function stop(){ if(synth) synth.cancel(); queue=[]; playingAll=false; current=null; marks(); setAll(false); }
  function speak(t,el,done){ if(!synth){ if(done) done(); return; }
    var u=new SpeechSynthesisUtterance(t), v=voice(); u.lang=v?v.lang:'es-MX'; if(v) u.voice=v;
    u.onstart=function(){ marks(); if(el){ el.classList.add('reading'); el.querySelector('.spk').classList.add('on'); if(playingAll){ try{el.scrollIntoView({behavior:calm?'auto':'smooth',block:'start'})}catch(e){el.scrollIntoView()} } } };
    u.onend=function(){ if(el){ el.classList.remove('reading'); el.querySelector('.spk').classList.remove('on'); } if(done) done(); };
    synth.speak(u); }
  document.querySelectorAll('.say').forEach(function(el){
    var b=document.createElement('button'); b.type='button'; b.className='spk'; b.innerHTML=SPK;
    b.setAttribute('aria-label','Escuchar: '+el.querySelector('h2').textContent);
    b.addEventListener('click',function(){ var same=current===el; stop(); if(same) return; current=el; speak(text(el),el,function(){current=null}); });
    el.appendChild(b); });
  function next(){ if(!playingAll) return; var el=queue.shift(); if(!el){ stop(); return; } current=el; speak(text(el),el,next); }
  document.getElementById('all').addEventListener('click',function(){ if(playingAll){ stop(); return; } stop(); queue=Array.prototype.slice.call(document.querySelectorAll('.say')); playingAll=true; setAll(true); next(); });
  document.getElementById('probar').addEventListener('click',function(){ stop(); speak('Hola. Así suena esta voz.',null); });
})();
