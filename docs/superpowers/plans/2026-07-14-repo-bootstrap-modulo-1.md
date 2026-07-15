# Repo Bootstrap + Módulo 1 (Fundamentos + Context Engineering) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stand up the root README with the full learning-path roadmap, and ship the first complete, self-contained module (`modulos/01-fundamentos-context-engineering/`) with theory, exercises + solutions, and group-session materials.

**Architecture:** Pure Markdown content repository. No build system, no application code. Each module lives under `modulos/NN-nombre/` and is self-contained (theory + exercises + group session together). Módulos 2-5 and the three example projects under `proyectos/` are out of scope for this plan — they get their own follow-up plans, matching the deferral already stated in the design spec.

**Tech Stack:** Markdown only. Git for version control.

## Global Constraints

- All content in Spanish (per design spec `docs/superpowers/specs/2026-07-14-harness-engineering-repo-design.md`).
- Claude Code is the reference tool for all practical content; no full examples in other tools.
- No automated test suite — verification is manual (read-through + structural grep checks), consistent with the design spec's decision for the example projects and extended here to content modules.
- Module folder structure is fixed: `README.md`, `ejercicios/enunciados/`, `ejercicios/soluciones/`, `sesion-grupal/facilitador.md`, `sesion-grupal/participante.md`.
- Root README roadmap table must list all 8 steps (5 módulos + 3 proyectos) with a status column, even though only Módulo 1 is ✅ in this plan.

---

### Task 1: Root README.md

**Files:**
- Modify: `README.md` (currently just the title + one-line description)

**Interfaces:**
- Consumes: nothing (first task)
- Produces: the roadmap table referenced by nothing else in this plan, but future plans will flip status cells from 🚧 to ✅ as each module/project ships.

- [ ] **Step 1: Replace the root README with the full roadmap content**

Write this exact content to `README.md`, overwriting the current 2-line file:

```markdown
# HER — Harness Engineering Repository

Currículo práctico para aprender **Harness Engineering**: la disciplina de diseñar
el sistema que rodea a un modelo de lenguaje — contexto, herramientas, memoria,
loops de ejecución y guardrails — que en la práctica determina el desempeño de un
agente IA mucho más que el modelo subyacente.

> Inspirado en el video [Cómo Funciona un Arnés de Agentes IA (Harness Engineering
> Explicado)](https://www.youtube.com/watch?v=z3KF8OaLCG4) de Benjamín Cordero, y
> en el trabajo de ingeniería de Anthropic sobre gestión de contexto en agentes.

## ¿Qué vas a aprender?

Al completar este repositorio vas a poder:

1. Reconocer y evaluar las piezas de cualquier harness de agentes IA existente.
2. Dominar las capacidades de Claude Code (skills, subagentes, hooks, memoria)
   como implementación de referencia.
3. Diseñar tu propio harness desde cero para un proyecto propio.

## Prerrequisitos

- [Claude Code](https://claude.com/claude-code) instalado y funcionando.
- Familiaridad básica con la línea de comandos y git.
- No se requiere experiencia previa diseñando agentes IA.

## Ruta de aprendizaje

El currículo combina teoría, ejercicios, sesiones grupales opcionales y proyectos
prácticos. Los módulos se completan en orden; los proyectos son checkpoints que
aplican lo aprendido hasta ese punto.

| Paso | Contenido | Estado |
|---|---|---|
| 1 | [Módulo 1 — Fundamentos + Context Engineering](modulos/01-fundamentos-context-engineering/) | ✅ Disponible |
| 2 | Módulo 2 — Herramientas y Skills | 🚧 Próximamente |
| 3 | Proyecto — Asistente de code review | 🚧 Próximamente |
| 4 | Módulo 3 — Memoria y Persistencia | 🚧 Próximamente |
| 5 | Módulo 4 — Loops y Orquestación | 🚧 Próximamente |
| 6 | Proyecto — Planificador de tareas personal | 🚧 Próximamente |
| 7 | Módulo 5 — Evaluación y Guardrails | 🚧 Próximamente |
| 8 | Proyecto insignia — Harness de meta-aprendizaje | 🚧 Próximamente |

## Cómo usar este repo

**Autoestudio:** sigue la ruta de aprendizaje en orden. Cada módulo tiene su
propio `README.md` con la teoría, seguido de una carpeta `ejercicios/` con
enunciados y, en una carpeta separada, soluciones de referencia para
autoevaluarte sin arruinar el reto.

**Taller grupal:** cada módulo incluye una carpeta `sesion-grupal/` con dos
documentos — `facilitador.md` (agenda, timing, preguntas disparadoras) y
`participante.md` (material para seguir en vivo). Usa el primero si vas a
dirigir la sesión, comparte el segundo con el grupo.

## Estructura del repositorio

```
modulos/      # Teoría + ejercicios + sesión grupal, por tema
proyectos/    # Configuraciones de Claude Code 100% funcionales, de dificultad creciente
docs/         # Documentos de diseño y planes de este mismo repositorio
```
```

