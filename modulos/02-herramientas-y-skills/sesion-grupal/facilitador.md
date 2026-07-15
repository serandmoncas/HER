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
