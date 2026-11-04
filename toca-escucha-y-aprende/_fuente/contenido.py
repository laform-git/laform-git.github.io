# Toca, escucha y aprende · Nivel 1 · contenido de las seis lecciones.
# Español de México. Habla con ella (tú) y con mamá (tú). Sin nombres.

LECCIONES = [
# ───────────────────────── LECCIÓN 1 ─────────────────────────
dict(num=1, titulo="¿Qué es la accesibilidad?", nivel="a",
 intro="Cada pantalla tiene un solo botón. Para seguir, desliza un dedo a la derecha hasta oír «Empezar, botón». Luego toca dos veces la pantalla.",
 secciones=[
  dict(nombre="Historia", pantallas=[
   dict(t="texto", text="¡Hola! Hoy vas a aprender una palabra nueva: accesibilidad."),
   dict(t="texto", text="Quiere decir que todas las personas pueden usar las cosas, cada quien a su manera."),
   dict(t="texto", text="Tú conoces el mundo con tus oídos y con tus manos. Tu iPhone está hecho para trabajar así contigo."),
   dict(t="texto", text="Cuando tocas la pantalla, VoiceOver te dice en voz alta qué hay ahí. No necesitas verla."),
   dict(t="texto", text="Y si le hablas a Siri, te escucha. Le puedes pedir que llame a mamá o que te diga la hora."),
   dict(t="salud", titulo="Tip de salud", text="Tu cuerpo también tiene un reloj. Cada mañana, sal unos minutos al sol con mamá. La luz de la mañana le dice a tu cuerpo que ya es de día, y en la noche duermes mejor."),
  ]),
  dict(nombre="Juego", pantallas=[
   dict(t="texto", titulo="Juego: ¿cierto o falso?", text="Te digo una frase sobre tu iPhone. Tú eliges: Cierto o Falso."),
   dict(t="pregunta", text="VoiceOver te dice en voz alta lo que tocas en la pantalla.", ok=True, fb="¡Cierto! Por eso puedes usar el iPhone sin verlo."),
   dict(t="pregunta", text="Para usar un iPhone necesitas ver la pantalla.", ok=False, fb="¡Bien! Es falso. Con VoiceOver y Siri lo usas con tus oídos y tus dedos."),
   dict(t="pregunta", text="Siri puede llamar a mamá si se lo pides.", ok=True, fb="¡Cierto! Solo dile: Oye Siri, llama a mamá."),
   dict(t="pregunta", text="Las herramientas de accesibilidad hay que comprarlas aparte.", ok=False, fb="¡Bien! Es falso. Ya vienen dentro de tu iPhone."),
   dict(t="pregunta", text="Puedes encontrar los botones del iPhone con los dedos.", ok=True, fb="¡Cierto! Están en los lados, y cada uno tiene su lugar."),
   dict(t="pregunta", text="La luz de la mañana te ayuda a dormir mejor en la noche.", ok=True, fb="¡Cierto! Le dice a tu cuerpo que ya empezó el día."),
  ]),
  dict(nombre="Reto", pantallas=[
   dict(t="texto", titulo="Tu reto de hoy", text="Toma tu iPhone. Busca con los dedos los botones de los lados. Cuéntale a mamá cuántos encontraste y para qué crees que sirve cada uno."),
  ]),
 ],
 despedida="En la próxima lección aparece un botón nuevo: Atrás.",
 mama=[
  ("Su salud: la luz de la mañana", ["<p>Un ratito de luz de día por la mañana le ayuda a su cuerpo a saber que empezó el día, y en la noche duerme mejor. No hace falta nada especial: que desayune junto a una ventana abierta o salga unos minutos al patio.</p>"]),
  ("De qué trata esta lección", [
   "<p>Accesibilidad es diseñar las cosas para que todas las personas las puedan usar, sin importar cómo ven, oyen o se mueven.</p>",
   "<p>En el iPhone eso quiere decir que ella no necesita ver la pantalla: el teléfono le dice en voz alta lo que hay, y ella le puede hablar para pedirle cosas.</p>"]),
  ("Dónde está en el iPhone", [
   "<p>Todo viene incluido, en <span class=\"path\">Configuración → Accesibilidad</span>. Lo importante para ella está en el grupo Visión:</p>",
   "<ul><li><b>VoiceOver.</b> El lector de pantalla. Lee en voz alta lo que ella toca y se usa con gestos.</li><li><b>Siri.</b> Hace cosas solo hablando: llamar, mandar un mensaje, preguntar la hora.</li><li><b>Lectura en voz alta.</b> Lee un texto o una pantalla completa. Ahí se descargan las voces: busca «Voces» en Configuración.</li></ul>"]),
  ("Antes de empezar: la salida de emergencia", [
   "<p>Ve a <span class=\"path\">Configuración → Accesibilidad → Atajo de accesibilidad</span> y elige VoiceOver.</p>",
   "<p>Desde entonces, tres clics seguidos en el botón lateral encienden o apagan VoiceOver. Si te pierdes con VoiceOver encendido, tres clics y se apaga.</p>"]),
  ("Cómo funciona su página", [
   "<ul><li><b>Una pantalla a la vez,</b> con un solo botón grande. No hay que desplazar nada.</li><li><b>Lo único que aprende hoy:</b> deslizar un dedo a la derecha hasta oír el botón, y tocar dos veces la pantalla para presionarlo.</li><li>Si se pierde, puede tocar el botón directamente: ocupa toda la parte de abajo.</li></ul>"]),
  ("Cómo acompañarla", [
   "<ul><li><b>Enciende VoiceOver</b> con los tres clics y abre la lección con ella.</li><li><b>El juego:</b> seis preguntas de cierto o falso. Deja que conteste sola, aunque se equivoque.</li><li><b>El reto:</b> que encuentre los botones de los lados y te diga cuántos hay y para qué cree que sirve cada uno. No le digas la respuesta: eso es la Lección 3.</li><li><b>Ayuda con palabras, no con las manos.</b> La meta es que ella use el iPhone sola.</li></ul>"]),
  ("Palabras de esta lección", [
   "<dl><dt>Accesibilidad</dt><dd>Que todas las personas puedan usar algo, cada quien a su manera.</dd><dt>VoiceOver</dt><dd>El lector de pantalla del iPhone.</dd><dt>Siri</dt><dd>La asistente de voz del iPhone.</dd></dl>"]),
 ]),

# ───────────────────────── LECCIÓN 2 ─────────────────────────
dict(num=2, titulo="¿Por qué iPhone?", nivel="b",
 intro="Hoy hay un botón nuevo: Atrás. Siguiente avanza y Atrás regresa. Desliza a la derecha para encontrarlos.",
 secciones=[
  dict(nombre="Historia", pantallas=[
   dict(t="texto", text="Hay muchos teléfonos. Los que usan Android también tienen un lector de pantalla. Se llama TalkBack."),
   dict(t="texto", text="En el iPhone, VoiceOver funciona igual en todos los modelos y en casi todas las apps. Lo que aprendas hoy te va a servir por muchos años."),
   dict(t="texto", text="VoiceOver y Siri ya vienen dentro de tu iPhone. No tienes que instalar nada."),
   dict(t="texto", text="Los gestos de VoiceOver son los mismos en todas las apps. Una app nueva solo tiene otros botones en otro lugar."),
   dict(t="texto", text="Muchas personas con discapacidad visual usan iPhone: estudiantes, maestros y hasta programadores. Si tienes una duda, hay mucha gente que te puede ayudar."),
   dict(t="salud", titulo="Tip de salud", text="Tu cuerpo necesita moverse, igual que tu cerebro necesita aprender. Brinca, baila o pon tu canción favorita. Lo mejor es moverte un rato todos los días."),
  ]),
  dict(nombre="Juego", pantallas=[
   dict(t="texto", titulo="Juego: ¿cierto o falso?", text="Seis frases más. Recuerda: si quieres oír otra vez una pantalla, usa Atrás."),
   dict(t="pregunta", text="Los teléfonos Android también tienen un lector de pantalla.", ok=True, fb="¡Cierto! Se llama TalkBack."),
   dict(t="pregunta", text="Para usar VoiceOver tienes que descargar una app.", ok=False, fb="¡Bien! Es falso. VoiceOver ya viene en tu iPhone."),
   dict(t="pregunta", text="VoiceOver funciona igual en todos los iPhone.", ok=True, fb="¡Cierto! Por eso lo que aprendes te sirve siempre."),
   dict(t="pregunta", text="Cada app tiene sus propios gestos de VoiceOver.", ok=False, fb="¡Bien! Es falso. Los gestos son los mismos en todas las apps."),
   dict(t="pregunta", text="Siri y VoiceOver pueden trabajar juntos.", ok=True, fb="¡Cierto! Puedes hablarle a Siri aunque VoiceOver esté encendido."),
   dict(t="pregunta", text="Moverte un rato todos los días es bueno para tu cuerpo y para tu cerebro.", ok=True, fb="¡Cierto! Brincar, bailar y caminar cuentan."),
  ]),
  dict(nombre="Reto", pantallas=[
   dict(t="texto", titulo="Tu reto de hoy", text="Con mamá cerca, di: «Oye Siri, ¿qué es VoiceOver?». Escucha la respuesta. Después cuéntale a mamá una cosa nueva que aprendiste hoy."),
  ]),
 ],
 despedida="La próxima lección es para tus manos: vas a conocer cada parte de tu iPhone.",
 mama=[
  ("Su salud: moverse jugando", ["<p>A ella le hace bien moverse un rato todos los días. No tiene que ser ejercicio: bailar una canción en la sala, jugar o ir caminando a la tienda cuentan.</p>", "<p>Tu papel es acompañarla: poner su música, contar sus brincos o aplaudirle. Que sea en un espacio que ella ya conoce, para que se mueva con confianza.</p>"]),
  ("De qué trata esta lección", [
   "<p>Android también tiene herramientas para personas con discapacidad visual, como TalkBack, que lee la pantalla en voz alta, y permite personalizar más el teléfono. La diferencia es que en Android cada marca funciona un poco distinto, mientras que VoiceOver funciona igual en todos los iPhone y en casi todas las aplicaciones.</p>",
   "<p>Así, lo que ella aprenda hoy le va a servir por muchos años. Además, la mayoría de las apps están hechas para funcionar bien con VoiceOver, y hay más maestros, escuelas y personas con discapacidad visual que usan iPhone, por eso es más fácil encontrar ayuda cuando la necesiten.</p>"]),
  ("Lo nuevo en su página", [
   "<ul><li><b>Dos botones abajo:</b> Atrás y Siguiente. Ahora tiene que elegir cuál quiere, escuchándolos.</li><li>Deslizando a la derecha oye primero el texto, luego «Atrás, botón» y luego «Siguiente, botón».</li><li>En las preguntas, Siguiente aparece cuando ya contestó.</li></ul>"]),
  ("Antes de empezar", [
   "<p>Revisa que Siri esté encendido: en Configuración, busca «Siri». Si todavía no lo configuras, hazlo con ella para el reto; en la Lección 5 lo vemos a fondo.</p>"]),
  ("Cómo acompañarla", [
   "<ul><li><b>Pregúntale qué cree</b> antes de cada respuesta del juego. A ella le va a servir explicar por qué.</li><li><b>El reto:</b> que ella le hable a Siri, no tú. Si Siri no entiende, que lo repita con otras palabras.</li></ul>"]),
  ("Palabras de esta lección", [
   "<dl><dt>Android</dt><dd>Otro sistema de teléfonos, de muchas marcas.</dd><dt>TalkBack</dt><dd>El lector de pantalla de Android.</dd><dt>App</dt><dd>Un programa del teléfono, como Mensajes o Reloj.</dd><dt>Gesto</dt><dd>Un movimiento de los dedos en la pantalla.</dd></dl>"]),
 ]),

# ───────────────────────── LECCIÓN 3 ─────────────────────────
dict(num=3, titulo="Conoce tu iPhone con las manos", nivel="b",
 intro="Hoy vas a conocer tu iPhone con las manos. Tenlo cerca. Usa Atrás y Siguiente como en la lección 2.",
 secciones=[
  dict(nombre="Historia", pantallas=[
   dict(t="texto", text="Toma tu iPhone con las dos manos. La pantalla es la parte lisa de vidrio. Atrás, en una esquina de arriba, sientes un círculo con relieve: es la cámara."),
   dict(t="texto", text="Así sabes cuál lado es arriba: la cámara de atrás queda arriba. El agujero para el cable queda abajo."),
   dict(t="texto", text="Del lado derecho hay un solo botón largo: el botón lateral. Enciende y apaga la pantalla."),
   dict(t="texto", text="Si aprietas el botón lateral tres veces rápido, VoiceOver se enciende o se apaga. Si lo dejas apretado, contesta Siri."),
   dict(t="texto", text="Del lado izquierdo hay tres botones. Los dos de abajo son el volumen: el de arriba sube y el de abajo baja."),
   dict(t="texto", text="El botón más pequeño, arriba de los de volumen, es el botón de Acción. Mamá puede elegir qué hace, por ejemplo poner el teléfono en silencio."),
   dict(t="texto", text="Abajo, en el centro, está el agujero ovalado para cargar. A los lados hay agujeritos: son las bocinas."),
   dict(t="salud", titulo="Tip de salud", text="Después de un rato con el iPhone, ponlo en la mesa y estírate: brazos arriba, cuenta hasta diez, y gira los hombros. Tus manos y tu cuello también descansan."),
  ]),
  dict(nombre="Juego", pantallas=[
   dict(t="texto", titulo="Juego: ¿cierto o falso?", text="Puedes tocar tu iPhone para comprobar cada respuesta."),
   dict(t="pregunta", text="El botón lateral está del lado derecho.", ok=True, fb="¡Cierto! Es el único botón de ese lado."),
   dict(t="pregunta", text="Para subir el volumen aprietas el botón de abajo del lado izquierdo.", ok=False, fb="¡Bien! Es falso. El de arriba sube y el de abajo baja."),
   dict(t="pregunta", text="Tres clics rápidos en el botón lateral encienden o apagan VoiceOver.", ok=True, fb="¡Cierto! Es tu salida de emergencia."),
   dict(t="pregunta", text="El cable para cargar se conecta arriba.", ok=False, fb="¡Bien! Es falso. Se conecta abajo, en el centro."),
   dict(t="pregunta", text="La cámara de atrás te ayuda a saber cuál lado es arriba.", ok=True, fb="¡Cierto! La cámara siempre queda arriba."),
   dict(t="pregunta", text="Después de usar el iPhone un rato, es bueno levantarte y estirarte.", ok=True, fb="¡Cierto! Tu cuerpo descansa y regresas con más energía."),
  ]),
  dict(nombre="Reto", pantallas=[
   dict(t="texto", titulo="Tu reto de hoy", text="Sin ayuda: sube el volumen dos veces, bájalo una vez y apaga la pantalla con el botón lateral. Luego conecta el cable para cargar. Mamá solo escucha."),
  ]),
 ],
 despedida="En la próxima lección conoces bien a VoiceOver, y la lección tendrá un menú.",
 mama=[
  ("Su salud: una pausa", ["<p>Después de un rato con el iPhone, recuérdale hacer una pausa para estirarse: brazos arriba, hombros y cuello.</p>", "<p>Enséñale a dejar el teléfono sobre la mesa en lugar de sostenerlo con el cuello doblado.</p>"]),
  ("De qué trata esta lección", [
   "<p>Ella aprende a ubicar cada parte del iPhone por tacto: cuál lado es arriba, el botón lateral, los dos botones de volumen, el botón de Acción, el puerto de carga y las bocinas.</p>"]),
  ("Antes de empezar", [
   "<ul><li><b>Botón de Acción:</b> en Configuración busca «Botón de Acción». Al principio déjalo en Silencio, para que ella no lo active sin querer. Más adelante pueden ponerle algo útil.</li><li><b>Funda:</b> si usa funda, que deje los botones fáciles de sentir. Una funda gruesa que tapa los botones hace más difícil esta lección.</li></ul>"]),
  ("Lo nuevo en su página", [
   "<p>Las historias tienen más pantallas. Que use Atrás para volver a escuchar una parte mientras toca el teléfono con la otra mano.</p>"]),
  ("Cómo acompañarla", [
   "<ul><li><b>Que tenga el iPhone en la mano</b> mientras escucha, y que toque cada parte cuando la oiga.</li><li><b>En el juego</b> puede comprobar cada respuesta tocando el teléfono. Eso está bien: es parte de aprender.</li><li><b>El reto:</b> no le digas dónde está cada botón. Si se equivoca, pregúntale qué escuchó.</li></ul>"]),
  ("Palabras de esta lección", [
   "<dl><dt>Botón lateral</dt><dd>El botón largo del lado derecho.</dd><dt>Botón de Acción</dt><dd>El botón pequeño de arriba a la izquierda. Se puede configurar.</dd><dt>Puerto de carga</dt><dd>El agujero de abajo para el cable.</dd></dl>"]),
 ]),

# ───────────────────────── LECCIÓN 4 ─────────────────────────
dict(num=4, titulo="Conoce a VoiceOver", nivel="c",
 intro="Desde hoy hay un menú. Elige una burbuja. El botón Menú siempre te regresa aquí.",
 secciones=[
  dict(nombre="Historia", pantallas=[
   dict(t="texto", text="VoiceOver es la voz de tu iPhone. Lee en voz alta lo que tocas."),
   dict(t="texto", text="Toca la pantalla con un dedo y VoiceOver te dice qué hay ahí. Puedes arrastrar el dedo para explorar sin abrir nada."),
   dict(t="texto", text="Desliza un dedo a la derecha para ir a lo siguiente. A la izquierda, para regresar. Así recorres todo en orden."),
   dict(t="texto", text="Toca dos veces rápido en cualquier parte de la pantalla para presionar lo último que VoiceOver dijo."),
   dict(t="texto", text="Toca una vez con dos dedos para que VoiceOver se calle. Otra vez con dos dedos, y sigue hablando."),
   dict(t="texto", text="Para ir a la pantalla de inicio, pon un dedo en el borde de abajo y deslízalo hacia arriba hasta sentir una vibración. Luego suelta."),
   dict(t="texto", text="Para prestarle el teléfono a mamá, aprieta tres veces el botón lateral: VoiceOver se apaga. Cuando te lo regrese, otra vez tres veces."),
   dict(t="salud", titulo="Tip de salud", text="Dormir bien te ayuda a aprender. A tu edad necesitas entre 9 y 12 horas de sueño. Una hora antes de dormir, deja el iPhone cargando lejos de tu cama."),
  ]),
  dict(nombre="Juego", pantallas=[
   dict(t="texto", titulo="Juego: encuentra el botón", text="Hay varios botones en la pantalla. Desliza a la derecha para escucharlos y toca dos veces el que te pido."),
   dict(t="busca", text="Encuentra el botón Estrella.", opciones=["Luna","Sol","Estrella","Nube"], correcta="Estrella"),
   dict(t="busca", text="Encuentra el botón Perro.", opciones=["Gato","Pez","Pájaro","Perro","Conejo","Tortuga"], correcta="Perro"),
   dict(t="busca", text="Encuentra el botón Pastel.", opciones=["Pan","Galleta","Helado","Fruta","Dulce","Pastel"], correcta="Pastel"),
   dict(t="busca", text="Encuentra el botón Guitarra.", opciones=["Piano","Tambor","Guitarra","Flauta","Violín","Trompeta"], correcta="Guitarra"),
   dict(t="busca", text="Ahora arrastra un dedo por la pantalla hasta oír Mariposa. Luego toca dos veces.", opciones=["Abeja","Hormiga","Grillo","Mariposa"], correcta="Mariposa"),
  ]),
  dict(nombre="Reto", pantallas=[
   dict(t="texto", titulo="Tu reto de hoy", text="Ve a la pantalla de inicio deslizando desde abajo. Busca la app Reloj, ábrela con dos toques y escucha qué hay. Después regresa a la pantalla de inicio. ¡Sin ayuda!"),
  ]),
 ],
 despedida="Ya sabes los gestos más importantes de VoiceOver. En la próxima lección conoces a Siri.",
 mama=[
  ("Su salud: el descanso", ["<p>A su edad se recomiendan entre 9 y 12 horas de sueño. Una hora antes de dormir, su iPhone se queda cargando fuera de la cama.</p>", "<p>Un horario fijo para dormir y despertar le ayuda más que cualquier truco. Ayuda también que la casa baje el ritmo a esa hora.</p>"]),
  ("De qué trata esta lección", [
   "<p>Los gestos básicos de VoiceOver: tocar para escuchar, deslizar a la derecha y a la izquierda, tocar dos veces para presionar, tocar con dos dedos para callar, ir a la pantalla de inicio y apagar VoiceOver para prestar el teléfono.</p>"]),
  ("Antes de empezar", [
   "<ul><li><b>Desbloqueo:</b> en Configuración busca «Requerir atención para Face ID» y apágalo, para que pueda desbloquear sin mirar al teléfono.</li><li><b>Velocidad de la voz:</b> en <span class=\"path\">Configuración → Accesibilidad → VoiceOver</span> ajusta la velocidad de habla. Empiecen lento y súbanla cuando ella quiera.</li><li><b>Práctica de VoiceOver:</b> en esa misma pantalla hay una práctica donde ella puede probar gestos sin abrir nada. Úsenla para el juego de hoy.</li><li><b>App Reloj:</b> déjala en la primera pantalla de inicio, para el reto.</li></ul>"]),
  ("Lo nuevo en su página", [
   "<ul><li><b>Un menú de burbujas:</b> Historia, Juego y Reto. Ella elige a dónde ir.</li><li><b>Botones más pequeños y más numerosos,</b> como en una app de verdad.</li><li><b>El juego</b> pone hasta seis botones y ella tiene que encontrar uno deslizando. La última pregunta es para explorar arrastrando el dedo.</li></ul>"]),
  ("Prestarle el teléfono a mamá", [
   "<p>Ella aprieta tres veces el botón lateral y VoiceOver se apaga; tú usas el teléfono normal. Antes de devolverlo, tres clics otra vez. También puede decir «Oye Siri, desactiva VoiceOver» y «activa VoiceOver».</p>"]),
  ("Cómo acompañarla", [
   "<ul><li><b>Un gesto a la vez.</b> Si se confunde, regresen a la pantalla de ese gesto con Atrás.</li><li><b>No toques la pantalla por ella.</b> Si se pierde, que use el menú o los tres clics.</li></ul>"]),
  ("Gestos de esta lección", [
   "<dl><dt>Tocar</dt><dd>Escuchar qué hay.</dd><dt>Deslizar a la derecha o izquierda</dt><dd>Siguiente o anterior.</dd><dt>Dos toques</dt><dd>Presionar.</dd><dt>Un toque con dos dedos</dt><dd>Callar o seguir.</dd><dt>Deslizar desde abajo hasta la vibración</dt><dd>Pantalla de inicio.</dd><dt>Tres clics al botón lateral</dt><dd>Encender o apagar VoiceOver.</dd></dl>"]),
 ]),

# ───────────────────────── LECCIÓN 5 ─────────────────────────
dict(num=5, titulo="Conoce a Siri", nivel="c",
 intro="Hoy conoces a Siri, la asistente que te escucha. Elige una burbuja.",
 secciones=[
  dict(nombre="Historia", pantallas=[
   dict(t="texto", text="Siri es la asistente de tu iPhone. Le hablas y hace cosas por ti."),
   dict(t="texto", text="Para llamarla, di «Oye Siri» y luego lo que quieres. También puedes dejar apretado el botón lateral y hablar."),
   dict(t="texto", text="Habla claro y normal, como con una persona. No tienes que gritar ni hablar despacio."),
   dict(t="texto", text="Siri te dice la hora, el clima o cuánta batería tienes. También pone alarmas, llama y manda mensajes."),
   dict(t="texto", text="Siri también ayuda con VoiceOver. Di «Oye Siri, desactiva VoiceOver» o «activa VoiceOver»."),
   dict(t="texto", text="Si Siri no te entiende, no pasa nada. Dilo otra vez con otras palabras."),
   dict(t="salud", titulo="Tip de salud", text="Siri te ayuda a cuidarte. Pregúntale «¿A qué hora sale el sol?» y pon una alarma para despertarte a la misma hora todos los días. Tu cuerpo lo agradece."),
  ]),
  dict(nombre="Juego", pantallas=[
   dict(t="texto", titulo="Juego: ¿cierto o falso?", text="Siete frases sobre Siri y sobre cuidarte."),
   dict(t="pregunta", text="Para hablar con Siri puedes decir «Oye Siri».", ok=True, fb="¡Cierto! Y luego dices lo que quieres."),
   dict(t="pregunta", text="Tienes que gritar para que Siri te escuche.", ok=False, fb="¡Bien! Es falso. Habla normal."),
   dict(t="pregunta", text="Siri puede decirte cuánta batería tiene tu iPhone.", ok=True, fb="¡Cierto! Pregunta: ¿cuánta batería tengo?"),
   dict(t="pregunta", text="Siri puede apagar VoiceOver.", ok=True, fb="¡Cierto! Di: Oye Siri, desactiva VoiceOver."),
   dict(t="pregunta", text="Si Siri no te entiende, el iPhone se descompone.", ok=False, fb="¡Bien! Es falso. Solo dilo otra vez con otras palabras."),
   dict(t="pregunta", text="Puedes poner una alarma solo con la voz.", ok=True, fb="¡Cierto! Di: Oye Siri, pon una alarma a las siete."),
   dict(t="pregunta", text="Los niños de tu edad necesitan dormir entre 9 y 12 horas.", ok=True, fb="¡Cierto! Dormir bien te ayuda a aprender y a crecer."),
  ]),
  dict(nombre="Reto", pantallas=[
   dict(t="texto", titulo="Tu reto de hoy", text="Tres cosas con Siri: pregúntale la hora, pregúntale qué tiempo hace hoy y pon una alarma en cinco minutos. Cuando suene, apágala tú."),
  ]),
 ],
 despedida="En la última lección del nivel usas todo lo que aprendiste, con misiones.",
 mama=[
  ("Su salud: Siri ayuda con las rutinas", ["<p>Ella puede usar Siri para una alarma diaria a la misma hora, para saber a qué hora sale el sol o para un temporizador de baile. Así la tecnología le ayuda con sus rutinas, sin depender de nadie.</p>"]),
  ("De qué trata esta lección", [
   "<p>Cómo hablarle a Siri y qué le puede pedir: la hora, el clima, la batería, alarmas, llamadas, mensajes y encender o apagar VoiceOver.</p>"]),
  ("Antes de empezar", [
   "<ul><li><b>Configura Siri:</b> en Configuración busca «Siri». Elige español (México) y activa que responda a «Oye Siri». Dejen que responda también con el teléfono bloqueado.</li><li><b>Que Siri sepa quién es mamá:</b> con ella al lado, di «Oye Siri, [tu nombre] es mi mamá» desde su teléfono y confirma. Así «llama a mamá» funciona. 🟡 Si no lo guarda, agrega la relación en tu contacto, en la app Contactos.</li><li><b>Tu número en sus contactos,</b> con tu nombre bien escrito.</li></ul>"]),
  ("Lo nuevo en su página", [
   "<p>Igual que la Lección 4: menú de burbujas y botones de tamaño normal. El juego tiene siete preguntas.</p>"]),
  ("Cómo acompañarla", [
   "<ul><li><b>Que hable ella.</b> Si Siri no entiende, no repitas tú: que ella lo intente con otras palabras.</li><li><b>Apagar la alarma:</b> cuando suene, VoiceOver dice el botón para detenerla. Que lo busque deslizando y lo toque dos veces.</li><li><b>Siri no es infalible.</b> Cuando conteste algo raro, pregúntenle juntas otra vez.</li></ul>"]),
  ("Cosas para pedirle a Siri", [
   "<ul><li>«¿Qué hora es?»</li><li>«¿Qué tiempo hace hoy?»</li><li>«¿Cuánta batería tengo?»</li><li>«Pon una alarma en cinco minutos»</li><li>«Llama a mamá»</li><li>«Mándale un mensaje a mamá»</li><li>«Activa VoiceOver» o «Desactiva VoiceOver»</li></ul>"]),
 ]),

# ───────────────────────── LECCIÓN 6 ─────────────────────────
dict(num=6, titulo="Practicamos juntas", nivel="c",
 intro="Hoy no hay nada nuevo: vas a usar todo lo que aprendiste. Elige una burbuja.",
 secciones=[
  dict(nombre="Misiones", pantallas=[
   dict(t="mision", text="Encuentra los cuatro botones de tu iPhone y di el nombre de cada uno en voz alta."),
   dict(t="mision", text="Sube el volumen hasta que la voz de VoiceOver se oiga cómoda."),
   dict(t="mision", text="Di «Oye Siri, pon un temporizador de diez minutos» y baila o brinca hasta que suene."),
   dict(t="mision", text="Ve a la pantalla de inicio deslizando un dedo desde abajo hasta sentir la vibración."),
   dict(t="mision", text="Di «Oye Siri, ¿cuánta batería tengo?» y cuéntale a mamá la respuesta."),
   dict(t="mision", text="Mañana temprano: pregúntale a Siri qué tiempo hace, y sal un rato a la luz de la mañana con mamá."),
   dict(t="mision", text="Di «Oye Siri, mándale un mensaje a mamá». Cuando Siri pregunte qué dice, contesta: «Ya terminé mi misión»."),
   dict(t="mision", text="Apaga VoiceOver con tres clics, préstale el teléfono a mamá, y cuando te lo regrese, enciéndelo otra vez."),
  ]),
  dict(nombre="Juego", pantallas=[
   dict(t="texto", titulo="Juego: repaso", text="Preguntas de todo el nivel. Unas son de cierto o falso y otras de encontrar un botón."),
   dict(t="pregunta", text="Deslizar un dedo a la derecha te lleva a lo siguiente.", ok=True, fb="¡Cierto! Y a la izquierda regresas."),
   dict(t="busca", text="Encuentra el botón Volumen.", opciones=["Cámara","Pantalla","Volumen","Bocina","Cable","Siri"], correcta="Volumen"),
   dict(t="pregunta", text="Para presionar un botón con VoiceOver lo tocas una sola vez.", ok=False, fb="¡Bien! Es falso. Lo tocas dos veces."),
   dict(t="pregunta", text="Un toque con dos dedos hace que VoiceOver se calle.", ok=True, fb="¡Cierto! Otro toque con dos dedos, y sigue."),
   dict(t="pregunta", text="Es buena idea dormir con el iPhone debajo de la almohada.", ok=False, fb="¡Bien! Es falso. Déjalo cargando lejos de tu cama."),
   dict(t="busca", text="Encuentra el botón Botón lateral.", opciones=["Botón de Acción","Subir volumen","Bajar volumen","Botón lateral"], correcta="Botón lateral"),
  ]),
  dict(nombre="Reto", pantallas=[
   dict(t="texto", titulo="Reto final", text="Enséñale a mamá un gesto de VoiceOver que ella no sepa. Explícale cómo se hace, sin tocar su mano."),
  ]),
 ],
 despedida="¡Terminaste el Nivel 1! Ya sabes moverte con VoiceOver y hablar con Siri.",
 mama=[
  ("Su salud: las misiones", ["<p>Dos misiones son de salud: bailar o brincar con un temporizador de Siri, y salir un rato a la luz de la mañana.</p>", "<p>Tu papel es acompañarla y celebrarla. Si le gustan, que las siga haciendo aunque ya termine el nivel.</p>"]),
  ("De qué trata esta lección", [
   "<p>Repaso del Nivel 1 con misiones reales: botones, volumen, pantalla de inicio, Siri, mensajes y prestar el teléfono. Al final ella le enseña un gesto a mamá.</p>"]),
  ("Cómo funcionan las misiones", [
   "<p>Cada misión es una pantalla. Ella hace la tarea en su iPhone y luego toca dos veces «¡Lo logré!» para pasar a la siguiente. Si una misión no sale, pueden volver a la lección donde se vio.</p>",
   "<ul><li>Botones y volumen: Lección 3.</li><li>Pantalla de inicio y prestar el teléfono: Lección 4.</li><li>Siri y mensajes: Lección 5.</li></ul>"]),
  ("Antes de empezar", [
   "<p>Ten tu teléfono a la mano para recibir su mensaje, y revisa que Siri ya sepa quién es mamá (Lección 5).</p>"]),
  ("Cómo acompañarla", [
   "<ul><li><b>Celebra cada misión.</b> Son tareas reales que ya puede hacer sola.</li><li><b>En el reto final,</b> déjate enseñar. Explicar un gesto es la mejor señal de que ya lo domina.</li></ul>"]),
  ("Qué sigue", [
   "<p>El Nivel 2 entra a apps de verdad, con más botones: el rotor para saltar por partes, escribir, Mensajes y apps hechas para personas con discapacidad visual.</p>"]),
 ]),
]
