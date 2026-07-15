# Ejercicio 3: Aplica mínimo privilegio

## Escenario

Un equipo le dio a su agente de codificación permiso para ejecutar
**cualquier comando de shell sin restricciones** y acceso de
lectura/escritura a **todo el sistema de archivos del servidor**, "para no
tener que estar ajustando permisos cada vez que el agente necesita algo
nuevo". La tarea real del agente es: revisar pull requests y dejar
comentarios sugiriendo cambios — nunca necesita modificar archivos
directamente ni ejecutar nada fuera de leer el código y correr el linter
del proyecto.

Un día, el agente procesa un PR que contiene, dentro de un comentario de
código, texto diseñado para manipularlo (inyección de prompt) e intenta
ejecutar un comando destructivo.

## Tu tarea

1. Identifica qué principio del módulo se violó en el diseño original de
   permisos de este agente, y por qué el radio de daño del incidente fue
   mayor de lo necesario.
2. Propón el conjunto mínimo de permisos que este agente debería tener para
   cumplir su tarea real (revisar PRs y comentar), siendo específico sobre
   qué debería poder leer, qué debería poder ejecutar, y qué debería tener
   explícitamente prohibido.
3. El equipo argumenta que ajustar permisos caso por caso "es mucho
   trabajo". Responde ese argumento conectándolo con la idea del módulo de
   que los permisos son la primera línea de guardrails, aplicada en el
   momento de diseño.
