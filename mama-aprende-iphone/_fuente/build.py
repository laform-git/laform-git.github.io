# Arma las páginas de «Mamá aprende iPhone».
#   python3 mama-aprende-iphone/_fuente/build.py mama-aprende-iphone
# Los PDF para leer sin internet se generan aparte con pdf.js (Playwright).
import sys, os, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from contenido import LECCIONES, PARTES

OUT = sys.argv[1]
SERIE = "Mamá aprende iPhone"
N = len(LECCIONES)
FONT = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&display=swap">'
HEAD = '<!doctype html><html lang="es-MX"><head><meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
THEME = '<script src="../lib/tech-theme.js" data-toggle="top" data-lang="es"></script>'
VOICE = '''  <button type="button" class="all" id="all"><span id="all-i" aria-hidden="true">▶</span><span id="all-t">Escuchar todo</span></button>
  <div class="voice">
    <label for="voz">Voz</label>
    <select id="voz"><option value="">Automática</option></select>
    <button type="button" id="probar">Probar</button>
    <p class="hint">¿No aparece la voz que quieres? En Configuración busca «Voces», descarga una en español, cierra Safari por completo y vuelve a abrir esta página.</p>
  </div>
'''

def sec(h, parts, k, cls=''):
    return f'  <section class="sec say{cls}" style="--k:var(--c{k%6+1})">\n    <h2>{h}</h2>\n    ' + '\n    '.join(parts) + '\n  </section>\n'

def leccion(L):
    n = L['num']
    secs = [sec(h, p, k) for k, (h, p) in enumerate(L['secciones'])]
    secs.append(sec('Practica', [f'<p>{L["practica"]}</p>'], 1, ' practica'))
    if L.get('problemas'):
        secs.append(sec('Si algo sale mal', [L['problemas']], 4))
    secs.append(sec('Con tu hija', [f'<p>{L["hija"]}</p>'], 3, ' hija'))
    lis = ''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{html.escape(t)}</a></li>' for t, u in L['apple'])
    secs.append(f'  <section class="sec say apple" style="--k:var(--sky)">\n    <h2>Aprende más con Apple</h2>\n    <ul>{lis}</ul>\n  </section>\n')
    prev = f'<a href="leccion-{n-1}.html"><small>Anterior</small>Lección {n-1}</a>' if n > 1 else '<a href="./"><small>Inicio</small>Todas las lecciones</a>'
    nxt = f'<a class="next" href="leccion-{n+1}.html"><small>Siguiente</small>Lección {n+1}</a>' if n < N else '<a class="next" href="./"><small>Inicio</small>Todas las lecciones</a>'
    parte = PARTES[L['parte']-1][0]
    return (HEAD + f'<title>Lección {n} · {html.escape(L["titulo"])} · {SERIE}</title>\n{FONT}\n<link rel="stylesheet" href="estilo.css">\n{THEME}\n</head><body>\n<main class="wrap">\n'
            f'  <p class="kicker"><a href="./">{SERIE}</a> · {html.escape(parte.split(" · ")[0])} · Lección {n}</p>\n  <h1>{html.escape(L["titulo"])}</h1>\n'
            f'  <p class="intro">{L["intro"]}</p>\n  <p class="pdf"><a href="pdf/leccion-{n}.pdf" download>Guardar esta lección para leer sin internet (PDF)</a></p>\n\n'
            + VOICE + '\n' + '\n'.join(secs) +
            f'\n  <nav class="end" aria-label="Más">\n    {prev}\n    {nxt}\n  </nav>\n</main>\n<script src="mama.js"></script>\n</body></html>\n')

def index():
    partes = ''
    for k, (nombre, sub) in enumerate(PARTES, 1):
        items = ''.join(f'      <li><a class="l" href="leccion-{L["num"]}.html"><span class="n">{L["num"]}</span><span><b>{html.escape(L["titulo"])}</b><small>{L["intro"]}</small></span></a>'
                        f'<a class="p" href="pdf/leccion-{L["num"]}.pdf" download>PDF para leer sin internet</a></li>\n' for L in LECCIONES if L['parte'] == k)
        partes += f'  <section class="lvl" aria-labelledby="p{k}">\n    <h2 id="p{k}">{html.escape(nombre)}</h2>\n    <p class="sub">{html.escape(sub)}</p>\n    <ol>\n{items}    </ol>\n  </section>\n'
    return (HEAD + f'<title>{SERIE}</title>\n{FONT}\n<link rel="stylesheet" href="estilo.css">\n{THEME}\n</head><body>\n<main class="wrap home">\n'
            f'  <h1>{SERIE}</h1>\n  <p class="intro">Clases de iPhone desde cero, para mamá. Primero tú aprendes a usar tu iPhone; después, cómo enseñarle a tu hija con la serie «Toca, escucha y aprende».</p>\n'
            '  <section class="how" aria-labelledby="como">\n    <h2 id="como">Cómo usar estas lecciones</h2>\n    <ul>\n'
            '      <li><b>Escuchar:</b> en cada lección, el botón amarillo «Escuchar todo» lee la lección en voz alta.</li>\n'
            '      <li><b>Sin internet:</b> cada lección tiene un PDF. Descárgalo con Wi-Fi y ábrelo después desde la app Archivos.</li>\n'
            '      <li><b>Una por día:</b> lee una lección, haz la práctica, y sigue mañana.</li>\n    </ul>\n  </section>\n'
            + partes +
            '  <a class="toca" href="../toca-escucha-y-aprende/">Toca, escucha y aprende<small>La serie de ella: lecciones de iPhone con VoiceOver.</small></a>\n'
            '  <p class="help">¿Necesitas ayuda? Apple tiene soporte en español por teléfono, chat o en tienda: <a href="https://support.apple.com/es-lamr/111749" target="_blank" rel="noopener">cómo pedir ayuda</a>.</p>\n'
            '</main>\n</body></html>\n')

for L in LECCIONES:
    open(f'{OUT}/leccion-{L["num"]}.html', 'w').write(leccion(L))
open(f'{OUT}/index.html', 'w').write(index())
print('ok', N)
