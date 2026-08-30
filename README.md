# CINENOVA

Este proyecto conserva la aplicación Android recuperada desde el APK original.

## Archivos actualizados

- `dist/CINENOVA-player-pro.apk` — APK instalable con el reproductor rediseñado para CINENOVA.
- `dist/CINENOVA-glass-info.apk` — APK instalable con la pantalla de información rediseñada con estilo glass.
- `dist/CINENOVA-lista-creativa.apk` — APK instalable con carruseles renovados y una cuadrícula tipo lista para “Todas”.
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

## Importante

El APK fue reconstruido porque el código fuente original no estaba disponible. Está firmado con una clave nueva de recuperación para instalación de prueba. Para actualizar una instalación existente o publicar una actualización en una tienda, se necesita la clave de firma original de la aplicación.