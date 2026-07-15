# Solución — Ejercicio 1: Loop principal, subagente o paralelo

Esta es una solución de referencia. Tu razonamiento puede variar en los
detalles siempre que aplique correctamente el marco práctico del módulo.

1. **→ Loop principal.** Es un paso simple, con ubicación ya conocida, sin
   necesidad de exploración — delegarlo solo añadiría coordinación sin
   ahorrar nada.
2. **→ Delegar a subagente.** Requiere mucha exploración (500 archivos)
   cuyo detalle intermedio no es relevante después de encontrar la
   respuesta — candidato clásico de delegación según el módulo.
3. **→ Delegar a subagente.** Es una revisión del trabajo que el propio
   loop acaba de producir, hecha idealmente sin el sesgo de haberlo
   escrito — exactamente el segundo caso descrito en el marco práctico.
4. **→ Delegar en paralelo.** Son tareas genuinamente independientes
   (ningún archivo depende del contenido de los otros) — cumple el
   criterio estricto de independencia para paralelizar.
5. **→ Loop principal.** Depende directamente del contexto inmediato que
   el loop ya tiene (el resultado de dos líneas atrás) — delegarlo
   rompería esa dependencia sin necesidad.
