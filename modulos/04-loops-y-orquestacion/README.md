# Módulo 4 — Loops y Orquestación

## ¿Qué es un loop de agente?

Todo lo que hemos visto hasta ahora — contexto, herramientas, skills,
memoria — son piezas que un harness pone a disposición del modelo. El
**loop de agente** es el mecanismo que las conecta en el tiempo: observar
el estado actual (incluyendo el resultado del paso anterior), decidir la
siguiente acción, ejecutarla (normalmente invocando una herramienta),
observar su resultado, y repetir hasta que la tarea esté completa o el
agente decida detenerse.

Esta es la diferencia entre un modelo que responde una vez y un agente que
trabaja: un solo llamado al modelo produce una respuesta; un loop permite
que esa respuesta incluya la decisión de investigar más, corregir un error
que acaba de descubrir, o dividir el trabajo en pasos — y que cada uno de
esos pasos informe al siguiente.

## El loop crece: por qué cada paso es más contexto

Cada vuelta del loop añade algo al contexto: el resultado de la
herramienta que se acaba de invocar, la nueva información descubierta, la
decisión que se acaba de tomar. Esto significa que un loop largo, por
diseño, acumula contexto a medida que avanza — exactamente el escenario
que el Módulo 1 anticipó al hablar de compactación y poda: mientras más
pasos toma un agente en una sola conversación, más presión hay sobre el
presupuesto de contexto, y más importa descartar lo que ya cumplió su
propósito.

Un loop mal diseñado — uno que nunca poda resultados intermedios que ya no
aportan, o que reintenta lo mismo sin aprender del intento anterior — no
solo es lento: es exactamente el mecanismo de *context rot* del Módulo 1,
ahora producido por el propio agente en tiempo real, paso a paso, en vez
de por un volcado inicial de información.

## Delegar a un subagente: la promesa del Módulo 1, cumplida

El Módulo 1 mencionó la delegación como una estrategia para manejar el
presupuesto de contexto, y prometió cubrirla en profundidad aquí. La idea
central: en vez de que todos los pasos de una tarea ocurran dentro del
mismo loop y la misma ventana de contexto, el agente puede despachar una
subtarea a un **subagente** — que corre su propio loop, con su propia
ventana de contexto limpia — y esperar solo el resultado final.

Esto cambia la aritmética del contexto de forma importante. Si una
subtarea necesita 20 pasos de exploración para llegar a una respuesta,
esos 20 pasos — y todo el contexto que acumulan — viven en la ventana del
subagente, no en la del agente principal. El loop principal solo ve una
llamada (despachar la subtarea) y un resultado (lo que el subagente
devolvió), sin importar cuántas vueltas de loop le tomó al subagente
llegar ahí. El Módulo 2 ya había establecido cuándo conviene un subagente
frente a una skill; este módulo añade el mecanismo concreto: un subagente
es, en esencia, un loop de agente completo corriendo dentro de otro, con
el único punto de contacto siendo la tarea que se le encarga y el
resultado que devuelve.

## Subagentes en paralelo: cuándo tiene sentido

Cuando varias subtareas son verdaderamente independientes entre sí —
ninguna depende del resultado de otra, ninguna modifica el mismo estado
compartido — un agente puede despachar varios subagentes a la vez en vez
de uno por uno. Esto reduce el tiempo total de la tarea, porque los loops
de los subagentes corren en paralelo en vez de esperar su turno.

Pero la independencia real es una condición estricta, no una suposición
cómoda. Dos subagentes que editan el mismo archivo, o que dependen de que
uno termine antes de que el otro pueda empezar con información correcta,
no son candidatos para paralelismo — coordinarlos mal genera conflictos
que son más caros de resolver que el tiempo que el paralelismo pretendía
ahorrar. La pregunta antes de paralelizar no es "¿esto sería más rápido en
paralelo?" sino "¿estos subagentes pueden trabajar sin pisarse el uno al
otro en absoluto?".

## Cuándo delegar dentro de un loop: marco práctico

El Módulo 2 ya estableció cuándo usar una skill frente a un subagente en
general. Dentro de un loop de agente en marcha, esa misma pregunta se
vuelve más concreta: en cada paso, ¿este trabajo específico debería seguir
ocurriendo en el loop principal, o debería salir de él?

Son buenos candidatos para delegar a un subagente dentro de un loop:
- Un paso que requiere mucha exploración cuyo detalle no es relevante
  después de obtenido el resultado (por ejemplo, buscar en un repositorio
  grande).
- Una revisión del trabajo que el propio loop principal acaba de producir,
  hecha por un subagente sin el sesgo de haberlo escrito — una segunda
  mirada con contexto limpio.
- Fragmentos de trabajo genuinamente independientes que se benefician de
  correr en paralelo, como se describió arriba.

Son malos candidatos: pasos simples que dependen directamente del
contexto inmediato que el loop principal ya tiene — delegarlos solo añade
el costo de coordinar un subagente sin ahorrar nada de contexto ni de
tiempo.

## Para reflexionar / Referencias

- La documentación oficial de Claude Code sobre subagentes y orquestación
  de tareas es la referencia más actualizada para los detalles de
  implementación de despacho paralelo.
- Este módulo cumple la promesa del Módulo 1 de cubrir la delegación en
  profundidad, y construye directamente sobre el marco de decisión
  skill-vs-subagente del Módulo 2.
