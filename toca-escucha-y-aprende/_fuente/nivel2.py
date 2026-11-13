# Toca, escucha y aprende · Nivel 2 · lecciones 7 a 12 y la página de apps.
# Español de México. Habla con ella (tú) y con mamá (tú). Sin nombres.
# Gestos y nombres de ajustes revisados contra el Manual del iPhone de Apple (es-lamr), noviembre de 2026.

APPLE_GESTOS = "https://support.apple.com/es-lamr/guide/iphone/iph3e2e2281/ios"
APPLE_ROTOR = "https://support.apple.com/es-lamr/guide/iphone/iph3e2e3a6d/ios"
APPLE_TECLADO = "https://support.apple.com/es-lamr/guide/iphone/iph3e2e3d1d/ios"
APPLE_SIRI_MUSICA = "https://support.apple.com/es-lamr/105053"
CNIB = "https://www.cnib.ca/en/node/610"
PATHS = "https://www.pathstoliteracy.org/resource/ios-device-skills-checklist/"
COMMON = "https://www.commonsensemedia.org/es/listas/los-mejores-podcasts-bilingues-y-en-espanol-para-ninos"
BME = "https://www.bemyeyes.com/terms-conditions/"
ONCE_SEEING = "https://club.once.es/afiliados/servicios/autonomia-personal-y-tecnologia/tiflotecnologia/valoraciones-de-accesibilidad-de-aplicaciones-para-moviles/seeing-ai-1/seeing-ai-ios.pdf"
SONOKIDS = "https://www.sonokids.org/ballyland-early-learning/ballyland-game-apps/ballyland-magico/"
AFB27 = "https://afb.org/ios-27-accessibility"
AFB26 = "https://afb.org/blog/entry/ios-26-accessibility-features"

def a(url, texto):
    return f'<a href="{url}">{texto}</a>'

