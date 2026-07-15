# Módulo 4 (Loops y Orquestación) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship the fourth complete, self-contained module (`modulos/04-loops-y-orquestacion/`) with theory, exercises + solutions, and group-session materials, then flip the root README roadmap row for Módulo 4 from 🚧 to ✅.

**Architecture:** Pure Markdown content repository. No build system, no application code. This module follows the exact same internal structure as Módulos 1-3 (`README.md`, `ejercicios/enunciados/`, `ejercicios/soluciones/`, `sesion-grupal/facilitador.md`, `sesion-grupal/participante.md`) and explicitly fulfills a promise Módulo 1 made ("Este patrón se cubre en profundidad en el Módulo 4" regarding delegación), while building on Módulo 2's skill-vs-subagente decision framework rather than treating orchestration as an unrelated topic. Proyecto 02, Módulo 5, and the meta-aprendizaje project are out of scope for this plan.

**Tech Stack:** Markdown only. Git for version control.

## Global Constraints

- All content in Spanish (per design spec `docs/superpowers/specs/2026-07-14-harness-engineering-repo-design.md`).
- Claude Code is the reference tool for all practical content; other tools get at most a brief comparative note, never a full example.
- No automated test suite — verification is manual (read-through + structural grep checks), matching Módulos 1-3's precedent.
- Module folder structure is fixed: `README.md`, `ejercicios/enunciados/`, `ejercicios/soluciones/`, `sesion-grupal/facilitador.md`, `sesion-grupal/participante.md`.
- Content must explicitly connect back to already-shipped terminology by name: *context rot*, compactación/poda, and the "delegación" promise (Módulo 1); the skill-vs-subagente decision framework (Módulo 2) — not silently reinvented.
- The root README roadmap table (`README.md:39`) must have its Módulo 4 row flipped from `🚧 Próximamente` to `✅ Disponible` with a working relative link, as the final step of this plan — same pattern already used for Módulos 1-3 and Proyecto 01.

---

### Task 1: Módulo 4 — Teoría

**Files:**
- Create: `modulos/04-loops-y-orquestacion/README.md`

**Interfaces:**
- Consumes: `modulos/01-fundamentos-context-engineering/README.md` and `modulos/02-herramientas-y-skills/README.md` (already shipped) — this task's content must reference *context rot*, compactación/poda, and delegación (Módulo 1), and the skill-vs-subagente decision framework (Módulo 2) by name, not redefine them.
- Produces: the "marco práctico" for delegating within a loop, and the independence criterion for parallelism, that Tasks 2-3 of this plan reference by name.

- [ ] **Step 1: Write the module theory content**

Create `modulos/04-loops-y-orquestacion/README.md`:

