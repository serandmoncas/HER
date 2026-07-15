---
name: revisar-diff
description: Usa esta skill cuando el usuario pida revisar código, un diff, un pull request, o cambios recientes en busca de bugs, problemas de seguridad o violaciones de las convenciones del proyecto. Se activa con frases como "revisa este código", "haz code review", "revisa este diff" o "revisa los cambios en <archivo>".
---

# Revisar diff

## Cuándo usar esta skill

Actívate cuando el usuario pida una revisión de código: de un archivo
específico, de un conjunto de cambios, o de algo que describa como "diff" o
"pull request". Esta skill es de solo lectura — nunca modifiques el código
que estás revisando, solo repórtalo.

## Procedimiento

1. **Lee el código a revisar.** Si el usuario no especifica qué archivo o
   cambio revisar, pregunta antes de asumir.
2. **Lee las convenciones del proyecto**, si existe un archivo
   `CONVENCIONES.md` en el directorio del proyecto. Si no existe, evalúa
   solo bugs de lógica y problemas de seguridad genéricos, y dilo
   explícitamente en tu reporte.
3. **Evalúa el código en tres categorías**, sin mezclarlas:
   - **Bugs de lógica:** errores de comportamiento — casos no manejados,
     condiciones incorrectas, resultados que no coinciden con lo que la
     función dice hacer.
   - **Problemas de seguridad:** uso de funciones peligrosas (`eval`,
     `exec`, concatenación de queries sin parametrizar, etc.), secretos o
     credenciales expuestas en el código, validación de entrada ausente.
   - **Violaciones de convenciones:** cualquier regla de `CONVENCIONES.md`
     que el código no cumpla.
4. **Reporta cada hallazgo con evidencia concreta**: referencia el
   archivo y la línea exacta, cita el fragmento de código relevante, y
   explica por qué es un problema. No inventes números de línea ni
   describas un problema que no puedas señalar en el código que leíste.
5. **No propongas ni apliques el arreglo tú mismo** — esta skill da
   feedback, no corrige. Sugerir la corrección en palabras está bien;
   editar el archivo no.

## Formato del reporte

Agrupa los hallazgos exactamente en este orden, omitiendo cualquier
categoría sin hallazgos:

```
### Bugs de lógica
### Problemas de seguridad
### Violaciones de convenciones
```

Para cada hallazgo: archivo:línea, qué está mal, por qué importa. Si no
encontraste ningún problema en una categoría, no incluyas esa sección — no
la incluyas vacía ni escribas "ninguno encontrado".
