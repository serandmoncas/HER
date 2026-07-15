# Módulo 3 (Memoria y Persistencia) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship the third complete, self-contained module (`modulos/03-memoria-y-persistencia/`) with theory, exercises + solutions, and group-session materials, then flip the root README roadmap row for Módulo 3 from 🚧 to ✅.

**Architecture:** Pure Markdown content repository. No build system, no application code. This module follows the exact same internal structure as Módulos 1-2 (`README.md`, `ejercicios/enunciados/`, `ejercicios/soluciones/`, `sesion-grupal/facilitador.md`, `sesion-grupal/participante.md`) and builds explicitly on Módulo 1's concepts (contexto mínimo de alta señal, *context rot*, compactación/poda) and Módulo 2's concepts (carga "justo a tiempo" of skills vs. always-loaded content) rather than introducing memory as an unrelated topic. Módulo 4, Módulo 5, Proyecto 02, and the meta-aprendizaje project are out of scope for this plan.

**Tech Stack:** Markdown only. Git for version control.

## Global Constraints

- All content in Spanish (per design spec `docs/superpowers/specs/2026-07-14-harness-engineering-repo-design.md`).
- Claude Code is the reference tool for all practical content; other tools get at most a brief comparative note, never a full example.
- No automated test suite — verification is manual (read-through + structural grep checks), matching Módulos 1-2's precedent.
- Module folder structure is fixed: `README.md`, `ejercicios/enunciados/`, `ejercicios/soluciones/`, `sesion-grupal/facilitador.md`, `sesion-grupal/participante.md`.
- Content must explicitly connect back to already-shipped terminology: "contexto mínimo de alta señal", *context rot*, compactación/poda (Módulo 1); the contrast between skills' "justo a tiempo" loading and always-present context (Módulo 2) — named by term, not silently reinvented.
- The root README roadmap table (`README.md:38`) must have its Módulo 3 row flipped from `🚧 Próximamente` to `✅ Disponible` with a working relative link, as the final step of this plan — same pattern already used for Módulos 1-2 and Proyecto 01.

---

### Task 1: Módulo 3 — Teoría

**Files:**
- Create: `modulos/03-memoria-y-persistencia/README.md`

**Interfaces:**
- Consumes: `modulos/01-fundamentos-context-engineering/README.md` and `modulos/02-herramientas-y-skills/README.md` (already shipped) — this task's content must reference "contexto mínimo de alta señal", *context rot*, compactación/poda (Módulo 1), and the skills' "justo a tiempo" vs. always-loaded contrast (Módulo 2) by name, not redefine them.
- Produces: the CLAUDE.md-vs-memoria-de-usuario distinction and the "memoria como riesgo compuesto" concept that Tasks 2-3 of this plan reference by name.

- [ ] **Step 1: Write the module theory content**

Create `modulos/03-memoria-y-persistencia/README.md`:

