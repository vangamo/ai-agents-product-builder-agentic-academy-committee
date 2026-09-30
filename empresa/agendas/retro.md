# Agenda · Retrospectiva del comité

- **Formato:** completo si hay cambios de proceso que discutir; rápido si solo se revisan datos.
- **Cuándo:** cada 8 semanas (la primera, al cierre de S8) o cuando la persona fundadora note que el comité no le ayuda.
- **Asistentes:** direccion-estrategica, operaciones y las áreas cuyas métricas o reglas se revisen (máximo 5).
- **Preparación (Secretaría):** pega en la convocatoria la tabla «Salud del comité» de `empresa/metricas.md`, la tabla de horas estimadas frente a reales y la salida de `python3 herramientas/pba.py check`.

## Objetivo

Revisar si el comité, el protocolo y las herramientas ayudan a la persona fundadora o solo le cuestan tiempo, y proponer cambios concretos al sistema (no al negocio).

## Puntos

1. **Coste** — lidera: operaciones
   - Horas de la persona fundadora en reuniones y validación frente al total. ¿Supera el 10 %?
   - Ejecuciones de agentes y líneas por reunión. ¿Se respetan los presupuestos del protocolo §9?
2. **Calidad de las decisiones** — lidera: direccion-estrategica
   - Decisiones escaladas y cuántas se eligieron en contra de la recomendación. Si casi nunca, ¿se escala de más? Si a menudo, ¿el comité no entiende las prioridades de la persona fundadora?
   - Decisiones tomadas que hubo que revertir y por qué.
   - ¿Las rondas de los distintos roles aportan puntos de vista distintos, o dicen lo mismo? (ADR-0001)
3. **Estimaciones** — lidera: operaciones
   - Desviación media de horas reales frente a estimadas, por área. Ajustes a las referencias de coste.
4. **Reglas y herramientas** — lidera: direccion-estrategica · aportan: las áreas afectadas
   - Bloqueos del hook de guardia: ¿errores evitados o fricción innecesaria? (ADR-0005)
   - Fugas detectadas por `pba.py privacidad`. (ADR-0006)
   - Escenarios de `evals/` que fallan.

## Salidas esperadas

- Acta con los cambios propuestos al protocolo, a los roles o a las herramientas, cada uno como decisión para la persona fundadora (el protocolo lo cambia ella).
- Referencias de coste actualizadas (operaciones, en su documento de área).
- Escenarios de evaluación nuevos si se ha detectado un fallo que no estaba cubierto.