- [ ] **Step 2: Verify structure**

Run: `grep -c '^## ' README.md`
Expected: `5` (five level-2 headings: "¿Qué vas a aprender?", "Prerrequisitos",
"Ruta de aprendizaje", "Cómo usar este repo", "Estructura del repositorio")

Run: `grep -c '01-fundamentos-context-engineering' README.md`
Expected: `1` (the roadmap link)

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "$(cat <<'EOF'
Write root README with full learning-path roadmap

Replaces the placeholder README with the curriculum overview,
prerequisites, and an 8-step roadmap table (5 módulos + 3 proyectos)
tracking what's shipped vs. planned.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 2: Módulo 1 — Teoría

**Files:**
- Create: `modulos/01-fundamentos-context-engineering/README.md`

**Interfaces:**
- Consumes: nothing new
- Produces: the five-pillar map (Herramientas/Skills, Memoria, Loops, Evaluación) that Módulo 1's closing section previews — Tasks 3-4 of this plan (exercises, session) reference this same theory content by section name ("¿Qué es un harness?", "Context Engineering", "La ventana de contexto y la compactación").

- [ ] **Step 1: Write the module theory content**

Create `modulos/01-fundamentos-context-engineering/README.md`:

```markdown
# Módulo 1 — Fundamentos + Context Engineering

## ¿Qué es un harness?

Un **agente IA = modelo + harness**. El modelo es el motor de razonamiento
crudo — recibe texto, produce texto. El harness es todo lo que lo rodea y lo
convierte en algo capaz de hacer trabajo real: el system prompt, las
herramientas que puede invocar, la memoria que se le inyecta, el bucle que
decide cuándo volver a llamar al modelo y con qué, y los guardrails que
evitan que se salga de control.

Es la misma relación que hay entre el motor de un auto de carreras y el
chasis, la suspensión y los frenos que lo rodean. Un motor de Fórmula 1
montado en un chasis de kart pierde contra un motor mediocre en un chasis
bien afinado. El modelo importa, pero el harness es lo que determina si esa
capacidad se traduce en resultados.

## Por qué el harness importa más que el modelo

Sam Altman llamó a este año "el año de los agentes IA". Pero el salto real
que estamos viendo en productos de agentes no viene principalmente de
modelos más grandes — viene de mejores harnesses alrededor de modelos que ya
existían. Jensen Huang, en su presentación en el GTC, planteó una idea
similar: el futuro de la IA no está solo en los modelos aislados, sino en
los sistemas que los envuelven.

La evidencia práctica está a la vista: herramientas como Claude Code, Cursor
u otros agentes de código usan modelos subyacentes muy similares (a veces el
mismo modelo, literalmente), y aun así su desempeño en tareas reales puede
ser radicalmente distinto. La diferencia no está en el modelo — está en cómo
cada herramienta gestiona el contexto, qué herramientas expone, cómo
recuerda información entre pasos, y cómo decide su propio siguiente paso.
Ese conjunto de decisiones de diseño es Harness Engineering.

## Context Engineering: la disciplina central

**Contexto** es todo lo que el modelo puede "ver" en el momento de generar
una respuesta: el system prompt, las definiciones de las herramientas
disponibles, el historial de la conversación, cualquier dato inyectado
(archivos de memoria, resultados de búsquedas, contenido de archivos) y el
turno actual del usuario.

La idea central de Context Engineering es que **el contexto no es gratis**.
La atención del modelo es un recurso finito: a medida que la ventana de
contexto se llena de tokens de bajo valor (resultados de herramientas
verbosos, historial irrelevante, instrucciones redundantes), esos tokens
compiten por atención con la información que sí importa. El resultado es lo
que en la práctica se conoce como *context rot*: el modelo pierde el hilo,
ignora instrucciones tempranas, o alucina detalles porque la señal relevante
quedó enterrada entre ruido.

Anthropic ha documentado extensamente, en su trabajo de ingeniería sobre
agentes, que gestionar bien esta ventana de contexto tiene más impacto en el
desempeño real de un agente que casi cualquier otro factor, incluyendo el
tamaño o la capacidad bruta del modelo.

Esto marca una diferencia importante frente al viejo "prompt engineering".
Prompt engineering optimiza un texto estático: un prompt bien pulido que se
reutiliza tal cual. Context Engineering trata el contexto como un
**presupuesto dinámico** que se gestiona activamente a lo largo de toda una
tarea o sesión — decidiendo en cada paso qué información entra, qué se
resume, qué se descarta y qué se recupera justo a tiempo en vez de cargarla
por adelantado.

El principio práctico que se deriva de esto es **contexto mínimo de alta
señal**: incluir solo lo que la tarea actual necesita, y preferir recuperar
información justo cuando se necesita ("just in time") en vez de volcar todo
el conocimiento posible al inicio "por si acaso".

## La ventana de contexto y la compactación

La ventana de contexto es un presupuesto finito compartido entre el system
prompt, las definiciones de herramientas, el historial de la conversación y
el espacio que necesita el modelo para responder. A medida que ese
presupuesto se agota:

- Sube el costo y la latencia de cada llamada al modelo.
- La información relevante corre más riesgo de quedar "enterrada en el
  medio" y ser ignorada.
- Eventualmente se topa con el límite físico de la ventana.

Para manejar esto, un harness bien diseñado usa varias estrategias:

- **Compactación**: condensar turnos antiguos de la conversación en un
  resumen, conservando las decisiones y hechos importantes y descartando el
  detalle que ya no aporta.
- **Poda**: eliminar resultados de herramientas que ya cumplieron su
  propósito y no se van a volver a necesitar.
- **Delegación**: en vez de acumular todo en una sola conversación,
  encargarle una subtarea a un subagente con su propia ventana de contexto
  limpia, y traer de vuelta solo el resultado destilado — no el proceso
  completo que le costó llegar ahí. Este patrón se cubre en profundidad en
  el Módulo 4.

Claude Code es un ejemplo concreto de estos principios en acción: compacta
automáticamente el historial de la conversación a medida que se acerca al
límite de contexto, y su sistema de *skills* — instrucciones que se cargan
solo cuando son relevantes para la tarea actual, en vez de estar siempre
presentes en el system prompt — es en sí mismo una técnica de gestión de
contexto, no solo una forma de organizar funcionalidad.

## Las piezas de un harness (mapa del resto del currículo)

Context Engineering es el principio transversal; los siguientes módulos
cubren las piezas concretas de un harness que lo aplican:

- **Herramientas y Skills** (Módulo 2) — qué puede *hacer* el agente, y
  cuándo esa capacidad debe vivir en una skill vs. en un subagente.
- **Memoria y Persistencia** (Módulo 3) — qué *recuerda* el agente entre
  sesiones, y cómo eso se inyecta como contexto sin saturarlo.
- **Loops y Orquestación** (Módulo 4) — cómo *decide* el agente sus propios
  pasos, incluyendo cuándo delegar trabajo a un subagente con contexto
  limpio.
- **Evaluación y Guardrails** (Módulo 5) — cómo *sabes* si el harness
  funciona, y cómo evitas que se salga de control.

## Para reflexionar / Referencias

- Video: [Cómo Funciona un Arnés de Agentes IA (Harness Engineering
  Explicado)](https://www.youtube.com/watch?v=z3KF8OaLCG4) — Benjamín
  Cordero. Punto de partida de este currículo.
- Los escritos de ingeniería de Anthropic sobre gestión de contexto en
  agentes (referenciados en el video anterior) documentan con más
  profundidad por qué el contexto es, en la práctica, el factor de mayor
  impacto en el desempeño de un agente.
- Comentarios públicos de Sam Altman y Jensen Huang sobre el rol de los
  sistemas ("harnesses") por encima del modelo aislado, también citados en
  el video de origen.
```