```markdown
# Módulo 3 — Memoria y Persistencia

## ¿Qué es la memoria en un harness?

El contexto de una conversación es efímero: cuando la sesión termina (o se
compacta más allá de cierto punto), esa información desaparece. La
**memoria** es la pieza del harness que resuelve ese problema — información
que persiste más allá de una sola conversación, y que el harness reintroduce
como contexto en sesiones futuras cuando es relevante.

Esto convierte a la memoria en un problema de context engineering en sí
mismo, no en una pieza aparte. El Módulo 1 estableció que el contexto es un
presupuesto finito que hay que gestionar con cuidado; la memoria es,
literalmente, contexto que el harness decide reinyectar en una sesión
nueva. Las mismas preguntas — ¿qué vale la pena incluir?, ¿cuándo se carga?,
¿qué pasa si se acumula sin control? — aplican igual de directo a la
memoria que a cualquier otro contenido del contexto.

## CLAUDE.md: memoria de proyecto cargada siempre

`CLAUDE.md` es el ejemplo más directo de memoria de proyecto en Claude
Code: un archivo, típicamente en la raíz del repositorio, que Claude Code
carga automáticamente al inicio de cada sesión en ese proyecto — no justo a
tiempo, como una skill del Módulo 2, sino siempre, en cada conversación sin
excepción.

Esa diferencia de diseño respecto a las skills no es accidental: una skill
se activa condicionalmente porque su contenido solo aplica cuando la tarea
coincide con su descripción; `CLAUDE.md` se carga siempre porque su
contenido — cómo correr las pruebas, la arquitectura general del proyecto,
las convenciones del equipo — es relevante para prácticamente cualquier
tarea en ese repositorio.

Pero cargar algo siempre tiene un costo mayor que cargarlo
condicionalmente: cada línea de `CLAUDE.md` se paga en el presupuesto de
contexto de cada conversación, la necesite esa tarea puntual o no. Por eso
`CLAUDE.md` exige una disciplina de "contexto mínimo de alta señal" incluso
más estricta que una skill — información que solo aplica a un caso
específico pertenece a una skill, no a `CLAUDE.md`.

## Memoria de usuario: aprender entre sesiones

Además de la memoria de proyecto, un harness puede mantener memoria a nivel
de usuario: preferencias de cómo trabajar, retroalimentación correctiva que
el usuario ya dio antes ("no hagas X", "siempre haz Y así"), y contexto
sobre iniciativas en curso que no vive en el código del proyecto. A
diferencia de `CLAUDE.md`, esta memoria suele ser personal, no se comparte
con el equipo, y se actualiza a partir de las propias conversaciones — el
harness aprende observando, no solo leyendo lo que alguien escribió a mano
de antemano.

Esta distinción entre memoria de proyecto (compartida, sobre el código) y
memoria de usuario (personal, sobre cómo colaborar) es útil porque cada una
responde una pregunta distinta: "¿qué necesita saber cualquiera que trabaje
en este proyecto?" vs. "¿qué necesito saber yo específicamente sobre cómo
esta persona quiere que trabajemos juntos?".

## Qué guardar y qué no: la misma disciplina de contexto mínimo

No todo merece guardarse en memoria. El Módulo 1 describió el escenario de
un bot que pega 200 páginas de wiki en cada conversación "por si acaso" —
una memoria mal disciplinada recrea exactamente ese problema, solo que la
carga ocurre al escribir en vez de al leer.

Un criterio práctico: guarda algo en memoria solo si es sorprendente, no
obvio a partir del código o los archivos del proyecto, o si el usuario lo
corrigió explícitamente. Un hecho que cualquiera podría deducir leyendo el
repositorio no necesita vivir en memoria — ya está disponible justo a
tiempo, sin ocupar presupuesto de contexto en cada sesión. Guardar de más
no es gratis: cada entrada de memoria innecesaria es contexto de bajo valor
compitiendo por atención en cada conversación futura, la misma dinámica de
*context rot* del Módulo 1, ahora aplicada a lo que el harness decide
recordar.

## Memoria como guardrail y riesgo

La memoria tiene una propiedad que el contexto de una sola conversación no
tiene: un error persiste. Si el harness guarda un hecho incorrecto, esa
equivocación se reintroduce en cada sesión futura hasta que alguien la
corrija — un error que en una conversación aislada se olvidaría al
cerrarla, en memoria se vuelve compuesto.

Esto tiene una segunda cara: `CLAUDE.md`, al vivir dentro del repositorio,
se revisa como cualquier otro cambio de código (pull requests, revisión de
pares). La memoria de usuario, en cambio, normalmente no pasa por ese mismo
proceso de revisión — lo que la hace más rápida de actualizar, pero también
un lugar donde información sensible podría terminar guardada sin la misma
supervisión. Diseñar bien qué vive en cada tipo de memoria, y con qué nivel
de revisión, es una primera forma de guardrail — el Módulo 5 retoma este
tema con más profundidad.

## Para reflexionar / Referencias

- La documentación oficial de Claude Code sobre `CLAUDE.md` y sobre
  sistemas de memoria es la referencia más actualizada para los detalles de
  implementación.
- Este módulo construye directamente sobre "contexto mínimo de alta señal"
  y *context rot* (Módulo 1), y sobre la distinción entre carga "justo a
  tiempo" y carga siempre-presente introducida al comparar skills con
  `CLAUDE.md` (Módulo 2).
```

