import json, sys, html
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from contenido import LECCIONES as NIVEL1
from nivel2 import LECCIONES2, APPS
LECCIONES = NIVEL1 + LECCIONES2
NIVELES = [('Nivel 1 · Primeros pasos', NIVEL1), ('Nivel 2 · Apps, música y mensajes', LECCIONES2)]

OUT = sys.argv[1]
SERIE = "Toca, escucha y aprende"
FONT = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&display=swap">'
HEAD = '<!doctype html><html lang="es-MX"><head><meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
N = len(LECCIONES)

def leccion(L):
    n = L['num']
    data = {k: L[k] for k in ('num', 'titulo', 'nivel', 'intro', 'despedida')}
    data['secciones'] = L['secciones']
    data['siguiente'] = ({'texto': 'Siguiente lección', 'href': f'leccion-{n+1}.html'} if n < N
                         else {'texto': 'Todas las lecciones', 'href': './'})
    js = json.dumps(data, ensure_ascii=False, indent=1).replace('</', '<\\/')
    # Texto de respaldo si el script no carga
    nos = ''.join(f'<p>{html.escape(p["text"])}</p>' for s in L['secciones'] for p in s['pantallas'])
    return (HEAD + f'<title>Lección {n} · {SERIE}</title>\n{FONT}\n<link rel="stylesheet" href="estilo.css">\n<script src="../lib/tech-theme.js" data-toggle="top" data-lang="es"></script>\n</head><body>\n'
            f'<main id="app"></main>\n<noscript><div style="padding:20px;font-size:24px"><h1>Lección {n}: {html.escape(L["titulo"])}</h1>{nos}</div></noscript>\n'
            f'<script>window.LECCION={js};</script>\n<script src="leccion.js"></script>\n</body></html>\n')

VOICE = '''  <button type="button" class="all" id="all"><span id="all-i" aria-hidden="true">▶</span><span id="all-t">Escuchar todo</span></button>
  <div class="voice">
    <label for="voz">Voz</label>
    <select id="voz"><option value="">Automática</option></select>
    <button type="button" id="probar">Probar</button>
    <p class="hint">¿No aparece la voz que quieres? En Configuración busca «Voces», descarga una en español, cierra Safari por completo y vuelve a abrir esta página.</p>
  </div>
'''

def mama(L):
    n = L['num']
    secs = []
    for k, (h, parts) in enumerate(L['mama']):
        secs.append(f'  <section class="sec say" style="--k:var(--c{k%6+1})">\n    <h2>{h}</h2>\n    ' + '\n    '.join(parts) + '\n  </section>\n')
    nxt = (f'<a class="next" href="leccion-{n+1}-mama.html"><small>Siguiente</small>Notas de la lección {n+1}</a>' if n < N
           else '<a class="next" href="./"><small>Inicio</small>Todas las lecciones</a>')
    return (HEAD + f'<title>Lección {n} · Notas para mamá · {SERIE}</title>\n{FONT}\n<link rel="stylesheet" href="mama.css">\n<script src="../lib/tech-theme.js" data-toggle="top" data-lang="es"></script>\n</head><body>\n<main class="wrap">\n'
            f'  <p class="kicker">{SERIE} · Lección {n}</p>\n  <h1>Notas para mamá: {html.escape(L["titulo"])}</h1>\n\n' + VOICE + '\n' + '\n'.join(secs) +
            f'\n  <nav class="end" aria-label="Más">\n    <a href="leccion-{n}.html"><small>Volver</small>La lección de ella</a>\n    {nxt}\n  </nav>\n</main>\n<script src="mama.js"></script>\n</body></html>\n')