- [ ] **Step 2: Verify structure**

Run: `grep -c '^## ' modulos/01-fundamentos-context-engineering/README.md`
Expected: `6`

Run: `wc -w modulos/01-fundamentos-context-engineering/README.md`
Expected: at least `700` (substantive theory content, not a stub)

- [ ] **Step 3: Commit**

```bash
git add modulos/01-fundamentos-context-engineering/README.md
git commit -m "$(cat <<'EOF'
Add Módulo 1 theory: Fundamentos + Context Engineering

Covers what a harness is, why it outweighs the raw model, the core
Context Engineering principle (minimal high-signal context), context
window/compaction mechanics, and previews the four remaining pillars.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 3: Módulo 1 — Ejercicios (enunciados + soluciones)

**Files:**
- Create: `modulos/01-fundamentos-context-engineering/ejercicios/enunciados/01-diagnostico-harness.md`
- Create: `modulos/01-fundamentos-context-engineering/ejercicios/enunciados/02-contexto-minimo.md`
- Create: `modulos/01-fundamentos-context-engineering/ejercicios/enunciados/03-modelo-vs-harness.md`
- Create: `modulos/01-fundamentos-context-engineering/ejercicios/soluciones/01-diagnostico-harness.md`
- Create: `modulos/01-fundamentos-context-engineering/ejercicios/soluciones/02-contexto-minimo.md`
- Create: `modulos/01-fundamentos-context-engineering/ejercicios/soluciones/03-modelo-vs-harness.md`

**Interfaces:**
- Consumes: the theory README from Task 2 (exercises reference "context rot", "contexto mínimo de alta señal", and the model-vs-harness framing defined there)
- Produces: nothing consumed elsewhere in this plan

- [ ] **Step 1: Write exercise 1 statement — diagnóstico de harness**

Create `modulos/01-fundamentos-context-engineering/ejercicios/enunciados/01-diagnostico-harness.md`:

```markdown
# Ejercicio 1: Diagnóstico de harness