LECCIONES2 = [
# ───────────────────────── LECCIÓN 7 ─────────────────────────
dict(num=7, titulo="Tres gestos nuevos", nivel="c",
 intro="Bienvenida al Nivel 2. Hoy aprendes tres gestos nuevos. Elige una burbuja.",
 secciones=[
  dict(nombre="Historia", pantallas=[
   dict(t="texto", text="Ya sabes tocar, deslizar y dar dos toques. Hoy aprendes tres gestos nuevos. Los tres usan más de un dedo."),
   dict(t="texto", text="El primero: leer todo. Desliza dos dedos hacia arriba y VoiceOver lee la pantalla completa, desde el principio. Tú solo escuchas."),
   dict(t="texto", text="Si quieres que se detenga, toca una vez con dos dedos. Ese gesto ya lo conoces."),
   dict(t="texto", text="El segundo: pasar la página. Hay pantallas largas que no caben completas. Desliza tres dedos hacia arriba para bajar una página. Tres dedos hacia abajo, y regresas."),
   dict(t="texto", text="En la pantalla de inicio, desliza tres dedos a la izquierda o a la derecha para cambiar de página de apps."),
   dict(t="texto", text="El tercero: regresar. Mueve dos dedos rápido de un lado a otro, tres veces, como si borraras con una goma. Así cierras lo que abriste o vuelves a la pantalla anterior."),
   dict(t="texto", text="Antes de probarlos en la pantalla, practica en la mesa: dos dedos juntos, luego tres dedos juntos. Suave, como cosquillas."),
   dict(t="salud", titulo="Tip de salud", text="Tus oídos trabajan mucho con el iPhone. Mantén el volumen a la mitad o menos. Si no alcanzas a oír a quien te habla a tu lado, está muy fuerte."),
  ]),
  dict(nombre="Juego", pantallas=[
   dict(t="texto", titulo="Juego: ¿cierto o falso?", text="Seis preguntas. Una es de encontrar un botón, y una es de repaso del Nivel 1."),
   dict(t="pregunta", text="Deslizar dos dedos hacia arriba hace que VoiceOver lea toda la pantalla.", ok=True, fb="¡Cierto! Y un toque con dos dedos lo detiene."),
   dict(t="pregunta", text="Para pasar la página deslizas un solo dedo hacia arriba.", ok=False, fb="¡Bien! Es falso. Se pasa con tres dedos."),
   dict(t="pregunta", text="Mover dos dedos de un lado a otro, tres veces, te regresa a la pantalla anterior.", ok=True, fb="¡Cierto! Como si borraras con una goma."),
   dict(t="busca", text="Encuentra el gesto que lee toda la pantalla.", opciones=["Tres dedos hacia arriba","Dos dedos hacia arriba","Dos toques","Tres clics"], correcta="Dos dedos hacia arriba"),
   dict(t="pregunta", text="Dos toques rápidos presionan lo último que VoiceOver dijo.", ok=True, fb="¡Cierto! Eso lo aprendiste en el Nivel 1 y lo usas siempre."),
   dict(t="pregunta", text="Si el volumen está tan fuerte que no oyes a quien te habla, hay que bajarlo.", ok=True, fb="¡Cierto! Así cuidas tus oídos."),
  ]),
  dict(nombre="Reto", pantallas=[
   dict(t="texto", titulo="Tu reto de hoy", text="Abre Configuración desde la pantalla de inicio. Desliza dos dedos hacia arriba para que VoiceOver lea todo. Luego pasa la página con tres dedos, dos veces. Al final, regresa a la pantalla de inicio."),
  ]),
 ],
 despedida="En la próxima lección conoces el rotor: una perilla invisible.",
 mama=[
  ("Su salud: cuidar sus oídos", [
   "<p>Ella usa los oídos para todo, así que vale la pena cuidarlos. La regla sencilla: volumen a la mitad o menos, y si no alcanza a oírte cuando le hablas a su lado, está muy fuerte.</p>",
   "<p>Si usa audífonos, en Configuración busca «Seguridad de audífonos» y activa la opción que reduce el audio fuerte.</p>"]),
  ("De qué trata esta lección", [
   "<p>Tres gestos con más de un dedo: leer toda la pantalla (dos dedos hacia arriba), pasar la página (tres dedos hacia arriba o abajo, y a los lados en la pantalla de inicio) y regresar (dos dedos de un lado a otro, tres veces).</p>",
   f"<p>Son los gestos del {a(APPLE_GESTOS, 'Manual del iPhone de Apple')}. No cambiaron con las versiones nuevas del sistema.</p>"]),
  ("Cómo se enseña un gesto nuevo", [
   f"<p>Esto es lo que recomiendan los maestros de niños con discapacidad visual ({a(CNIB, 'manual ABCs of iOS, de la CNIB de Canadá')}):</p>",
   "<ul><li><b>Primero en la mesa, luego en la pantalla.</b> Que haga el movimiento sobre la mesa o sobre tu brazo antes de probarlo en el teléfono.</li><li><b>Toque suave.</b> Como cosquillas. Si aprieta fuerte, el iPhone no entiende el gesto.</li><li><b>Tu mano debajo de la suya, no encima.</b> Si necesita sentir el movimiento, tú lo haces y ella pone su mano sobre la tuya. No le muevas los dedos.</li><li><b>Poquito y seguido.</b> Un gesto a la vez, sesiones cortas y repetir al día siguiente funciona mejor que una sesión larga.</li><li><b>Dile lo que va a pasar</b> antes de un sonido nuevo, para que no se asuste.</li></ul>"]),
  ("Antes de empezar", [
   "<ul><li><b>No muevas sus apps de lugar.</b> Ella se aprende dónde está cada una. Deja Configuración, Reloj, Música, Podcasts y Mensajes en la primera pantalla de inicio, siempre en el mismo sitio.</li><li><b>Indicaciones:</b> en <span class=\"path\">Configuración → Accesibilidad → VoiceOver → Verbosidad</span>, deja activadas las indicaciones. Así VoiceOver le dice qué puede hacer con cada botón.</li></ul>"]),
  ("Cómo acompañarla", [
   "<ul><li><b>Si le sale otro gesto sin querer,</b> casi siempre es porque los dedos no tocaron al mismo tiempo. Que lo practique otra vez en la mesa.</li><li><b>El reto</b> usa Configuración porque es una pantalla larga y segura para practicar. Que no cambie nada: solo escuchar y pasar la página.</li></ul>"]),
  ("Gestos de esta lección", [
   "<dl><dt>Dos dedos hacia arriba</dt><dd>Leer toda la pantalla desde el principio.</dd><dt>Dos dedos hacia abajo</dt><dd>Leer desde donde está.</dd><dt>Tres dedos hacia arriba o hacia abajo</dt><dd>Pasar la página.</dd><dt>Tres dedos a la izquierda o a la derecha</dt><dd>Cambiar de página en la pantalla de inicio.</dd><dt>Dos dedos de un lado a otro, tres veces</dt><dd>Regresar o cerrar.</dd></dl>"]),
 ]),

# ───────────────────────── LECCIÓN 8 ─────────────────────────
dict(num=8, titulo="El rotor: tu perilla invisible", nivel="c",
 intro="Hoy conoces el rotor. Ten cerca un frasco con tapa. Elige una burbuja.",
 secciones=[
  dict(nombre="Historia", pantallas=[
   dict(t="texto", text="Toma un frasco y gira la tapa con dos dedos. El rotor de VoiceOver se usa igual: es una perilla invisible en la pantalla."),
   dict(t="texto", text="Pon dos dedos en la pantalla, un poco separados, y gíralos como si giraras la tapa. VoiceOver dice una palabra. Esa es una opción del rotor."),
   dict(t="texto", text="Sigue girando y oyes más opciones: Caracteres, Palabras, Velocidad de habla, Volumen."),
   dict(t="texto", text="Cuando oigas la que quieres, deja de girar. Ahora desliza un dedo hacia arriba o hacia abajo para usarla."),
   dict(t="texto", text="Un ejemplo. Gira hasta oír «Velocidad de habla». Desliza hacia arriba y VoiceOver habla más rápido. Hacia abajo, más lento."),
   dict(t="texto", text="Otro ejemplo. Gira hasta oír «Caracteres». Desliza hacia abajo y VoiceOver te lee letra por letra. Sirve para saber cómo se escribe una palabra."),
   dict(t="texto", text="El rotor se queda donde lo dejaste. Si VoiceOver hace algo raro cuando deslizas hacia arriba o hacia abajo, gira el rotor y escucha en qué opción está."),
   dict(t="salud", titulo="Tip de salud", text="Toma agua. Tu cuerpo y tu cerebro trabajan mejor con agua. Deja un vaso cerca cuando hagas tu lección."),
  ]),
  dict(nombre="Juego", pantallas=[
   dict(t="texto", titulo="Juego: el rotor", text="Seis preguntas. Las dos últimas son de repaso de la lección 7."),
   dict(t="pregunta", text="El rotor se usa girando dos dedos en la pantalla.", ok=True, fb="¡Cierto! Como la tapa de un frasco."),
   dict(t="pregunta", text="Después de elegir una opción del rotor, deslizas un dedo hacia arriba o hacia abajo para usarla.", ok=True, fb="¡Cierto! Girar elige. Deslizar usa."),
   dict(t="pregunta", text="Con el rotor en Velocidad de habla, deslizar hacia arriba hace que VoiceOver hable más lento.", ok=False, fb="¡Bien! Es falso. Hacia arriba habla más rápido."),
   dict(t="busca", text="Encuentra la opción del rotor que lee letra por letra.", opciones=["Palabras","Volumen","Caracteres","Velocidad de habla"], correcta="Caracteres"),
   dict(t="pregunta", text="Deslizar tres dedos hacia arriba pasa la página.", ok=True, fb="¡Cierto! Lo aprendiste en la lección 7."),
   dict(t="pregunta", text="Para regresar a la pantalla anterior aprietas tres veces el botón lateral.", ok=False, fb="¡Bien! Es falso. Mueves dos dedos de un lado a otro. Los tres clics apagan VoiceOver."),
  ]),
  dict(nombre="Reto", pantallas=[
   dict(t="texto", titulo="Tu reto de hoy", text="Gira el rotor hasta oír «Velocidad de habla». Sube la velocidad dos veces y bájala una. Luego gira hasta «Caracteres», toca una app en la pantalla de inicio y pídele a VoiceOver que te deletree su nombre."),
  ]),
 ],
 despedida="Ya tienes el rotor. En la próxima lección tu iPhone se vuelve tu radio.",
 mama=[
  ("Su salud: agua", ["<p>Un vaso de agua cerca durante la lección. Es un hábito fácil de pegar a algo que ya hace todos los días.</p>"]),
  ("De qué trata esta lección", [
   f"<p>El rotor es un menú que se abre girando dos dedos sobre la pantalla, «como si estuvieras dándole vuelta a un dial», dice {a(APPLE_ROTOR, 'el manual de Apple')}. Girar elige una opción; deslizar un dedo hacia arriba o hacia abajo la usa.</p>",
   "<p>Es el gesto más difícil de todo el curso. Es normal que tarde varios días en salirle.</p>"]),
  ("Cómo enseñarlo", [
   "<ul><li><b>Con un objeto real.</b> La tapa de un frasco o una perilla. Que la gire con el pulgar y el índice, y luego haga el mismo movimiento sobre la pantalla. Los maestros usan materiales que se tocan para explicar el rotor.</li><li><b>Otra forma, con dos manos:</b> un dedo de cada mano sobre la pantalla; uno sube y el otro baja al mismo tiempo. Apple lo da como alternativa, y a muchos niños les sale más fácil.</li><li><b>Movimiento chico.</b> No hace falta dar la vuelta completa: un cuarto de vuelta ya cambia de opción.</li></ul>"]),
  ("Antes de empezar: deja pocas opciones", [
   "<p>El rotor trae muchas opciones y eso confunde. Ve a <span class=\"path\">Configuración → Accesibilidad → VoiceOver → Rotor</span> y deja solo estas: Caracteres, Palabras, Velocidad de habla, Volumen y Encabezados. Después se agregan más.</p>",
   "<p>En <span class=\"path\">Verbosidad</span> activa «Confirmación de voz», para que VoiceOver diga en voz alta cada cambio que ella haga con el rotor.</p>"]),
  ("Cómo acompañarla", [
   "<ul><li><b>Si «se descompone» VoiceOver,</b> casi siempre es el rotor que quedó en otra opción. Enséñale a girarlo y escuchar dónde está.</li><li><b>La velocidad es suya.</b> Muchas personas ciegas escuchan muy rápido. Si ella la sube y entiende, déjala.</li></ul>"]),
  ("Palabras de esta lección", [
   "<dl><dt>Rotor</dt><dd>El menú que se abre girando dos dedos.</dd><dt>Caracteres</dt><dd>Letras, números y signos. Con esta opción, VoiceOver lee letra por letra.</dd><dt>Velocidad de habla</dt><dd>Qué tan rápido habla VoiceOver.</dd></dl>"]),
 ]),

# ───────────────────────── LECCIÓN 9 ─────────────────────────
dict(num=9, titulo="Tu música", nivel="c",
 intro="Hoy tu iPhone se vuelve tu radio. Elige una burbuja.",
 secciones=[
  dict(nombre="Historia", pantallas=[
   dict(t="texto", text="Puedes pedir música con tu voz. Di: «Oye Siri, pon música para bailar». O di el nombre de una canción, o de quien la canta."),
   dict(t="texto", text="Para detener la música hay un gesto especial: toca dos veces con dos dedos, en cualquier parte de la pantalla. Otra vez, y la música sigue."),
   dict(t="texto", text="Ese mismo gesto contesta una llamada. Y también la cuelga."),
   dict(t="texto", text="También lo puedes pedir con la voz. «Siri, pausa». «Oye Siri, sáltate esta canción». «Oye Siri, sube el volumen»."),
   dict(t="texto", text="Si oyes una canción que te gusta y no sabes cuál es, pregunta: «Oye Siri, ¿cómo se llama esta canción?»."),
   dict(t="texto", text="En la app Música hay botones como los que ya conoces. Desliza a la derecha para encontrarlos: Anterior, Pausa, Siguiente. Dos toques para presionar."),
   dict(t="salud", titulo="Tip de salud", text="Cantar y bailar mueven todo tu cuerpo y te ponen de buen humor. Pon una canción y baila con alguien de tu familia."),
  ]),
  dict(nombre="Juego", pantallas=[
   dict(t="texto", titulo="Juego: música", text="Seis preguntas. Una es de repaso del rotor."),
   dict(t="pregunta", text="Tocar dos veces con dos dedos detiene la música.", ok=True, fb="¡Cierto! Y otra vez, para que siga."),
   dict(t="pregunta", text="Para pedir una canción tienes que escribir su nombre.", ok=False, fb="¡Bien! Es falso. Se la pides a Siri con tu voz."),
   dict(t="pregunta", text="Siri puede decirte cómo se llama la canción que está sonando.", ok=True, fb="¡Cierto! Pregunta: ¿cómo se llama esta canción?"),
   dict(t="busca", text="Encuentra el botón que detiene la música.", opciones=["Siguiente","Anterior","Pausa","Volumen"], correcta="Pausa"),
   dict(t="pregunta", text="El rotor se usa girando dos dedos en la pantalla.", ok=True, fb="¡Cierto! Lo aprendiste en la lección 8."),
   dict(t="pregunta", text="Escuchar música muy fuerte por mucho tiempo puede lastimar tus oídos.", ok=True, fb="¡Cierto! Por eso el volumen va a la mitad o menos."),
  ]),
  dict(nombre="Reto", pantallas=[
   dict(t="texto", titulo="Tu reto de hoy", text="Pídele a Siri una canción que te guste. Detenla con dos toques de dos dedos. Hazla seguir. Luego pídele a Siri que suba el volumen, y después que lo baje."),
  ]),
 ],
 despedida="En la próxima lección escuchas cuentos y podcasts.",
 mama=[
  ("Su salud: bailar", ["<p>La música es la forma más fácil de que se mueva. Una canción al día, bailando contigo o con sus hermanos, ya cuenta.</p>"]),
  ("De qué trata esta lección", [
   "<p>Pedir música con Siri, detenerla y seguirla con un solo gesto (dos toques con dos dedos) y encontrar los botones de la app Música.</p>",
   f"<p>Las frases para Siri son las que da {a(APPLE_SIRI_MUSICA, 'Apple en su página de ayuda')}.</p>"]),
  ("Antes de empezar", [
   "<ul><li><b>Suscripción:</b> según Apple, pedirle música a Siri de esta forma es para quienes tienen suscripción a Apple Music. Sin suscripción, Siri solo puede poner la música que ya esté guardada en el teléfono.</li><li>🟡 <b>Si usan Spotify u otra app:</b> muchas funcionan con Siri diciendo el nombre de la app al final de la frase. Pruébenlo antes de la lección; no lo pude confirmar para todas.</li><li><b>Música apta para su edad:</b> en Configuración busca «Tiempo en pantalla» y, en las restricciones de contenido, limita la música con contenido explícito.</li><li><b>El gesto de dos toques con dos dedos</b> debe poder controlar la música. Viene activado. Si no funciona, revisa en <span class=\"path\">Configuración → Accesibilidad → VoiceOver → Comandos</span>.</li></ul>"]),
  ("Cómo acompañarla", [
   "<ul><li><b>Que practique el gesto en la mesa:</b> dos dedos juntos, dos golpecitos rápidos.</li><li><b>Si Siri pone otra canción,</b> que lo intente diciendo también quién la canta.</li><li><b>Hagan juntas una lista</b> con sus canciones favoritas. Después podrá pedirla por su nombre.</li></ul>"]),
  ("Frases para Siri", [
   "<ul><li>«Oye Siri, pon música relajante»</li><li>«Siri, pausa»</li><li>«Oye Siri, sáltate esta canción»</li><li>«Oye Siri, sube el volumen»</li><li>«Oye Siri, ¿cómo se llama esta canción?»</li><li>«Oye Siri, ¿quién canta esta canción?»</li></ul>"]),
  ("Gesto de esta lección", [
   "<dl><dt>Dos toques con dos dedos</dt><dd>Detener o seguir la música o el podcast. Contestar o colgar una llamada.</dd></dl>"]),
 ]),

# ───────────────────────── LECCIÓN 10 ─────────────────────────
dict(num=10, titulo="Cuentos y podcasts", nivel="c",
 intro="Hoy vas a escuchar cuentos y programas. Elige una burbuja.",
 secciones=[
  dict(nombre="Historia", pantallas=[
   dict(t="texto", text="Un podcast es un programa para escuchar. Hay de cuentos, de ciencia y de música. Escucharlos es gratis."),
   dict(t="texto", text="Cada podcast tiene muchos capítulos. Se llaman episodios."),
   dict(t="texto", text="Para oír uno, di «Oye Siri, pon el podcast» y luego su nombre. Por ejemplo: «Oye Siri, pon el podcast Cuentos Increíbles»."),
   dict(t="texto", text="Se detiene igual que la música: dos toques con dos dedos. Otra vez, y sigue."),
   dict(t="texto", text="En la app Podcasts, cada episodio es un botón. Desliza a la derecha para oír los nombres y da dos toques en el que quieras."),
   dict(t="texto", text="Hay listas largas con muchos episodios. Ya sabes qué hacer: tres dedos hacia arriba para pasar la página."),
   dict(t="texto", text="Si un podcast te gusta, lo puedes seguir. Así los episodios nuevos te llegan solos. Pídele a mamá que te ayude la primera vez."),
   dict(t="salud", titulo="Tip de salud", text="Escuchar un cuento es un buen descanso. Acuéstate en un sillón o en el piso y solo escucha. Y recuerda: una hora antes de dormir, el iPhone se queda cargando lejos de tu cama."),
  ]),
  dict(nombre="Juego", pantallas=[
   dict(t="texto", titulo="Juego: podcasts", text="Seis preguntas. Una es de repaso de la lección 7."),
   dict(t="pregunta", text="Un podcast es un programa para escuchar.", ok=True, fb="¡Cierto! Hay de cuentos, de ciencia y de música."),
   dict(t="pregunta", text="Los capítulos de un podcast se llaman episodios.", ok=True, fb="¡Cierto! Cada episodio es una historia o un tema."),
   dict(t="pregunta", text="Para detener un podcast hay que apagar el iPhone.", ok=False, fb="¡Bien! Es falso. Dos toques con dos dedos, igual que la música."),
   dict(t="busca", text="Encuentra el podcast de cuentos.", opciones=["Reloj","Mensajes","Cuentos Increíbles","Configuración"], correcta="Cuentos Increíbles"),
   dict(t="pregunta", text="Siri puede poner un podcast si le dices su nombre.", ok=True, fb="¡Cierto! Di: Oye Siri, pon el podcast, y su nombre."),
   dict(t="pregunta", text="Para pasar la página de una lista larga deslizas tres dedos hacia arriba.", ok=True, fb="¡Cierto! Lo aprendiste en la lección 7."),
  ]),
  dict(nombre="Reto", pantallas=[
   dict(t="texto", titulo="Tu reto de hoy", text="Con mamá, elige un podcast. Pídeselo a Siri. Escucha un episodio completo y después cuéntale a alguien de tu familia de qué trató."),
  ]),
 ],
 despedida="En la próxima lección escribes mensajes, con tu voz y con tus dedos.",
 mama=[
  ("Su salud: escuchar para descansar", ["<p>Un cuento en audio es descanso de verdad: sin pantalla y sin prisa. Que lo escuche acostada o sentada cómoda.</p>", "<p>La regla del Nivel 1 sigue igual: una hora antes de dormir, el iPhone se queda cargando fuera de la cama.</p>"]),
  ("De qué trata esta lección", [
   "<p>Qué es un podcast, cómo pedirlo con Siri, cómo encontrar episodios en la app Podcasts y cómo seguir un programa. Usa dos gestos que ya conoce: dos toques con dos dedos para detener, y tres dedos para pasar la página.</p>"]),
  ("Podcasts en español para su edad", [
   f"<p>Estos vienen de {a(COMMON, 'la lista de Common Sense Media')}, que revisa contenido para niños y da una edad recomendada:</p>",
   "<ul><li><b>Cuentos Increíbles</b> (5 años o más). Cuentos con imaginación y una enseñanza.</li><li><b>Hada de Fresa</b> (5 o más). Cuentos divertidos con mensajes positivos.</li><li><b>Tumble en Español</b> (6 o más). Ciencia explicada para niños curiosos.</li><li><b>Allegro Mágico</b> (7 o más). Música clásica para niños.</li><li><b>Cuentos de Buenas Noches para Niñas Rebeldes</b> (7 o más). Historias de mujeres que lograron cosas grandes.</li><li><b>Brains On! en Español</b> (8 o más). Ciencia para niños curiosos.</li></ul>",
   "<p>Escucha tú primero un episodio de cada uno. Tú conoces mejor que nadie lo que le gusta y lo que le conviene.</p>"]),
  ("Antes de empezar", [
   "<ul><li><b>Sigue por ella dos o tres podcasts</b> en la app Podcasts, para que al abrirla ya encuentre algo suyo.</li><li><b>Contenido explícito:</b> en las restricciones de «Tiempo en pantalla» también se limitan los podcasts.</li><li><b>App Podcasts en la primera pantalla de inicio,</b> en un lugar fijo.</li></ul>"]),
  ("Cómo acompañarla", [
   "<ul><li><b>El reto termina contando el cuento.</b> Contar lo que oyó es lo que más le ayuda a recordar y a ordenar ideas. Hazle preguntas: ¿quién era?, ¿qué pasó al final?</li><li><b>Si Siri no encuentra el podcast,</b> que diga el nombre completo y despacio.</li></ul>"]),
  ("Palabras de esta lección", [
   "<dl><dt>Podcast</dt><dd>Un programa para escuchar, por capítulos.</dd><dt>Episodio</dt><dd>Cada capítulo de un podcast.</dd><dt>Seguir</dt><dd>Pedir que los episodios nuevos lleguen solos.</dd></dl>"]),
 ]),

# ───────────────────────── LECCIÓN 11 ─────────────────────────
dict(num=11, titulo="Escribe con tu voz y con tus dedos", nivel="c",
 intro="Hoy aprendes a escribir en tu iPhone. Elige una burbuja.",
 secciones=[
  dict(nombre="Historia", pantallas=[
   dict(t="texto", text="Hay dos maneras de escribir en tu iPhone: con tu voz y con tus dedos."),
   dict(t="texto", text="Con tu voz se llama dictado. Cuando aparezca el teclado, toca dos veces con dos dedos sobre él. Oyes un sonido: habla. Otra vez dos toques con dos dedos, y el iPhone escribe lo que dijiste."),
   dict(t="texto", text="Con tus dedos: el teclado está en la parte de abajo de la pantalla. Pon un dedo y arrástralo. VoiceOver te dice cada letra."),
   dict(t="texto", text="Cuando oigas la letra que quieres, levanta el dedo. La letra se escribe. Si no es la que quieres, sigue arrastrando sin levantar."),
   dict(t="texto", text="Las letras están siempre en el mismo lugar. La Q está arriba a la izquierda. La P, arriba a la derecha. El espacio, abajo en medio."),
   dict(t="texto", text="Si te equivocas, busca la tecla que borra. Está del lado derecho, arriba de la última fila. VoiceOver dice «Suprimir»."),
   dict(t="texto", text="En la app Mensajes, escribe tu mensaje y busca el botón Enviar. Dos toques, y se va."),
   dict(t="salud", titulo="Tip de salud", text="Escribir cansa los dedos y los hombros. Sacude las manos como si tuvieran agua, y abre y cierra los dedos cinco veces."),
  ]),
  dict(nombre="Juego", pantallas=[
   dict(t="texto", titulo="Juego: escribir", text="Seis preguntas. La última es de repaso de la música."),
   dict(t="pregunta", text="Dictar es escribir con tu voz.", ok=True, fb="¡Cierto! Tú hablas y el iPhone escribe."),
   dict(t="pregunta", text="Para empezar a dictar tocas dos veces con dos dedos sobre el teclado.", ok=True, fb="¡Cierto! Y otra vez para terminar."),
   dict(t="pregunta", text="Cuando escribes con un dedo, la letra se escribe al levantar el dedo.", ok=True, fb="¡Cierto! Por eso puedes buscar con calma antes de soltar."),
   dict(t="pregunta", text="Las letras del teclado cambian de lugar todos los días.", ok=False, fb="¡Bien! Es falso. Siempre están en el mismo lugar."),
   dict(t="busca", text="Encuentra la tecla que borra.", opciones=["Espacio","Intro","Suprimir","Mayúsculas"], correcta="Suprimir"),
   dict(t="pregunta", text="Dos toques con dos dedos también detienen la música.", ok=True, fb="¡Cierto! Es el mismo gesto, y hace lo que toca en cada momento."),
  ]),
  dict(nombre="Reto", pantallas=[
   dict(t="texto", titulo="Tu reto de hoy", text="Abre Mensajes y escríbele a mamá. Primero dicta: «Hola, mamá». Después escribe con tus dedos una sola palabra: tu comida favorita. Envía el mensaje."),
  ]),
 ],
 despedida="En la última lección del nivel conoces apps que te ayudan, y haces misiones.",
 mama=[
  ("Su salud: manos y hombros", ["<p>Escribir en una pantalla lisa cansa. Que sacuda las manos y mueva los hombros al terminar. Con el teléfono apoyado en la mesa se cansa menos que sosteniéndolo en el aire.</p>"]),
  ("De qué trata esta lección", [
   "<p>Dos formas de escribir: el dictado (dos toques con dos dedos sobre el teclado, para empezar y para terminar) y el teclado con un dedo. Al final manda un mensaje de verdad.</p>",
   f"<p>Los nombres y gestos vienen de {a(APPLE_TECLADO, 'la página de Apple sobre el teclado con VoiceOver')}.</p>"]),
  ("Antes de empezar: el estilo de escritura", [
   "<p>La lección da por hecho que la letra se escribe <b>al levantar el dedo</b>. Eso se llama «Escritura táctil». Ve a <span class=\"path\">Configuración → Accesibilidad → VoiceOver → Estilo de escritura</span> y elige <b>Escritura táctil</b>.</p>",
   "<p>La otra opción, «Tecleo estándar», pide encontrar la letra y luego dar dos toques. Es más lenta y es la que viene puesta.</p>",
   "<ul><li><b>Dictado:</b> en Configuración busca «Dictado» y actívalo, en español (México).</li><li><b>Mensajes en la primera pantalla de inicio.</b></li><li><b>Con quién puede escribirse:</b> en «Tiempo en pantalla» hay límites de comunicación para que solo pueda escribirle a los contactos que tú elijas.</li></ul>"]),
  ("Cómo enseñar el teclado", [
   "<ul><li><b>Un teclado que se toca.</b> Los maestros usan modelos con relieve. Uno casero: un cartón con tres filas de puntos de silicón o de calcomanías con relieve, en el mismo orden que el teclado. Que aprenda primero dónde quedan la Q, la P, la A, la L y el espacio.</li><li><b>Una palabra corta al día.</b> Su nombre, «mamá», «hola». Mejor poco y diario.</li><li><b>El dictado no es trampa.</b> Para mensajes largos es lo que usa la mayoría de las personas ciegas. El teclado sirve para corregir y para lo que no se quiere decir en voz alta.</li></ul>"]),
  ("Cómo acompañarla", [
   "<ul><li><b>Si el dictado escribe mal una palabra,</b> que borre con «Suprimir» y la dicte otra vez más despacio.</li><li><b>Para revisar lo que escribió,</b> que toque el texto: VoiceOver lo lee.</li><li><b>Si aprende braille en la escuela,</b> más adelante puede escribir braille directamente sobre la pantalla. Pregúntale a su maestra; queda para un nivel posterior.</li></ul>"]),
  ("Palabras de esta lección", [
   "<dl><dt>Dictado</dt><dd>Escribir hablando.</dd><dt>Escritura táctil</dt><dd>El estilo en que la letra se escribe al levantar el dedo.</dd><dt>Suprimir</dt><dd>La tecla que borra la última letra.</dd></dl>"]),
 ]),

# ───────────────────────── LECCIÓN 12 ─────────────────────────
dict(num=12, titulo="Apps que te ayudan", nivel="c",
 intro="Última lección del Nivel 2. Hoy conoces apps que te ayudan, y haces misiones. Elige una burbuja.",
 secciones=[
  dict(nombre="Historia", pantallas=[
   dict(t="texto", text="Tu iPhone tiene una cámara. Con ayuda de una app, la cámara te puede decir qué hay enfrente."),
   dict(t="texto", text="Seeing AI es una app gratis. Le apuntas a una hoja y te lee el texto en voz alta. También describe fotos y te dice de qué color es algo."),
   dict(t="texto", text="Para que la cámara vea bien, pon el iPhone sobre lo que quieres leer y levántalo despacio, como un elevador. Mantenlo derechito."),
   dict(t="texto", text="Be My Eyes te conecta con una persona voluntaria. Ella ve por tu cámara y te dice lo que hay. Es una app para personas adultas, así que se usa con mamá, desde su cuenta."),
   dict(t="texto", text="Lazarillo es como un guía en la calle. Cuando caminas con tu familia, te dice en voz alta por dónde vas y qué lugares hay cerca."),
   dict(t="texto", text="Las apps ayudan mucho, pero a veces se equivocan. Si algo es importante, como una medicina, pregúntale siempre a una persona adulta."),
   dict(t="texto", text="Antes de bajar una app nueva, pregúntale a mamá. Ella revisa que funcione bien con VoiceOver."),
   dict(t="salud", titulo="Tip de salud", text="Lo más divertido no está en el teléfono. Hoy, después de tu lección, sal a jugar: toca un árbol, escucha a los pájaros, corre con alguien de la mano."),
  ]),
  dict(nombre="Misiones", pantallas=[
   dict(t="mision", text="Abre Configuración y haz que VoiceOver lea toda la pantalla, con dos dedos hacia arriba."),
   dict(t="mision", text="Gira el rotor hasta «Velocidad de habla» y deja la voz a la velocidad que más te guste."),
   dict(t="mision", text="Pídele a Siri tu canción favorita. Detenla con dos toques de dos dedos."),
   dict(t="mision", text="Pon un episodio de tu podcast favorito y escúchalo acostada, con los ojos cerrados."),
   dict(t="mision", text="Mándale a mamá un mensaje dictado que diga: «Ya terminé el Nivel 2»."),
   dict(t="mision", text="Con mamá, abre Seeing AI y pídele que lea la portada de un libro o una caja de la cocina."),
  ]),
  dict(nombre="Juego", pantallas=[
   dict(t="texto", titulo="Juego: repaso", text="Seis preguntas de todo el Nivel 2."),
   dict(t="pregunta", text="Seeing AI puede leer en voz alta el texto de una hoja.", ok=True, fb="¡Cierto! Solo le apuntas con la cámara."),
   dict(t="pregunta", text="Be My Eyes se usa con mamá, desde su cuenta.", ok=True, fb="¡Cierto! Es una app para personas adultas."),
   dict(t="pregunta", text="Las apps que describen cosas nunca se equivocan.", ok=False, fb="¡Bien! Es falso. Si algo es importante, pregúntale a una persona adulta."),
   dict(t="busca", text="Encuentra la app que te guía en la calle.", opciones=["Seeing AI","Lazarillo","Podcasts","Música"], correcta="Lazarillo"),
   dict(t="pregunta", text="Para dictar tocas dos veces con dos dedos sobre el teclado.", ok=True, fb="¡Cierto! Lo aprendiste en la lección 11."),
   dict(t="pregunta", text="El rotor se gira con un solo dedo.", ok=False, fb="¡Bien! Es falso. Se gira con dos dedos."),
  ]),
  dict(nombre="Reto", pantallas=[
   dict(t="texto", titulo="Reto final", text="Enséñale a alguien de tu familia tu gesto favorito del Nivel 2. Explícale cómo se hace y para qué sirve."),
  ]),
 ],
 despedida="¡Terminaste el Nivel 2! Ya escuchas música y cuentos, escribes mensajes y conoces apps que te ayudan.",
 mama=[
  ("Su salud: afuera", ["<p>El teléfono es una herramienta, no el plan del día. Después de la lección, un rato afuera: tocar, oler, escuchar y correr de la mano de alguien.</p>"]),
  ("De qué trata esta lección", [
   "<p>Tres apps hechas para personas con discapacidad visual (Seeing AI, Be My Eyes y Lazarillo), dos reglas de seguridad y seis misiones de repaso de todo el Nivel 2.</p>",
   "<p>La lista completa, con más apps y con lo que ya trae el iPhone, está en <a href=\"apps.html\">Apps recomendadas</a>.</p>"]),
  ("Antes de empezar", [
   "<ul><li><b>Instala Seeing AI</b> y pruébala tú primero con una caja de cereal y la portada de un libro.</li><li><b>Be My Eyes es para mayores de 18 años,</b> según sus propios términos. La cuenta es tuya y se usa contigo al lado.</li><li><b>Lazarillo</b> es para cuando salgan juntas. No es para que camine sola.</li><li><b>Que las apps se bajen solo con tu permiso:</b> en Configuración busca «Compartir en familia» y activa que ella tenga que pedirte permiso para descargar.</li></ul>"]),
  ("Las dos reglas de seguridad", [
   "<ul><li><b>Las apps se equivocan.</b> Para medicinas, dinero o cruzar una calle, siempre confirma una persona.</li><li><b>La cámara muestra lo que hay alrededor.</b> Con una persona voluntaria en Be My Eyes, cuida que no se vean documentos, direcciones ni otras personas de la casa.</li></ul>"]),
  ("Cómo acompañarla", [
   "<ul><li><b>Las misiones</b> repasan una cosa de cada lección. Si una no sale, vuelvan a esa lección otro día; no hay prisa.</li><li><b>En el reto final,</b> que le enseñe a alguien más de la familia. Enseñar es la mejor señal de que ya lo sabe.</li></ul>"]),
  ("Qué sigue", [
   "<p>Que use todos los días lo que ya sabe: su música, sus cuentos y un mensaje para ti. La práctica diaria vale más que una lección nueva.</p>"]),
 ]),
]

