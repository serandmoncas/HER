# Solución — Ejercicio 2: Diseña una entrada de CLAUDE.md

Esta es una solución de referencia; el objetivo es el razonamiento sobre
qué pertenece a `CLAUDE.md`, no una redacción exacta.

## Sección propuesta

```markdown
## Comandos comunes
- `npm test` — correr toda la suite de pruebas.
- `npm run build` — compilar el proyecto.
- `npm run test:single -- <archivo>` — correr una sola prueba.
```

## Por qué no copiar docs/arquitectura.md completo

`docs/arquitectura.md` tiene 3000 palabras — copiarlo completo dentro de
`CLAUDE.md` significaría pagar ese costo de contexto en cada conversación
del proyecto, sin importar si la tarea actual tiene algo que ver con la
arquitectura. En vez de eso, `CLAUDE.md` debería solo mencionar que existe
ese archivo y dónde está (por ejemplo, "para una explicación detallada de
la arquitectura, ver `docs/arquitectura.md`") — así el agente puede leerlo
justo a tiempo, cuando una tarea realmente lo necesite, en vez de cargarlo
siempre.

## Qué NO incluir

Tentador pero incorrecto: detalles de una migración o refactor en curso
que va a cambiar pronto (por ejemplo, "estamos migrando el módulo X a Y,
ten cuidado con Z"). Esa información cambia con frecuencia y se vuelve
obsoleta rápido — `CLAUDE.md` se revisa como código pero no se actualiza
con la frecuencia de una conversación normal, así que un dato así de
volátil tiende a quedar desactualizado y confundir en vez de ayudar.
