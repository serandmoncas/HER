# Ejercicio 3: Diagnostica una memoria mal diseñada

## Escenario

Un equipo lleva 6 meses usando un agente de código con memoria de usuario
habilitada. Con el tiempo, su archivo de memoria personal creció a 4000
palabras: incluye desde la preferencia real del usuario ("prefiero PRs
pequeños") hasta anotaciones que ya no aplican ("en marzo estábamos
migrando de X a Y", proyecto que ya terminó hace 3 meses), pasando por
hechos que cualquiera podría ver leyendo el código ("el proyecto usa
TypeScript"). El usuario nota que el agente ahora tarda más en responder y
a veces menciona contexto de proyectos que ya no existen.

## Tu tarea

1. Clasifica el contenido descrito en al menos tres categorías: memoria
   que vale la pena conservar, memoria obsoleta que debería eliminarse, y
   memoria que nunca debió guardarse.
2. Conecta el síntoma de lentitud y las menciones de proyectos ya
   terminados con el concepto de *context rot* del Módulo 1 — ¿por qué una
   memoria que crece sin poda produce exactamente ese problema?
3. Propón una práctica concreta que el equipo podría adoptar para evitar
   que esto vuelva a pasar.
