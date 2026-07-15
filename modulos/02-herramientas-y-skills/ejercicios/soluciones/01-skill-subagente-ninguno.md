# Solución — Ejercicio 1: Skill, subagente o ninguno

Esta es una solución de referencia. Tu razonamiento puede variar en los
detalles siempre que aplique correctamente el marco de decisión del
módulo.

1. **→ Subagente.** Es una tarea de exploración pesada (40 archivos) cuyo
   proceso intermedio (leer cada archivo, razonar sobre cada uno)
   inundaría la conversación principal; solo el resultado destilado (los
   hallazgos) importa de vuelta.
2. **→ Ninguno.** Es puntual, liviana, no se repite — una instrucción
   directa basta, no justifica el costo de mantener una skill ni de
   aislar contexto en un subagente.
3. **→ Skill.** Es un procedimiento específico y repetible que se necesita
   cada vez que ocurre cierta condición (terminar de escribir código) —
   exactamente el patrón de "instrucciones que solo hace falta cargar
   cuando la tarea coincide". El número de pasos (15) no cambia esto: una
   skill puede contener un procedimiento largo, lo que importa es que es
   conocimiento a aplicar, no trabajo pesado a aislar.
4. **→ Subagente** (posiblemente varios, uno por página o en lotes). El
   volumen de contenido intermedio (50 páginas completas) ensuciaría el
   contexto principal; solo el resumen agregado debe volver a la
   conversación.
5. **→ Ninguno.** La información ya está en el contexto actual; no hace
   falta ni instrucciones nuevas ni aislar trabajo en otro lado, es una
   respuesta directa sobre algo que ya se sabe.