```markdown
# Módulo 4 — Loops y Orquestación

## ¿Qué es un loop de agente?

Todo lo que hemos visto hasta ahora — contexto, herramientas, skills,
memoria — son piezas que un harness pone a disposición del modelo. El
**loop de agente** es el mecanismo que las conecta en el tiempo: observar
el estado actual (incluyendo el resultado del paso anterior), decidir la
siguiente acción, ejecutarla (normalmente invocando una herramienta),
observar su resultado, y repetir hasta que la tarea esté completa o el
agente decida detenerse.

Esta es la diferencia entre un modelo que responde una vez y un agente que
trabaja: un solo llamado al modelo produce una respuesta; un loop permite
que esa respuesta incluya la decisión de investigar más, corregir un error
que acaba de descubrir, o dividir el trabajo en pasos — y que cada uno de
esos pasos informe al siguiente.

## El loop crece: por qué cada paso es más contexto

Cada vuelta del loop añade algo al contexto: el resultado de la
herramienta que se acaba de invocar, la nueva información descubierta, la
decisión que se acaba de tomar. Esto significa que un loop largo, por
diseño, acumula contexto a medida que avanza — exactamente el escenario
que el Módulo 1 anticipó al hablar de compactación y poda: mientras más
pasos toma un agente en una sola conversación, más presión hay sobre el
presupuesto de contexto, y más importa descartar lo que ya cumplió su
propósito.

Un loop mal diseñado — uno que nunca poda resultados intermedios que ya no
aportan, o que reintenta lo mismo sin aprender del intento anterior — no
solo es lento: es exactamente el mecanismo de *context rot* del Módulo 1,
ahora producido por el propio agente en tiempo real, paso a paso, en vez
de por un volcado inicial de información.

## Delegar a un subagente: la promesa del Módulo 1, cumplida

El Módulo 1 mencionó la delegación como una estrategia para manejar el
presupuesto de contexto, y prometió cubrirla en profundidad aquí. La idea
central: en vez de que todos los pasos de una tarea ocurran dentro del
mismo loop y la misma ventana de contexto, el agente puede despachar una
subtarea a un **subagente** — que corre su propio loop, con su propia
ventana de contexto limpia — y esperar solo el resultado final.

Esto cambia la aritmética del contexto de forma importante. Si una
subtarea necesita 20 pasos de exploración para llegar a una respuesta,
esos 20 pasos — y todo el contexto que acumulan — viven en la ventana del
subagente, no en la del agente principal. El loop principal solo ve una
llamada (despachar la subtarea) y un resultado (lo que el subagente
devolvió), sin importar cuántas vueltas de loop le tomó al subagente
llegar ahí. El Módulo 2 ya había establecido cuándo conviene un subagente
frente a una skill; este módulo añade el mecanismo concreto: un subagente
es, en esencia, un loop de agente completo corriendo dentro de otro, con
el único punto de contacto siendo la tarea que se le encarga y el
resultado que devuelve.

## Subagentes en paralelo: cuándo tiene sentido

Cuando varias subtareas son verdaderamente independientes entre sí —
ninguna depende del resultado de otra, ninguna modifica el mismo estado
compartido — un agente puede despachar varios subagentes a la vez en vez
de uno por uno. Esto reduce el tiempo total de la tarea, porque los loops
de los subagentes corren en paralelo en vez de esperar su turno.

Pero la independencia real es una condición estricta, no una suposición
cómoda. Dos subagentes que editan el mismo archivo, o que dependen de que
uno termine antes de que el otro pueda empezar con información correcta,
no son candidatos para paralelismo — coordinarlos mal genera conflictos
que son más caros de resolver que el tiempo que el paralelismo pretendía
ahorrar. La pregunta antes de paralelizar no es "¿esto sería más rápido en
paralelo?" sino "¿estos subagentes pueden trabajar sin pisarse el uno al
otro en absoluto?".

## Cuándo delegar dentro de un loop: marco práctico

El Módulo 2 ya estableció cuándo usar una skill frente a un subagente en
general. Dentro de un loop de agente en marcha, esa misma pregunta se
vuelve más concreta: en cada paso, ¿este trabajo específico debería seguir
ocurriendo en el loop principal, o debería salir de él?

Son buenos candidatos para delegar a un subagente dentro de un loop:
- Un paso que requiere mucha exploración cuyo detalle no es relevante
  después de obtenido el resultado (por ejemplo, buscar en un repositorio
  grande).
- Una revisión del trabajo que el propio loop principal acaba de producir,
  hecha por un subagente sin el sesgo de haberlo escrito — una segunda
  mirada con contexto limpio.
- Fragmentos de trabajo genuinamente independientes que se benefician de
  correr en paralelo, como se describió arriba.

Son malos candidatos: pasos simples que dependen directamente del
contexto inmediato que el loop principal ya tiene — delegarlos solo añade
el costo de coordinar un subagente sin ahorrar nada de contexto ni de
tiempo.

## Para reflexionar / Referencias

- La documentación oficial de Claude Code sobre subagentes y orquestación
  de tareas es la referencia más actualizada para los detalles de
  implementación de despacho paralelo.
- Este módulo cumple la promesa del Módulo 1 de cubrir la delegación en
  profundidad, y construye directamente sobre el marco de decisión
  skill-vs-subagente del Módulo 2.
```

