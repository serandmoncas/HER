# Solución — Ejercicio 2: Diseña el contexto mínimo

Esta es una solución de referencia; el objetivo es el razonamiento, no una
lista exacta de archivos (que varía según el proyecto real).

## Contexto mínimo necesario

En orden, obtenido justo a tiempo en vez de todo de una vez:

1. El nombre/ruta del componente del formulario de perfil de usuario (no su
   código todavía) — típicamente localizable por nombre de archivo o
   búsqueda de texto ("Guardar", "profile form"), no leyendo todo el
   proyecto.
2. El contenido completo de ese archivo (y del archivo del manejador del
   evento de clic si está separado), una vez localizado.
3. Solo si el bug no es evidente ahí: el código de la función/handler que
   debería ejecutarse al guardar (el servicio o API que el botón debería
   estar llamando).
4. Solo si sigue sin ser evidente: logs o salida de la consola del
   navegador al reproducir el clic.

La idea central es no leer 2-4 por adelantado "por si acaso" — cada paso
solo se ejecuta si el anterior no fue suficiente para diagnosticar el
problema.

## Qué NO incluir

- **Código completo de módulos no relacionados** (ej. el módulo de
  facturación): no aporta señal para este bug y compite por atención con lo
  que sí importa — es la definición misma de contexto de bajo valor que
  causa *context rot*.
- **Historial completo de git del proyecto**: es contexto masivo (miles de
  commits) para un problema que casi seguro se explica por el estado
  *actual* del código, no por su historia completa. Incluirlo no es solo
  "innecesario" — activamente diluye la atención del modelo sobre el código
  real que tiene que leer y cambiar.
- **Documentación general del proyecto no relacionada con el formulario de
  perfil** (ej. guías de arquitectura de otros módulos): mismo problema —
  volumen sin señal para esta tarea puntual.

## Logs de reproducción del bug

Deberían resumirse una vez cumplen su propósito, no quedarse completos en
el contexto. El agente los necesita para *confirmar* el diagnóstico (por
ejemplo, "el evento onClick nunca se dispara"), pero una vez extraído ese
hecho, mantener el log crudo completo (que puede tener cientos de líneas de
ruido de otras partes de la aplicación) solo ocupa presupuesto de contexto
sin aportar nada nuevo para el resto de la tarea (escribir y verificar el
fix). Esto es exactamente el patrón de compactación/poda visto en el
módulo: condensar el hallazgo, descartar el detalle que ya cumplió su
función.
