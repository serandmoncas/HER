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
| 2 | [Módulo 2 — Herramientas y Skills](modulos/02-herramientas-y-skills/) | ✅ Disponible |
| 3 | [Proyecto — Asistente de code review](proyectos/01-principiante-code-review/) | ✅ Disponible |
| 4 | [Módulo 3 — Memoria y Persistencia](modulos/03-memoria-y-persistencia/) | ✅ Disponible |
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