- [ ] **Step 2: Verify structure**

Run: `grep -c '^## ' modulos/04-loops-y-orquestacion/README.md`
Expected: `6`

Run: `wc -w modulos/04-loops-y-orquestacion/README.md`
Expected: at least `700`

Run: `grep -c 'Módulo 1' modulos/04-loops-y-orquestacion/README.md`
Expected: at least `1`

Run: `grep -c 'Módulo 2' modulos/04-loops-y-orquestacion/README.md`
Expected: at least `1`

- [ ] **Step 3: Commit**

```bash
git add modulos/04-loops-y-orquestacion/README.md
git commit -m "$(cat <<'EOF'
Add Módulo 4 theory: Loops y Orquestación

Covers the observe-decide-act-observe agent loop, why each step adds
context (fulfilling Módulo 1's delegación promise), the subagent
mechanism for isolating context, the strict independence criterion
for parallel dispatch, and a practical framework for when to delegate
within a running loop, building on Módulo 2's decision framework.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 2: Módulo 4 — Ejercicios (enunciados + soluciones)

**Files:**
- Create: `modulos/04-loops-y-orquestacion/ejercicios/enunciados/01-loop-o-subagente.md`
- Create: `modulos/04-loops-y-orquestacion/ejercicios/enunciados/02-diagnostico-loop.md`
- Create: `modulos/04-loops-y-orquestacion/ejercicios/enunciados/03-disena-el-loop.md`
- Create: `modulos/04-loops-y-orquestacion/ejercicios/soluciones/01-loop-o-subagente.md`
- Create: `modulos/04-loops-y-orquestacion/ejercicios/soluciones/02-diagnostico-loop.md`
- Create: `modulos/04-loops-y-orquestacion/ejercicios/soluciones/03-disena-el-loop.md`

**Interfaces:**
- Consumes: the theory README from Task 1 (exercises reference the loop-vs-subagente-vs-paralelo framework and the independence criterion)
- Produces: `01-loop-o-subagente` is the exercise Task 3 (group session) reuses as its live group activity — its filename must match exactly.

- [ ] **Step 1: Write exercise 1 statement — loop principal, subagente o paralelo**

Create `modulos/04-loops-y-orquestacion/ejercicios/enunciados/01-loop-o-subagente.md`:

```markdown
# Ejercicio 1: Loop principal, subagente o paralelo

## Tu tarea

Para cada situación, decide si el trabajo descrito debería ocurrir **(a)**
en el loop principal, **(b)** delegado a un solo subagente, o **(c)**
delegado a varios subagentes en paralelo. Justifica cada respuesta en 1-2
frases usando el marco práctico del módulo.

1. Un agente necesita corregir un typo en un archivo que ya tiene abierto
   y cuya ubicación exacta ya conoce.
2. Un agente necesita investigar, en un monorepo de 500 archivos, en qué
   módulo vive una función específica antes de poder modificarla.
3. Un agente acaba de terminar de escribir una función y quiere una
   revisión de calidad antes de continuar.
4. Un agente necesita actualizar 3 archivos de configuración completamente
   independientes entre sí (ninguno depende del contenido de los otros)
   en un proyecto grande.
5. Un agente necesita leer el resultado de la herramienta que acaba de
   invocar dos líneas atrás para decidir su siguiente paso.
```

- [ ] **Step 2: Write exercise 2 statement — diagnóstico de un loop que no poda**

Create `modulos/04-loops-y-orquestacion/ejercicios/enunciados/02-diagnostico-loop.md`:

```markdown
# Ejercicio 2: Diagnostica un loop que no poda

## Escenario

