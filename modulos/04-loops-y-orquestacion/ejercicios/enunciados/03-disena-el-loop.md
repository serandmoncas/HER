# Ejercicio 3: Diseña el loop de una tarea

## Escenario

Un agente recibe la tarea: "Actualiza la versión de una dependencia en 8
microservicios distintos del monorepo, corriendo las pruebas de cada uno
después de actualizar, y repórtame cuáles fallaron."

## Tu tarea

1. Describe cómo estructurarías esta tarea: ¿qué pasos ocurren en el loop
   principal, y qué pasos delegarías a subagentes? Justifica con el marco
   práctico del módulo.
2. ¿Deberían los 8 microservicios procesarse en paralelo o en secuencia?
   Justifica tu respuesta con el criterio de independencia real visto en
   el módulo.
3. ¿Qué información necesita el loop principal recibir de vuelta de cada
   subagente para poder generar el reporte final, y qué NO necesita
   recibir?
