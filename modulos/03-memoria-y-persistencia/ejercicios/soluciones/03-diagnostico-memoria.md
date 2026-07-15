# Solución — Ejercicio 3: Diagnostica una memoria mal diseñada

Esta es una solución de referencia. Tu razonamiento puede variar en los
detalles siempre que identifique correctamente el mecanismo de *context
rot* aplicado a memoria.

## Clasificación

- **Vale la pena conservar:** "prefiero PRs pequeños" — preferencia
  estable, sigue aplicando.
- **Obsoleta, debería eliminarse:** la nota sobre la migración de marzo
  que ya terminó.
- **Nunca debió guardarse:** "el proyecto usa TypeScript" — visible con
  solo leer el código, no aporta nada nuevo en memoria.

## Conexión con context rot

Es el mismo mecanismo del Módulo 1: cada entrada de memoria, sin importar
si sigue siendo relevante, compite por atención en cada sesión nueva. Con
4000 palabras acumuladas sin poda, la señal real (la preferencia de PRs
pequeños que sí sigue aplicando) queda enterrada entre ruido obsoleto — el
agente tarda más porque hay más contexto que procesar, y menciona
proyectos terminados porque esa información nunca se retiró, solo se
acumuló encima.

## Práctica propuesta

Una revisión periódica de la memoria (por ejemplo, cada cierto número de
semanas, o al cerrar un proyecto o iniciativa) donde se poda explícitamente
lo que ya no aplica — el mismo principio de compactación y poda que el
Módulo 1 describe para el contexto de una conversación, aplicado aquí a la
memoria persistente en vez de a una sola sesión.