## Escenario

Una empresa construyó un bot de soporte interno. Así es como está armado:

- Cada vez que un empleado le escribe, el sistema pega **el wiki completo de
  la empresa** (200 páginas) al inicio del prompt, "por si el modelo lo
  necesita".
- El bot no tiene ninguna herramienta: no puede consultar el sistema de
  tickets, ni el calendario, ni buscar en el wiki de forma selectiva.
- Cada conversación empieza desde cero. Si un empleado vuelve al día
  siguiente con una pregunta relacionada, el bot no tiene ningún recuerdo de
  la conversación anterior.
- No hay ninguna validación sobre lo que el bot responde antes de
  mostrárselo al empleado.

Los empleados reportan que el bot es lento, a veces "se le olvida" lo que
preguntaron dos mensajes atrás en la misma conversación, y ocasionalmente
inventa políticas de la empresa que no existen.

## Tu tarea

1. Identifica qué piezas de un harness están presentes en este sistema y
   cuáles faltan por completo (usa las categorías del Módulo 1: contexto,
   herramientas, memoria, loop, guardrails).
2. Para cada síntoma reportado (lentitud, "olvido" dentro de la misma
   conversación, invención de políticas), explica cuál pieza faltante o mal
   diseñada del harness es la causa más probable. Conecta tu respuesta con
   el concepto de *context rot* visto en el módulo.
3. Propón, en un párrafo, el cambio de mayor impacto que harías primero y
   por qué.
```

- [ ] **Step 2: Write exercise 2 statement — contexto mínimo**

Create `modulos/01-fundamentos-context-engineering/ejercicios/enunciados/02-contexto-minimo.md`:

```markdown
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
```

- [ ] **Step 3: Write exercise 3 statement — modelo vs. harness**

Create `modulos/01-fundamentos-context-engineering/ejercicios/enunciados/03-modelo-vs-harness.md`:

```markdown
# Ejercicio 3: Modelo vs. harness en tu propia experiencia

## Tu tarea

Piensa en dos herramientas de IA que hayas usado tú mismo (pueden ser dos
asistentes de código, dos chatbots, o un antes/después de la misma
herramienta tras una actualización).

1. Describe brevemente una diferencia notable en el comportamiento o la
   calidad de resultados entre ambas.
2. Clasifica esa diferencia: ¿es más probable que se deba al modelo
   subyacente (capacidad bruta de razonamiento) o al harness que lo rodea
   (qué contexto le dan, qué herramientas tiene, cómo gestiona memoria,
   cómo estructura su propio loop de trabajo)? No hace falta que sepas la
   respuesta con certeza técnica — el objetivo es practicar el marco mental,
   no acertar.
3. Si tu conclusión es "harness", identifica a cuál de las cuatro piezas
   (herramientas/skills, memoria, loops, guardrails) del mapa del módulo
   atribuirías la diferencia, y por qué.
