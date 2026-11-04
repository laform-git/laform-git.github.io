# Fuente de las lecciones

Las páginas `leccion-N.html` y `leccion-N-mama.html` y el `index.html` de esta carpeta se generan con:

    python3 toca-escucha-y-aprende/_fuente/build.py toca-escucha-y-aprende

- `contenido.py`: todo el texto (historia, juegos, retos, tips de salud, notas para mamá).
- `build.py`: arma las páginas. El motor de la página de ella está en `../leccion.js` y `../estilo.css`; las notas usan `../mama.js` y `../mama.css`.

Para cambiar una lección, edita `contenido.py` y vuelve a correr `build.py`. No edites los .html a mano.