Un agente está resolviendo un bug complejo. En su intento de
diagnosticarlo, ejecuta la suite de pruebas completa 15 veces (cada vez
con salida de cientos de líneas), lee 40 archivos distintos buscando la
causa, y prueba 6 hipótesis distintas antes de encontrar la correcta —
pero nunca descarta la salida de los intentos anteriores ni de las
hipótesis descartadas; todo permanece en el contexto de la misma
conversación. Para cuando encuentra el bug real, el agente empieza a
"olvidar" instrucciones que el usuario dio al principio de la tarea, y
tarda notablemente más en cada paso nuevo.

## Tu tarea

1. Identifica qué principio de este módulo (y del Módulo 1) explica los
   síntomas descritos.
2. Propón al menos dos cambios concretos al diseño del loop de este
   agente para evitar que esto vuelva a pasar — uno relacionado con
   poda/compactación dentro del mismo loop, y otro relacionado con
   delegación a subagentes.
3. Explica por qué correr las 6 hipótesis como 6 subagentes en paralelo
   NO sería una buena idea en este caso.
```

- [ ] **Step 3: Write exercise 3 statement — diseña el loop de una tarea**

Create `modulos/04-loops-y-orquestacion/ejercicios/enunciados/03-disena-el-loop.md`:

```markdown
# Ejercicio 3: Diseña el loop de una tarea

## Escenario

Un agente recibe la tarea: "Actualiza la versión de una dependencia en 8
microservicios distintos del monorepo, corriendo las pruebas de cada uno
después de actualizar, y repórtame cuáles fallaron."

## Tu tarea

1. Describe cómo estructurarías esta tarea: ¿qué pasos ocurren en el loop
   principal, y qué pasos delegarías a subagentes? Justifica con el marco
   práctico del módulo.
2. ¿Deberían los 8 microservicios procesarse en paralelo o en secuencia?
   Justifica tu respuesta con el criterio de independencia real visto en
   el módulo.
3. ¿Qué información necesita el loop principal recibir de vuelta de cada
   subagente para poder generar el reporte final, y qué NO necesita
   recibir?
```

- [ ] **Step 4: Write solution 1**

Create `modulos/04-loops-y-orquestacion/ejercicios/soluciones/01-loop-o-subagente.md`:

```markdown
# Solución — Ejercicio 1: Loop principal, subagente o paralelo

Esta es una solución de referencia. Tu razonamiento puede variar en los
detalles siempre que aplique correctamente el marco práctico del módulo.

1. **→ Loop principal.** Es un paso simple, con ubicación ya conocida, sin
   necesidad de exploración — delegarlo solo añadiría coordinación sin
   ahorrar nada.
2. **→ Delegar a subagente.** Requiere mucha exploración (500 archivos)
   cuyo detalle intermedio no es relevante después de encontrar la
   respuesta — candidato clásico de delegación según el módulo.
3. **→ Delegar a subagente.** Es una revisión del trabajo que el propio
   loop acaba de producir, hecha idealmente sin el sesgo de haberlo
   escrito — exactamente el segundo caso descrito en el marco práctico.
4. **→ Delegar en paralelo.** Son tareas genuinamente independientes
   (ningún archivo depende del contenido de los otros) — cumple el
   criterio estricto de independencia para paralelizar.
5. **→ Loop principal.** Depende directamente del contexto inmediato que
   el loop ya tiene (el resultado de dos líneas atrás) — delegarlo
   rompería esa dependencia sin necesidad.
```

- [ ] **Step 5: Write solution 2**

Create `modulos/04-loops-y-orquestacion/ejercicios/soluciones/02-diagnostico-loop.md`:

```markdown
# Solución — Ejercicio 2: Diagnostica un loop que no poda

Esta es una solución de referencia. Tu razonamiento puede variar en los
detalles siempre que identifique correctamente el mecanismo de context rot
aplicado a un loop.

## Principio que explica los síntomas

Es el mismo mecanismo de *context rot* del Módulo 1, ahora producido por
el propio loop en tiempo real: cada intento, cada hipótesis descartada, y
cada corrida completa de pruebas se acumula sin podarse, hasta que la
señal real (las instrucciones originales del usuario) queda enterrada
entre ruido de bajo valor. El módulo lo describe explícitamente: un loop
mal diseñado que nunca poda resultados intermedios recrea context rot paso
a paso.