```

- [ ] **Step 4: Write solution 1**

Create `modulos/01-fundamentos-context-engineering/ejercicios/soluciones/01-diagnostico-harness.md`:

```markdown
# Solución — Ejercicio 1: Diagnóstico de harness

Esta es una solución de referencia. Tu razonamiento puede variar en los
detalles siempre que identifiques correctamente las piezas y conecte los
síntomas con sus causas.

## Piezas presentes vs. ausentes

- **Contexto**: presente, pero mal diseñado — es un volcado masivo y
  estático (todo el wiki, siempre), no un contexto curado para la pregunta
  actual.
- **Herramientas**: ausentes. El bot no puede consultar nada de forma
  selectiva; depende 100% de lo que venga pegado en el prompt.
- **Memoria**: ausente. Cada conversación arranca desde cero, sin
  persistencia entre sesiones.
- **Loop**: inexistente — es una sola llamada de ida y vuelta, no hay
  ningún ciclo de "pensar, actuar, verificar".
- **Guardrails**: ausentes. No hay validación de las respuestas antes de
  mostrarlas.

## Síntomas y sus causas

- **Lentitud**: causada directamente por pegar 200 páginas de wiki en cada
  prompt. Más tokens de contexto significan más tiempo de procesamiento en
  cada llamada, independientemente de si esas 200 páginas son relevantes
  para la pregunta.
- **"Olvido" dentro de la misma conversación**: es el síntoma clásico de
  *context rot*. Con tanto contenido de bajo valor (wiki completo) compitiendo
  por atención, la información que el empleado mencionó dos mensajes atrás
  queda "enterrada" entre ruido y el modelo pierde el hilo, aunque
  técnicamente esa información sigue en la ventana de contexto.
- **Invención de políticas**: combinación de falta de herramientas (no
  puede verificar una política específica contra una fuente autoritativa,
  solo "recordarla" de un volcado masivo de texto) y falta de guardrails
  (nada valida la respuesta antes de enviarla).

## Cambio de mayor impacto

El cambio de mayor impacto sería reemplazar el volcado estático del wiki
completo por una herramienta de búsqueda que traiga solo las secciones
relevantes a la pregunta actual ("justo a tiempo" en vez de "por si acaso").
Esto ataca directamente la causa raíz de los tres síntomas: reduce el
contexto irrelevante (arregla lentitud y "olvido"), y le da al bot una
forma de anclar sus respuestas a una fuente verificable en vez de inventar
(reduce alucinaciones), incluso antes de tocar memoria o guardrails.
```

- [ ] **Step 5: Write solution 2**

Create `modulos/01-fundamentos-context-engineering/ejercicios/soluciones/02-contexto-minimo.md`:

```markdown
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
```

- [ ] **Step 6: Write solution 3**

Create `modulos/01-fundamentos-context-engineering/ejercicios/soluciones/03-modelo-vs-harness.md`:

```markdown
# Solución — Ejercicio 3: Modelo vs. harness en tu propia experiencia

Este ejercicio no tiene una respuesta única correcta — es personal y
depende de la experiencia de cada quien. En vez de una solución, aquí tienes
los criterios que debería cumplir una buena respuesta:

## Cómo evaluar tu propia respuesta

- **Evidencia de que fue el harness, no el modelo**: si la diferencia
  aparece en *cómo* la herramienta usa la información (recuerda contexto de
  antes, usa herramientas para verificar en vez de inventar, se mantiene en
  la tarea sin desviarse, evita acciones peligrosas sin confirmación) más
  que en la calidad del razonamiento puro sobre un problema aislado, es una
  señal fuerte de harness.
- **Evidencia de que fue el modelo**: si la diferencia aparece incluso en
  tareas de razonamiento aislado, sin herramientas ni contexto adicional de
  por medio (por ejemplo, resolver un problema lógico autocontenido en un
  solo turno), es más atribuible al modelo subyacente.
- **Mapeo a las cuatro piezas**: una buena respuesta conecta explícitamente
  la observación con una pieza concreta del mapa del módulo, no solo dice
  "harness" en general. Ejemplos típicos:
  - "Recuerda lo que le dije la semana pasada" → Memoria y Persistencia.
  - "Puede ejecutar código o buscar en internet para verificar en vez de
    inventar" → Herramientas y Skills.
  - "No se pierde en tareas largas de varios pasos" → Loops y Orquestación.
  - "Rechaza o confirma antes de hacer algo irreversible" → Evaluación y
    Guardrails.

