# Módulo 1 — Fundamentos + Context Engineering

## ¿Qué es un harness?

Un **agente IA = modelo + harness**. El modelo es el motor de razonamiento
crudo — recibe texto, produce texto. El harness es todo lo que lo rodea y lo
convierte en algo capaz de hacer trabajo real: el system prompt, las
herramientas que puede invocar, la memoria que se le inyecta, el bucle que
decide cuándo volver a llamar al modelo y con qué, y los guardrails que
evitan que se salga de control.

Es la misma relación que hay entre el motor de un auto de carreras y el
chasis, la suspensión y los frenos que lo rodean. Un motor de Fórmula 1
montado en un chasis de kart pierde contra un motor mediocre en un chasis
bien afinado. El modelo importa, pero el harness es lo que determina si esa
capacidad se traduce en resultados.

## Por qué el harness importa más que el modelo

Sam Altman llamó a este año "el año de los agentes IA". Pero el salto real
que estamos viendo en productos de agentes no viene principalmente de
modelos más grandes — viene de mejores harnesses alrededor de modelos que ya
existían. Jensen Huang, en su presentación en el GTC, planteó una idea
similar: el futuro de la IA no está solo en los modelos aislados, sino en
los sistemas que los envuelven.

La evidencia práctica está a la vista: herramientas como Claude Code, Cursor
u otros agentes de código usan modelos subyacentes muy similares (a veces el
mismo modelo, literalmente), y aun así su desempeño en tareas reales puede
ser radicalmente distinto. La diferencia no está en el modelo — está en cómo
cada herramienta gestiona el contexto, qué herramientas expone, cómo
recuerda información entre pasos, y cómo decide su propio siguiente paso.
Ese conjunto de decisiones de diseño es Harness Engineering.

## Context Engineering: la disciplina central

**Contexto** es todo lo que el modelo puede "ver" en el momento de generar
una respuesta: el system prompt, las definiciones de las herramientas
disponibles, el historial de la conversación, cualquier dato inyectado
(archivos de memoria, resultados de búsquedas, contenido de archivos) y el
turno actual del usuario.

La idea central de Context Engineering es que **el contexto no es gratis**.
La atención del modelo es un recurso finito: a medida que la ventana de
contexto se llena de tokens de bajo valor (resultados de herramientas
verbosos, historial irrelevante, instrucciones redundantes), esos tokens
compiten por atención con la información que sí importa. El resultado es lo
que en la práctica se conoce como *context rot*: el modelo pierde el hilo,
ignora instrucciones tempranas, o alucina detalles porque la señal relevante
quedó enterrada entre ruido.

Anthropic ha documentado extensamente, en su trabajo de ingeniería sobre
agentes, que gestionar bien esta ventana de contexto tiene más impacto en el
desempeño real de un agente que casi cualquier otro factor, incluyendo el
tamaño o la capacidad bruta del modelo.

Esto marca una diferencia importante frente al viejo "prompt engineering".
Prompt engineering optimiza un texto estático: un prompt bien pulido que se
reutiliza tal cual. Context Engineering trata el contexto como un
**presupuesto dinámico** que se gestiona activamente a lo largo de toda una
tarea o sesión — decidiendo en cada paso qué información entra, qué se
resume, qué se descarta y qué se recupera justo a tiempo en vez de cargarla
por adelantado.

El principio práctico que se deriva de esto es **contexto mínimo de alta
señal**: incluir solo lo que la tarea actual necesita, y preferir recuperar
información justo cuando se necesita ("just in time") en vez de volcar todo
el conocimiento posible al inicio "por si acaso".

## La ventana de contexto y la compactación

La ventana de contexto es un presupuesto finito compartido entre el system
prompt, las definiciones de herramientas, el historial de la conversación y
el espacio que necesita el modelo para responder. A medida que ese
presupuesto se agota:

- Sube el costo y la latencia de cada llamada al modelo.
- La información relevante corre más riesgo de quedar "enterrada en el
  medio" y ser ignorada.
- Eventualmente se topa con el límite físico de la ventana.

Para manejar esto, un harness bien diseñado usa varias estrategias:

- **Compactación**: condensar turnos antiguos de la conversación en un
  resumen, conservando las decisiones y hechos importantes y descartando el
  detalle que ya no aporta.
- **Poda**: eliminar resultados de herramientas que ya cumplieron su
  propósito y no se van a volver a necesitar.
- **Delegación**: en vez de acumular todo en una sola conversación,
  encargarle una subtarea a un subagente con su propia ventana de contexto
  limpia, y traer de vuelta solo el resultado destilado — no el proceso
  completo que le costó llegar ahí. Este patrón se cubre en profundidad en
  el Módulo 4.

Claude Code es un ejemplo concreto de estos principios en acción: compacta
automáticamente el historial de la conversación a medida que se acerca al
límite de contexto, y su sistema de *skills* — instrucciones que se cargan
solo cuando son relevantes para la tarea actual, en vez de estar siempre
presentes en el system prompt — es en sí mismo una técnica de gestión de
contexto, no solo una forma de organizar funcionalidad.

## Las piezas de un harness (mapa del resto del currículo)

Context Engineering es el principio transversal; los siguientes módulos
cubren las piezas concretas de un harness que lo aplican:

- **Herramientas y Skills** (Módulo 2) — qué puede *hacer* el agente, y
  cuándo esa capacidad debe vivir en una skill vs. en un subagente.
- **Memoria y Persistencia** (Módulo 3) — qué *recuerda* el agente entre
  sesiones, y cómo eso se inyecta como contexto sin saturarlo.
- **Loops y Orquestación** (Módulo 4) — cómo *decide* el agente sus propios
  pasos, incluyendo cuándo delegar trabajo a un subagente con contexto
  limpio.
- **Evaluación y Guardrails** (Módulo 5) — cómo *sabes* si el harness
  funciona, y cómo evitas que se salga de control.

## Para reflexionar / Referencias

- Video: [Cómo Funciona un Arnés de Agentes IA (Harness Engineering
  Explicado)](https://www.youtube.com/watch?v=z3KF8OaLCG4) — Benjamín
  Cordero. Punto de partida de este currículo.
- Los escritos de ingeniería de Anthropic sobre gestión de contexto en
  agentes (referenciados en el video anterior) documentan con más
  profundidad por qué el contexto es, en la práctica, el factor de mayor
  impacto en el desempeño de un agente.
- Comentarios públicos de Sam Altman y Jensen Huang sobre el rol de los
  sistemas ("harnesses") por encima del modelo aislado, también citados en
  el video de origen.
