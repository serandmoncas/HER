# Solución — Ejercicio 3: Diseña el loop de una tarea

Esta es una solución de referencia; el objetivo es el razonamiento sobre
qué delegar y cuándo paralelizar, no una arquitectura exacta.

## Qué va en el loop principal vs. subagentes

Loop principal: coordinar la lista de los 8 microservicios, despachar el
trabajo, y ensamblar el reporte final. Delegado a subagentes: el trabajo
de cada microservicio individual (actualizar la dependencia, correr sus
pruebas) — es un paso de exploración/ejecución cuyo detalle intermedio
(logs completos de la corrida de pruebas) no necesita vivir en el loop
principal, solo el resultado.

## Paralelo o secuencial

En paralelo, si los 8 microservicios son realmente independientes entre sí
(no comparten código, no hay dependencias de build entre ellos) — que es
la premisa típica de microservicios bien separados. Si compartieran
alguna dependencia interna entre sí, habría que verificar esa
independencia antes de asumir que el paralelismo es seguro.

## Qué información debe volver al loop principal

Necesita: el nombre del microservicio, si la actualización se aplicó con
éxito, y si las pruebas pasaron o fallaron (y de fallar, un resumen corto
del fallo). NO necesita: la salida completa de cada corrida de pruebas, ni
los pasos intermedios que cada subagente tomó para hacer la actualización
— eso es exactamente el tipo de detalle que debería quedarse en la
ventana de contexto del subagente, no propagarse al loop principal.