- [ ] **Step 2: Verify structure**

Run: `grep -c '^## ' modulos/03-memoria-y-persistencia/README.md`
Expected: `6`

Run: `wc -w modulos/03-memoria-y-persistencia/README.md`
Expected: at least `700`

Run: `grep -c 'Módulo 1' modulos/03-memoria-y-persistencia/README.md`
Expected: at least `1`

Run: `grep -c 'Módulo 2' modulos/03-memoria-y-persistencia/README.md`
Expected: at least `1`

- [ ] **Step 3: Commit**

```bash
git add modulos/03-memoria-y-persistencia/README.md
git commit -m "$(cat <<'EOF'
Add Módulo 3 theory: Memoria y Persistencia

Covers memory as reintroduced context, CLAUDE.md as always-loaded
project memory vs. skills' just-in-time loading, user-level memory,
what's worth persisting under the minimal-context discipline, and
memory's compounding-error risk as a preview of Módulo 5 guardrails.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 2: Módulo 3 — Ejercicios (enunciados + soluciones)

**Files:**
- Create: `modulos/03-memoria-y-persistencia/ejercicios/enunciados/01-claude-md-o-memoria-usuario.md`
- Create: `modulos/03-memoria-y-persistencia/ejercicios/enunciados/02-entrada-claude-md.md`
- Create: `modulos/03-memoria-y-persistencia/ejercicios/enunciados/03-diagnostico-memoria.md`
- Create: `modulos/03-memoria-y-persistencia/ejercicios/soluciones/01-claude-md-o-memoria-usuario.md`
- Create: `modulos/03-memoria-y-persistencia/ejercicios/soluciones/02-entrada-claude-md.md`
- Create: `modulos/03-memoria-y-persistencia/ejercicios/soluciones/03-diagnostico-memoria.md`

**Interfaces:**
- Consumes: the theory README from Task 1 (exercises reference the CLAUDE.md-vs-memoria-de-usuario distinction and "context rot" applied to memory)
- Produces: `01-claude-md-o-memoria-usuario` is the exercise Task 3 (group session) reuses as its live group activity — its filename must match exactly.

- [ ] **Step 1: Write exercise 1 statement — CLAUDE.md, memoria de usuario o ninguno**

Create `modulos/03-memoria-y-persistencia/ejercicios/enunciados/01-claude-md-o-memoria-usuario.md`:

```markdown
# Ejercicio 1: CLAUDE.md, memoria de usuario o ninguno

## Tu tarea

Para cada pieza de información, decide si debería guardarse en **(a)**
`CLAUDE.md`, **(b)** memoria de usuario, o **(c)** ninguno de los dos.
Justifica cada respuesta en 1-2 frases usando la distinción del módulo.

1. El comando exacto para correr la suite de pruebas del proyecto.
2. El hecho de que a un usuario específico le gusta que los commits sean
   cortos y sin resúmenes al final.
3. Una corrección que el usuario dio explícitamente: "no uses --force push
   sin preguntar primero".
4. El nombre de una variable en un archivo específico del código — algo
   visible con solo leer el archivo.
5. La arquitectura general de cómo se comunican los módulos del backend
   entre sí.
```

- [ ] **Step 2: Write exercise 2 statement — entrada de CLAUDE.md**

Create `modulos/03-memoria-y-persistencia/ejercicios/enunciados/02-entrada-claude-md.md`:

```markdown
# Ejercicio 2: Diseña una entrada de CLAUDE.md

## Escenario

Vas a escribir la sección de "Comandos comunes" del `CLAUDE.md` de un
proyecto Node.js. El proyecto usa `npm test` para correr pruebas, `npm run
build` para compilar, y tiene un comando especial `npm run test:single --
<archivo>` para correr una sola prueba. El proyecto también tiene, en un
archivo separado `docs/arquitectura.md`, una explicación de 3000 palabras
de la arquitectura completa del sistema.