## Cambios concretos propuestos

- **Poda/compactación dentro del mismo loop:** una vez que una hipótesis
  se descarta, condensar ese intento a una sola línea de resumen
  ("hipótesis X descartada porque Y") en vez de conservar la salida
  completa de la prueba; lo mismo para las 15 corridas de pruebas — solo
  la última corrida relevante, o un resumen de qué cambió entre corridas,
  necesita quedarse completo.
- **Delegación a subagentes:** cada hipótesis podría investigarse en un
  subagente separado con su propia ventana de contexto, devolviendo solo
  un veredicto corto (confirmada/descartada + por qué) al loop principal,
  en vez de que toda la exploración de cada hipótesis viva en la
  conversación principal.

## Por qué el paralelismo no sería buena idea aquí

Las 6 hipótesis probablemente no son independientes entre sí en el
sentido estricto del módulo: descartar una hipótesis casi siempre informa
cuál probar después (el agente aprende algo de cada intento que ajusta su
siguiente paso). Correrlas en paralelo desde el inicio significaría perder
esa información — algunos subagentes probarían hipótesis que ya se
habrían descartado si hubieran sabido lo que otro subagente encontró
primero.
```

- [ ] **Step 6: Write solution 3**

Create `modulos/04-loops-y-orquestacion/ejercicios/soluciones/03-disena-el-loop.md`:

```markdown
# Solución — Ejercicio 3: Diseña el loop de una tarea

Esta es una solución de referencia; el objetivo es el razonamiento sobre
qué delegar y cuándo paralelizar, no una arquitectura exacta.

## Qué va en el loop principal vs. subagentes

Loop principal: coordinar la lista de los 8 microservicios, despachar el
trabajo, y ensamblar el reporte final. Delegado a subagentes: el trabajo
de cada microservicio individual (actualizar la dependencia, correr sus
pruebas) — es un paso de exploración/ejecución cuyo detalle intermedio
(logs completos de la corrida de pruebas) no necesita vivir en el loop
principal, solo el resultado.

## Paralelo o secuencial

En paralelo, si los 8 microservicios son realmente independientes entre sí
(no comparten código, no hay dependencias de build entre ellos) — que es
la premisa típica de microservicios bien separados. Si compartieran
alguna dependencia interna entre sí, habría que verificar esa
independencia antes de asumir que el paralelismo es seguro.

## Qué información debe volver al loop principal

Necesita: el nombre del microservicio, si la actualización se aplicó con
éxito, y si las pruebas pasaron o fallaron (y de fallar, un resumen corto
del fallo). NO necesita: la salida completa de cada corrida de pruebas, ni
los pasos intermedios que cada subagente tomó para hacer la actualización
— eso es exactamente el tipo de detalle que debería quedarse en la
ventana de contexto del subagente, no propagarse al loop principal.
```

- [ ] **Step 7: Verify enunciados/soluciones pairing**

Run:
```bash
diff <(ls modulos/04-loops-y-orquestacion/ejercicios/enunciados/) \
     <(ls modulos/04-loops-y-orquestacion/ejercicios/soluciones/)
```
Expected: no output (empty diff — every enunciado has a matching solución filename)

- [ ] **Step 8: Commit**

```bash
git add modulos/04-loops-y-orquestacion/ejercicios/
git commit -m "$(cat <<'EOF'
Add Módulo 4 exercises with reference solutions

Three exercises covering loop/subagent/parallel classification,
diagnosing an unpruned loop through the context rot lens, and
designing the orchestration of a multi-microservice task — each with
a matching solution in a separate folder for self-assessment.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 3: Módulo 4 — Sesión grupal

**Files:**
- Create: `modulos/04-loops-y-orquestacion/sesion-grupal/facilitador.md`
- Create: `modulos/04-loops-y-orquestacion/sesion-grupal/participante.md`

