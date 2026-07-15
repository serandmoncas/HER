# Módulo 2 (Herramientas y Skills) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship the second complete, self-contained module (`modulos/02-herramientas-y-skills/`) with theory, exercises + solutions, and group-session materials, then flip the root README roadmap row for Módulo 2 from 🚧 to ✅.

**Architecture:** Pure Markdown content repository. No build system, no application code. This module follows the exact same internal structure as Módulo 1 (`README.md`, `ejercicios/enunciados/`, `ejercicios/soluciones/`, `sesion-grupal/facilitador.md`, `sesion-grupal/participante.md`) and builds explicitly on Módulo 1's concepts (contexto mínimo de alta señal, *context rot*, delegación) rather than introducing them from scratch. Módulos 3-5, the three example projects, and the "Proyecto — Asistente de code review" checkpoint that follows this module are out of scope for this plan — they get their own follow-up plans.

**Tech Stack:** Markdown only. Git for version control.

## Global Constraints

- All content in Spanish (per design spec `docs/superpowers/specs/2026-07-14-harness-engineering-repo-design.md`).
- Claude Code is the reference tool for all practical content; other tools (Cursor, Codex/AGENTS.md) get at most a brief comparative note, never a full example.
- No automated test suite — verification is manual (read-through + structural grep checks), matching Módulo 1's precedent.
- Module folder structure is fixed: `README.md`, `ejercicios/enunciados/`, `ejercicios/soluciones/`, `sesion-grupal/facilitador.md`, `sesion-grupal/participante.md`.
- Content must explicitly connect back to Módulo 1 terminology already shipped (contexto mínimo de alta señal, *context rot*, "justo a tiempo", delegación) rather than reintroducing those ideas under different names — this module is Módulo 1's own "Herramientas y Skills" preview cashed in.
- The root README roadmap table (`README.md:33-42`) must have its Módulo 2 row (currently line 36) flipped from `🚧 Próximamente` to `✅ Disponible` with a working relative link, as the final step of this plan — same pattern already used for Módulo 1's row.

---

### Task 1: Módulo 2 — Teoría

**Files:**
- Create: `modulos/02-herramientas-y-skills/README.md`

**Interfaces:**
- Consumes: `modulos/01-fundamentos-context-engineering/README.md` (already shipped) — this task's content must reference its "contexto mínimo de alta señal", *context rot*, "justo a tiempo", and "Delegación" concepts by name, not redefine them.
- Produces: the skill-vs-subagent decision framework and the "mínimo privilegio" concept that Tasks 2-3 of this plan reference by name ("el marco de decisión del módulo", "principio de mínimo privilegio").

- [ ] **Step 1: Write the module theory content**

Create `modulos/02-herramientas-y-skills/README.md`:

```markdown
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
```

- [ ] **Step 2: Verify structure**

Run: `grep -c '^## ' modulos/02-herramientas-y-skills/README.md`
Expected: `6`

Run: `wc -w modulos/02-herramientas-y-skills/README.md`
Expected: at least `700`

Run: `grep -c 'Módulo 1' modulos/02-herramientas-y-skills/README.md`
Expected: at least `1` (confirms the explicit cross-reference required by Global Constraints)

- [ ] **Step 3: Commit**

```bash
git add modulos/02-herramientas-y-skills/README.md
git commit -m "$(cat <<'EOF'
Add Módulo 2 theory: Herramientas y Skills

Covers what a tool is, how Claude Code Skills apply the "just in time"
context principle from Módulo 1, when to use a subagent instead, a
skill-vs-subagent decision framework, and least-privilege permissions
as the first line of harness guardrails.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 2: Módulo 2 — Ejercicios (enunciados + soluciones)

**Files:**
- Create: `modulos/02-herramientas-y-skills/ejercicios/enunciados/01-skill-subagente-ninguno.md`
- Create: `modulos/02-herramientas-y-skills/ejercicios/enunciados/02-contrato-herramienta.md`
- Create: `modulos/02-herramientas-y-skills/ejercicios/enunciados/03-minimo-privilegio.md`
- Create: `modulos/02-herramientas-y-skills/ejercicios/soluciones/01-skill-subagente-ninguno.md`
- Create: `modulos/02-herramientas-y-skills/ejercicios/soluciones/02-contrato-herramienta.md`
- Create: `modulos/02-herramientas-y-skills/ejercicios/soluciones/03-minimo-privilegio.md`

**Interfaces:**
- Consumes: the theory README from Task 1 (exercises reference the skill-vs-subagent decision framework and the "principio de mínimo privilegio" defined there)
- Produces: `01-skill-subagente-ninguno` is the exercise Task 3 (group session) reuses as its live group activity — its filename must match exactly.

- [ ] **Step 1: Write exercise 1 statement — skill, subagente o ninguno**

Create `modulos/02-herramientas-y-skills/ejercicios/enunciados/01-skill-subagente-ninguno.md`:

```markdown
# Ejercicio 1: Skill, subagente o ninguno

