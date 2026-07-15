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