def index():
    def lista(Ls):
        items = []
        for L in Ls:
            n = L['num']
            items.append(f'      <li><a class="l" href="leccion-{n}.html"><span class="n">{n}</span>{html.escape(L["titulo"])}</a>'
                         f'<a class="m" href="leccion-{n}-mama.html">Notas para mamá de la lección {n}</a></li>')
        return '\n'.join(items)
    niveles = ''.join(f'  <section class="lvl" aria-labelledby="n{k}">\n    <h2 id="n{k}">{html.escape(nombre)}</h2>\n    <ol>\n{lista(Ls)}\n    </ol>\n  </section>\n'
                      for k, (nombre, Ls) in enumerate(NIVELES, 1))
    return (HEAD + f'<title>{SERIE}</title>\n{FONT}\n<style>\n'
 ':root{color-scheme:light;--bg:#fff;--fg:#14213d;--muted:#4a5568;--line:#e2e8f0;--sky:#1d4ed8;--sun:#ffd23f;--font:"Atkinson Hyperlegible",Verdana,"Segoe UI",system-ui,sans-serif}\n'
 '*{box-sizing:border-box}\nbody{background:var(--bg);color:var(--fg);font-family:var(--font);margin:0;line-height:1.5}\n'
 '.wrap{max-width:760px;margin:0 auto;padding-block:max(24px,env(safe-area-inset-top,0px)) 60px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}\n'
 'h1{font-size:clamp(34px,8vw,48px);line-height:1.05;margin:0 0 8px}\n.lede{font-size:21px;color:var(--muted);margin:0 0 28px;max-width:34em}\nh2{font-size:26px;margin:0 0 12px}\n'
 '.lvl{border-top:6px solid var(--sky);border-radius:4px 4px 18px 18px;box-shadow:0 0 0 1px var(--line) inset;padding:18px;margin-bottom:28px}\n'
 'ol{list-style:none;margin:0;padding:0;display:grid;gap:18px}\nli{display:grid;gap:4px}\n'
 'a.l{display:flex;align-items:center;gap:14px;min-height:76px;border-radius:16px;padding:12px 16px;font-size:22px;font-weight:700;text-decoration:none;background:var(--sun);color:#5c4400}\n'
 'a.m{font-size:16px;color:var(--sky);font-weight:700;padding:6px 16px}\n'
 'a.apps{display:block;border-radius:16px;padding:16px;font-size:20px;font-weight:700;text-decoration:none;color:var(--sky);box-shadow:0 0 0 2px var(--sky) inset}\na.apps small{display:block;font-size:16px;font-weight:400;color:var(--muted)}\n'
 'a:focus-visible{outline:4px solid var(--sky);outline-offset:3px}\n'
 '.n{flex:none;width:40px;height:40px;border-radius:50%;display:grid;place-items:center;background:#fff;font-weight:700}\n'
 '</style>\n<script src="../lib/tech-theme.js" data-toggle="top" data-lang="es"></script>\n</head><body>\n<div class="wrap">\n'
 f'  <h1>{SERIE}</h1>\n  <p class="lede">Lecciones para aprender a usar el iPhone con VoiceOver y Siri, desde cero. Cada lección tiene una página para ella, que se escucha con VoiceOver, y notas para mamá.</p>\n'
 + niveles +
 '  <a class="apps" href="apps.html">Apps recomendadas<small>Para mamá: las mejores apps para personas con discapacidad visual, y cómo elegir una nueva.</small></a>\n</div>\n</body></html>\n')

def apps():
    secs = []
    for k, (h, parts) in enumerate(APPS['secciones']):
        secs.append(f'  <section class="sec say" style="--k:var(--c{k%6+1})">\n    <h2>{h}</h2>\n    ' + '\n    '.join(parts) + '\n  </section>\n')
    return (HEAD + f'<title>{APPS["titulo"]} · {SERIE}</title>\n{FONT}\n<link rel="stylesheet" href="mama.css">\n<script src="../lib/tech-theme.js" data-toggle="top" data-lang="es"></script>\n</head><body>\n<main class="wrap">\n'
            f'  <p class="kicker">{SERIE} · Para mamá</p>\n  <h1>{APPS["titulo"]} para personas con discapacidad visual</h1>\n\n' + VOICE + '\n' + '\n'.join(secs) +
            '\n  <nav class="end" aria-label="Más">\n    <a href="./"><small>Inicio</small>Todas las lecciones</a>\n    <a class="next" href="leccion-12-mama.html"><small>Notas</small>Lección 12: Apps que te ayudan</a>\n  </nav>\n</main>\n<script src="mama.js"></script>\n</body></html>\n')

def redirect(t):
    return ('<!doctype html><html lang="es-MX"><head><meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'
            f'<title>{SERIE}</title>\n<meta http-equiv="refresh" content="0; url={t}">\n<link rel="canonical" href="{t}">\n'
            f'<script>location.replace("{t}"+location.hash)</script>\n</head><body><p><a href="{t}">{SERIE}</a></p></body></html>\n')

for L in LECCIONES:
    open(f'{OUT}/leccion-{L["num"]}.html', 'w').write(leccion(L))
    open(f'{OUT}/leccion-{L["num"]}-mama.html', 'w').write(mama(L))
open(f'{OUT}/index.html', 'w').write(index())
open(f'{OUT}/apps.html', 'w').write(apps())
open(f'{OUT}/leccion-1-padres.html', 'w').write(redirect('leccion-1-mama.html'))
print('ok')