## Tu tarea

Para cada situación, decide si el agente debería resolverla con **(a)** una
instrucción directa en el momento (sin skill ni subagente), **(b)** una
skill, o **(c)** un subagente. Justifica cada respuesta en 1-2 frases
usando el marco de decisión del módulo.

1. Un usuario le pide al agente que revise un pull request completo de 40
   archivos, identificando bugs, problemas de seguridad y violaciones de
   las convenciones del proyecto, antes de que el agente continúe con la
   conversación principal.
2. Un usuario le pide al agente que convierta una fecha de un formato a
   otro, una sola vez, dentro de una tarea más grande.
3. Un equipo quiere que, cada vez que el agente termine de escribir código
   nuevo, automáticamente aplique un procedimiento de 15 pasos específico
   de la empresa para formatear, documentar y verificar el estilo del
   código, sin que nadie tenga que repetir esas instrucciones cada vez.
4. Un agente necesita, como parte de una tarea de investigación, leer y
   resumir el contenido de 50 páginas web distintas, y solo el resumen
   final le importa a la conversación principal.
5. Un usuario le pide al agente que le explique, en sus propias palabras,
   la diferencia entre dos conceptos que ya están claros en la
   conversación actual.
```

- [ ] **Step 2: Write exercise 2 statement — contrato de una herramienta**

Create `modulos/02-herramientas-y-skills/ejercicios/enunciados/02-contrato-herramienta.md`:

```markdown
# Ejercicio 2: Diseña el contrato de una herramienta

## Escenario

Vas a diseñar una herramienta nueva para un agente: **consultar el precio
actual de una acción bursátil dado su símbolo (ticker)**.

## Tu tarea

1. Define el nombre de la herramienta, su descripción (el texto que el
   modelo va a leer para decidir cuándo usarla) y el esquema de parámetros
   que necesita, siguiendo el principio de superficie mínima visto en el
   módulo.
2. Explica, en un párrafo, por qué la descripción que escribiste cuenta
   como contexto y qué pasaría si fuera demasiado vaga (el modelo no la usa
   cuando debería) o demasiado amplia (el modelo la usa cuando no debería).
3. Menciona un parámetro tentador de añadir a esta herramienta que en
   realidad NO deberías incluir, y explica por qué agregarlo violaría el
   principio de superficie mínima.
```

- [ ] **Step 3: Write exercise 3 statement — mínimo privilegio**

Create `modulos/02-herramientas-y-skills/ejercicios/enunciados/03-minimo-privilegio.md`:

```markdown
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
```

- [ ] **Step 4: Write solution 1**

Create `modulos/02-herramientas-y-skills/ejercicios/soluciones/01-skill-subagente-ninguno.md`:

```markdown
# Solución — Ejercicio 1: Skill, subagente o ninguno

Esta es una solución de referencia. Tu razonamiento puede variar en los
detalles siempre que aplique correctamente el marco de decisión del
módulo.

1. **→ Subagente.** Es una tarea de exploración pesada (40 archivos) cuyo
   proceso intermedio (leer cada archivo, razonar sobre cada uno)
   inundaría la conversación principal; solo el resultado destilado (los
   hallazgos) importa de vuelta.
2. **→ Ninguno.** Es puntual, liviana, no se repite — una instrucción
   directa basta, no justifica el costo de mantener una skill ni de
   aislar contexto en un subagente.
3. **→ Skill.** Es un procedimiento específico y repetible que se necesita
   cada vez que ocurre cierta condición (terminar de escribir código) —
   exactamente el patrón de "instrucciones que solo hace falta cargar
   cuando la tarea coincide". El número de pasos (15) no cambia esto: una
   skill puede contener un procedimiento largo, lo que importa es que es
   conocimiento a aplicar, no trabajo pesado a aislar.
