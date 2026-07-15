# Ejercicio 2: Diagnostica un loop que no poda

## Escenario

Un agente está resolviendo un bug complejo. En su intento de
diagnosticarlo, ejecuta la suite de pruebas completa 15 veces (cada vez
con salida de cientos de líneas), lee 40 archivos distintos buscando la
causa, y prueba 6 hipótesis distintas antes de encontrar la correcta —
pero nunca descarta la salida de los intentos anteriores ni de las
hipótesis descartadas; todo permanece en el contexto de la misma
conversación. Para cuando encuentra el bug real, el agente empieza a
"olvidar" instrucciones que el usuario dio al principio de la tarea, y
tarda notablemente más en cada paso nuevo.

## Tu tarea

1. Identifica qué principio de este módulo (y del Módulo 1) explica los
   síntomas descritos.
2. Propón al menos dos cambios concretos al diseño del loop de este
   agente para evitar que esto vuelva a pasar — uno relacionado con
   poda/compactación dentro del mismo loop, y otro relacionado con
   delegación a subagentes.
3. Explica por qué correr las 6 hipótesis como 6 subagentes en paralelo
   NO sería una buena idea en este caso.
