# Solución — Ejercicio 3: Aplica mínimo privilegio

Esta es una solución de referencia. Tu razonamiento puede variar en los
detalles siempre que identifique correctamente el principio violado y
proponga un conjunto de permisos acotado a la tarea real.

## Qué se violó

Se violó el principio de mínimo privilegio: se le dieron permisos amplios
(todo el sistema de archivos, cualquier comando) que exceden por mucho lo
que la tarea real (leer código, correr el linter, comentar) necesita. El
radio de daño fue mayor de lo necesario porque, cuando el agente fue
manipulado, tenía la capacidad técnica de ejecutar un comando destructivo —
una capacidad que nunca debió tener para esta tarea, independientemente de
si el modelo se equivoca por su cuenta o es engañado por contenido externo.

## Conjunto mínimo de permisos propuesto

- **Lectura:** acceso de solo lectura al código del repositorio del PR en
  cuestión (no al sistema de archivos completo del servidor).
- **Ejecución:** permiso para correr únicamente el comando del linter del
  proyecto (no shell sin restricciones).
- **Escritura:** ninguna — la tarea es comentar en la interfaz de revisión
  de PRs, no modificar archivos directamente.
- **Explícitamente prohibido:** cualquier comando de shell arbitrario,
  escritura en el sistema de archivos, acceso a directorios fuera del
  repositorio del PR en revisión.

## Respuesta al argumento de "es mucho trabajo"

Ajustar permisos caso por caso tiene un costo de configuración, pero ese
costo se paga una sola vez por tipo de tarea, mientras que el costo de no
hacerlo se paga potencialmente en cada incidente. Los permisos son la
primera línea de guardrails porque actúan en el momento de diseño: limitan
lo que puede pasar en el peor caso, antes de que el agente ejecute un solo
paso, en vez de depender de que cada acción individual sea validada
correctamente en tiempo real. Un incidente evitado por permisos bien
acotados es más barato que cualquier cantidad de configuración cuidadosa
que se hubiera "ahorrado" dándole acceso total al agente desde el inicio.