4. **→ Subagente** (posiblemente varios, uno por página o en lotes). El
   volumen de contenido intermedio (50 páginas completas) ensuciaría el
   contexto principal; solo el resumen agregado debe volver a la
   conversación.
5. **→ Ninguno.** La información ya está en el contexto actual; no hace
   falta ni instrucciones nuevas ni aislar trabajo en otro lado, es una
   respuesta directa sobre algo que ya se sabe.
```

- [ ] **Step 5: Write solution 2**

Create `modulos/02-herramientas-y-skills/ejercicios/soluciones/02-contrato-herramienta.md`:

```markdown
# Solución — Ejercicio 2: Diseña el contrato de una herramienta

Esta es una solución de referencia; el objetivo es el razonamiento sobre
superficie mínima, no un esquema exacto (que puede variar en detalles).

## Contrato propuesto

- **Nombre:** `obtener_precio_accion`
- **Descripción:** "Devuelve el precio actual de una acción bursátil dado
  su símbolo (ticker). Úsala cuando el usuario pregunte por el precio
  actual o reciente de una acción específica."
- **Parámetros:** `ticker` (string, requerido) — el símbolo bursátil, por
  ejemplo "AAPL".

## Por qué la descripción es contexto

La descripción es lo que el modelo lee para decidir, sin haber leído el
código de la herramienta, si esta es la herramienta correcta para la tarea
actual. Si es demasiado vaga (por ejemplo, "Obtiene datos financieros"), el
modelo puede no reconocer que aplica cuando sí debería, o confundirla con
otra herramienta de datos financieros parecida. Si es demasiado amplia o
imprecisa (por ejemplo, sugiriendo que también sirve para históricos o
para otras clases de activos que no maneja), el modelo la va a invocar en
casos donde no corresponde y va a fallar o devolver resultados incorrectos
— el mismo problema de superficie difusa que el módulo describe para
skills mal descritas.

## Parámetro a NO incluir

Un parámetro tentador pero incorrecto sería una "moneda de conversión" o
un "rango de fechas históricas". Aunque parezca útil, la herramienta se
definió específicamente para el precio *actual* — añadir ese parámetro
amplía la superficie de la herramienta más allá de su propósito único, lo
que la hace más difícil de describir con precisión y aumenta la
probabilidad de que el modelo la use mal. Si se necesita esa
funcionalidad, debería ser una herramienta separada, con su propia
descripción específica.
```

- [ ] **Step 6: Write solution 3**

Create `modulos/02-herramientas-y-skills/ejercicios/soluciones/03-minimo-privilegio.md`:

```markdown
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
```

- [ ] **Step 7: Verify enunciados/soluciones pairing**

Run:
```bash
diff <(ls modulos/02-herramientas-y-skills/ejercicios/enunciados/) \
     <(ls modulos/02-herramientas-y-skills/ejercicios/soluciones/)
```
Expected: no output (empty diff — every enunciado has a matching solución filename)

- [ ] **Step 8: Commit**

```bash
git add modulos/02-herramientas-y-skills/ejercicios/
git commit -m "$(cat <<'EOF'
Add Módulo 2 exercises with reference solutions

Three exercises covering skill/subagent/neither classification, tool
contract design under a minimal-surface-area principle, and applying
least privilege to an over-permissioned agent — each with a matching
solution in a separate folder for self-assessment.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 3: Módulo 2 — Sesión grupal

**Files:**
- Create: `modulos/02-herramientas-y-skills/sesion-grupal/facilitador.md`
- Create: `modulos/02-herramientas-y-skills/sesion-grupal/participante.md`

**Interfaces:**
- Consumes: the theory README from Task 1 and Exercise 1 (`01-skill-subagente-ninguno`) from Task 2 — the group session reuses that exact exercise as its live group activity.
- Produces: nothing consumed elsewhere in this plan

- [ ] **Step 1: Write the facilitator guide**

Create `modulos/02-herramientas-y-skills/sesion-grupal/facilitador.md`:

