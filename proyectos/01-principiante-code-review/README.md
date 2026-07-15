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
