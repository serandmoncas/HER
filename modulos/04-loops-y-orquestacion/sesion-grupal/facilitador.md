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