```markdown
# Sesión grupal — Módulo 2: Facilitador

**Duración total:** ~75 minutos
**Tamaño de grupo recomendado:** 4-12 personas
**Requisito previo:** los participantes deben haber leído el `README.md`
de este módulo antes de la sesión.

## Agenda

### 1. Apertura: repaso rápido de Módulo 1 (10 min)

Pregunta disparadora para abrir, en plenaria:

> "¿Alguien puede dar un ejemplo, de su propia experiencia con Claude Code
> u otro agente, de algo que se sintió como 'contexto cargado justo a
> tiempo'?"

Conecta las respuestas con la idea de que las skills son una aplicación
directa de ese principio, tal como lo explica la primera sección del
módulo. No hace falta repasar "qué es un harness" desde cero — solo anclar
la sesión al principio de justo-a-tiempo antes de avanzar.

### 2. Refuerzo del concepto central (10 min)

Discusión guiada sobre la diferencia entre skill y subagente, usando la
pregunta:

> "Si tuvieran que explicarle a alguien sin experiencia técnica la
> diferencia entre una skill y un subagente en una sola frase, ¿cuál
> sería?"

Deja que 2-3 personas propongan su frase antes de reforzar la definición
formal del módulo: una skill añade conocimiento al contexto *actual*; un
subagente saca trabajo del contexto actual y lo hace en otro lado.

### 3. Actividad grupal: clasificación skill/subagente/ninguno (30 min)

Divide al grupo en equipos de 2-3 personas. Cada equipo trabaja el
**Ejercicio 1 (Skill, subagente o ninguno)** del módulo — está en
`ejercicios/enunciados/01-skill-subagente-ninguno.md`.

Timing sugerido dentro de este bloque:
- 15 min: cada equipo clasifica los 5 escenarios y prepara su
  justificación.
- 15 min: cada equipo comparte 1-2 de sus clasificaciones más discutidas
  (no las 5, para dejar tiempo a todos los equipos). Como facilitador,
  presta especial atención al escenario 3 (la skill de 15 pasos de la
  empresa) y a la comparación entre los escenarios 1 y 4 (ambos
  subagentes, pero por razones ligeramente distintas) — son los que más
  generan debate útil.

Nota para el facilitador: la solución de referencia está en
`ejercicios/soluciones/01-skill-subagente-ninguno.md`. No la compartas
antes de que los equipos presenten — úsala para guiar el cierre de la
discusión, no como veredicto impuesto sobre el razonamiento del grupo.

### 4. Cierre: permisos como primera línea de guardrails (15 min)

Cierra conectando con la última sección del módulo. Pregunta al grupo si
alguna vez han visto, o escuchado de, un agente o automatización con más
permisos de los que su tarea real necesitaba. Sin necesidad de resolver el
Ejercicio 3 en vivo, usa esas anécdotas para introducir el principio de
mínimo privilegio y anticipar que el Módulo 5 (Evaluación y Guardrails)
retoma este tema en profundidad.

### 5. Tarea antes de la siguiente sesión (5 min)

Pide que completen los Ejercicios 2 y 3 individualmente antes de la
siguiente sesión grupal (Módulo 3), ya que no se cubren en vivo.

## Notas generales de facilitación

- Si el grupo ya trabajó la sesión del Módulo 1, pueden arrancar más
  rápido en el paso 1 — no hace falta repasar "qué es un harness" desde
  cero, solo conectar con la idea de justo-a-tiempo.
- El escenario 3 del Ejercicio 1 (la skill de formateo/documentación de la
  empresa) suele generar la pregunta "¿por qué no simplemente un
  subagente?" — es una buena oportunidad para reforzar que las skills son
  para instrucciones, no para aislar trabajo pesado, incluso cuando el
  procedimiento tiene muchos pasos.
- Si el tiempo se acorta, el bloque que más se puede recortar sin perder
  el objetivo de la sesión es el paso 2 (a 5 min) — el paso 3 es el
  corazón de la sesión y no debería recortarse.
```

- [ ] **Step 2: Write the participant guide**

Create `modulos/02-herramientas-y-skills/sesion-grupal/participante.md`:

