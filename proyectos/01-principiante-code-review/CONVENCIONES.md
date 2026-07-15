# Convenciones del proyecto — Calculadora de ejemplo

Estas son las convenciones que cualquier cambio de código en este proyecto de
ejemplo debe cumplir. Sirven como referencia externa para la skill de
revisión de código de este proyecto — no están escritas dentro de la skill
misma, para que la skill se mantenga reutilizable en otros proyectos con
otras convenciones.

## Reglas

1. **Toda función pública debe tener docstring.** El docstring debe explicar
   qué hace la función, qué parámetros recibe y qué devuelve.
2. **Nunca usar `eval()` ni `exec()`**, bajo ninguna circunstancia, sin
   importar la fuente del texto a evaluar.
3. **Ninguna credencial, clave de API o secreto puede estar escrito
   directamente en el código.** Deben leerse de variables de entorno.
4. **Toda función que reciba parámetros numéricos usados como divisor debe
   validar explícitamente que el divisor no sea cero** antes de operar, y
   manejar ese caso sin dejar que el programa falle con una excepción no
   controlada.