**Interfaces:**
- Consumes: the theory README from Task 1 and Exercise 1 (`01-loop-o-subagente`) from Task 2 — the group session reuses that exact exercise as its live group activity.
- Produces: nothing consumed elsewhere in this plan

- [ ] **Step 1: Write the facilitator guide**

Create `modulos/04-loops-y-orquestacion/sesion-grupal/facilitador.md`:

```markdown
# Sesión grupal — Módulo 4: Facilitador

**Duración total:** ~75 minutos
**Tamaño de grupo recomendado:** 4-12 personas
**Requisito previo:** los participantes deben haber leído el `README.md`
de este módulo antes de la sesión.

## Agenda

### 1. Apertura: el loop como el motor del harness (10 min)

Pregunta disparadora para abrir, en plenaria:

> "En una frase, ¿qué hace que un agente sea distinto de una sola
> respuesta de un modelo de lenguaje?"

Conecta las respuestas con la idea del loop: observar, decidir, actuar,
observar el resultado, repetir.

### 2. Refuerzo del concepto central (10 min)

Discusión guiada sobre por qué cada paso de un loop añade contexto,
usando la pregunta:

> "Si un agente lleva 20 pasos trabajando en la misma tarea, ¿qué le
> pasaría a su contexto si nunca podara nada?"

Refuerza la conexión con *context rot* del Módulo 1, ahora producido por
el propio loop.

### 3. Actividad grupal: loop principal, subagente o paralelo (30 min)

Divide al grupo en equipos de 2-3 personas. Cada equipo trabaja el
**Ejercicio 1 (Loop principal, subagente o paralelo)** del módulo — está
en `ejercicios/enunciados/01-loop-o-subagente.md`.

Timing sugerido dentro de este bloque:
- 15 min: cada equipo clasifica los 5 escenarios y prepara su
  justificación.
- 15 min: cada equipo comparte 1-2 de sus clasificaciones más discutidas.
  Presta especial atención al escenario 3 (revisión del propio trabajo) y
  al escenario 4 (paralelismo) — suelen generar el debate más rico sobre
  independencia real.

Nota para el facilitador: la solución de referencia está en
`ejercicios/soluciones/01-loop-o-subagente.md`. No la compartas antes de
que los equipos presenten — úsala para guiar el cierre de la discusión,
no como veredicto impuesto sobre el razonamiento del grupo.

### 4. Cierre: los riesgos del paralelismo mal aplicado (15 min)

Cierra conectando con la sección de paralelismo del módulo. Pregunta al
grupo si alguna vez han visto (en cualquier contexto, no solo agentes IA)
un intento de paralelizar trabajo que en realidad no era independiente, y
qué salió mal. Usa esas anécdotas para reforzar el criterio estricto de
independencia antes de paralelizar.

### 5. Tarea antes de la siguiente sesión (5 min)

Pide que completen los Ejercicios 2 y 3 individualmente antes de la
siguiente sesión grupal (Proyecto — Planificador de tareas personal), ya
que no se cubren en vivo.

## Notas generales de facilitación

- Si el grupo ya trabajó las sesiones de Módulos 1-3, pueden arrancar más
  rápido en el paso 1 — conecta directamente con delegación y context rot
  sin repasarlos desde cero.
- El escenario 2 del Ejercicio 1 (exploración en un monorepo grande) y el
  escenario 4 (paralelismo) a veces generan la pregunta de si deberían
  combinarse — es una buena oportunidad para señalar que la exploración
  de cada microservicio podría delegarse Y correr en paralelo si son
  realmente independientes entre sí.
```

- [ ] **Step 2: Write the participant guide**

Create `modulos/04-loops-y-orquestacion/sesion-grupal/participante.md`:

