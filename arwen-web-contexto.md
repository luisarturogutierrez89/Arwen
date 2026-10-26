# Web de ARWEN · Contexto

## Qué es
El sitio oficial de ARWEN (DJ y productor de Afro House y Melodic Techno, CDMX / Estado de México). Es una sola página que funciona como press kit para promotores, venues y marcas.

## Cómo llegamos aquí
1. **Versión 1:** sitio editorial negro y dorado (Cormorant Garamond + Jost) con dos mundos. El **Press Kit** tenía bio, el arco de BPM, rider, ARWEN Sessions, galería y booking. El **ARWEN Lab** tenía 10 herramientas de código: 5 guías interactivas (Color FX, Beat FX, Smart CFX, La Fórmula del Mix, Crate Starter), además de DJ Prep Tool, Mix Replicator, arwen_reels.py, el generador de media kit y el EPK builder.
2. **Versión 2:** quitamos el Lab por ahora y rediseñamos el home tomando como referencia el póster de Nina Kraviz para Kappa FuTuR Festival.
3. **Versiones 3 y 4:** cambiamos las ilustraciones por fotos reales. La del rooftop quedó de fondo del hero y tres fotos en cabina quedaron en la galería.

## Diseño actual
- **Lenguaje:** póster suizo / festival. Retícula de 12 columnas, líneas finas blancas que separan las filas de datos y tipografía grotesca enorme (Inter Tight 800).
- **Hero:** "ARWEN" gigante arriba y otra vez recortado abajo, "ARWEN DJ" enorme en la columna derecha, y datos sueltos en la retícula: ciudad, géneros, "Sets 1–3H", "Presence is energy", "120–132 BPM".
- **Foto del hero:** blanco y negro con alto contraste y una trama de anillos concéntricos centrada en la cara.
- **Acentos:** cuadros blancos sólidos y cuadros con contorno en dorado ARWEN (#C6A268). El póster original usa rojo.
- **Paleta:** negro #0A0A0A, blanco hueso #F2F0EC, dorado #C6A268. Solo modo oscuro.
- **Responsive:** la retícula se adapta en el teléfono y la página no hace scroll horizontal.

## Secciones
1. **Hero / póster**
2. **Bio:** texto largo basado en el Press Kit 2026 (propuesta, Frecuencia Zero, fechas 2026 y activaciones) y botón "Copiar bio corta". Incluye la barra del arco del set: Afro House 120–125, Afro Tech 125–128, Melodic Techno 128–132 BPM.
3. **ARWEN Sessions:** Coffee (10:00–14:00, cafeterías y brunch), Sunset (16:00–21:00, terrazas y rooftops), Garden (jardines y hoteles), Night (clubs y venues nocturnos) y Sport (torneos y activaciones). Debajo, la Sesión 001 (ARWEN B2B BAZT_TZ) con link al perfil de SoundCloud.
4. **Rider & sonido**
   - Cabina: 2× CDJ-3000 en Pro DJ Link y DJM-900NXS2. Alternativas: Pioneer XDJ-AZ o equipo propio (DDJ-FLX4 + laptop).
   - En vivo 2026: Revo Rooftop (02.10, Frecuencia Zero × Revo Rooftop), Annua (04.09, ARWEN B2B BAZT_TZ) y Rumores (30.07, Frecuencia Zero × Rumores, Funktion-One).
   - Activaciones: Torneo Tecnifibre (22.08, tenis), Padelab (pádel) y MOEV Training Lab (evento de marca).
   - Referencias: Rampa, Adam Port, Adriatique, Keinemusik, Anyma y Yotto.
   - Lineups compartidos: Alexx Fall, Sanlika, BAZT_TZ, Andrreas, Shedlee, Francø, HOMM, Vargrbo, Nattsoo, Tlakoh, Angelo Diablo, Deja Böö, Bassenerg, Davor y Chávez.
5. **Galería:** 3 fotos en cabina, en blanco y negro, que recuperan su color al pasar el cursor. Debajo, botón "Descargar press kit".
6. **Booking:** arwenmusicmx@gmail.com (con botón de copiar), @arwen.dj, SoundCloud (soundcloud.com/luis-arturo-gutierrez-juarez-989173934), youtube.com/@arwen.musicdj, @frecuenciazerocolectivo, frecuenciazerocolectivo.com, descarga del press kit y linktr.ee/arwenmusicmx.

## ARWEN Lab
- Página aparte en `lab/index.html`, enlazada desde la nav del home ("Lab") y con regreso al press kit.
- Guías: Vol. I Color FX (`color-fx-afro-house.html`), Vol. II Beat FX (`beat-fx-afro-house.html`), Vol. III Smart CFX (`smart-cfx-sistema.html`), La Fórmula del Mix (`dj-formula-mezcla.html`) y Crate Starter (`dj-transiciones.html`).
- `lab/agregar-regreso.py` inserta el botón fijo "← ARWEN Lab" en cada guía de la carpeta (se puede correr varias veces).
- Fuera por ahora: DJ Prep Tool, Mix Replicator, arwen_reels.py, generador de media kit y EPK builder.

## Marca e íconos
- `marca/arwen-logo.png`: logo completo (emblema dorado + ARWEN + géneros) sobre negro, 1254×1254.
- `favicon.svg`: versión simplificada del emblema para la pestaña, con `favicon-32.png` de respaldo. `apple-touch-icon.png` es el emblema recortado del logo, para el ícono en iPhone.
- El home, el Lab y las guías enlazan los tres íconos.
- El PDF del press kit todavía dice soundcloud.com/arwenmusic; hay que corregirlo en la próxima versión.

## Descargas (`descargas/`)
- `ARWEN-Press-Kit-2026.pdf`: press kit de 9 páginas en vertical. Se enlaza desde Rider y Booking.
- El press kit incluye el WhatsApp, así que queda público al descargarlo.
- El media kit de ARWEN Sessions (16:9 y 4:5) no se publica porque trae la tarifa: se manda por correo. Los PDFs están en `descargas/`, pero el `.gitignore` los deja fuera del repo.

## Archivo
`index.html` funciona solo, sin carpetas aparte, porque las fotos van incrustadas. Se puede abrir en el navegador o subir tal cual a un hosting (Netlify, Vercel, GitHub Pages).

## Pendientes
- Agregar embeds de sets (ya hay links a los perfiles de SoundCloud y YouTube y a la Sesión 001).
- Hacer una versión en inglés para promotores fuera de México.
- Agregar las próximas fechas de ARWEN Sessions al hero, como las fechas del festival en el póster.
- Revisar la bio cuando haya releases o logros nuevos.
