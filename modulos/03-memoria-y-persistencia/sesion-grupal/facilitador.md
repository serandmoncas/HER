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