Si tu respuesta cumple estos tres puntos, vas bien encaminado — el objetivo
de este ejercicio es practicar el marco mental de separar modelo de harness
en el mundo real, no llegar a una conclusión técnica verificable.
```

- [ ] **Step 7: Verify enunciados/soluciones pairing**

Run:
```bash
diff <(ls modulos/01-fundamentos-context-engineering/ejercicios/enunciados/) \
     <(ls modulos/01-fundamentos-context-engineering/ejercicios/soluciones/)
```
Expected: no output (empty diff — every enunciado has a matching solución filename)

- [ ] **Step 8: Commit**

```bash
git add modulos/01-fundamentos-context-engineering/ejercicios/
git commit -m "$(cat <<'EOF'
Add Módulo 1 exercises with reference solutions

Three exercises covering harness diagnosis, minimal-context design,
and model-vs-harness attribution, each with a matching solution in a
separate folder for self-assessment.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 4: Módulo 1 — Sesión grupal

**Files:**
- Create: `modulos/01-fundamentos-context-engineering/sesion-grupal/facilitador.md`
- Create: `modulos/01-fundamentos-context-engineering/sesion-grupal/participante.md`

**Interfaces:**
- Consumes: the theory README from Task 2 and Exercise 1 from Task 3 (the group session reuses the "diagnóstico de harness" exercise as its live group activity)
- Produces: nothing consumed elsewhere in this plan

- [ ] **Step 1: Write the facilitator guide**

Create `modulos/01-fundamentos-context-engineering/sesion-grupal/facilitador.md`:

```markdown
# Sesión grupal — Módulo 1: Facilitador

**Duración total:** ~75 minutos
**Tamaño de grupo recomendado:** 4-12 personas
**Requisito previo:** los participantes deben haber leído el `README.md` del
módulo antes de la sesión — esta sesión no reemplaza la teoría, la aplica.

## Agenda

### 1. Apertura y pulso del grupo (10 min)

Pregunta disparadora para abrir, en plenaria:

> "Sin mirar el módulo — en una frase, ¿qué es un harness?"

No corrijas todavía. El objetivo es exponer las intuiciones y confusiones
iniciales del grupo antes de reforzar el concepto. Frases comunes que
suelen aparecer y cómo reconducirlas:

- "Es el prompt" → reconducir hacia: el prompt es una pieza, pero el
  harness incluye herramientas, memoria y el loop de ejecución también.
- "Es el modelo con instrucciones" → reconducir hacia la distinción
  modelo/harness del módulo: el harness es todo lo que *rodea* al modelo,
  no el modelo con texto extra pegado.

### 2. Refuerzo del concepto central (10 min)

Guía una discusión corta sobre por qué el harness importa más que el
modelo, usando la analogía del motor de carreras del módulo. Pregunta:

> "¿Alguien ha usado dos herramientas de IA distintas que probablemente
> usan el mismo modelo por debajo, pero se sienten muy distintas de usar?
> ¿Qué se sentía diferente?"

Deja que 2-3 personas compartan ejemplos concretos antes de continuar. Esto
sirve como calentamiento directo para el Ejercicio 3 del módulo.

### 3. Actividad grupal: diagnóstico de harness (30 min)

Divide al grupo en equipos de 2-3 personas. Cada equipo trabaja el
**Ejercicio 1 (Diagnóstico de harness)** del módulo — está en
`ejercicios/enunciados/01-diagnostico-harness.md`.

Timing sugerido dentro de este bloque:
- 15 min: cada equipo diagnostica el escenario y prepara su respuesta.
- 15 min: cada equipo comparte en 2 minutos su diagnóstico y la solución
  propuesta. Como facilitador, anota en una pizarra/documento compartido las
  piezas del harness (contexto, herramientas, memoria, loop, guardrails)
  que cada equipo identificó, para visualizar al final si hubo consenso o
  divergencia.

Nota para el facilitador: la solución de referencia está en
`ejercicios/soluciones/01-diagnostico-harness.md`. No la compartas antes de
que los equipos presenten — úsala para guiar la discusión de cierre, no
como respuesta "correcta" que se impone sobre el análisis del grupo.

### 4. Cierre: mapa del resto del currículo (15 min)

Cierra conectando el ejercicio con el mapa de los próximos módulos:

> "En el diagnóstico que acaban de hacer, identificaron piezas faltantes
> como herramientas, memoria o guardrails. Cada una de esas piezas es
> exactamente uno de los próximos módulos del currículo."

Recorre brevemente los cuatro módulos restantes (Herramientas y Skills,
Memoria y Persistencia, Loops y Orquestación, Evaluación y Guardrails) y
cómo cada uno conecta con algo que el grupo ya mencionó en su diagnóstico.

### 5. Tarea antes de la siguiente sesión (5 min)

Pide que completen los Ejercicios 2 y 3 individualmente antes de la
siguiente sesión grupal (Módulo 2), ya que no se cubren en vivo.

## Notas generales de facilitación

- Si el grupo tiene experiencia previa muy dispareja (algunos ya usan
  Claude Code a diario, otros nunca lo han abierto), arma los equipos del
  paso 3 mezclando niveles, no agrupando por experiencia — el ejercicio de
  diagnóstico no requiere experiencia técnica previa, solo el marco mental
  del módulo.
- Si el tiempo se acorta, el bloque que más se puede recortar sin perder el
  objetivo de la sesión es el paso 2 (a 5 min) — el paso 3 es el corazón de
  la sesión y no debería recortarse.
```

