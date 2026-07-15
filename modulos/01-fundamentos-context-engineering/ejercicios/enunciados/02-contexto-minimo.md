# Ejercicio 2: Diseña el contexto mínimo

## Escenario

Le vas a pedir a Claude Code que haga lo siguiente en un proyecto de
software real: **"Arregla el bug donde el botón de 'Guardar' del formulario
de perfil de usuario no hace nada al hacer clic."**

## Tu tarea

Sin ejecutar nada — solo en papel — responde:

1. Lista exactamente qué contexto necesitaría el agente para resolver esta
   tarea bien, siguiendo el principio de "contexto mínimo de alta señal" del
   módulo. Sé específico: no digas "el código relevante", di qué archivos,
   qué tipo de información sobre esos archivos, y en qué orden se debería
   obtener esa información (¿todo de una vez, o "justo a tiempo" a medida
   que se necesita?).
2. Lista tres cosas que **no** deberías incluir en el contexto de entrada
   aunque estén disponibles (por ejemplo: el código completo de módulos no
   relacionados, el historial completo de git del proyecto, etc.) y explica
   por qué incluirlas sería contraproducente, no solo innecesario.
3. Si el agente necesitara ejecutar la aplicación y reproducir el bug antes
   de arreglarlo, ¿ese resultado (logs, capturas, salida de consola) debería
   quedarse en el contexto completo para el resto de la tarea, o debería
   resumirse/descartarse una vez cumplido su propósito? Justifica con el
   concepto de compactación/poda visto en el módulo.
