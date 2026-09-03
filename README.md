# CINENOVA BLUE

Este proyecto conserva únicamente la aplicación Android recuperada:

- `CINENOVA-BLUE2_sign.apk` — APK instalable de CINENOVA BLUE.
- `CINENOVA-BLUE2_android-football-fixed.apk` — APK de prueba con el carrusel de fútbol habilitado también en Android y con resolución de enlaces del reproductor.
- `CINENOVA-BLUE2_android-football-fixed-resolved.apk` — APK de prueba con la resolución HLS aplicada también a la ruta Android.

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