# CINENOVA BLUE

Este proyecto conserva únicamente la aplicación Android recuperada:

- `CINENOVA-BLUE2_android-football-fixed-tv-crash-fix-signed.apk` — APK de prueba con reproducción directa de partidos Android y protección contra el cierre de `MediaActivity` cuando ExoPlayer informa un error.
- `CINENOVA-BLUE2_android-football-logos-hora-tv-signed.apk` — versión editada para Android y TV que carga directamente el `logoUrl` de la API y coloca la `hora` al principio de cada tarjeta deportiva.
- `CINENOVA-BLUE2_android-football-local-logos-tv-signed.apk` — versión recomendada: incluye copias locales ampliadas y transparentes de todos los logos de país/competición actuales, para que también se vean en TV aunque falle la descarga remota. Incluye además la corrección del crash causado por el enlace del cargador local.

## Importante

El APK fue reconstruido porque el código fuente original no estaba disponible. Está firmado
con una clave nueva de recuperación para instalación de prueba. Para actualizar una
instalación existente o publicar una actualización en una tienda, se necesita la clave de
firma original de la aplicación.

La versión corregida necesita conexión a Internet para cargar las transmisiones. Fue
reconstruida y firmada con una clave de recuperación nueva; debe instalarse como una
aplicación nueva si la versión anterior usa otra firma.

## Resolución del reproductor

La API de fútbol devuelve enlaces de páginas PHP que contienen un iframe y, dentro
de ese iframe, la URL HLS `.m3u8`. La versión `*-resolved.apk` sigue el iframe,
extrae la URL HLS temporal y se la entrega al reproductor ExoPlayer. La URL se
resuelve al cargar el carrusel, por lo que requiere conexión activa y puede caducar
cuando el proveedor renueve el token.

## Corrección de transmisiones en vivo

El reproductor original trataba como error cualquier fuente cuya duración reportada
fuera menor de cinco minutos. Las playlists HLS en vivo normalmente reportan solo
una ventana corta de segmentos, así que esa validación podía detener una transmisión
válida. La versión `*-live-signed.apk` conserva esa validación para vídeos normales,
pero la omite para fuentes `.m3u8`.

Cuando una transmisión falla, la ruta de fútbol no tiene el objeto `WebResult` que
usa el manejador genérico de errores para probar servidores alternativos. La variante
`*-tv-crash-fix-signed.apk` detecta ese caso y muestra el diálogo de error sin provocar
un cierre por referencia nula.

En Android, el adaptador del carrusel usa una ruta distinta a la de TV. Esta versión
también reconoce los partidos de fútbol en esa ruta y abre directamente el reproductor,
sin pasar por `InfoActivity`.

## Logos y horarios del carrusel

La API `https://ultrago-xi.vercel.app/gol-3` entrega los campos `hora` y `logoUrl`.
Las versiones `*-logos-hora-tv-signed.apk` usan la URL absoluta de `logoUrl` sin anteponer
la ruta de posters de TMDB, y muestran la hora antes del nombre del evento en las
tarjetas de Android y TV. La versión `*-local-logos-tv-signed.apk` además incluye
los recursos locales ampliados para evitar el respaldo genérico en TV. El endpoint actual entrega un solo logo por evento,
normalmente de la liga o del país; no entrega `equipo1Logo` y `equipo2Logo`
individuales, por lo que esta versión no puede mostrar dos escudos específicos
por partido sin ampliar la fuente de datos.