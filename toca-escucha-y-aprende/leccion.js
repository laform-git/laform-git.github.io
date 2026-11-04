/* Toca, escucha y aprende: motor de las lecciones de ella.
   Cada lección define window.LECCION (ver leccion-N.html). Se muestra una pantalla a la vez;
   al cambiar de pantalla el foco va al texto, para que VoiceOver lo lea solo.
   Nivel a: un botón gigante. Nivel b: Atrás y Siguiente. Nivel c: menú de burbujas, Atrás, Siguiente y Menú. */
(function(){
  var L=window.LECCION, app=document.getElementById('app');
  document.body.classList.add('nivel-'+L.nivel);
  var C=L.nivel==='c';

  // Lista plana de pantallas. Cada una sabe a qué sección pertenece.
  var list=[];
  list.push({t:'inicio',text:L.intro});
  L.secciones.forEach(function(s,si){
    var qn=0, total=s.pantallas.filter(function(p){return p.t==='pregunta'||p.t==='busca'}).length;
    s.pantallas.forEach(function(p,k){
      var o=Object.assign({},p); o.sec=si; o.k=k+1; o.n=s.pantallas.length; o.secName=s.nombre;
      if(p.t==='pregunta'||p.t==='busca'){ qn++; o.qn=qn; o.qt=total; }
      list.push(o);
    });
  });
  list.push({t:'fin'});
  var FIN=list.length-1, done={}, stars=0;

  function el(tag,attrs,text){ var e=document.createElement(tag); for(var a in attrs){ if(a==='class') e.className=attrs[a]; else e.setAttribute(a,attrs[a]); } if(text!=null) e.textContent=text; return e; }
  function btn(label,cls,fn){ var b=el('button',{type:'button','class':cls||''},label); b.addEventListener('click',fn); return b; }
  function link(label,href,cls){ return el('a',{href:href,'class':cls||''},label); }
  function first(si){ for(var i=0;i<list.length;i++) if(list[i].sec===si) return i; return 1; }
  function lastOf(si){ var r=-1; for(var i=0;i<list.length;i++) if(list[i].sec===si) r=i; return r; }

  function go(route){ var h='#'+route; if(location.hash===h) render(route); else location.hash=route; }
  window.addEventListener('hashchange',function(){ render(location.hash.slice(1)); });

  function render(route){
    app.innerHTML='';
    var screen=el('section',{'class':'screen'}), top=el('p',{'class':'top'}), body=el('div',{'class':'body'}), bar=el('div',{'class':'bar'});
    screen.appendChild(top); screen.appendChild(body); screen.appendChild(bar); app.appendChild(screen);
    var focusEl=null;

    // Menú de burbujas (solo nivel c)
    if(C && (route==='menu' || route==='')){
      var h=el('h1',{tabindex:'-1'},'Lección '+L.num+': '+L.titulo); body.appendChild(h);
      body.appendChild(el('p',{'class':'txt',style:'font-size:clamp(20px,5vw,24px);color:var(--muted);margin-bottom:8px'},L.intro));
      var bub=el('div',{'class':'bubbles'});
      L.secciones.forEach(function(s,si){
        var b=btn('', 'bubble', function(){ go('p'+first(si)); });
        b.appendChild(el('span',{'class':'n','aria-hidden':'true'},String(si+1))); b.appendChild(document.createTextNode(s.nombre));
        bub.appendChild(b);
      });
      body.appendChild(bub);
      bar.appendChild(link('Todas las lecciones','./','home'));
      return focus(h);
    }

    var i=parseInt((/^p(\d+)$/.exec(route)||[])[1],10);
    if(isNaN(i)||i<0||i>=list.length) i=0;
    if(C && i===0 && route!=='p0'){ return render('menu'); }
    var p=list[i];

    // Texto de arriba: dónde va
    if(p.t==='pregunta'||p.t==='busca') top.textContent='Pregunta '+p.qn+' de '+p.qt;
    else if(p.t==='mision') top.textContent='Misión '+p.k+' de '+p.n;
    else if(p.sec!=null) top.textContent=p.secName+(p.n>1?' · '+p.k+' de '+p.n:'');
    else top.textContent='Lección '+L.num;

    if(p.t==='inicio'){
      var h1=el('h1',{tabindex:'-1'},'Lección '+L.num+': '+L.titulo); body.appendChild(h1);
      body.appendChild(el('p',{'class':'txt'},p.text));
      focusEl=h1;
    } else if(p.t==='fin'){
      var hf=el('h2',{},'¡Terminaste!'); body.appendChild(hf);
      var ft=el('p',{'class':'txt',tabindex:'-1'},'Terminaste la lección '+L.num+'. '+(stars?'Ganaste '+stars+(stars===1?' estrella. ':' estrellas. '):'')+(L.despedida||''));
      body.appendChild(ft); focusEl=ft;
    } else {
      if(p.k===1 || p.t!=='texto') body.appendChild(el('h2',{},p.titulo||p.secName));
      var t=el('p',{'class':'txt',tabindex:'-1'},p.text); body.appendChild(t); focusEl=t;
    }

    // Preguntas y juegos
    var fb=el('p',{'class':'fb',tabindex:'-1',role:'status'}), st=el('p',{'class':'stars','aria-hidden':'true'});
    var answered=!!done[i];
    if(p.t==='pregunta'){
      var ch=el('div',{'class':'choices'});
      var ans=function(v){ if(done[i]) return; done[i]=true; var right=(v===p.ok); if(right) stars++;
        fb.className='fb '+(right?'good':'bad');
        fb.textContent=right?p.fb:'Casi. Es '+(p.ok?'cierto':'falso')+'. '+p.fb.replace(/^¡[^!]*!\s*/,'');
        ch.remove(); next.hidden=false; showStars(); focus(fb); };
      ch.appendChild(btn('Cierto','yes',function(){ans(true)})); ch.appendChild(btn('Falso','nope',function(){ans(false)}));
      if(!answered) body.appendChild(ch); else { fb.textContent='Ya contestaste esta pregunta.'; }
    }
    if(p.t==='busca'){
      var grid=el('div',{'class':'choices'+(p.opciones.length>4?' many':'')});
      p.opciones.forEach(function(o){
        grid.appendChild(btn(o,'pick',function(){
          if(o===p.correcta){ if(!done[i]){ done[i]=true; stars++; } this.classList.add('found'); fb.className='fb good'; fb.textContent='¡Lo encontraste! Ese es '+o+'.'; next.hidden=false; showStars(); focus(fb); }
          else { fb.className='fb bad'; fb.textContent='Ese es '+o+'. Sigue buscando.'; focus(fb); }
        }));
      });
      body.appendChild(grid);
    }
    body.appendChild(fb); body.appendChild(st);
    function showStars(){ st.textContent=stars?'⭐'.repeat(stars):''; }
    showStars();

    // Barra de abajo
    var backTo=null, nextTo=null, nextLabel='Siguiente';
    if(C){
      if(p.t==='fin'){ backTo='menu'; }
      else { backTo= i===first(p.sec) ? 'menu' : 'p'+(i-1); }
      if(p.t!=='fin'){
        if(i===lastOf(p.sec)){ if(p.sec===L.secciones.length-1){ nextTo='p'+FIN; } else { nextTo='menu'; nextLabel='Terminar'; } }
        else nextTo='p'+(i+1);
      }
    } else {
      if(i>0 && L.nivel==='b') backTo='p'+(i-1);
      if(p.t!=='fin') nextTo='p'+(i+1);
    }
    if(p.t==='inicio') nextLabel='Empezar';
    if(p.t==='mision') nextLabel='¡Lo logré!';

    var hasBack=!!backTo && p.t!=='inicio';
    if(hasBack){ bar.classList.add('two'); bar.appendChild(btn(backTo==='menu'&&C?'Menú':'Atrás','',function(){ go(backTo); })); }
    var next;
    if(p.t==='fin'){
      next=link(L.siguiente?L.siguiente.texto:'Todas las lecciones', L.siguiente?L.siguiente.href:'./','go');
      if(!hasBack) next.style.gridColumn='1/-1';
    } else {
      next=btn(nextLabel,'go',function(){ go(nextTo); });
      if((p.t==='pregunta'||p.t==='busca') && !done[i]) next.hidden=true;
    }
    bar.appendChild(next);
    if(C && p.t!=='fin' && route!=='menu') bar.appendChild(btn('Menú','home',function(){ go('menu'); }));
    if(C && hasBack && backTo==='menu'){ var hb=bar.querySelector('.home'); if(hb) hb.remove(); } // Atrás ya lleva al menú
    if(!C && p.t==='fin' && !hasBack) bar.classList.remove('two');
    focus(focusEl);
  }
  function focus(e){ if(e) setTimeout(function(){ e.focus(); },60); }

  render(location.hash.slice(1) || (C?'menu':'p0'));
})();