- [ ] **Step 2: Write the participant guide**

Create `modulos/01-fundamentos-context-engineering/sesion-grupal/participante.md`:

```markdown
# Sesión grupal — Módulo 1: Participante

**Antes de esta sesión:** lee el `README.md` de este módulo. Esta sesión
asume que ya conoces los conceptos de harness, context engineering y
context rot — aquí los vamos a aplicar, no a repasar desde cero.

## Qué vamos a hacer

1. **Apertura (10 min):** compartimos en grupo nuestras intuiciones sobre
   qué es un harness, antes de aplicar el concepto formalmente.
2. **Discusión (10 min):** comparamos experiencias con distintas
   herramientas de IA y qué tanto de la diferencia se sintió como "modelo"
   vs. "harness".
3. **Actividad en equipos (30 min):** en equipos de 2-3, van a resolver el
   **Ejercicio 1 (Diagnóstico de harness)** de este módulo — está en
   `ejercicios/enunciados/01-diagnostico-harness.md`. Tendrán 15 minutos
   para diagnosticar el escenario en equipo, y cada equipo presentará su
   diagnóstico en 2 minutos.
4. **Cierre (15 min):** conectamos lo que encontraron en el ejercicio con
   el mapa de los próximos módulos del currículo.

## Qué traer

- Tu lectura previa del `README.md` del módulo.
- Una laptop o cuaderno para trabajar el ejercicio en equipo.

## Después de la sesión

Antes de la siguiente sesión grupal (Módulo 2), completa individualmente
los **Ejercicios 2 y 3** de este módulo (`02-contexto-minimo.md` y
`03-modelo-vs-harness.md`) — no se cubren en vivo, pero construyen sobre lo
mismo que trabajamos hoy. Puedes revisar tus respuestas contra las
soluciones de referencia en la carpeta `ejercicios/soluciones/`.
```

- [ ] **Step 3: Verify both files exist and reference the shared exercise**

Run:
```bash
grep -l '01-diagnostico-harness' modulos/01-fundamentos-context-engineering/sesion-grupal/*.md
```
Expected: both files listed —
```
modulos/01-fundamentos-context-engineering/sesion-grupal/facilitador.md
modulos/01-fundamentos-context-engineering/sesion-grupal/participante.md
```

- [ ] **Step 4: Commit**

```bash
git add modulos/01-fundamentos-context-engineering/sesion-grupal/
git commit -m "$(cat <<'EOF'
Add Módulo 1 group session materials

Facilitator guide (agenda, timing, discussion prompts) and participant
guide for a 75-minute session built around the diagnóstico-harness
exercise, closing with a preview of the remaining four módulos.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

## Follow-up plans (not in this plan's scope)

- Módulo 2 — Herramientas y Skills
- Módulo 3 — Memoria y Persistencia
- Módulo 4 — Loops y Orquestación
- Módulo 5 — Evaluación y Guardrails
- Proyecto 01 — Asistente de code review (principiante)
- Proyecto 02 — Planificador de tareas personal (intermedio)
- Proyecto 03 — Harness de meta-aprendizaje (insignia)

Each should update the root README roadmap table (flip the relevant row from
🚧 to ✅) as its final step.
