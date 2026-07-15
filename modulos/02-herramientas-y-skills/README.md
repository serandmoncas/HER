# Módulo 2 — Herramientas y Skills

## ¿Qué es una herramienta?

En términos de un harness, una **herramienta** es una capacidad con nombre que
el modelo puede invocar: un nombre, una descripción de qué hace y cuándo
usarla, y un esquema de parámetros que el modelo debe llenar para invocarla.
A diferencia de generar texto, invocar una herramienta produce un efecto o
una consulta fuera del propio modelo — leer un archivo, ejecutar un comando,
llamar una API, buscar en internet.

La descripción de cada herramienta disponible es, en sí misma, contexto — y
el Módulo 1 ya estableció que el contexto no es gratis. Un agente con veinte
herramientas cargadas, la mitad de ellas irrelevantes para la tarea actual,
no solo desperdicia presupuesto de contexto: aumenta la probabilidad de que
el modelo confunda dos herramientas parecidas o invoque la equivocada. El
principio de "contexto mínimo de alta señal" aplica igual de directo a las
herramientas que al resto del contexto: menos herramientas, bien descritas y
sin solapamiento, superan a un catálogo extenso de capacidades parecidas
entre sí.

## Skills en Claude Code: contexto cargado justo a tiempo

Una **skill** en Claude Code no es solo una herramienta — es una pieza de
instrucciones y conocimiento (un archivo Markdown con un encabezado de
nombre y descripción, seguido del cuerpo con el procedimiento completo) que
permanece fuera del contexto activo hasta que la tarea la necesita.

Esto es una aplicación directa del principio "justo a tiempo" del Módulo 1.
Lo único que ocupa contexto todo el tiempo es el nombre y la descripción de
cada skill disponible — una lista corta y barata de mantener presente. El
cuerpo completo de instrucciones solo se carga cuando el modelo, comparando
la tarea actual contra esas descripciones, decide que la skill es relevante.
Esto le permite a un agente tener acceso a cientos de procedimientos
especializados sin que ninguno de ellos infle el contexto de una tarea que
no los necesita.

Esto convierte escribir la descripción de una skill en un acto de context
engineering en sí mismo: tiene que ser lo bastante específica para que el
modelo la recupere de forma confiable cuando aplica, pero no tan amplia que
se cargue en tareas donde no aporta nada — cada carga innecesaria es
exactamente el tipo de contexto de bajo valor que el Módulo 1 identificó
como causa de *context rot*.

## Subagentes: delegar con una ventana de contexto limpia

El Módulo 1 mencionó la delegación como una de las estrategias para manejar
el presupuesto de contexto: encargarle una subtarea a un **subagente** con
su propia ventana de contexto, en vez de acumular todo en la conversación
principal.

Un subagente recibe una descripción de tarea acotada, hace su propio
trabajo — que puede incluir usar sus propias herramientas, leer muchos
archivos, iterar varias veces — en un contexto aislado, y devuelve a la
conversación principal solo el resultado destilado, no el proceso completo
que le costó llegar ahí. Esto resuelve un problema distinto al que resuelven
las skills: no es que falte una instrucción específica, es que el volumen
de exploración intermedia (grepear un repositorio grande, leer decenas de
archivos, descartar callejones sin salida) ensuciaría la conversación
principal si se hiciera ahí directamente.

La diferencia clave: una skill añade capacidad o conocimiento al contexto
*actual*; un subagente saca trabajo del contexto actual y lo hace en otro
lado.

## Skill vs. subagente: cómo decidir

Un marco práctico de decisión:

- **Usa una skill** cuando la tarea necesita una instrucción o conocimiento
  específico, pero el trabajo en sí es liviano — pocas invocaciones de
  herramientas, salida corta. El objetivo es enseñarle al agente principal
  cómo hacer algo, no sacarle trabajo de encima.
- **Usa un subagente** cuando la tarea requiere exploración o iteración
  pesada cuyos pasos intermedios inundarían el contexto si se hicieran en
  línea, cuando conviene paralelizar fragmentos de trabajo independientes, o
  cuando aislar un paso riesgoso o experimental del contexto de confianza de
  la conversación principal importa por sí solo.
- Muchas tareas reales combinan ambas: una skill puede instruir al agente
  para que despache un subagente como parte de su procedimiento, en vez de
  ser mutuamente excluyentes.

Ni la skill ni el subagente son gratis: cada uno tiene un costo de diseño y
de mantenimiento. Cuando ninguno de los dos criterios anteriores aplica — la
tarea es puntual, liviana y no se va a repetir — la respuesta correcta suele
ser ninguno de los dos: una instrucción directa en el prompt basta.

## Permisos y sandboxing: el principio de mínimo privilegio

Darle a una herramienta, skill o subagente acceso a todo — todo el sistema
de archivos, red sin restricciones, capacidad de ejecutar cualquier comando
de shell — aumenta el radio de daño cuando el modelo comete un error o es
manipulado por contenido malicioso que procesa (inyección de prompt).

La mitigación es el **principio de mínimo privilegio**: limitar los
permisos de cada pieza del harness a exactamente lo que su tarea necesita,
ni más. En Claude Code esto se ve en los modos de permisos y en las listas
explícitas de herramientas permitidas por skill o subagente; en general,
cualquier harness bien diseñado debería poder responder, para cada pieza,
"¿qué es lo peor que puede pasar si esta pieza se equivoca o es engañada?" y
que el radio de daño de esa respuesta sea aceptable.

Los permisos son la primera línea de guardrails de un harness — aplicada en
el momento de diseño, antes de que el agente ejecute un solo paso, en vez de
intentar validar cada acción después del hecho. El Módulo 5 (Evaluación y
Guardrails) retoma este tema en profundidad, incluyendo validación en
tiempo de ejecución como complemento a los permisos de diseño.

## Para reflexionar / Referencias

- La documentación oficial de Claude Code sobre Skills y Subagentes es la
  referencia más actualizada para los detalles de implementación de estos
  dos mecanismos.
- Herramientas equivalentes existen en otras plataformas de agentes (reglas
  de Cursor, `AGENTS.md` de Codex), aunque con diseños distintos de cuándo y
  cómo se carga esa información en el contexto — vale la pena compararlos
  una vez domines el modelo de Claude Code, no antes.
- Este módulo construye directamente sobre "contexto mínimo de alta señal" y
  *context rot*, cubiertos en el
  [Módulo 1](../01-fundamentos-context-engineering/).
