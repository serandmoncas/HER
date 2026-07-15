# Solución — Ejercicio 1: Diagnóstico de harness

Esta es una solución de referencia. Tu razonamiento puede variar en los
detalles siempre que identifiques correctamente las piezas y conecte los
síntomas con sus causas.

## Piezas presentes vs. ausentes

- **Contexto**: presente, pero mal diseñado — es un volcado masivo y
  estático (todo el wiki, siempre), no un contexto curado para la pregunta
  actual.
- **Herramientas**: ausentes. El bot no puede consultar nada de forma
  selectiva; depende 100% de lo que venga pegado en el prompt.
- **Memoria**: ausente. Cada conversación arranca desde cero, sin
  persistencia entre sesiones.
- **Loop**: inexistente — es una sola llamada de ida y vuelta, no hay
  ningún ciclo de "pensar, actuar, verificar".
- **Guardrails**: ausentes. No hay validación de las respuestas antes de
  mostrarlas.

## Síntomas y sus causas

- **Lentitud**: causada directamente por pegar 200 páginas de wiki en cada
  prompt. Más tokens de contexto significan más tiempo de procesamiento en
  cada llamada, independientemente de si esas 200 páginas son relevantes
  para la pregunta.
- **"Olvido" dentro de la misma conversación**: es el síntoma clásico de
  *context rot*. Con tanto contenido de bajo valor (wiki completo) compitiendo
  por atención, la información que el empleado mencionó dos mensajes atrás
  queda "enterrada" entre ruido y el modelo pierde el hilo, aunque
  técnicamente esa información sigue en la ventana de contexto.
- **Invención de políticas**: combinación de falta de herramientas (no
  puede verificar una política específica contra una fuente autoritativa,
  solo "recordarla" de un volcado masivo de texto) y falta de guardrails
  (nada valida la respuesta antes de enviarla).

## Cambio de mayor impacto

El cambio de mayor impacto sería reemplazar el volcado estático del wiki
completo por una herramienta de búsqueda que traiga solo las secciones
relevantes a la pregunta actual ("justo a tiempo" en vez de "por si acaso").
Esto ataca directamente la causa raíz de los tres síntomas: reduce el
contexto irrelevante (arregla lentitud y "olvido"), y le da al bot una
forma de anclar sus respuestas a una fuente verificable en vez de inventar
(reduce alucinaciones), incluso antes de tocar memoria o guardrails.
