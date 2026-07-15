# Proyecto 01 — Asistente de Code Review Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship the first example project (`proyectos/01-principiante-code-review/`) as a 100% functional Claude Code configuration — a single read-only skill that reviews code against project conventions — then flip the root README roadmap row for this project from 🚧 to ✅.

**Architecture:** Unlike the módulos (pure teaching Markdown), this is a *working* Claude Code project: a real `.claude/skills/revisar-diff/SKILL.md` that Claude Code auto-discovers when run from this directory, a `CONVENCIONES.md` reference file the skill reads at review time, and a deliberately flawed `ejemplo/calculadora.py` sample file a learner can point the skill at. Per the design spec, this project illustrates Módulos 1-2 without memory or subagent complexity: one skill, no orchestration. Proyecto 02, Módulos 3-5, and the meta-aprendizaje project are out of scope for this plan.

**Tech Stack:** Markdown (skill definition, docs), Python (sample file to review — chosen only as the reviewed artifact's language, not a project dependency; nothing here is executed, only read by the skill).

## Global Constraints

- All content in Spanish (per design spec `docs/superpowers/specs/2026-07-14-harness-engineering-repo-design.md`).
- Claude Code is the reference tool; this project's `.claude/skills/` structure must be a real, working Claude Code skill directory, not a documentation stand-in.
- No automated test suite — verification is manual (structural grep checks + a "Cómo probarlo" prompt walkthrough for a human to run against actual Claude Code), matching the design spec's explicit choice of "Guía manual de prompts" over a pass/fail checklist.
- The skill must be **read-only**: its own procedure must explicitly forbid modifying the code it reviews, as the project's least-privilege illustration (Módulo 2).
- Project-specific rules must live in `CONVENCIONES.md`, external to the skill body, so the skill itself stays reusable across projects — this is the project's explicit design decision to document in its README.
- Every `proyectos/NN-nombre/README.md` must include, per the design spec: which harness pillars it illustrates, its design decisions explained, and a "Cómo probarlo" section with step-by-step example prompts.
- The root README roadmap table (`README.md:37`) must have its "Proyecto — Asistente de code review" row flipped from `🚧 Próximamente` to `✅ Disponible` with a working relative link, as the final step of this plan — same pattern already used for Módulos 1 and 2.

---

### Task 1: Convenciones del proyecto de ejemplo

**Files:**
- Create: `proyectos/01-principiante-code-review/CONVENCIONES.md`

**Interfaces:**
- Consumes: nothing (foundational reference file)
- Produces: the 4 numbered rules that Task 2 (the skill) reads by reference and Task 3 (the sample file) is deliberately written to violate.

- [ ] **Step 1: Write the conventions file**

Create `proyectos/01-principiante-code-review/CONVENCIONES.md`:

```markdown
# Convenciones del proyecto — Calculadora de ejemplo

Estas son las convenciones que cualquier cambio de código en este proyecto de
ejemplo debe cumplir. Sirven como referencia externa para la skill de
revisión de código de este proyecto — no están escritas dentro de la skill
misma, para que la skill se mantenga reutilizable en otros proyectos con
otras convenciones.

## Reglas

1. **Toda función pública debe tener docstring.** El docstring debe explicar
   qué hace la función, qué parámetros recibe y qué devuelve.
2. **Nunca usar `eval()` ni `exec()`**, bajo ninguna circunstancia, sin
   importar la fuente del texto a evaluar.
3. **Ninguna credencial, clave de API o secreto puede estar escrito
   directamente en el código.** Deben leerse de variables de entorno.
4. **Toda función que reciba parámetros numéricos usados como divisor debe
   validar explícitamente que el divisor no sea cero** antes de operar, y
   manejar ese caso sin dejar que el programa falle con una excepción no
   controlada.
```

- [ ] **Step 2: Verify structure**

Run: `grep -c '^## ' proyectos/01-principiante-code-review/CONVENCIONES.md`
Expected: `1`

Run: `grep -cE '^[0-9]+\.' proyectos/01-principiante-code-review/CONVENCIONES.md`
Expected: `4`

Run: `grep -c 'eval' proyectos/01-principiante-code-review/CONVENCIONES.md`
Expected: `2`

- [ ] **Step 3: Commit**

```bash
git add proyectos/01-principiante-code-review/CONVENCIONES.md
git commit -m "$(cat <<'EOF'
Add sample project conventions for Proyecto 01

Defines the 4 rules (docstrings, no eval/exec, no hardcoded secrets,
divide-by-zero guards) that the code-review skill will check against
and that the example file is deliberately written to violate.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 2: La skill de revisión de código

**Files:**
- Create: `proyectos/01-principiante-code-review/.claude/skills/revisar-diff/SKILL.md`

**Interfaces:**
- Consumes: `proyectos/01-principiante-code-review/CONVENCIONES.md` (Task 1) — the skill's procedure references this filename by name; it must exist for the skill's own instructions to make sense, though the skill also handles its absence gracefully per its own Step 2.
- Produces: the three-category report format ("Bugs de lógica", "Problemas de seguridad", "Violaciones de convenciones") that Task 4 (README) documents as the expected output, and that a learner running the "Cómo probarlo" steps will observe.

- [ ] **Step 1: Write the skill file**

Create `proyectos/01-principiante-code-review/.claude/skills/revisar-diff/SKILL.md`:

```markdown
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
```

- [ ] **Step 2: Verify structure**

Run: `grep -c '^name: revisar-diff' proyectos/01-principiante-code-review/.claude/skills/revisar-diff/SKILL.md`
Expected: `1`

Run: `grep -c '^description:' proyectos/01-principiante-code-review/.claude/skills/revisar-diff/SKILL.md`
Expected: `1`

Run: `grep -c 'CONVENCIONES.md' proyectos/01-principiante-code-review/.claude/skills/revisar-diff/SKILL.md`
Expected: `2`

Run: `grep -c '^## ' proyectos/01-principiante-code-review/.claude/skills/revisar-diff/SKILL.md`
Expected: `3`

- [ ] **Step 3: Commit**

```bash
git add proyectos/01-principiante-code-review/.claude/skills/revisar-diff/SKILL.md
git commit -m "$(cat <<'EOF'
Add revisar-diff skill for Proyecto 01

A read-only code-review skill: reads the target code plus
CONVENCIONES.md, reports findings in three fixed categories with
file:line evidence, and is explicitly forbidden from editing the code
it reviews — the project's least-privilege illustration.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 3: Archivo de ejemplo con problemas plantados

**Files:**
- Create: `proyectos/01-principiante-code-review/ejemplo/calculadora.py`

**Interfaces:**
- Consumes: `proyectos/01-principiante-code-review/CONVENCIONES.md` (Task 1) — this file is deliberately written to violate specific numbered rules from it (rule 1: no docstrings; rule 2: uses `eval`; rule 3: hardcoded `API_KEY`; rule 4: `dividir` has no zero-guard).
- Produces: the concrete file a learner points the skill at in Task 4's "Cómo probarlo" walkthrough — the exact function names (`dividir`, `calcular_desde_texto`, `registrar_uso`, `API_KEY`) are referenced there and must match exactly.

- [ ] **Step 1: Write the example file**

Create `proyectos/01-principiante-code-review/ejemplo/calculadora.py`:

```python
API_KEY = "sk-live-51H8xK2eZvKYlo2Cxyz1234567890abcdef"


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular_desde_texto(expresion):
    return eval(expresion)


def registrar_uso(operacion):
    print(f"Usando API_KEY {API_KEY} para registrar operación: {operacion}")
```

- [ ] **Step 2: Verify structure**

Run: `grep -c '^def ' proyectos/01-principiante-code-review/ejemplo/calculadora.py`
Expected: `6`

Run: `grep -c 'def dividir' proyectos/01-principiante-code-review/ejemplo/calculadora.py`
Expected: `1`

Run: `grep -c 'eval(expresion)' proyectos/01-principiante-code-review/ejemplo/calculadora.py`
Expected: `1`

Run: `grep -c 'API_KEY' proyectos/01-principiante-code-review/ejemplo/calculadora.py`
Expected: `2`

Run: `grep -c '"""' proyectos/01-principiante-code-review/ejemplo/calculadora.py`
Expected: `0` (confirms no docstrings — the deliberate rule-1 violation)

- [ ] **Step 3: Commit**

```bash
git add proyectos/01-principiante-code-review/ejemplo/calculadora.py
git commit -m "$(cat <<'EOF'
Add example file with planted issues for Proyecto 01

A small calculator module that violates all 4 CONVENCIONES.md rules:
no docstrings, eval() on arbitrary input, a hardcoded API key that
gets logged, and an unguarded division by zero — one concrete target
per report category the revisar-diff skill produces.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 4: README del proyecto

**Files:**
- Create: `proyectos/01-principiante-code-review/README.md`

**Interfaces:**
- Consumes: Tasks 1-3 (`CONVENCIONES.md`, the skill, `ejemplo/calculadora.py`) — the "Cómo probarlo" section walks through using all three together, and the file paths/function names referenced must match exactly what those tasks created.
- Produces: nothing consumed elsewhere in this plan

- [ ] **Step 1: Write the project README**

Create `proyectos/01-principiante-code-review/README.md`:

```markdown
# Proyecto — Asistente de code review

## Qué es este proyecto

Este es el primer proyecto de ejemplo del currículo: una configuración de
Claude Code completa y funcional (no solo documentada) que implementa un
asistente de revisión de código como una única skill, sin subagentes ni
memoria persistente. Es el checkpoint práctico después de los Módulos 1 y 2.

## Qué pilares del harness ilustra

- **Contexto mínimo de alta señal (Módulo 1):** la skill `revisar-diff`
  permanece fuera del contexto de Claude Code hasta que una tarea de
  revisión de código la activa — nunca ocupa espacio en una conversación
  que no la necesita.
- **Skill vs. subagente (Módulo 2):** este proyecto usa deliberadamente una
  skill y no un subagente. Revisar un archivo o un diff pequeño es una
  tarea liviana — pocas lecturas, salida corta — exactamente el caso donde
  el Módulo 2 recomienda una skill en vez de aislar el trabajo en un
  subagente.
- **Mínimo privilegio (Módulo 2):** la skill es explícitamente de solo
  lectura. Nunca modifica el código que revisa — el `SKILL.md` lo prohíbe
  en su propio procedimiento, no como una convención externa que el modelo
  tendría que recordar por su cuenta.

## Decisiones de diseño

- **Las convenciones del proyecto viven en `CONVENCIONES.md`, no dentro de
  la skill.** La skill (`.claude/skills/revisar-diff/SKILL.md`) no
  hardcodea ninguna regla específica de este proyecto — lee
  `CONVENCIONES.md` como referencia externa. Esto la hace reutilizable: la
  misma skill podría copiarse a otro proyecto con otras convenciones sin
  tocar su procedimiento.
- **El reporte se agrupa en tres categorías fijas** (bugs de lógica,
  problemas de seguridad, violaciones de convenciones) para que el
  feedback sea fácil de escanear y nunca se mezclen preocupaciones de
  naturaleza distinta en un solo párrafo.
- **La skill se niega a inventar hallazgos.** El procedimiento exige
  evidencia concreta (archivo:línea) para cada reporte, y prohíbe
  reportar una categoría vacía como si tuviera contenido. Esto es una
  primera aproximación al tipo de guardrail que el Módulo 5 cubre en
  profundidad.

## Estructura de este proyecto

```
proyectos/01-principiante-code-review/
├── README.md              # este archivo
├── CONVENCIONES.md        # reglas del proyecto de ejemplo que la skill verifica
├── .claude/
│   └── skills/
│       └── revisar-diff/
│           └── SKILL.md   # la skill de revisión de código
└── ejemplo/
    └── calculadora.py     # archivo de ejemplo con problemas plantados a propósito
```

## Cómo probarlo

1. Abre una terminal y navega hasta este directorio:
   ```bash
   cd proyectos/01-principiante-code-review
   ```
2. Inicia Claude Code en este directorio (`claude`, o el comando
   equivalente de tu instalación). Al estar dentro de esta carpeta, Claude
   Code descubre automáticamente la skill en
   `.claude/skills/revisar-diff/`.
3. Pide una revisión del archivo de ejemplo:
   > Revisa el archivo ejemplo/calculadora.py
4. Observa el comportamiento esperado: la skill debería activarse, leer
   `CONVENCIONES.md`, y devolver un reporte agrupado en las tres
   categorías. En `ejemplo/calculadora.py` deberías ver, como mínimo: un
   bug de lógica (la función `dividir` no protege contra división por
   cero), al menos un problema de seguridad (el uso de `eval()` en
   `calcular_desde_texto`, y la clave `API_KEY` escrita directamente en el
   código), y una violación de convenciones (ninguna función tiene
   docstring, violando la regla 1 de `CONVENCIONES.md`).
5. Prueba pedir algo más acotado para confirmar que la skill sigue
   activándose con instrucciones más específicas:
   > Revisa ejemplo/calculadora.py buscando específicamente problemas de
   > seguridad
   El reporte debería seguir citando evidencia concreta (archivo y línea)
   en vez de generalidades.
6. Como contraste, pide algo que la skill NO debería activar, por ejemplo:
   > Explícame qué hace la función sumar
   Esto debería responderse directamente, sin que se dispare el
   procedimiento completo de revisión — es una buena señal de que la
   descripción de la skill no es tan amplia que se activa de más.

## Referencias

- Este proyecto aplica directamente lo cubierto en el
  [Módulo 1](../../modulos/01-fundamentos-context-engineering/) y el
  [Módulo 2](../../modulos/02-herramientas-y-skills/).
```

- [ ] **Step 2: Verify structure**

Run: `grep -c '^## ' proyectos/01-principiante-code-review/README.md`
Expected: `6`

Run: `grep -c '01-fundamentos-context-engineering' proyectos/01-principiante-code-review/README.md`
Expected: `1`

Run: `grep -c '02-herramientas-y-skills' proyectos/01-principiante-code-review/README.md`
Expected: `1`

- [ ] **Step 3: Commit**

```bash
git add proyectos/01-principiante-code-review/README.md
git commit -m "$(cat <<'EOF'
Add Proyecto 01 README: pillars, design decisions, how to test

Documents which harness pillars this project illustrates (contexto
mínimo, skill-vs-subagente, mínimo privilegio), the three design
decisions behind it, and a step-by-step manual prompt walkthrough for
verifying the skill against the planted-issues example file.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 5: Actualizar roadmap del README raíz

**Files:**
- Modify: `README.md:37`

**Interfaces:**
- Consumes: the existence of `proyectos/01-principiante-code-review/README.md` (Task 4) — the new link target must resolve.
- Produces: nothing consumed elsewhere in this plan (this is the plan's final step)

- [ ] **Step 1: Flip the Proyecto 01 roadmap row**

In `README.md`, find this exact line (currently line 37):

```markdown
| 3 | Proyecto — Asistente de code review | 🚧 Próximamente |
```

Replace it with:

```markdown
| 3 | [Proyecto — Asistente de code review](proyectos/01-principiante-code-review/) | ✅ Disponible |
```

Leave every other row in the table unchanged — Módulo 3 (step 4) and beyond remain `🚧 Próximamente`, since they are out of scope for this plan.

- [ ] **Step 2: Verify**

Run: `grep -c '01-principiante-code-review' README.md`
Expected: `1`

Run: `grep -c '🚧 Próximamente' README.md`
Expected: `5` (one more row flipped to ✅, five remain 🚧 — steps 4 through 8)

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "$(cat <<'EOF'
Mark Proyecto 01 available in the root README roadmap

Links the roadmap's code-review project row to the now-shipped
project and flips its status from 🚧 to ✅, following the same pattern
used for Módulos 1 and 2.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
```

---

## Follow-up plans (not in this plan's scope)

- Módulo 3 — Memoria y Persistencia
- Módulo 4 — Loops y Orquestación
- Proyecto 02 — Planificador de tareas personal (intermedio)
- Módulo 5 — Evaluación y Guardrails
- Proyecto 03 — Harness de meta-aprendizaje (insignia)

Each should update the root README roadmap table (flip the relevant row from
🚧 to ✅) as its final step, following this plan's Task 5 pattern.
