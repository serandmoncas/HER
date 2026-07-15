# Solución — Ejercicio 2: Diagnostica un loop que no poda

Esta es una solución de referencia. Tu razonamiento puede variar en los
detalles siempre que identifique correctamente el mecanismo de context rot
aplicado a un loop.

## Principio que explica los síntomas

Es el mismo mecanismo de *context rot* del Módulo 1, ahora producido por
el propio loop en tiempo real: cada intento, cada hipótesis descartada, y
cada corrida completa de pruebas se acumula sin podarse, hasta que la
señal real (las instrucciones originales del usuario) queda enterrada
entre ruido de bajo valor. El módulo lo describe explícitamente: un loop
mal diseñado que nunca poda resultados intermedios recrea context rot paso
a paso.

## Cambios concretos propuestos

- **Poda/compactación dentro del mismo loop:** una vez que una hipótesis
  se descarta, condensar ese intento a una sola línea de resumen
  ("hipótesis X descartada porque Y") en vez de conservar la salida
  completa de la prueba; lo mismo para las 15 corridas de pruebas — solo
  la última corrida relevante, o un resumen de qué cambió entre corridas,
  necesita quedarse completo.
- **Delegación a subagentes:** cada hipótesis podría investigarse en un
  subagente separado con su propia ventana de contexto, devolviendo solo
  un veredicto corto (confirmada/descartada + por qué) al loop principal,
  en vez de que toda la exploración de cada hipótesis viva en la
  conversación principal.

## Por qué el paralelismo no sería buena idea aquí

Las 6 hipótesis probablemente no son independientes entre sí en el
sentido estricto del módulo: descartar una hipótesis casi siempre informa
cuál probar después (el agente aprende algo de cada intento que ajusta su
siguiente paso). Correrlas en paralelo desde el inicio significaría perder
esa información — algunos subagentes probarían hipótesis que ya se
habrían descartado si hubieran sabido lo que otro subagente encontró
primero.