```markdown
# Sesión grupal — Módulo 4: Participante

**Antes de esta sesión:** lee el `README.md` de este módulo. Esta sesión
asume que ya conoces el loop de agente, la delegación a subagentes, y el
criterio de independencia para paralelismo — aquí los vamos a aplicar, no
a repasar desde cero.

## Qué vamos a hacer

1. **Apertura (10 min):** discutimos qué hace que un agente sea distinto
   de una sola respuesta de un modelo.
2. **Discusión (10 min):** en plenaria, exploramos qué le pasa al
   contexto de un loop que nunca poda nada.
3. **Actividad en equipos (30 min):** en equipos de 2-3, van a clasificar
   5 escenarios como "loop principal", "delegar a subagente", o "delegar
   en paralelo" — es el **Ejercicio 1** de este módulo
   (`ejercicios/enunciados/01-loop-o-subagente.md`). Tendrán 15 minutos
   para clasificar en equipo, y luego compartiremos algunas de las
   clasificaciones más debatidas.
4. **Cierre (15 min):** conectamos con los riesgos del paralelismo mal
   aplicado, a partir de ejemplos reales del grupo.

## Qué traer

- Tu lectura previa del `README.md` del módulo.
- Una laptop o cuaderno para trabajar el ejercicio en equipo.

## Después de la sesión

Antes de la siguiente sesión grupal (Proyecto — Planificador de tareas
personal), completa individualmente los **Ejercicios 2 y 3** de este
módulo (`02-diagnostico-loop.md` y `03-disena-el-loop.md`) — no se cubren
en vivo. Puedes revisar tus respuestas contra las soluciones de
referencia en `ejercicios/soluciones/`.
```

- [ ] **Step 3: Verify both files exist and reference the shared exercise**

Run:
```bash
grep -l '01-loop-o-subagente' modulos/04-loops-y-orquestacion/sesion-grupal/*.md
```
Expected: both files listed —
```
modulos/04-loops-y-orquestacion/sesion-grupal/facilitador.md
modulos/04-loops-y-orquestacion/sesion-grupal/participante.md
```

- [ ] **Step 4: Commit**

```bash
git add modulos/04-loops-y-orquestacion/sesion-grupal/
git commit -m "$(cat <<'EOF'
Add Módulo 4 group session materials

Facilitator guide (agenda, timing, discussion prompts) and participant
guide for a 75-minute session built around the loop/subagent/parallel
classification exercise, closing with the risks of misapplied
parallelism.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 4: Actualizar roadmap del README raíz

**Files:**
- Modify: `README.md:39`

**Interfaces:**
- Consumes: the existence of `modulos/04-loops-y-orquestacion/README.md` (Task 1) — the new link target must resolve.
- Produces: nothing consumed elsewhere in this plan (this is the plan's final step)

- [ ] **Step 1: Flip the Módulo 4 roadmap row**

In `README.md`, find this exact line (currently line 39):

```markdown
| 5 | Módulo 4 — Loops y Orquestación | 🚧 Próximamente |
```

Replace it with:

```markdown
| 5 | [Módulo 4 — Loops y Orquestación](modulos/04-loops-y-orquestacion/) | ✅ Disponible |
```

Leave every other row in the table unchanged — Proyecto 02 (step 6) and beyond remain `🚧 Próximamente`, since they are out of scope for this plan.

- [ ] **Step 2: Verify**

Run: `grep -c '04-loops-y-orquestacion' README.md`
Expected: `1`

Run: `grep -c '🚧 Próximamente' README.md`
Expected: `3` (one more row flipped to ✅, three remain 🚧 — steps 6 through 8)

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "$(cat <<'EOF'
Mark Módulo 4 available in the root README roadmap

Links the roadmap's Módulo 4 row to the now-shipped module and flips
its status from 🚧 to ✅, following the same pattern used for Módulos
1-3 and Proyecto 01.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

## Follow-up plans (not in this plan's scope)

- Proyecto 02 — Planificador de tareas personal (intermedio)
- Módulo 5 — Evaluación y Guardrails
- Proyecto 03 — Harness de meta-aprendizaje (insignia)

Each should update the root README roadmap table (flip the relevant row from
🚧 to ✅) as its final step, following this plan's Task 4 pattern.