```markdown
# Sesión grupal — Módulo 2: Participante

**Antes de esta sesión:** lee el `README.md` de este módulo. Esta sesión
asume que ya conoces los conceptos de herramientas, skills, subagentes y
mínimo privilegio — aquí los vamos a aplicar, no a repasar desde cero.

## Qué vamos a hacer

1. **Apertura (10 min):** repasamos brevemente la conexión entre este
   módulo y el concepto de "contexto justo a tiempo" del Módulo 1.
2. **Discusión (10 min):** en plenaria, buscamos la forma más simple de
   explicar la diferencia entre una skill y un subagente.
3. **Actividad en equipos (30 min):** en equipos de 2-3, van a clasificar
   5 escenarios como "skill", "subagente" o "ninguno" — es el **Ejercicio
   1** de este módulo (`ejercicios/enunciados/01-skill-subagente-ninguno.md`).
   Tendrán 15 minutos para clasificar y justificar en equipo, y luego
   compartiremos algunas de las clasificaciones más debatidas.
4. **Cierre (15 min):** conectamos con la última sección del módulo —
   permisos y mínimo privilegio — a partir de ejemplos reales del grupo.

## Qué traer

- Tu lectura previa del `README.md` del módulo.
- Una laptop o cuaderno para trabajar el ejercicio en equipo.

## Después de la sesión

Antes de la siguiente sesión grupal (Módulo 3), completa individualmente
los **Ejercicios 2 y 3** de este módulo (`02-contrato-herramienta.md` y
`03-minimo-privilegio.md`) — no se cubren en vivo, pero construyen sobre lo
mismo que trabajamos hoy. Puedes revisar tus respuestas contra las
soluciones de referencia en la carpeta `ejercicios/soluciones/`.
```

- [ ] **Step 3: Verify both files exist and reference the shared exercise**

Run:
```bash
grep -l '01-skill-subagente-ninguno' modulos/02-herramientas-y-skills/sesion-grupal/*.md
```
Expected: both files listed —
```
modulos/02-herramientas-y-skills/sesion-grupal/facilitador.md
modulos/02-herramientas-y-skills/sesion-grupal/participante.md
```

- [ ] **Step 4: Commit**

```bash
git add modulos/02-herramientas-y-skills/sesion-grupal/
git commit -m "$(cat <<'EOF'
Add Módulo 2 group session materials

Facilitator guide (agenda, timing, discussion prompts) and participant
guide for a 75-minute session built around the skill/subagent/neither
classification exercise, opening with a Módulo 1 callback and closing
with a preview of Módulo 5's guardrails content.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 4: Actualizar roadmap del README raíz

**Files:**
- Modify: `README.md:36`

**Interfaces:**
- Consumes: the existence of `modulos/02-herramientas-y-skills/README.md` (Task 1) — the new link target must resolve.
- Produces: nothing consumed elsewhere in this plan (this is the plan's final step)

- [ ] **Step 1: Flip the Módulo 2 roadmap row**

In `README.md`, find this exact line (currently line 36):

```markdown
| 2 | Módulo 2 — Herramientas y Skills | 🚧 Próximamente |
```

Replace it with:

```markdown
| 2 | [Módulo 2 — Herramientas y Skills](modulos/02-herramientas-y-skills/) | ✅ Disponible |
```

Leave every other row in the table unchanged — Task 3 (Proyecto — Asistente de code review) and beyond remain `🚧 Próximamente`, since they are out of scope for this plan.

- [ ] **Step 2: Verify**

Run: `grep -c '02-herramientas-y-skills' README.md`
Expected: `1`

Run: `grep -c '🚧 Próximamente' README.md`
Expected: `6` (one row flipped to ✅, six remain 🚧 — steps 3 through 8)

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "$(cat <<'EOF'
Mark Módulo 2 available in the root README roadmap

Links the roadmap's Módulo 2 row to the now-shipped module and flips
its status from 🚧 to ✅, following the same pattern used for Módulo 1.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

## Follow-up plans (not in this plan's scope)

- Proyecto 01 — Asistente de code review (principiante) — the roadmap checkpoint that follows this module
- Módulo 3 — Memoria y Persistencia
- Módulo 4 — Loops y Orquestación
- Proyecto 02 — Planificador de tareas personal (intermedio)
- Módulo 5 — Evaluación y Guardrails
- Proyecto 03 — Harness de meta-aprendizaje (insignia)

Each should update the root README roadmap table (flip the relevant row from
🚧 to ✅) as its final step, following this plan's Task 4 pattern.
