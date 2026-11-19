# Mamá aprende iPhone · contenido de las lecciones.
# Español de México. Habla con mamá (tú). Sin nombres. Solo apps de Apple (nada de Meta).
# Rutas de Configuración: cuando Apple las cambia seguido, se enseña a usar la búsqueda de Configuración.

G = "https://support.apple.com/es-lamr/guide/iphone/%s/ios"
TOCA = "../toca-escucha-y-aprende/"

def toca(n, titulo):
    return f'<a href="{TOCA}leccion-{n}.html">Lección {n} · {titulo}</a>'

def pasos(*items):
    return '<ol class="steps">' + ''.join(f'<li>{i}</li>' for i in items) + '</ol>'

def lista(*items):
    return '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'

R = '<span class="path">%s</span>'

PARTES = [
 ("Parte 1 · Tu iPhone, paso a paso", "Para que tú uses tu iPhone con confianza."),
 ("Parte 2 · Cómo enseñarle a ella", "Para acompañar a tu hija con «Toca, escucha y aprende»."),
]

LECCIONES = [
# ───────────── PARTE 1 ─────────────
dict(num=1, parte=1, titulo="Conoce tu iPhone",
 intro="Las partes de tu iPhone, cómo encenderlo, cargarlo y abrirlo.",
 secciones=[
  ("Las partes", [lista(
    "<b>La pantalla:</b> el vidrio del frente. Ahí tocas con el dedo.",
    "<b>Del lado derecho:</b> el botón lateral. Enciende y apaga la pantalla.",
    "<b>Del lado izquierdo:</b> arriba, el botón de Acción (normalmente pone el teléfono en silencio). Abajo, los dos botones de volumen: el de arriba sube y el de abajo baja.",
    "<b>Abajo:</b> el puerto para cargar, en el centro, y las bocinas.",
    "<b>Atrás:</b> la cámara, en una esquina de arriba.")]),
  ("Encender, apagar y la pantalla", [lista(
    "<b>Prender la pantalla:</b> aprieta una vez el botón lateral. Otra vez, y se apaga. El teléfono sigue encendido.",
    "<b>Encender el iPhone:</b> deja apretado el botón lateral hasta que aparezca la manzana.",
    "<b>Apagarlo:</b> deja apretados al mismo tiempo el botón lateral y un botón de volumen, y desliza «apagar». Suéltalos en cuanto aparezca: si los sigues apretando, el iPhone empieza a llamar a emergencias.")]),
  ("Abrir el iPhone", [pasos(
    "Prende la pantalla con el botón lateral.",
    "Mira el iPhone: Face ID reconoce tu cara y se abre el candado.",
    "Desliza un dedo desde el borde de abajo hacia arriba.",
    "Si te pide el código, escribe tus números.")]),
  ("Cargar", [lista(
    "Conecta el cable en el puerto de abajo y el otro lado al cargador.",
    "Arriba a la derecha está el dibujo de la batería. Cuando carga, aparece un rayito.",
    "Puedes usarlo mientras carga.")]),
 ],
 practica="Apaga la pantalla y préndela. Sube el volumen y bájalo. Abre tu iPhone con tu cara.",
 problemas=lista("<b>No prende:</b> cárgalo media hora y deja apretado el botón lateral.", "<b>Face ID no te reconoce:</b> escribe tu código; es normal de vez en cuando."),
 hija=f"Ella aprende las mismas partes con las manos en la {toca(3,'Conoce tu iPhone con las manos')}. Ve tú primero, así le puedes decir dónde está cada cosa sin tocarle las manos.",
 apple=[("Encender y configurar el iPhone", G % "iph1fd7e482f")]),

dict(num=2, parte=1, titulo="Tocar y deslizar",
 intro="Los movimientos del dedo que se usan en todo el iPhone.",
 secciones=[
  ("Los movimientos básicos", [lista(
    "<b>Tocar:</b> un toque rápido abre una app o presiona un botón.",
    "<b>Deslizar:</b> pon el dedo y muévelo hacia arriba, abajo o a los lados, para mover la pantalla.",
    "<b>Mantener presionado:</b> deja el dedo quieto un segundo para ver más opciones.")]),
  ("Ir a la pantalla de inicio", [
    "<p>La pantalla de inicio es donde están todas las apps. Para regresar ahí desde cualquier lugar, <b>desliza un dedo desde el borde de abajo hacia arriba</b>.</p>"]),
  ("Regresar", [lista(
    "Muchas apps tienen arriba a la izquierda una flecha «‹» o la palabra «Atrás». Tócala.",
    "También puedes deslizar el dedo desde el borde izquierdo hacia la derecha.")]),
  ("Cambiar de app", [
    "<p>Desliza desde abajo hacia arriba y <b>deja el dedo quieto a la mitad</b>. Aparecen las apps abiertas; desliza a los lados y toca la que quieres.</p>"]),
  ("Los dos lugares de arriba", [lista(
    "<b>Avisos (Centro de notificaciones):</b> desliza desde arriba al centro, hacia abajo.",
    "<b>Botones rápidos (Centro de control):</b> desliza desde la esquina de arriba a la derecha, hacia abajo. Ahí están la linterna, el brillo y el modo avión.")]),
 ],
 practica="Abre la app Reloj, regresa a inicio, abre Calendario, cambia a Reloj sin ir a inicio, y prende y apaga la linterna.",
 problemas=lista("<b>La pantalla se movió sola:</b> tal vez tocaste con dos dedos. Regresa a inicio y vuelve a empezar.", "<b>Las apps tiemblan:</b> dejaste el dedo mucho tiempo. Toca «Listo» arriba a la derecha."),
 hija=f"Con VoiceOver estos movimientos cambian: un toque solo lee, y dos toques presionan. Ella los aprende en la {toca(4,'Conoce a VoiceOver')}. Para ayudarle, ten a la mano la página {f'<a href=\"{TOCA}voiceover.html\">Encender y apagar VoiceOver</a>'}.",
 apple=[("Aprender los gestos básicos", G % "iph75e97af9b")]),

dict(num=3, parte=1, titulo="Configuración: tu iPhone a tu gusto",
 intro="La app de los engranes, donde se cambia todo. Y el truco para encontrar cualquier ajuste.",
 secciones=[
  ("El truco: buscar", [pasos(
    "Abre Configuración (el engrane gris).",
    "Desliza la lista un poco hacia abajo y aparece arriba la barra «Buscar».",
    "Escribe lo que quieres, por ejemplo «brillo», y toca el resultado."),
    "<p>Así no tienes que memorizar dónde está cada cosa. En estas lecciones lo vas a usar mucho.</p>"]),
  ("Letra más grande", [
    "<p>Busca «Tamaño del texto» y mueve la barra a la derecha. También puedes activar «Texto en negritas».</p>"]),
  ("Brillo y sonido", [lista(
    "<b>Brillo:</b> en el Centro de control (esquina de arriba a la derecha) desliza la barra del sol.",
    "<b>Tono de llamada:</b> busca «Tonos» en Configuración y elige uno que oigas bien.")]),
  ("Tu nombre y tu cuenta", [
    "<p>Hasta arriba de Configuración está tu nombre: es tu <b>Cuenta de Apple</b>. Ahí están tu correo, tu contraseña y tus copias de seguridad. Lo vemos en la lección 12.</p>"]),
 ],
 practica="Usa la búsqueda de Configuración para encontrar «Tamaño del texto» y pon la letra como te guste.",
 problemas=lista("<b>Cambié algo y no sé qué:</b> la mayoría de los ajustes se regresan igual; búscalo otra vez y cámbialo.", "<b>No aparece la barra Buscar:</b> desliza la lista hacia abajo desde arriba."),
 hija=f"Su iPhone se configura distinto: VoiceOver, el atajo y Siri. Lo vemos en la lección 15 de esta serie. Ella aprende a ajustar su voz en la {toca(16,'Tu VoiceOver a tu manera')}.",
 apple=[("Buscar configuraciones", G % "iph079e1fe9d")]),

dict(num=4, parte=1, titulo="Señal, Wi-Fi y datos",
 intro="Cómo saber si tienes señal e internet, y cómo cuidar tus datos.",
 secciones=[
  ("Leer la parte de arriba", [lista(
    "<b>Rayitas:</b> la señal de tu compañía. Más rayitas, mejor señal.",
    "<b>Abanico:</b> estás conectada a un Wi-Fi.",
    "<b>Avión:</b> el modo avión está prendido; no hay llamadas ni internet.",
    "<b>Batería:</b> cuánta carga queda.")]),
  ("Conectarte a un Wi-Fi", [pasos(
    "Abre Configuración y toca Wi-Fi.",
    "Toca el nombre de la red.",
    "Escribe la contraseña y toca «Conectar».")]),
  ("Ahorrar datos", [lista(
    "Cuando haya Wi-Fi, úsalo para descargar y actualizar.",
    "Busca «Modo de datos bajos» en Configuración y actívalo: el iPhone gasta menos datos.",
    "Las actualizaciones grandes, siempre con Wi-Fi.")]),
  ("Modo avión", [
    "<p>Corta llamadas e internet. Sirve si quieres que nadie te interrumpa o para ahorrar batería. Se prende y apaga en el Centro de control. Si un día no puedes llamar, revisa que esté apagado.</p>"]),
 ],
 practica="Mira cuántas rayitas de señal tienes. Abre el Centro de control y encuentra el modo avión, sin prenderlo.",
 problemas=lista("<b>No hay internet:</b> revisa el modo avión, luego el Wi-Fi o los datos. Si sigue igual, apaga y prende el iPhone.", "<b>Señal muy baja:</b> acércate a una ventana o sal un momento."),
 hija=f"Ella encuentra el modo avión en el Centro de control en la {toca(15,'Avisos y botones rápidos')}.",
 apple=[("Usar y personalizar el centro de control", G % "iph59095ec58")]),

dict(num=5, parte=1, titulo="Contactos",
 intro="Guardar los números de tu familia con su nombre.",
 secciones=[
  ("Agregar un contacto", [pasos(
    "Abre la app Contactos (o Teléfono y toca Contactos).",
    "Toca el «+» de arriba.",
    "Escribe el nombre y toca «agregar teléfono» para escribir el número.",
    "Toca «OK» o «Listo» arriba a la derecha.")]),
  ("Buscar y llamar", [
    "<p>En Contactos, escribe el nombre en la barra de búsqueda de arriba. Toca el contacto y luego el botón de llamar.</p>"]),
  ("Favoritos", [
    "<p>Dentro de un contacto, toca «Agregar a favoritos». Aparece en Teléfono, en Favoritos, para llamar rápido.</p>"]),
  ("Tú eres «mamá»", [
    "<p>En el iPhone de tu hija, guarda tu número con tu nombre. Luego, desde su iPhone, di «Oye Siri, [tu nombre] es mi mamá» y confirma. Así ella puede decir «llama a mamá».</p>"]),
 ],
 practica="Agrega un contacto nuevo de alguien de tu familia y ponlo en Favoritos.",
 problemas=lista("<b>Guardé el número mal:</b> abre el contacto, toca «Editar» y corrígelo.",),
 hija=f"Con los contactos bien guardados, VoiceOver le dice quién llama. Lo usa en la {toca(5,'Conoce a Siri')} y en la {toca(14,'Llamadas y FaceTime')}.",
 apple=[("Agregar y usar información de contacto", G % "iph3e0ca2db")]),

dict(num=6, parte=1, titulo="Llamadas y FaceTime",
 intro="Llamar, contestar, colgar y hacer videollamadas.",
 secciones=[
  ("Llamar", [pasos(
    "Abre la app Teléfono (el teléfono verde).",
    "Toca Favoritos o Contactos y elige a la persona.",
    "O toca Teclado, marca el número y toca el botón verde.")]),
  ("Contestar y colgar", [lista(
    "<b>Si el iPhone está bloqueado:</b> desliza el botón verde.",
    "<b>Si está abierto:</b> toca el botón verde.",
    "<b>Colgar:</b> toca el botón rojo, o aprieta el botón lateral.")]),
  ("Durante la llamada", [
    "<p>Toca <b>Altavoz</b> para hablar sin tener el teléfono en la oreja.</p>"]),
  ("FaceTime: llamada con video", [
    "<p>Abre FaceTime, toca «Nuevo FaceTime», elige el contacto y toca FaceTime. Funciona con internet y la otra persona necesita un iPhone. Sostén el teléfono frente a tu cara.</p>"]),
 ],
 practica="Llama a alguien de tu familia y pon el altavoz. Después hazle una llamada de FaceTime a tu hija.",
 problemas=lista("<b>No me escuchan:</b> revisa que no esté tocado el botón de silenciar.", "<b>FaceTime no conecta:</b> necesita Wi-Fi o datos."),
 hija=f"Ella contesta y cuelga con dos toques de dos dedos, en la {toca(14,'Llamadas y FaceTime')}. Practiquen: tú la llamas desde otro cuarto.",
 apple=[("Contestar o rechazar llamadas entrantes", G % "iph3c9947bf"), ("Realizar llamadas de FaceTime", G % "iph7801d5771")]),

dict(num=7, parte=1, titulo="Mensajes",
 intro="Escribir, mandar notas de voz y fotos con la app Mensajes.",
 secciones=[
  ("Mandar un mensaje", [pasos(
    "Abre Mensajes (la burbuja verde).",
    "Toca el botón de escribir arriba a la derecha.",
    "Escribe el nombre de la persona.",
    "Toca abajo, escribe tu mensaje y toca la flecha para enviar.")]),
  ("Azul o verde", [
    "<p>Si el mensaje sale <b>azul</b>, va por internet a otro iPhone. Si sale <b>verde</b>, va como mensaje de texto normal de tu plan.</p>"]),
  ("Hablar en vez de escribir", [lista(
    "<b>Dictado:</b> toca el micrófono del teclado, habla y el iPhone escribe.",
    "<b>Mensaje de voz:</b> toca el «+» junto al mensaje, elige Audio y habla.")]),
  ("Mandar una foto", [
    "<p>Toca el «+», elige Fotos, toca la foto y envía.</p>"]),
 ],
 practica="Mándale a tu hija un mensaje escrito con dictado y otro con una nota de voz.",
 problemas=lista("<b>No se envía (signo rojo):</b> revisa la señal y toca el signo para volver a intentarlo.",),
 hija=f"Ella escribe mensajes con el teclado, el dictado y Siri en la {toca(11,'Escribe y manda mensajes')}, y en braille en la {toca(18,'Escribe en braille')}.",
 apple=[("Enviar y responder a mensajes", G % "iph82fb73ba3"), ("Dictar texto", G % "iph2c0651d2")]),

dict(num=8, parte=1, titulo="Correo",
 intro="Poner tu correo en el iPhone y leer, escribir y responder.",
 secciones=[
  ("Agregar tu correo", [pasos(
    "Abre Configuración y busca «Cuentas».",
    "Toca «Agregar cuenta» y elige tu servicio, por ejemplo iCloud o Google.",
    "Escribe tu correo y tu contraseña, y activa Correo.")]),
  ("Leer", [
    "<p>Abre la app Correo (el sobre azul). Los correos nuevos están arriba. Toca uno para leerlo; con la flecha «‹» regresas.</p>"]),
  ("Escribir y responder", [lista(
    "<b>Nuevo:</b> toca el botón de escribir abajo a la derecha. Escribe para quién, el asunto y el mensaje, y toca la flecha.",
    "<b>Responder:</b> dentro del correo, toca la flecha de responder.")]),
  ("Cuidado", [
    "<p>Si un correo te pide contraseñas, códigos o datos del banco, no respondas ni toques enlaces. Lo vemos en la lección 12.</p>"]),
 ],
 practica="Escríbete un correo a ti misma con el asunto «Prueba» y respóndelo.",
 problemas=lista("<b>No llegan correos:</b> revisa el internet y desliza la lista hacia abajo para actualizar.",),
 hija="Ella todavía no necesita correo. Cuando llegue el momento, tú le creas la cuenta y la revisas con ella.",
 apple=[("Agregar o eliminar cuentas de correo electrónico", G % "iph44d1ae58a")]),

dict(num=9, parte=1, titulo="Cámara y fotos",
 intro="Tomar fotos y videos, verlos y mandarlos.",
 secciones=[
  ("Tomar una foto", [pasos(
    "Abre Cámara. Si el iPhone está bloqueado, desliza la pantalla hacia la izquierda.",
    "Apunta y toca el botón blanco grande.",
    "Para video, desliza hasta «Video» y toca el botón rojo; otra vez para terminar.")]),
  ("Ver tus fotos", [
    "<p>Abre la app Fotos. Las más nuevas están abajo. Toca una para verla grande y desliza a los lados para ver las demás.</p>"]),
  ("Mandar o borrar", [lista(
    "<b>Mandar:</b> abre la foto y toca el botón de compartir (un cuadro con flecha hacia arriba). Elige Mensajes o Correo.",
    "<b>Borrar:</b> toca el bote de basura. Se queda 30 días en «Eliminado» por si te arrepientes.")]),
 ],
 practica="Toma una foto de tu cocina, ábrela en Fotos y mándasela a alguien de tu familia.",
 problemas=lista("<b>Sale borrosa:</b> limpia la cámara de atrás con una tela suave y quédate quieta.", "<b>No hay espacio:</b> borra videos que ya no quieras. Lo vemos en la lección 13."),
 hija=f"Para ella la cámara sirve de otra forma: le describe lo que hay enfrente y le lee etiquetas. Lo aprende en la {toca(17,'La cámara que ve por ti')}.",
 apple=[("Elementos básicos de Cámara", G % "iph263472f78")]),

dict(num=10, parte=1, titulo="Siri y dictado",
 intro="Hablarle al iPhone para que haga cosas por ti.",
 secciones=[
  ("Llamar a Siri", [lista(
    "Di <b>«Oye Siri»</b> y luego lo que quieres.",
    "O deja apretado el botón lateral y habla.")]),
  ("Cosas útiles", [lista(
    "«Llama a [nombre]».",
    "«Mándale un mensaje a [nombre] que diga…».",
    "«Pon una alarma a las seis».",
    "«Recuérdame mañana a las nueve llevar la credencial».",
    "«¿Qué tiempo hace hoy?».")]),
  ("Dictado", [
    "<p>En cualquier lugar donde escribes, toca el micrófono del teclado y habla. Di «punto» o «coma» para poner signos.</p>"]),
  ("Prepararlo", [
    "<p>Busca «Siri» en Configuración: elige español (México) y activa que responda a «Oye Siri».</p>"]),
 ],
 practica="Pídele a Siri una alarma en cinco minutos y un recordatorio para mañana.",
 problemas=lista("<b>Siri no entiende:</b> habla normal, no muy rápido, y dilo con otras palabras.",),
 hija=f"Siri es una de las herramientas más importantes para ella. La aprende en la {toca(5,'Conoce a Siri')}.",
 apple=[("Activar e invocar a Siri", G % "iph83aad8922"), ("Dictar texto", G % "iph2c0651d2")]),

dict(num=11, parte=1, titulo="Encontrar: tu iPhone y el de ella",
 intro="La app Encontrar sirve para ver dónde está el iPhone de tu hija y para hacer sonar un iPhone perdido.",
 secciones=[
  ("Hacer sonar un iPhone", [
    "<p>Abre la app Encontrar, toca Dispositivos, elige el iPhone y toca <b>Reproducir sonido</b>. Suena fuerte aunque esté en silencio. Muy útil si tu hija no encuentra el suyo en la casa.</p>"]),
  ("Ver dónde está ella", [pasos(
    "Abre Encontrar y toca Personas.",
    "Si ella comparte su ubicación contigo, aparece en el mapa.",
    "Para compartir: toca el «+» y elige «Compartir mi ubicación».")]),
  ("Si se pierde un iPhone", [lista(
    "En Encontrar, elige el iPhone y activa <b>Marcar como perdido</b>: se bloquea y muestra tu número.",
    "Sin tu iPhone, entra desde otro teléfono o computadora a icloud.com/find con tu Cuenta de Apple.")]),
  ("Compartir en familia", [
    "<p>Si unes su iPhone a tu familia en Configuración (busca «Familia»), puedes ver su iPhone en Encontrar y su cuenta queda a tu cargo.</p>"]),
 ],
 practica="Haz sonar el iPhone de tu hija desde tu Encontrar. Después pídele que lo busque siguiendo el sonido.",
 problemas=lista("<b>No aparece su iPhone:</b> revisa en su iPhone que Encontrar esté activado (búscalo en Configuración).",),
 hija=f"Ella comparte su ubicación contigo en la {toca(13,'Tu seguridad')}. El juego de hacer sonar su iPhone le sirve para encontrarlo sola.",
 apple=[("Compartir la ubicación en Encontrar", G % "iph01954dc44"), ("Configurar Compartir en familia", G % "iph223f61318")]),

dict(num=12, parte=1, titulo="Seguridad y tu Cuenta de Apple",
 intro="Cuidar tu código, tu cuenta y no caer en estafas.",
 secciones=[
  ("Tu código", [
    "<p>El código abre tu iPhone cuando Face ID no puede. No uses tu fecha de nacimiento ni 1234. No se lo des a nadie fuera de tu casa.</p>"]),
  ("Tu Cuenta de Apple", [lista(
    "Es tu correo y una contraseña. Con ella se recupera todo si pierdes el iPhone.",
    "Escríbela en papel y guárdala en un lugar seguro de tu casa.",
    "Apple te puede mandar un código de 6 números para entrar. <b>Ese código nunca se lo dictes a nadie</b>, aunque diga que es del banco o de Apple.")]),
  ("Mensajes y llamadas de estafa", [lista(
    "Paquetes que «no llegaron», premios, multas o el banco pidiendo datos: casi siempre son estafa.",
    "No toques enlaces de mensajes que no esperabas.",
    "Si dudas, cuelga y llama tú al número oficial.")]),
  ("Actualizaciones", [
    "<p>Busca «Actualización de software» en Configuración. Instala cuando haya Wi-Fi y el iPhone esté cargando: arreglan problemas de seguridad.</p>"]),
 ],
 practica="Revisa que tu código no sea fácil. Escribe en papel tu correo y la contraseña de tu Cuenta de Apple y guárdalo.",
 problemas=lista("<b>Olvidé mi código:</b> se necesita borrar el iPhone y recuperarlo con la Cuenta de Apple. Por eso es tan importante tenerla anotada.",),
 hija=f"Su seguridad (llamada de emergencia, ubicación y ficha médica) está en la {toca(13,'Tu seguridad')}.",
 apple=[("Usar Emergencia SOS", G % "iph3c99374c")]),

dict(num=13, parte=1, titulo="Cuidar tu iPhone",
 intro="Batería, espacio y protección para que dure muchos años.",
 secciones=[
  ("Batería", [lista(
    "Cárgalo cuando quede poca; no hace falta esperar a cero.",
    "Si te queda poca, activa el <b>Modo de bajo consumo</b> en el Centro de control o búscalo en Configuración.",
    "Usa un cargador de buena calidad.")]),
  ("Espacio", [
    "<p>Busca «Almacenamiento» en Configuración: ahí ves qué ocupa más. Los videos son lo más pesado.</p>"]),
  ("Protección", [lista(
    "Una funda y una mica protegen de golpes.",
    "Para su iPhone, que la funda deje sentir bien los botones.",
    "Límpialo con una tela suave y seca.")]),
  ("Copia de seguridad", [
    "<p>Busca «Respaldo en iCloud» en Configuración y actívalo. Se hace solo cuando el iPhone está cargando y con Wi-Fi.</p>"]),
 ],
 practica="Revisa cuánta batería y cuánto espacio tienes. Activa y desactiva el Modo de bajo consumo.",
 problemas=lista("<b>Se calienta:</b> quítale la funda mientras carga y no lo dejes al sol.",),
 hija="Enséñale a cargar su iPhone sola cada noche, en el mismo lugar y lejos de su cama.",
 apple=[("Recargar la batería", G % "iph63eecc618"), ("Usar iCloud", G % "iphde0f868fd")]),

# ───────────── PARTE 2 ─────────────
dict(num=14, parte=2, titulo="Cómo aprende tu hija",
 intro="Las ideas más importantes para enseñarle, antes de empezar.",
 secciones=[
  ("Con palabras, no con las manos", [
    "<p>Cuando le tomas la mano y la llevas, ella no aprende el camino. Mejor dile dónde está: «arriba a la izquierda», «desliza a la derecha». Que lo encuentre ella.</p>"]),
  ("Ella usa el iPhone con VoiceOver", [
    "<p>Su iPhone habla. Un toque lee y dos toques presionan. Por eso no funciona igual que el tuyo. Si tú necesitas usarlo, apaga VoiceOver con tres clics al botón lateral.</p>"]),
  ("Equivocarse está bien", [
    "<p>Cada error le enseña algo. Espera unos segundos antes de ayudar. Pregunta «¿qué escuchaste?» en lugar de darle la respuesta.</p>"]),
  ("Poco y seguido", [
    "<p>Quince minutos al día enseñan más que una hora el domingo. Terminen siempre con algo que le salió bien.</p>"]),
 ],
 practica="Lee con ella la portada de «Toca, escucha y aprende» y decidan juntas a qué hora van a practicar cada día.",
 problemas=lista("<b>Se frustra:</b> paren, hagan algo que ya sabe, y regresen mañana.",),
 hija=f'Empiecen por la {toca(1,"¿Qué es la accesibilidad?")}.',
 apple=[("Introducción a las funciones de accesibilidad", G % "iph3e2e4367")]),

dict(num=15, parte=2, titulo="Preparar su iPhone",
 intro="Lo que tú configuras una sola vez en su iPhone, antes de la primera lección.",
 secciones=[
  ("Lista para prepararlo", [pasos(
    "<b>Atajo de VoiceOver:</b> en Configuración busca «Atajo de accesibilidad» y elige VoiceOver.",
    "<b>Siri:</b> busca «Siri», elige español (México) y activa «Oye Siri».",
    "<b>Contactos:</b> guarda tu número y el de la familia con su nombre.",
    "<b>Mamá:</b> desde su iPhone di «Oye Siri, [tu nombre] es mi mamá».",
    "<b>Face ID sin mirar:</b> busca «Requerir atención para Face ID» y apágalo.",
    "<b>Ficha médica y contacto de emergencia:</b> en la app Salud.",
    "<b>Encontrar:</b> que comparta su ubicación contigo.",
    "<b>Menos avisos:</b> apaga las notificaciones de apps que no necesita.")]),
  ("La página de ayuda", [
    f'<p>Guarda en tu iPhone la página <a href="{TOCA}voiceover.html">Encender y apagar VoiceOver</a>: tiene todas las formas de prenderlo y apagarlo.</p>']),
 ],
 practica="Prepara su iPhone con la lista. Marca cada punto cuando lo termines.",
 problemas=lista("<b>No encuentro un ajuste:</b> usa la búsqueda de Configuración (lección 3).",),
 hija=f"Con esto listo, ya pueden hacer la {toca(1,'¿Qué es la accesibilidad?')}.",
 apple=[("Activar y practicar con VoiceOver", G % "iph3e2e415f")]),

dict(num=16, parte=2, titulo="Una rutina de práctica",
 intro="Cómo armar 15 minutos al día que funcionen.",
 secciones=[
  ("Los 15 minutos", [pasos(
    "<b>Calentar (3 minutos):</b> algo que ya sabe hacer.",
    "<b>Lo nuevo (7 minutos):</b> una parte de la lección, no toda.",
    "<b>El juego (5 minutos):</b> el juego o el reto de la lección.")]),
  ("Siempre igual", [lista(
    "A la misma hora y en el mismo lugar.",
    "Con el iPhone cargado.",
    "Sin televisión ni ruido de fondo, para que oiga bien.")]),
  ("Celebrar", [
    "<p>Dile qué hizo bien, con detalle: «encontraste el botón tú sola». Las estrellas del juego también cuentan.</p>"]),
 ],
 practica="Hagan su primera rutina de 15 minutos con la lección que les toca.",
 problemas=lista("<b>No hay tiempo un día:</b> 5 minutos de calentar también cuentan.",),
 hija='Cada lección de «Toca, escucha y aprende» tiene Historia, Juego y Reto: se pueden repartir en varios días.',
 apple=[("Práctica de VoiceOver", G % "iph3e2e415f")]),

dict(num=17, parte=2, titulo="Cuando se atora",
 intro="Qué decir y qué hacer cuando algo no sale.",
 secciones=[
  ("Frases que ayudan", [lista(
    "«¿Qué escuchaste?»",
    "«Desliza a la derecha despacio hasta oírlo.»",
    "«Regresa al menú y empieza otra vez.»",
    "«Ya casi; inténtalo una vez más.»")]),
  ("Si el iPhone hace algo raro", [lista(
    "<b>La pantalla está negra pero habla:</b> es la cortina de pantalla. Tres toques con tres dedos.",
    "<b>Habla muy rápido o muy lento:</b> rotor en «Velocidad de habla».",
    "<b>No responde:</b> tres clics para apagar VoiceOver, revisa, y tres clics otra vez.")]),
  ("Pedir ayuda", [
    '<p>Apple tiene soporte de accesibilidad en español por teléfono, chat o en tienda: <a href="https://support.apple.com/es-lamr/111749">cómo pedir ayuda</a>.</p>']),
 ],
 practica="Apaga y prende VoiceOver en su iPhone con tres clics hasta que te salga sin pensar.",
 problemas=lista("<b>Nada funciona:</b> apaga y prende el iPhone. Casi siempre se arregla.",),
 hija=f'Ten siempre a la mano <a href="{TOCA}voiceover.html">Encender y apagar VoiceOver</a>.',
 apple=[("Cómo pedirle ayuda a Apple con la accesibilidad", "https://support.apple.com/es-lamr/111749")]),

dict(num=18, parte=2, titulo="El camino de «Toca, escucha y aprende»",
 intro="Qué aprende ella en cada nivel y qué lección tuya va con cada una.",
 secciones=[
  ("Nivel 1 · Primeros pasos", [lista(
    f"Lecciones 1 a 6: accesibilidad, las partes del iPhone, VoiceOver y Siri.",
    "Tú, antes: lecciones 1, 2, 10 y 15 de esta serie.")]),
  ("Nivel 2 · Apps, música y mensajes", [lista(
    "Lecciones 7 a 12: gestos nuevos, el rotor, música, cuentos, mensajes y apps.",
    "Tú, antes: lecciones 7 y 9.")]),
  ("Nivel 3 · Seguridad, llamadas, cámara y braille", [lista(
    "Lecciones 13 a 18: seguridad, llamadas, avisos, ajustes de VoiceOver, la cámara y braille.",
    "Tú, antes: lecciones 4, 6, 11 y 12.")]),
  ("A su ritmo", [
    "<p>No hay prisa. Repetir una lección está muy bien. Lo importante es que ella use su iPhone sola, cada vez un poco más.</p>"]),
 ],
 practica="Abran juntas la portada de la serie de ella y elijan la próxima lección.",
 problemas="",
 hija=f'<a href="{TOCA}">Ir a «Toca, escucha y aprende»</a>.',
 apple=[("Accesibilidad en Apple (México)", "https://www.apple.com/mx/accessibility/")]),
]
