# Módulo 3 — Memoria y Persistencia

## ¿Qué es la memoria en un harness?

El contexto de una conversación es efímero: cuando la sesión termina (o se
compacta más allá de cierto punto), esa información desaparece. La
**memoria** es la pieza del harness que resuelve ese problema — información
que persiste más allá de una sola conversación, y que el harness reintroduce
como contexto en sesiones futuras cuando es relevante.

Esto convierte a la memoria en un problema de context engineering en sí
mismo, no en una pieza aparte. El Módulo 1 estableció que el contexto es un
presupuesto finito que hay que gestionar con cuidado; la memoria es,
literalmente, contexto que el harness decide reinyectar en una sesión
nueva. Las mismas preguntas — ¿qué vale la pena incluir?, ¿cuándo se carga?,
¿qué pasa si se acumula sin control? — aplican igual de directo a la
memoria que a cualquier otro contenido del contexto.

## CLAUDE.md: memoria de proyecto cargada siempre

`CLAUDE.md` es el ejemplo más directo de memoria de proyecto en Claude
Code: un archivo, típicamente en la raíz del repositorio, que Claude Code
carga automáticamente al inicio de cada sesión en ese proyecto — no justo a
tiempo, como una skill del Módulo 2, sino siempre, en cada conversación sin
excepción.

Esa diferencia de diseño respecto a las skills no es accidental: una skill
se activa condicionalmente porque su contenido solo aplica cuando la tarea
coincide con su descripción; `CLAUDE.md` se carga siempre porque su
contenido — cómo correr las pruebas, la arquitectura general del proyecto,
las convenciones del equipo — es relevante para prácticamente cualquier
tarea en ese repositorio.

Pero cargar algo siempre tiene un costo mayor que cargarlo
condicionalmente: cada línea de `CLAUDE.md` se paga en el presupuesto de
contexto de cada conversación, la necesite esa tarea puntual o no. Por eso
`CLAUDE.md` exige una disciplina de "contexto mínimo de alta señal" incluso
más estricta que una skill — información que solo aplica a un caso
específico pertenece a una skill, no a `CLAUDE.md`.

## Memoria de usuario: aprender entre sesiones

Además de la memoria de proyecto, un harness puede mantener memoria a nivel
de usuario: preferencias de cómo trabajar, retroalimentación correctiva que
el usuario ya dio antes ("no hagas X", "siempre haz Y así"), y contexto
sobre iniciativas en curso que no vive en el código del proyecto. A
diferencia de `CLAUDE.md`, esta memoria suele ser personal, no se comparte
con el equipo, y se actualiza a partir de las propias conversaciones — el
harness aprende observando, no solo leyendo lo que alguien escribió a mano
de antemano.

Esta distinción entre memoria de proyecto (compartida, sobre el código) y
memoria de usuario (personal, sobre cómo colaborar) es útil porque cada una
responde una pregunta distinta: "¿qué necesita saber cualquiera que trabaje
en este proyecto?" vs. "¿qué necesito saber yo específicamente sobre cómo
esta persona quiere que trabajemos juntos?".

## Qué guardar y qué no: la misma disciplina de contexto mínimo

No todo merece guardarse en memoria. El Módulo 1 describió el escenario de
un bot que pega 200 páginas de wiki en cada conversación "por si acaso" —
una memoria mal disciplinada recrea exactamente ese problema, solo que la
carga ocurre al escribir en vez de al leer.

Un criterio práctico: guarda algo en memoria solo si es sorprendente, no
obvio a partir del código o los archivos del proyecto, o si el usuario lo
corrigió explícitamente. Un hecho que cualquiera podría deducir leyendo el
repositorio no necesita vivir en memoria — ya está disponible justo a
tiempo, sin ocupar presupuesto de contexto en cada sesión. Guardar de más
no es gratis: cada entrada de memoria innecesaria es contexto de bajo valor
compitiendo por atención en cada conversación futura, la misma dinámica de
*context rot* del Módulo 1, ahora aplicada a lo que el harness decide
recordar.

## Memoria como guardrail y riesgo

La memoria tiene una propiedad que el contexto de una sola conversación no
tiene: un error persiste. Si el harness guarda un hecho incorrecto, esa
equivocación se reintroduce en cada sesión futura hasta que alguien la
corrija — un error que en una conversación aislada se olvidaría al
cerrarla, en memoria se vuelve compuesto.

Esto tiene una segunda cara: `CLAUDE.md`, al vivir dentro del repositorio,
se revisa como cualquier otro cambio de código (pull requests, revisión de
pares). La memoria de usuario, en cambio, normalmente no pasa por ese mismo
proceso de revisión — lo que la hace más rápida de actualizar, pero también
un lugar donde información sensible podría terminar guardada sin la misma
supervisión. Diseñar bien qué vive en cada tipo de memoria, y con qué nivel
de revisión, es una primera forma de guardrail — el Módulo 5 retoma este
tema con más profundidad.

## Para reflexionar / Referencias

- La documentación oficial de Claude Code sobre `CLAUDE.md` y sobre
  sistemas de memoria es la referencia más actualizada para los detalles de
  implementación.
- Este módulo construye directamente sobre "contexto mínimo de alta señal"
  y *context rot* (Módulo 1), y sobre la distinción entre carga "justo a
  tiempo" y carga siempre-presente introducida al comparar skills con
  `CLAUDE.md` (Módulo 2).
