# Ejercicio 1: Diagnóstico de harness

## Escenario

Una empresa construyó un bot de soporte interno. Así es como está armado:

- Cada vez que un empleado le escribe, el sistema pega **el wiki completo de
  la empresa** (200 páginas) al inicio del prompt, "por si el modelo lo
  necesita".
- El bot no tiene ninguna herramienta: no puede consultar el sistema de
  tickets, ni el calendario, ni buscar en el wiki de forma selectiva.
- Cada conversación empieza desde cero. Si un empleado vuelve al día
  siguiente con una pregunta relacionada, el bot no tiene ningún recuerdo de
  la conversación anterior.
- No hay ninguna validación sobre lo que el bot responde antes de
  mostrárselo al empleado.

Los empleados reportan que el bot es lento, a veces "se le olvida" lo que
preguntaron dos mensajes atrás en la misma conversación, y ocasionalmente
inventa políticas de la empresa que no existen.

## Tu tarea

1. Identifica qué piezas de un harness están presentes en este sistema y
   cuáles faltan por completo (usa las categorías del Módulo 1: contexto,
   herramientas, memoria, loop, guardrails).
2. Para cada síntoma reportado (lentitud, "olvido" dentro de la misma
   conversación, invención de políticas), explica cuál pieza faltante o mal
   diseñada del harness es la causa más probable. Conecta tu respuesta con
   el concepto de *context rot* visto en el módulo.
3. Propón, en un párrafo, el cambio de mayor impacto que harías primero y
   por qué.
