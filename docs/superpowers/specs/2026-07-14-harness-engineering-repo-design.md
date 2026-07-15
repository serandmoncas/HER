# Diseño: Repositorio de Harness Engineering

## Contexto

Este repositorio (`HER` — Harness Engineering Repository) es un currículo práctico
sobre **Harness Engineering**: la disciplina de diseñar el sistema alrededor de un
modelo de lenguaje (contexto, herramientas, memoria, loops de ejecución y
guardrails) que determina el desempeño real de un agente IA, más que el modelo en
sí mismo.

Inspirado en el video ["Cómo Funciona un Arnés de Agentes IA (Harness Engineering
Explicado)"](https://www.youtube.com/watch?v=z3KF8OaLCG4) de Benjamín Cordero, y en
los papers de Anthropic sobre gestión de contexto en agentes.

## Audiencia y objetivo

El repositorio sirve simultáneamente para:
- Autoestudio personal
- Talleres/cursos impartidos en vivo
- Material abierto de comunidad
- Onboarding interno de equipo

Al completarlo, alguien debe poder:
1. Entender conceptualmente las piezas de un harness y evaluar harnesses existentes.
2. Dominar las capacidades de Claude Code (skills, subagentes, hooks, memoria) como
   implementación de referencia.
3. Diseñar su propio harness desde cero para un proyecto propio.

## Herramienta de referencia

Todo el contenido práctico usa **Claude Code** como implementación de referencia.
Cada concepto puede incluir una nota comparativa breve de cómo se ve en otras
herramientas (Cursor, Codex/AGENTS.md, etc.), pero sin ejemplos completos en esas
otras herramientas — eso queda fuera de alcance por ahora.

Todo el contenido está en **español**.

## Arquitectura del repositorio

Organización por **módulo autocontenido**: cada módulo agrupa su propia teoría,
ejercicios y sesión grupal, en vez de separar por tipo de contenido. Esto permite
seguir el currículo secuencialmente y facilita añadir un módulo nuevo completo sin
tocar múltiples carpetas dispersas.

```
HER/
├── README.md
├── modulos/
│   ├── 01-fundamentos-context-engineering/
│   ├── 02-herramientas-y-skills/
│   ├── 03-memoria-y-persistencia/
│   ├── 04-loops-y-orquestacion/
│   └── 05-evaluacion-y-guardrails/
├── proyectos/
│   ├── 01-principiante-code-review/
│   ├── 02-intermedio-planificador-tareas/
│   └── 03-meta-aprendizaje/
└── docs/superpowers/specs/
```

## Estructura interna de cada módulo

```
modulos/NN-nombre-modulo/
├── README.md              # Contenido teórico: conceptos, referencias
├── ejercicios/
│   ├── enunciados/        # Ejercicios sin resolver
│   └── soluciones/        # Soluciones de referencia, separadas para autoevaluación
└── sesion-grupal/
    ├── facilitador.md     # Timing, preguntas disparadoras, notas de facilitación
    └── participante.md    # Material y ejercicios para seguir en vivo
```

### Los 5 módulos

1. **01-fundamentos-context-engineering** — Qué es un harness, por qué importa más
   que el modelo, gestión de contexto (papers de Anthropic), ventanas de contexto,
   compactación.
2. **02-herramientas-y-skills** — Diseño de tools/skills, cuándo crear una skill vs.
   un subagente, permisos y sandboxing.
3. **03-memoria-y-persistencia** — CLAUDE.md, memory files, cómo un agente
   aprende/recuerda entre sesiones.
4. **04-loops-y-orquestacion** — Agentic loops, subagentes paralelos,
   planificación multi-paso, cuándo delegar a un subagente.
5. **05-evaluacion-y-guardrails** — Cómo medir si un harness funciona bien,
   seguridad, hooks de validación, prevención de errores costosos.

## Proyectos de ejemplo

Cada proyecto es una configuración de Claude Code **100% funcional** (carpeta
`.claude/` real con skills, subagentes, hooks y `CLAUDE.md` que efectivamente se
pueden ejecutar), no solo documentación. Progresión de dificultad:

### 01-principiante: Asistente de code review
Un solo skill enfocado, sin orquestación. Revisa un diff y da feedback
estructurado. Ilustra los módulos 1-2 (fundamentos + skills) sin la complejidad de
memoria o delegación.

### 02-intermedio: Planificador de tareas personal
Introduce memoria persistente (prioridades/hábitos del usuario entre sesiones) y un
subagente (delegado para búsqueda/investigación de información). Ilustra los
módulos 3-4.

### 03-meta-aprendizaje (proyecto insignia)
Combina los 5 pilares. Un agente que:
- Ayuda a un humano a aprender: genera planes de estudio, quizzes, rastrea progreso
  y ajusta la dificultad con el tiempo.
- Aprende sobre sí mismo: evalúa qué estrategias de enseñanza funcionaron y ajusta
  sus propias skills/prompts, guardando eso como memoria persistente.

Este proyecto sirve como el ejercicio de cierre del currículo — demuestra
integración completa de contexto, herramientas, memoria, loops y guardrails.

### Convención común para los 3 proyectos

Cada `proyectos/NN-nombre/README.md` incluye:
- Qué pilares del harness ilustra el proyecto.
- Decisiones de diseño explicadas (por qué skill vs. subagente, qué va en memoria,
  etc.).
- Sección **"Cómo probarlo"**: prompts de ejemplo paso a paso para ejecutar contra
  Claude Code y observar el comportamiento. Verificación manual guiada, no suite de
  tests automatizada — apropiado porque se evalúa comportamiento de agente, no
  lógica determinista.

## README raíz

El `README.md` de nivel superior reemplaza al actual (que solo dice "Harness
Engineering Repository") y contiene:
- Qué es Harness Engineering (resumen + crédito al video que inspiró el repo).
- Ruta de aprendizaje sugerida: los 5 módulos en orden, con los proyectos
  intercalados como checkpoints prácticos (proyecto 01 después del módulo 2,
  proyecto 02 después del módulo 4, proyecto 03 al final).
- Prerrequisitos (Claude Code instalado).
- Cómo usar el repo en modo autoestudio vs. modo taller grupal.

## Fuera de alcance (por ahora)

- Ejemplos prácticos completos en herramientas distintas a Claude Code.
- Tests automatizados para los proyectos de ejemplo.
- Traducción a otros idiomas.
- Contenido teórico detallado de cada módulo (este documento define la
  *estructura*; el contenido de cada `README.md` de módulo se escribe como
  siguiente fase, módulo por módulo).
