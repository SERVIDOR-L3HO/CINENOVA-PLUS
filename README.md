# CINENOVA

Este proyecto conserva la aplicación Android recuperada desde el APK original.

## Archivos actualizados

- `dist/CINENOVA-glass-info-button.apk` — APK instalable con el botón “Información” rediseñado con estilo glass.
- `tools/inject-football.py` — inyector reproducible para aplicar la integración al árbol decodificado del APK recuperado.
- `tools/replace-notification-icon.py` — reemplazo reproducible de las cinco densidades de `ic_stat_name.png`.
- `tools/replace-toast-logo.py` — reemplazo reproducible de `assets/ToastAndroForever.png`.
- `apk-edit/res/layout/media_controller.xml` — fuente de la nueva interfaz del reproductor.
- `apk-edit/res/layout/activity_info.xml` — composición glass de la pantalla de información.
- `apk-edit/res/layout/horizontal_raw.xml` — encabezados y espaciado de las secciones de inicio.
- `apk-edit/res/layout/media_raw.xml` — tarjetas visuales de los carruseles.
- `apk-edit/res/layout/media_list_raw.xml` — tarjetas con título para la vista tipo lista.

La edición conserva la reproducción ExoPlayer existente y añade una presentación más profesional:

- encabezado con título, descargar y compartir;
- controles centrales de reproducción, retroceso y avance;
- barra de progreso con tiempo actual, duración y buffer;
- controles reales de reproducción aleatoria y repetición;
- soporte existente para reanudar la posición, gestos de zoom y reproducción en horizontal.

La pantalla de inicio ahora combina carruseles con tarjetas glass y una cuadrícula vertical de dos columnas en “Todas”. La carga de contenido también limita cada sección al número real de resultados recibidos y evita intentar mostrar el héroe cuando la respuesta llega vacía.

La edición de fútbol:

- carga las transmisiones de forma asíncrona para no bloquear la pantalla principal;
- filtra eventos que no son fútbol y muestra hasta 18 partidos;
- intenta resolver las páginas HTML de los canales hasta localizar una fuente HLS `.m3u8`;
- inserta la sección entre “Recientes” y “Estrenos”;
- abre los canales reproducibles directamente en el reproductor ExoPlayer existente, con `referer` y manejo de error ya provisto por la actividad nativa.

## Importante

El APK fue reconstruido porque el código fuente original no estaba disponible. Está firmado con una clave nueva de recuperación para instalación de prueba. Para actualizar una instalación existente o publicar una actualización en una tienda, se necesita la clave de firma original de la aplicación.