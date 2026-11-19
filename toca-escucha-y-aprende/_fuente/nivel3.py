# Toca, escucha y aprende · Nivel 3 · lecciones 13 a 18.
# Español de México. Habla con ella (tú) y con mamá (tú). Sin nombres.
# Gestos y nombres revisados contra el Manual del iPhone de Apple (es-lamr), noviembre de 2026.

G = "https://support.apple.com/es-lamr/guide/iphone/%s/ios"
APPLE_CENTROS = "https://support.apple.com/es-lamr/HT202364"

def a(url, texto):
    return f'<a href="{url}">{texto}</a>'

LECCIONES3 = [
# ───────────────────────── LECCIÓN 13 ─────────────────────────
dict(num=13, titulo="Tu seguridad", nivel="c",
 apple=[("Usar Emergencia SOS en el iPhone", G % "iph3c99374c"), ("Configurar y consultar tu ficha médica", G % "iph08022b192"), ("Compartir la ubicación en Encontrar", G % "iph01954dc44")],
 intro="Bienvenida al Nivel 3. Hoy aprendes a pedir ayuda con tu iPhone. Elige una burbuja.",
 secciones=[
  dict(nombre="Historia", pantallas=[
   dict(t="texto", text="Tu iPhone te puede ayudar si algún día necesitas ayuda de verdad. Hoy aprendes tres cosas de seguridad."),
   dict(t="texto", text="La llamada de emergencia: deja apretados al mismo tiempo el botón lateral y un botón de volumen. El iPhone cuenta hacia atrás y llama al 911."),
   dict(t="texto", text="Solo es para una emergencia de verdad: si alguien está herido, si hay fuego o si estás en peligro. Si la activas sin querer, suelta los botones antes de que termine la cuenta."),
   dict(t="texto", text="Cuando termina una llamada de emergencia, tu iPhone le manda un mensaje a mamá con tu ubicación."),
   dict(t="texto", text="Con la app Encontrar, mamá puede saber dónde estás. No es para espiarte: es para que siempre te pueda encontrar."),
   dict(t="texto", text="Tu ficha médica guarda tus datos de salud y el número de mamá. Si algún día no puedes hablar, quien te ayude la puede ver."),
   dict(t="salud", titulo="Tip de salud", text="Cuidarte también es estar lista. Antes de salir, pregúntale a Siri cuánta batería tienes. Si queda poca, carga tu iPhone."),
  ]),
  dict(nombre="Juego", pantallas=[
   dict(t="texto", titulo="Juego: seguridad", text="Seis preguntas. Una es de encontrar un número."),
   dict(t="pregunta", text="La llamada de emergencia es solo para un peligro de verdad.", ok=True, fb="¡Cierto! No es para jugar ni para probar."),
   dict(t="pregunta", text="Para llamar a emergencias aprietas juntos el botón lateral y un botón de volumen.", ok=True, fb="¡Cierto! Y los dejas apretados mientras cuenta."),
   dict(t="busca", text="Encuentra el número de emergencias en México.", opciones=["123","911","100","555"], correcta="911"),
   dict(t="pregunta", text="Si la activas sin querer, puedes soltar los botones antes de que termine la cuenta.", ok=True, fb="¡Cierto! Así no se hace la llamada."),
   dict(t="pregunta", text="Mamá puede ver dónde estás para espiarte.", ok=False, fb="¡Bien! Es falso. Es para que siempre te pueda encontrar."),
   dict(t="pregunta", text="Tu ficha médica nadie la puede ver nunca.", ok=False, fb="¡Bien! Es falso. Se puede ver en una emergencia, para que te ayuden."),
  ]),
  dict(nombre="Reto", pantallas=[
   dict(t="texto", titulo="Tu reto de hoy", text="Con mamá, sin llamar: pon un dedo en el botón lateral y otro en un botón de volumen. ¡No aprietes! Solo aprende dónde van. Después dile a mamá su número de teléfono de memoria."),
  ]),
 ],
 despedida="En la próxima lección aprendes a contestar llamadas y a hacer videollamadas.",
 mama=[
  ("Su salud y su seguridad", [
   "<p>Para una niña con discapacidad visual, saber pedir ayuda vale más que cualquier app. Esta lección se explica con calma y en serio, sin asustarla: es una herramienta, como saber su dirección.</p>"]),
  ("De qué trata esta lección", [
   "<ul><li><b>Llamada de emergencia:</b> se dejan apretados al mismo tiempo el botón lateral y cualquier botón de volumen. Aparece una cuenta regresiva y, si sigue apretando, el iPhone llama al 911. Al terminar, le manda un mensaje con su ubicación a sus contactos de emergencia.</li><li><b>Ubicación:</b> en la app Encontrar, ustedes dos comparten la ubicación.</li><li><b>Ficha médica:</b> en la app Salud, con sus datos y tu número.</li></ul>"]),
  ("Antes de empezar", [
   "<ul><li><b>Su ficha médica:</b> en su iPhone, abre la app Salud y busca la ficha médica. Escribe su nombre, alergias si tiene, que tiene discapacidad visual y que usa VoiceOver, y agrégate como contacto de emergencia. Activa la opción para que se pueda ver con el teléfono bloqueado.</li><li><b>Ubicación:</b> en la app Encontrar, en Personas, compartan su ubicación entre ustedes.</li><li><b>Emergencia SOS:</b> en Configuración busca «Emergencia SOS». Deja activada la llamada al mantener presionados los botones. La opción de llamar con cinco pulsaciones déjala apagada al principio, para que no llame sin querer.</li></ul>"]),
  ("Cómo acompañarla", [
   "<ul><li><b>No hagan una llamada de prueba.</b> El reto es solo poner los dedos en su lugar, sin apretar.</li><li><b>Si llega a llamar sin querer, no cuelguen:</b> expliquen al 911 que fue un error.</li><li><b>Su número de memoria:</b> que aprenda tu teléfono como aprende una canción. Si un día no tiene el iPhone, lo va a necesitar.</li></ul>"]),
  ("Palabras de esta lección", [
   "<dl><dt>Emergencia SOS</dt><dd>La llamada de emergencia con los botones.</dd><dt>Encontrar</dt><dd>La app para compartir la ubicación.</dd><dt>Ficha médica</dt><dd>Sus datos de salud en la app Salud, para una emergencia.</dd></dl>"]),
 ]),

# ───────────────────────── LECCIÓN 14 ─────────────────────────
dict(num=14, titulo="Llamadas y FaceTime", nivel="c",
 apple=[("Contestar o rechazar llamadas entrantes", G % "iph3c9947bf"), ("Realizar llamadas de FaceTime", G % "iph7801d5771")],
 intro="Hoy aprendes a contestar, a colgar y a hacer videollamadas. Elige una burbuja.",
 secciones=[
  dict(nombre="Historia", pantallas=[
   dict(t="texto", text="Hoy aprendes a contestar y a colgar llamadas, y a hacer videollamadas con FaceTime."),
   dict(t="texto", text="Cuando suena tu iPhone, VoiceOver te dice quién llama. Para contestar, toca dos veces con dos dedos."),
   dict(t="texto", text="Para colgar, el mismo gesto: dos toques con dos dedos. Es el gesto que también pausa la música."),
   dict(t="texto", text="Para llamar, dile a Siri: «Llama a mamá». También puedes abrir la app Teléfono y buscar el contacto."),
   dict(t="texto", text="FaceTime es una llamada con video: la otra persona te ve. Di «Oye Siri, haz una llamada de FaceTime a mamá»."),
   dict(t="texto", text="En FaceTime, sostén el iPhone frente a tu cara, a la altura de tus ojos. Si no sabes si se te ve bien, pregunta: «¿Me ves bien?»"),
   dict(t="salud", titulo="Tip de salud", text="Platicar con quien quieres te pone de buen humor. Esta semana llama a alguien de tu familia, solo para platicar."),
  ]),
  dict(nombre="Juego", pantallas=[
   dict(t="texto", titulo="Juego: llamadas", text="Seis preguntas. Una es de encontrar una app."),
   dict(t="pregunta", text="Para contestar una llamada tocas dos veces con dos dedos.", ok=True, fb="¡Cierto! Y con el mismo gesto cuelgas."),
   dict(t="pregunta", text="Contestar y colgar usan el mismo gesto.", ok=True, fb="¡Cierto! Dos toques con dos dedos."),
   dict(t="busca", text="Encuentra la app de las videollamadas.", opciones=["Mensajes","Teléfono","FaceTime","Reloj"], correcta="FaceTime"),
   dict(t="pregunta", text="En FaceTime la otra persona te puede ver.", ok=True, fb="¡Cierto! Por eso el iPhone va frente a tu cara."),
   dict(t="pregunta", text="Para una videollamada, el iPhone va en la mesa, lejos de tu cara.", ok=False, fb="¡Bien! Es falso. Va frente a tu cara, a la altura de tus ojos."),
   dict(t="pregunta", text="VoiceOver te dice quién te llama, si está en tus contactos.", ok=True, fb="¡Cierto! Por eso es bueno guardar los números con su nombre."),
  ]),
  dict(nombre="Reto", pantallas=[
   dict(t="texto", titulo="Tu reto de hoy", text="Pídele a mamá que te llame. Contesta con dos toques de dos dedos, platiquen un momento y cuelga tú. Después haz una llamada de FaceTime a mamá con Siri."),
  ]),
 ],
 despedida="En la próxima lección descubres dos lugares escondidos arriba de la pantalla.",
 mama=[
  ("Su salud: platicar", [
   "<p>Las llamadas la conectan con su familia y sus amigos, y eso le hace bien. Anímala a llamar a alguien que quiera, aunque sea un ratito.</p>"]),
  ("De qué trata esta lección", [
   "<p>Contestar y colgar con dos toques de dos dedos, llamar con Siri o con la app Teléfono, y hacer videollamadas de FaceTime.</p>",
   "<p>El botón lateral también cuelga una llamada. Le enseñamos los dos toques porque es el mismo gesto en todas las apps.</p>"]),
  ("Antes de empezar", [
   "<ul><li><b>Contactos con nombre:</b> guarda en su iPhone los números de la familia con su nombre bien escrito, para que VoiceOver diga quién llama.</li><li><b>Que anuncie las llamadas:</b> en Configuración busca «Anunciar llamadas» y elige Siempre. Así oye quién llama aunque no tenga el teléfono en la mano.</li><li><b>FaceTime:</b> en Configuración busca «FaceTime» y revisa que esté activado.</li></ul>"]),
  ("Cómo acompañarla", [
   "<ul><li><b>En FaceTime, dile qué ves:</b> «solo te veo la frente», «ahora sí te veo la cara». Así aprende a acomodar el teléfono.</li><li><b>Llámala tú</b> desde otro cuarto para practicar contestar, varias veces.</li></ul>"]),
  ("Gestos de esta lección", [
   "<dl><dt>Dos toques con dos dedos</dt><dd>Contestar o colgar.</dd><dt>«Oye Siri, llama a mamá»</dt><dd>Llamar.</dd><dt>«Oye Siri, haz una llamada de FaceTime a mamá»</dt><dd>Videollamada.</dd></dl>"]),
 ]),

# ───────────────────────── LECCIÓN 15 ─────────────────────────
dict(num=15, titulo="Avisos y botones rápidos", nivel="c",
 apple=[("Abrir el Centro de notificaciones y el Centro de control con VoiceOver", APPLE_CENTROS), ("Ver y responder a las notificaciones", G % "iph6534c01bc"), ("Usar y personalizar el centro de control", G % "iph59095ec58")],
 intro="Hoy descubres dos lugares escondidos arriba de la pantalla. Elige una burbuja.",
 secciones=[
  dict(nombre="Historia", pantallas=[
   dict(t="texto", text="Tu iPhone tiene dos lugares escondidos: el Centro de notificaciones y el Centro de control."),
   dict(t="texto", text="Las notificaciones son avisos: un mensaje nuevo, una alarma, un recordatorio. Se juntan en el Centro de notificaciones."),
   dict(t="texto", text="Para abrirlo: toca la parte de arriba de la pantalla, donde está la hora. Luego desliza tres dedos hacia abajo."),
   dict(t="texto", text="Desliza a la derecha para oír cada aviso. Para cerrar, haz el gesto de la goma: dos dedos de un lado a otro."),
   dict(t="texto", text="El Centro de control tiene botones rápidos: el volumen, la linterna, el modo avión y No molestar."),
   dict(t="texto", text="Para abrirlo: toca arriba, donde está la hora. Luego desliza tres dedos hacia arriba desde la parte de abajo."),
   dict(t="salud", titulo="Tip de salud", text="Los avisos en la noche no te dejan descansar. Antes de dormir, abre el Centro de control y activa No molestar."),
  ]),
  dict(nombre="Juego", pantallas=[
   dict(t="texto", titulo="Juego: avisos", text="Seis preguntas. Una es de encontrar un botón."),
   dict(t="pregunta", text="Los avisos de mensajes nuevos se juntan en el Centro de notificaciones.", ok=True, fb="¡Cierto! Ahí los escuchas todos juntos."),
   dict(t="pregunta", text="Para abrir el Centro de notificaciones tocas donde está la hora y deslizas tres dedos hacia abajo.", ok=True, fb="¡Cierto! Hacia abajo, las notificaciones."),
   dict(t="busca", text="Encuentra el botón que prende la linterna.", opciones=["Modo avión","Linterna","Volumen","Cámara"], correcta="Linterna"),
   dict(t="pregunta", text="No molestar hace que el iPhone no te interrumpa con avisos.", ok=True, fb="¡Cierto! Es bueno para la noche."),
   dict(t="pregunta", text="El modo avión sirve para hacer llamadas más rápido.", ok=False, fb="¡Bien! Es falso. El modo avión apaga las llamadas y el internet."),
   dict(t="pregunta", text="Para cerrar el Centro de notificaciones usas el gesto de la goma.", ok=True, fb="¡Cierto! Dos dedos de un lado a otro."),
  ]),
  dict(nombre="Reto", pantallas=[
   dict(t="texto", titulo="Tu reto de hoy", text="Abre el Centro de notificaciones y escucha tus avisos. Ciérralo con la goma. Después abre el Centro de control, busca No molestar y escucha si está activado. ¡No cambies nada más!"),
  ]),
 ],
 despedida="En la próxima lección ajustas VoiceOver a tu gusto.",
 mama=[
  ("Su salud: el descanso", [
   "<p>Los avisos en la noche interrumpen el sueño. Programen juntas el modo Dormir o No molestar para la hora de dormir, y quiten los avisos de juegos o apps que no necesita.</p>"]),
  ("De qué trata esta lección", [
   "<ul><li><b>Centro de notificaciones:</b> tocar arriba, donde está la hora, y deslizar tres dedos hacia abajo.</li><li><b>Centro de control:</b> tocar arriba y deslizar tres dedos hacia arriba desde la parte de abajo.</li><li><b>Cerrar:</b> el gesto de la goma, dos dedos de un lado a otro.</li></ul>",
   f"<p>Son los pasos de la {a(APPLE_CENTROS, 'guía de Apple para VoiceOver')}.</p>"]),
  ("Antes de empezar", [
   "<ul><li><b>Menos avisos:</b> en Configuración busca «Notificaciones» y apaga los de apps que ella no necesita. Menos avisos es más fácil de escuchar.</li><li><b>Modo avión:</b> si un día no puede llamar ni recibir mensajes, revisen en el Centro de control que el modo avión esté apagado.</li></ul>"]),
  ("Cómo acompañarla", [
   "<ul><li><b>El reto es solo escuchar.</b> Que no cambie botones del Centro de control todavía.</li><li><b>Si se abre otra cosa,</b> casi siempre es porque no tocó primero donde está la hora. Que empiece otra vez.</li></ul>"]),
 ]),

# ───────────────────────── LECCIÓN 16 ─────────────────────────
dict(num=16, titulo="Tu VoiceOver a tu manera", nivel="c",
 apple=[("Cambiar la configuración de VoiceOver", G % "iphfa3d32c50"), ("Controlar VoiceOver con el rotor", G % "iph3e2e3a6d")],
 intro="Hoy ajustas VoiceOver a tu gusto. Elige una burbuja.",
 secciones=[
  dict(nombre="Historia", pantallas=[
   dict(t="texto", text="VoiceOver se puede ajustar a tu gusto: más rápido o más lento, con otra voz, o que hable más o menos."),
   dict(t="texto", text="La velocidad ya la conoces: gira el rotor hasta «Velocidad de habla» y desliza un dedo hacia arriba o hacia abajo."),
   dict(t="texto", text="Para cambiar la voz: abre Configuración, Accesibilidad, VoiceOver, y busca Voz. Ahí puedes probar voces en español."),
   dict(t="texto", text="Algunas voces dicen «Mejorada» o «Premium». Suenan más naturales, pero hay que descargarlas. Pídele permiso a mamá."),
   dict(t="texto", text="La verbosidad es cuánto habla VoiceOver. Con las indicaciones encendidas, te dice qué puedes hacer con cada botón."),
   dict(t="texto", text="Cortina de pantalla: toca tres veces con tres dedos y la pantalla se pone negra. VoiceOver sigue funcionando y nadie ve lo que haces."),
   dict(t="salud", titulo="Tip de salud", text="Tus oídos también descansan. Después de un buen rato escuchando, quédate unos minutos sin audífonos y sin voz."),
  ]),
  dict(nombre="Juego", pantallas=[
   dict(t="texto", titulo="Juego: a tu manera", text="Seis preguntas. Una es de encontrar un ajuste."),
   dict(t="pregunta", text="Con el rotor puedes hacer que VoiceOver hable más rápido.", ok=True, fb="¡Cierto! Con «Velocidad de habla»."),
   dict(t="pregunta", text="Todas las voces ya vienen descargadas.", ok=False, fb="¡Bien! Es falso. Las Mejoradas y Premium hay que descargarlas."),
   dict(t="busca", text="Encuentra el ajuste de la rapidez de la voz.", opciones=["Voz","Velocidad de habla","Verbosidad","Volumen"], correcta="Velocidad de habla"),
   dict(t="pregunta", text="Con la cortina de pantalla, la pantalla se pone negra pero VoiceOver sigue funcionando.", ok=True, fb="¡Cierto! Y nadie ve lo que haces."),
   dict(t="pregunta", text="Para la cortina de pantalla tocas tres veces con tres dedos.", ok=True, fb="¡Cierto! Y otra vez igual para quitarla."),
   dict(t="pregunta", text="Las indicaciones te dicen qué puedes hacer con cada botón.", ok=True, fb="¡Cierto! Son parte de la verbosidad."),
  ]),
  dict(nombre="Reto", pantallas=[
   dict(t="texto", titulo="Tu reto de hoy", text="Con mamá: prueba tres voces en español y elige tu favorita. Después pon la cortina de pantalla, abre una app y quita la cortina otra vez."),
  ]),
 ],
 despedida="En la próxima lección tu cámara te cuenta lo que hay frente a ti.",
 mama=[
  ("Su salud: descansar los oídos", [
   "<p>Ella escucha muchas horas al día. Que haga pausas sin audífonos y con el volumen bajo, y que la voz vaya a una velocidad cómoda, no forzada.</p>"]),
  ("De qué trata esta lección", [
   "<p>Velocidad con el rotor, elegir voz, la verbosidad y la cortina de pantalla. Todo está en <span class=\"path\">Configuración → Accesibilidad → VoiceOver</span>.</p>"]),
  ("Antes de empezar", [
   "<ul><li><b>Voces nuevas:</b> las voces Mejoradas y Premium se descargan. Háganlo con Wi-Fi.</li><li><b>Cortina de pantalla:</b> si un día tú necesitas ver la pantalla y está negra, toca tres veces con tres dedos, o apaga VoiceOver con los tres clics del botón lateral.</li></ul>"]),
  ("Cómo acompañarla", [
   "<ul><li><b>Que elija ella.</b> La voz y la velocidad son gustos personales. Con el tiempo, casi todos suben la velocidad.</li><li><b>La cortina es privacidad:</b> explícale que sirve cuando hay gente cerca.</li></ul>"]),
  ("Gestos de esta lección", [
   "<dl><dt>Rotor en «Velocidad de habla»</dt><dd>Un dedo arriba o abajo para cambiarla.</dd><dt>Tres toques con tres dedos</dt><dd>Poner o quitar la cortina de pantalla.</dd></dl>"]),
 ]),

# ───────────────────────── LECCIÓN 17 ─────────────────────────
dict(num=17, titulo="La cámara que ve por ti", nivel="c",
 apple=[("Escuchar lo que hay en la pantalla y en el entorno con VoiceOver", G % "iph37e6b3844"), ("Detectar puertas, personas y muebles con Lupa", G % "iph35c335575"), ("Lupa en el iPhone", G % "iphe867dc99c")],
 intro="Hoy tu cámara te cuenta lo que hay frente a ti. Elige una burbuja.",
 secciones=[
  dict(nombre="Historia", pantallas=[
   dict(t="texto", text="La cámara de tu iPhone puede contarte qué hay frente a ti: escenas, personas, objetos y letras."),
   dict(t="texto", text="Con VoiceOver encendido, toca tres veces con cuatro dedos. Así empieza el reconocimiento en vivo."),
   dict(t="texto", text="Apunta la cámara de atrás hacia algo y mueve el iPhone despacio. VoiceOver te dice lo que ve."),
   dict(t="texto", text="Para terminar, otra vez: tres toques con cuatro dedos."),
   dict(t="texto", text="La app Lupa también describe lo que ve y lee letras en voz alta, como una etiqueta o un letrero."),
   dict(t="texto", text="Muy importante: la cámara a veces se equivoca. Úsala para conocer cosas, nunca para cruzar la calle ni para caminar por lugares nuevos."),
   dict(t="salud", titulo="Tip de salud", text="Practica con la cámara en el patio por la mañana. Aprendes algo nuevo y tomas la luz del día."),
  ]),
  dict(nombre="Juego", pantallas=[
   dict(t="texto", titulo="Juego: la cámara", text="Seis preguntas. Una es de encontrar una app."),
   dict(t="pregunta", text="Tres toques con cuatro dedos encienden el reconocimiento en vivo.", ok=True, fb="¡Cierto! Y otros tres toques lo apagan."),
   dict(t="pregunta", text="La cámara siempre acierta.", ok=False, fb="¡Bien! Es falso. A veces se equivoca."),
   dict(t="busca", text="Encuentra la app que describe lo que ve y lee letras.", opciones=["Lupa","Reloj","Música","Notas"], correcta="Lupa"),
   dict(t="pregunta", text="Puedes usar la cámara para cruzar la calle sola.", ok=False, fb="¡Bien! Es falso. Para cruzar la calle siempre con alguien."),
   dict(t="pregunta", text="Hay que mover el iPhone despacio para que la cámara entienda.", ok=True, fb="¡Cierto! Despacio y con buena luz."),
   dict(t="pregunta", text="La luz de la mañana es buena para tu cuerpo.", ok=True, fb="¡Cierto! Y en la noche duermes mejor."),
  ]),
  dict(nombre="Reto", pantallas=[
   dict(t="texto", titulo="Tu reto de hoy", text="Con mamá en la cocina: enciende el reconocimiento en vivo y descubre tres cosas. Después usa la Lupa para que te lea la etiqueta de una caja o de una lata."),
  ]),
 ],
 despedida="En la última lección del nivel escribes braille en la pantalla.",
 mama=[
  ("Su salud y su seguridad", [
   "<p>Apple advierte que no hay que depender del reconocimiento en situaciones de riesgo, ni para orientarse al caminar. La cámara es para conocer y leer cosas; para moverse por la calle, siempre con alguien.</p>"]),
  ("De qué trata esta lección", [
   "<ul><li><b>Reconocimiento en vivo:</b> con VoiceOver encendido, tres toques con cuatro dedos. Describe escenas, personas, puertas, muebles o texto.</li><li><b>Lupa:</b> la app que describe lo que ve y lee texto en voz alta.</li></ul>",
   "<p>🟡 La detección de personas, puertas y muebles solo funciona en algunos modelos de iPhone. En el suyo puede no aparecer; la descripción de escenas y la lectura de texto sí.</p>"]),
  ("Antes de empezar", [
   "<ul><li><b>Buena luz:</b> la cámara entiende mejor de día o con la luz prendida.</li><li><b>Botón de Acción:</b> si quieren, en Configuración busquen «Botón de Acción» y asígnenle la Lupa. Así la abre sin buscarla.</li></ul>"]),
  ("Cómo acompañarla", [
   "<ul><li><b>Pruébenlo con cosas que ella ya conoce,</b> para que note cuando la cámara se equivoca.</li><li><b>Etiquetas de comida:</b> la Lupa lee letras impresas. Busquen la parte con letras grandes.</li><li>Para más ayuda con la cámara, revisen la página de apps recomendadas (Be My Eyes y Seeing AI).</li></ul>"]),
  ("Gestos de esta lección", [
   "<dl><dt>Tres toques con cuatro dedos</dt><dd>Encender o apagar el reconocimiento en vivo.</dd><dt>Mover el iPhone despacio</dt><dd>Para que la cámara entienda.</dd></dl>"]),
 ]),

# ───────────────────────── LECCIÓN 18 ─────────────────────────
dict(num=18, titulo="Escribe en braille", nivel="c",
 apple=[("Escribir Braille directamente en la pantalla con VoiceOver", G % "iph10366cc30"), ("Usar una pantalla Braille", G % "iph73b8c43")],
 intro="Hoy escribes braille en la pantalla de tu iPhone. Elige una burbuja.",
 secciones=[
  dict(nombre="Historia", pantallas=[
   dict(t="texto", text="Tú ya sabes braille. Hoy aprendes a escribirlo en la pantalla de tu iPhone, sin papel y sin máquina."),
   dict(t="texto", text="La pantalla se convierte en una celda de seis puntos. Cada dedo es un punto."),
   dict(t="texto", text="Primero entra a un lugar para escribir, como un mensaje nuevo. Luego gira el rotor hasta oír «Ingreso de Braille»."),
   dict(t="texto", text="Pon el iPhone en la mesa, con la pantalla hacia arriba. Tres dedos de la mano izquierda son los puntos 1, 2 y 3. Tres de la derecha, los puntos 4, 5 y 6."),
   dict(t="texto", text="Para una letra, toca todos sus puntos al mismo tiempo, como un acorde. La a es solo el punto 1."),
   dict(t="texto", text="Espacio: desliza un dedo a la derecha. Borrar: un dedo a la izquierda. Nueva línea: dos dedos a la derecha."),
   dict(t="texto", text="En Mensajes, desliza tres dedos hacia arriba para enviar. Para salir del braille, haz el gesto de la goma con dos dedos."),
   dict(t="salud", titulo="Tip de salud", text="Antes de escribir, calienta las manos: abre y cierra los dedos diez veces, y sacude las manos."),
  ]),
  dict(nombre="Juego", pantallas=[
   dict(t="texto", titulo="Juego: braille", text="Seis preguntas. Dos son de encontrar un gesto."),
   dict(t="pregunta", text="Para escribir braille en la pantalla giras el rotor hasta «Ingreso de Braille».", ok=True, fb="¡Cierto! Dentro de un lugar para escribir."),
   dict(t="pregunta", text="Cada dedo es un punto de la celda.", ok=True, fb="¡Cierto! Seis dedos, seis puntos."),
   dict(t="pregunta", text="Para una letra tocas sus puntos uno por uno, despacio.", ok=False, fb="¡Bien! Es falso. Se tocan todos al mismo tiempo."),
   dict(t="busca", text="Encuentra el gesto para poner un espacio.", opciones=["Un dedo a la izquierda","Un dedo a la derecha","Dos dedos a la derecha","Tres dedos arriba"], correcta="Un dedo a la derecha"),
   dict(t="pregunta", text="Deslizar un dedo a la izquierda borra.", ok=True, fb="¡Cierto! Borra lo último que escribiste."),
   dict(t="busca", text="Encuentra el gesto para enviar un mensaje.", opciones=["Un dedo a la derecha","Dos dedos a la derecha","Tres dedos arriba","Goma con dos dedos"], correcta="Tres dedos arriba"),
  ]),
  dict(nombre="Reto", pantallas=[
   dict(t="texto", titulo="Reto final", text="Abre un mensaje nuevo para mamá. Escribe en braille: hola mamá. Envíalo deslizando tres dedos hacia arriba."),
  ]),
 ],
 despedida="¡Terminaste el Nivel 3! Ya pides ayuda, contestas llamadas, ajustas VoiceOver, usas la cámara y escribes en braille.",
 mama=[
  ("Su salud: manos descansadas", [
   "<p>Escribir con seis dedos en un vidrio cansa las manos. Pausas cortas, sacudir las manos, y sesiones breves al principio.</p>"]),
  ("De qué trata esta lección", [
   "<p>Escribir en braille directo en la pantalla, como en una máquina Perkins: seis dedos, seis puntos, y los puntos de cada letra se tocan al mismo tiempo. Solo tiene sentido porque ella ya está aprendiendo braille.</p>",
   "<ul><li><b>Entrar:</b> en un lugar para escribir, girar el rotor hasta «Ingreso de Braille».</li><li><b>Espacio:</b> un dedo a la derecha. <b>Borrar:</b> un dedo a la izquierda. <b>Nueva línea:</b> dos dedos a la derecha.</li><li><b>Enviar en Mensajes:</b> tres dedos hacia arriba.</li><li><b>Salir:</b> el gesto de la goma con dos dedos.</li></ul>"]),
  ("Antes de empezar", [
   "<ul><li><b>Agregar al rotor:</b> en <span class=\"path\">Configuración → Accesibilidad → VoiceOver → Rotor</span>, en Elementos del rotor, activa «Ingreso de Braille».</li><li><b>Tipo de braille:</b> en <span class=\"path\">Configuración → Accesibilidad → VoiceOver → Braille</span> revisen el idioma y si usa braille contraído o no. Pregúntenle a su maestra de braille cuál usa.</li><li><b>Posición:</b> en la mesa con la pantalla hacia arriba es lo más fácil para empezar. También se puede sostener de lado, con la pantalla hacia afuera.</li></ul>"]),
  ("Cómo acompañarla", [
   "<ul><li><b>Su maestra de braille es la experta.</b> Compártanle esta lección; puede practicar con ella.</li><li><b>Si las letras salen mal,</b> casi siempre es porque los dedos no tocaron al mismo tiempo, o el iPhone necesita ubicar de nuevo sus dedos. La guía de Apple explica cómo.</li><li><b>Más adelante:</b> si usa una pantalla braille en la escuela, se puede conectar al iPhone.</li></ul>"]),
  ("Qué sigue", [
   "<p>Con el Nivel 3 terminado, ella ya usa su iPhone con independencia. Lo que sigue es practicar todos los días en apps reales, a su ritmo.</p>"]),
 ]),
]
