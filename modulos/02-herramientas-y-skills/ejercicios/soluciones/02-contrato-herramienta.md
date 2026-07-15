# Solución — Ejercicio 2: Diseña el contrato de una herramienta

Esta es una solución de referencia; el objetivo es el razonamiento sobre
superficie mínima, no un esquema exacto (que puede variar en detalles).

## Contrato propuesto

- **Nombre:** `obtener_precio_accion`
- **Descripción:** "Devuelve el precio actual de una acción bursátil dado
  su símbolo (ticker). Úsala cuando el usuario pregunte por el precio
  actual o reciente de una acción específica."
- **Parámetros:** `ticker` (string, requerido) — el símbolo bursátil, por
  ejemplo "AAPL".

## Por qué la descripción es contexto

La descripción es lo que el modelo lee para decidir, sin haber leído el
código de la herramienta, si esta es la herramienta correcta para la tarea
actual. Si es demasiado vaga (por ejemplo, "Obtiene datos financieros"), el
modelo puede no reconocer que aplica cuando sí debería, o confundirla con
otra herramienta de datos financieros parecida. Si es demasiado amplia o
imprecisa (por ejemplo, sugiriendo que también sirve para históricos o
para otras clases de activos que no maneja), el modelo la va a invocar en
casos donde no corresponde y va a fallar o devolver resultados incorrectos
— el mismo problema de superficie difusa que el módulo describe para
skills mal descritas.

## Parámetro a NO incluir

Un parámetro tentador pero incorrecto sería una "moneda de conversión" o
un "rango de fechas históricas". Aunque parezca útil, la herramienta se
definió específicamente para el precio *actual* — añadir ese parámetro
amplía la superficie de la herramienta más allá de su propósito único, lo
que la hace más difícil de describir con precisión y aumenta la
probabilidad de que el modelo la use mal. Si se necesita esa
funcionalidad, debería ser una herramienta separada, con su propia
descripción específica.