## Tu tarea

1. Escribe la sección "Comandos comunes" para `CLAUDE.md`, aplicando el
   principio de contexto mínimo de alta señal del módulo.
2. Explica por qué NO deberías copiar el contenido completo de
   `docs/arquitectura.md` dentro de `CLAUDE.md`, y qué deberías hacer en su
   lugar.
3. Menciona un tipo de información que sería tentador añadir a esta
   sección pero que en realidad no pertenece ahí.
```

- [ ] **Step 3: Write exercise 3 statement — diagnóstico de memoria**

Create `modulos/03-memoria-y-persistencia/ejercicios/enunciados/03-diagnostico-memoria.md`:

```markdown
# Ejercicio 3: Diagnostica una memoria mal diseñada

## Escenario

Un equipo lleva 6 meses usando un agente de código con memoria de usuario
habilitada. Con el tiempo, su archivo de memoria personal creció a 4000
palabras: incluye desde la preferencia real del usuario ("prefiero PRs
pequeños") hasta anotaciones que ya no aplican ("en marzo estábamos
migrando de X a Y", proyecto que ya terminó hace 3 meses), pasando por
hechos que cualquiera podría ver leyendo el código ("el proyecto usa
TypeScript"). El usuario nota que el agente ahora tarda más en responder y
a veces menciona contexto de proyectos que ya no existen.

## Tu tarea

1. Clasifica el contenido descrito en al menos tres categorías: memoria
   que vale la pena conservar, memoria obsoleta que debería eliminarse, y
   memoria que nunca debió guardarse.
2. Conecta el síntoma de lentitud y las menciones de proyectos ya
   terminados con el concepto de *context rot* del Módulo 1 — ¿por qué una
   memoria que crece sin poda produce exactamente ese problema?
3. Propón una práctica concreta que el equipo podría adoptar para evitar
   que esto vuelva a pasar.
```

- [ ] **Step 4: Write solution 1**

Create `modulos/03-memoria-y-persistencia/ejercicios/soluciones/01-claude-md-o-memoria-usuario.md`:

```markdown
# Solución — Ejercicio 1: CLAUDE.md, memoria de usuario o ninguno

Esta es una solución de referencia. Tu razonamiento puede variar en los
detalles siempre que aplique correctamente la distinción del módulo.

1. **→ CLAUDE.md.** Es información objetiva sobre el proyecto que
   cualquiera que trabaje ahí necesita, no algo personal de un usuario.
2. **→ Memoria de usuario.** Es una preferencia personal de estilo, no una
   regla del proyecto que todo el equipo deba seguir.
3. **→ Memoria de usuario.** Es retroalimentación correctiva explícita —
   exactamente el tipo de información que el módulo identifica como
   candidata a memoria personal.
4. **→ Ninguno.** Es información visible con solo leer el archivo — está
   disponible justo a tiempo, sin necesidad de persistirla en ningún lado.
5. **→ CLAUDE.md.** Es arquitectura relevante para cualquiera trabajando en
   el proyecto — aunque si esta explicación es larga, puede convenir un
   archivo de referencia aparte enlazado desde `CLAUDE.md` en vez de todo
   el contenido inline (ver Ejercicio 2).
```

- [ ] **Step 5: Write solution 2**

Create `modulos/03-memoria-y-persistencia/ejercicios/soluciones/02-entrada-claude-md.md`:

```markdown
# Solución — Ejercicio 2: Diseña una entrada de CLAUDE.md

Esta es una solución de referencia; el objetivo es el razonamiento sobre
qué pertenece a `CLAUDE.md`, no una redacción exacta.

## Sección propuesta

```markdown
## Comandos comunes
- `npm test` — correr toda la suite de pruebas.
- `npm run build` — compilar el proyecto.
- `npm run test:single -- <archivo>` — correr una sola prueba.
```

## Por qué no copiar docs/arquitectura.md completo

`docs/arquitectura.md` tiene 3000 palabras — copiarlo completo dentro de
`CLAUDE.md` significaría pagar ese costo de contexto en cada conversación
del proyecto, sin importar si la tarea actual tiene algo que ver con la
arquitectura. En vez de eso, `CLAUDE.md` debería solo mencionar que existe
ese archivo y dónde está (por ejemplo, "para una explicación detallada de
la arquitectura, ver `docs/arquitectura.md`") — así el agente puede leerlo
justo a tiempo, cuando una tarea realmente lo necesite, en vez de cargarlo
siempre.

## Qué NO incluir

Tentador pero incorrecto: detalles de una migración o refactor en curso
que va a cambiar pronto (por ejemplo, "estamos migrando el módulo X a Y,
ten cuidado con Z"). Esa información cambia con frecuencia y se vuelve
obsoleta rápido — `CLAUDE.md` se revisa como código pero no se actualiza
con la frecuencia de una conversación normal, así que un dato así de
volátil tiende a quedar desactualizado y confundir en vez de ayudar.
```

- [ ] **Step 6: Write solution 3**

Create `modulos/03-memoria-y-persistencia/ejercicios/soluciones/03-diagnostico-memoria.md`:

```markdown
# Solución — Ejercicio 3: Diagnostica una memoria mal diseñada

Esta es una solución de referencia. Tu razonamiento puede variar en los
detalles siempre que identifique correctamente el mecanismo de *context
rot* aplicado a memoria.

## Clasificación

- **Vale la pena conservar:** "prefiero PRs pequeños" — preferencia
  estable, sigue aplicando.
- **Obsoleta, debería eliminarse:** la nota sobre la migración de marzo
  que ya terminó.
- **Nunca debió guardarse:** "el proyecto usa TypeScript" — visible con
  solo leer el código, no aporta nada nuevo en memoria.

## Conexión con context rot

Es el mismo mecanismo del Módulo 1: cada entrada de memoria, sin importar
si sigue siendo relevante, compite por atención en cada sesión nueva. Con
4000 palabras acumuladas sin poda, la señal real (la preferencia de PRs
pequeños que sí sigue aplicando) queda enterrada entre ruido obsoleto — el
agente tarda más porque hay más contexto que procesar, y menciona
proyectos terminados porque esa información nunca se retiró, solo se
acumuló encima.

## Práctica propuesta

Una revisión periódica de la memoria (por ejemplo, cada cierto número de
semanas, o al cerrar un proyecto o iniciativa) donde se poda explícitamente
lo que ya no aplica — el mismo principio de compactación y poda que el
Módulo 1 describe para el contexto de una conversación, aplicado aquí a la
memoria persistente en vez de a una sola sesión.
```

- [ ] **Step 7: Verify enunciados/soluciones pairing**

Run:
```bash
diff <(ls modulos/03-memoria-y-persistencia/ejercicios/enunciados/) \
     <(ls modulos/03-memoria-y-persistencia/ejercicios/soluciones/)
```
Expected: no output (empty diff — every enunciado has a matching solución filename)

- [ ] **Step 8: Commit**

```bash
git add modulos/03-memoria-y-persistencia/ejercicios/
git commit -m "$(cat <<'EOF'
Add Módulo 3 exercises with reference solutions

Three exercises covering CLAUDE.md/memoria-de-usuario/neither
classification, designing a minimal CLAUDE.md entry, and diagnosing
an unpruned memory file through the context rot lens — each with a
matching solution in a separate folder for self-assessment.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 3: Módulo 3 — Sesión grupal

**Files:**
- Create: `modulos/03-memoria-y-persistencia/sesion-grupal/facilitador.md`
- Create: `modulos/03-memoria-y-persistencia/sesion-grupal/participante.md`

**Interfaces:**
- Consumes: the theory README from Task 1 and Exercise 1 (`01-claude-md-o-memoria-usuario`) from Task 2 — the group session reuses that exact exercise as its live group activity.
- Produces: nothing consumed elsewhere in this plan

- [ ] **Step 1: Write the facilitator guide**

Create `modulos/03-memoria-y-persistencia/sesion-grupal/facilitador.md`:

```markdown
# Sesión grupal — Módulo 3: Facilitador

**Duración total:** ~75 minutos
**Tamaño de grupo recomendado:** 4-12 personas
**Requisito previo:** los participantes deben haber leído el `README.md`
de este módulo antes de la sesión.

## Agenda

### 1. Apertura: memoria como contexto reintroducido (10 min)

Pregunta disparadora para abrir, en plenaria:

> "¿Alguien ha usado un agente o asistente que 'recuerda' algo de una
> conversación anterior? ¿Cómo se sintió comparado con uno que empieza de
> cero cada vez?"

Conecta las respuestas con la idea de que la memoria es, literalmente,
contexto reintroducido en una sesión nueva — no un mecanismo aparte del
resto del harness.

### 2. Refuerzo del concepto central (10 min)

Discusión guiada sobre la diferencia entre `CLAUDE.md` (memoria de
proyecto, siempre cargada) y memoria de usuario (personal, aprendida de
las conversaciones), usando la pregunta:

> "Si tuvieran que decidir entre guardar algo en CLAUDE.md o en memoria de
> usuario, ¿qué pregunta se harían primero?"

Refuerza la distinción formal del módulo: "¿qué necesita saber cualquiera
en este proyecto?" vs. "¿qué necesito saber yo sobre cómo esta persona
quiere trabajar?".

### 3. Actividad grupal: CLAUDE.md, memoria de usuario o ninguno (30 min)

Divide al grupo en equipos de 2-3 personas. Cada equipo trabaja el
**Ejercicio 1 (CLAUDE.md, memoria de usuario o ninguno)** del módulo —
está en `ejercicios/enunciados/01-claude-md-o-memoria-usuario.md`.

Timing sugerido dentro de este bloque:
- 15 min: cada equipo clasifica las 5 piezas de información y prepara su
  justificación.
- 15 min: cada equipo comparte 1-2 de sus clasificaciones más discutidas.
  Presta especial atención al escenario 5 (la arquitectura general) —
  suele generar la pregunta de si un contenido largo debería vivir inline
  en `CLAUDE.md` o en un archivo aparte referenciado, que es exactamente
  el tema del Ejercicio 2.

Nota para el facilitador: la solución de referencia está en
`ejercicios/soluciones/01-claude-md-o-memoria-usuario.md`. No la compartas
antes de que los equipos presenten — úsala para guiar el cierre de la
discusión, no como veredicto impuesto sobre el razonamiento del grupo.

### 4. Cierre: memoria como riesgo compuesto (15 min)

Cierra conectando con la última sección del módulo. Pregunta al grupo si
alguna vez han visto un asistente "recordar" algo incorrecto o
desactualizado. Usa esas anécdotas para introducir la idea de que un error
en memoria se compone con el tiempo, a diferencia de un error en una sola
conversación, y anticipa que el Módulo 5 retoma este tema como parte de
guardrails.

### 5. Tarea antes de la siguiente sesión (5 min)

Pide que completen los Ejercicios 2 y 3 individualmente antes de la
siguiente sesión grupal (Módulo 4), ya que no se cubren en vivo.

## Notas generales de facilitación

- Si el grupo ya trabajó las sesiones de Módulos 1 y 2, pueden arrancar
  más rápido en el paso 1 — conecta directamente con "justo a tiempo" sin
  repasarlo desde cero.
- El escenario 2 del Ejercicio 1 (preferencia de PRs pequeños) y el
  escenario 3 (corrección explícita) a veces generan debate sobre si son
  la misma categoría — es una buena oportunidad para señalar que ambos son
  memoria de usuario, aunque uno se infiere y el otro se dice
  explícitamente.
```

- [ ] **Step 2: Write the participant guide**

Create `modulos/03-memoria-y-persistencia/sesion-grupal/participante.md`:

```markdown
# Sesión grupal — Módulo 3: Participante

**Antes de esta sesión:** lee el `README.md` de este módulo. Esta sesión
asume que ya conoces la diferencia entre `CLAUDE.md` y memoria de usuario,
y el principio de contexto mínimo aplicado a la memoria — aquí los vamos a
aplicar, no a repasar desde cero.

## Qué vamos a hacer

1. **Apertura (10 min):** compartimos experiencias con agentes que
   "recuerdan" (o no) entre conversaciones.
2. **Discusión (10 min):** en plenaria, buscamos la pregunta clave para
   decidir entre CLAUDE.md y memoria de usuario.
3. **Actividad en equipos (30 min):** en equipos de 2-3, van a clasificar
   5 piezas de información como CLAUDE.md, memoria de usuario, o ninguno —
   es el **Ejercicio 1** de este módulo
   (`ejercicios/enunciados/01-claude-md-o-memoria-usuario.md`). Tendrán 15
   minutos para clasificar en equipo, y luego compartiremos algunas de las
   clasificaciones más debatidas.
4. **Cierre (15 min):** conectamos con la última sección del módulo —
   memoria como riesgo compuesto — a partir de ejemplos reales del grupo.

## Qué traer

- Tu lectura previa del `README.md` del módulo.
- Una laptop o cuaderno para trabajar el ejercicio en equipo.

## Después de la sesión

Antes de la siguiente sesión grupal (Módulo 4), completa individualmente
los **Ejercicios 2 y 3** de este módulo (`02-entrada-claude-md.md` y
`03-diagnostico-memoria.md`) — no se cubren en vivo. Puedes revisar tus
respuestas contra las soluciones de referencia en `ejercicios/soluciones/`.
```

- [ ] **Step 3: Verify both files exist and reference the shared exercise**

Run:
```bash
grep -l '01-claude-md-o-memoria-usuario' modulos/03-memoria-y-persistencia/sesion-grupal/*.md
```
Expected: both files listed —
```
modulos/03-memoria-y-persistencia/sesion-grupal/facilitador.md
modulos/03-memoria-y-persistencia/sesion-grupal/participante.md
```

- [ ] **Step 4: Commit**

```bash
git add modulos/03-memoria-y-persistencia/sesion-grupal/
git commit -m "$(cat <<'EOF'
Add Módulo 3 group session materials

Facilitator guide (agenda, timing, discussion prompts) and participant
guide for a 75-minute session built around the CLAUDE.md/memoria-de-
usuario/neither classification exercise, closing with memory's
compounding-error risk as a Módulo 5 preview.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 4: Actualizar roadmap del README raíz

**Files:**
- Modify: `README.md:38`

**Interfaces:**
- Consumes: the existence of `modulos/03-memoria-y-persistencia/README.md` (Task 1) — the new link target must resolve.
- Produces: nothing consumed elsewhere in this plan (this is the plan's final step)

- [ ] **Step 1: Flip the Módulo 3 roadmap row**

In `README.md`, find this exact line (currently line 38):

```markdown
| 4 | Módulo 3 — Memoria y Persistencia | 🚧 Próximamente |
```

Replace it with:

```markdown
| 4 | [Módulo 3 — Memoria y Persistencia](modulos/03-memoria-y-persistencia/) | ✅ Disponible |
```

Leave every other row in the table unchanged — Módulo 4 (step 5) and beyond remain `🚧 Próximamente`, since they are out of scope for this plan.

- [ ] **Step 2: Verify**

Run: `grep -c '03-memoria-y-persistencia' README.md`
Expected: `1`

Run: `grep -c '🚧 Próximamente' README.md`
Expected: `4` (one more row flipped to ✅, four remain 🚧 — steps 5 through 8)

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "$(cat <<'EOF'
Mark Módulo 3 available in the root README roadmap

Links the roadmap's Módulo 3 row to the now-shipped module and flips
its status from 🚧 to ✅, following the same pattern used for Módulos
1-2 and Proyecto 01.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

## Follow-up plans (not in this plan's scope)

- Módulo 4 — Loops y Orquestación
- Proyecto 02 — Planificador de tareas personal (intermedio)
- Módulo 5 — Evaluación y Guardrails
- Proyecto 03 — Harness de meta-aprendizaje (insignia)

Each should update the root README roadmap table (flip the relevant row from
🚧 to ✅) as its final step, following this plan's Task 4 pattern.
