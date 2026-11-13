# Fuente de las lecciones

Las páginas `leccion-N.html` y `leccion-N-mama.html` y el `index.html` de esta carpeta se generan con:

    python3 toca-escucha-y-aprende/_fuente/build.py toca-escucha-y-aprende

- `contenido.py`: todo el texto del Nivel 1 (historia, juegos, retos, tips de salud, notas para mamá).
- `nivel2.py`: el Nivel 2 (lecciones 7 a 12) y la página `apps.html`, con los enlaces a las fuentes.
- `build.py`: arma las páginas. El motor de la página de ella está en `../leccion.js` y `../estilo.css`; las notas usan `../mama.js` y `../mama.css`.

Para cambiar una lección, edita `contenido.py` y vuelve a correr `build.py`. No edites los .html a mano.