# ───────────────────────── PÁGINA DE APPS ─────────────────────────
APPS = dict(
 titulo="Apps recomendadas",
 secciones=[
  ("Cómo leer esta lista", [
   "<p>Son apps y funciones para personas ciegas o con baja visión, revisadas en noviembre de 2026. Las apps cambian: antes de instalar una, pruébala tú con VoiceOver encendido.</p>",
   "<p>✅ confirmado en la fuente oficial · 🟢 buena evidencia · 🟡 no lo pude confirmar del todo; compruébalo en su teléfono.</p>"]),
  ("Lo que ya trae el iPhone", [
   "<ul>"
   f"<li>✅ <b>VoiceOver.</b> El lector de pantalla. Todo el curso se basa en él. {a(APPLE_GESTOS, 'Lista de gestos de Apple')}.</li>"
   "<li>✅ <b>Siri.</b> Para pedir cosas con la voz: llamar, poner música, alarmas, mensajes.</li>"
   "<li>✅ <b>Reconocimiento en tiempo real.</b> Con VoiceOver encendido, tocar tres veces con cuatro dedos lo empieza o lo detiene: el iPhone va diciendo lo que ve la cámara. 🟡 Lo que reconoce depende del modelo de iPhone.</li>"
   "<li>✅ <b>Lupa.</b> Una app de Apple que agranda con la cámara y también describe lo que ve.</li>"
   f"<li>🟡 <b>Descripciones de imágenes con inteligencia artificial.</b> El sistema más reciente (iOS 27) agregó al rotor opciones para describir una imagen o la pantalla completa y hacerle preguntas. Según {a(AFB27, 'la American Foundation for the Blind')}, varias de estas funciones necesitan un iPhone 15 Pro o más nuevo. No pude confirmar si ya funcionan en español.</li>"
   "</ul>"]),
  ("Para leer y reconocer cosas", [
   "<ul>"
   f"<li>✅ <b>Seeing AI</b> (Microsoft, gratis, en español). Lee texto corto y documentos, describe fotos y escenas, y reconoce colores, billetes y productos por su código de barras. {a(ONCE_SEEING, 'La ONCE de España la evaluó')} y la considera accesible para personas ciegas, con algunos detalles por mejorar. Es la primera que conviene instalar.</li>"
   f"<li>✅ <b>Be My Eyes</b> (gratis). Videollamada con una persona voluntaria que ve por la cámara, y un asistente de inteligencia artificial que describe fotos. {a(BME, 'Sus términos')} dicen que es para personas de 18 años o más: úsala tú, con ella al lado.</li>"
   "<li>🟡 <b>Envision.</b> Parecida a Seeing AI: lee texto y describe escenas. No revisé su precio actual ni su español.</li>"
   "</ul>"]),
  ("Para moverse", [
   "<ul><li>🟢 <b>Lazarillo</b> (gratis, hecha en Chile, en español). Un GPS que dice en voz alta las calles, los cruces y los lugares cercanos. Para ella, por ahora, solo caminando con un adulto. No revisé qué tan completos están sus datos en su ciudad: pruébenla en una calle que conozcan.</li></ul>"]),
  ("Para aprender VoiceOver jugando", [
   "<ul>"
   f"<li>🟡 <b>Ballyland Mágico</b> (Sonokids). Un juego en español hecho para que niños ciegos aprendan los gestos de VoiceOver: arrastrar un dedo, dos toques, deslizar con uno y con tres dedos. {a(SONOKIDS, 'Su página')} lo presenta como juego para iPad, no para iPhone, y no la actualizan desde 2020: revisa en la App Store si sigue disponible.</li>"
   "<li>✅ <b>Práctica de VoiceOver.</b> Está en <span class=\"path\">Configuración → Accesibilidad → VoiceOver</span>. Ella hace un gesto y el iPhone le dice cuál fue, sin abrir nada. Gratis y siempre a la mano.</li>"
   "</ul>"]),
  ("Para escuchar", [
   "<ul>"
   "<li>✅ <b>Podcasts</b> (de Apple, gratis). La lista de programas en español para su edad está en las notas de la Lección 10.</li>"
   "<li>✅ <b>Música</b> (de Apple). Pedirle música a Siri necesita suscripción a Apple Music.</li>"
   "</ul>"]),
  ("Cómo saber si una app nueva le va a servir", [
   "<ul>"
   f"<li><b>Mira la sección Accesibilidad en la App Store.</b> Desde iOS 26, los desarrolladores pueden declarar en la página de su app si funciona con VoiceOver. Es opcional y todavía pocas apps lo llenan ({a(AFB26, 'American Foundation for the Blind')}).</li>"
   "<li><b>Pruébala tú con VoiceOver encendido.</b> Desliza a la derecha por la primera pantalla. Si los botones dicen su nombre («Reproducir», «Enviar»), va bien. Si solo dice «botón, botón», no le va a servir.</li>"
   "<li><b>Busca la app en AppleVis</b> (applevis.com), un sitio en inglés donde personas ciegas califican qué tan bien funciona cada app con VoiceOver.</li>"
   "</ul>"]),
  ("De dónde sale el método del curso", [
   "<ul>"
   f"<li>{a(CNIB, 'ABCs of iOS')}, manual de la CNIB de Canadá para enseñar VoiceOver a niños pequeños: practicar el gesto fuera de la pantalla, toque suave, tu mano debajo de la suya, pasos chicos y mucha repetición, y no mover las apps de lugar.</li>"
   f"<li>{a(PATHS, 'Lista de habilidades de iOS')}, de Paths to Literacy (Perkins School for the Blind): el orden en que se aprenden los gestos, el rotor y las apps de todos los días.</li>"
   f"<li>Manual del iPhone de Apple: {a(APPLE_GESTOS, 'gestos')}, {a(APPLE_ROTOR, 'rotor')} y {a(APPLE_TECLADO, 'teclado')}.</li>"
   "</ul>"]),
 ])
