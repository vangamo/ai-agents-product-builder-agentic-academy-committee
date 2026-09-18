---
name: validar
description: Revisa con la persona fundadora de Product Builder Academy las decisiones pendientes y las tareas propuestas por el comité, y registra qué se aprueba, se modifica, se aparca o se descarta.
argument-hint: [IDs concretos, opcional]
disable-model-invocation: true
---

# Validación de la persona fundadora

Actúas como **Secretaría del comité**. Filtro opcional: `$ARGUMENTS`

## 1. Preparar

Lee `empresa/decisiones.md` (🟡 Pendientes), `empresa/backlog.md` (🟡 Propuestas) y `empresa/estado.md`; consulta el acta de origen si necesitas contexto. Si no hay nada pendiente, dilo y termina.

## 2. Decisiones primero

Las tareas pueden depender de ellas. Para cada decisión pendiente (hasta 4 por llamada) usa AskUserQuestion:

- Pregunta: la decisión en forma cerrada; en `header`, su ID (p. ej., `D-008`).
- Opciones: las del acta, con la recomendada por el comité en primer lugar y la etiqueta «(Recomendada)»; en la descripción, la consecuencia principal y si alguna área discrepa.
- Si la respuesta llega por «Other», interprétala; si no queda clara, vuelve a preguntar.

## 3. Tareas

1. Muestra una tabla compacta de las propuestas, agrupadas por semana: ID · título · área · h · prioridad · depende de, con el total de horas de cada semana (propuestas + ya aprobadas) frente a 16 h. Señala las tareas que dejan de tener sentido por las decisiones recién tomadas y propón descartarlas.
2. Pregunta con AskUserQuestion: «Aprobar todas» · «Aprobar P1 y P2 (aparcar P3)» · «Revisar una a una». La persona puede responder en texto libre (p. ej., «todas menos T-004; T-007 a 2 h; T-010 a S3»).
3. Si elige revisar una a una: AskUserQuestion con `multiSelect` (hasta 4 tareas por pregunta y 4 preguntas por llamada). Las marcadas se aprueban; de las no marcadas, pregunta si se aparcan o se descartan.

## 4. Registrar

- **Decisiones** → ✅ Tomadas, con `- Fecha: AAAA-MM-DD · Elegida: <opción>` (y la recomendación original si se eligió otra). Si la decisión cambia un hecho de `empresa/contexto.md`, actualízalo y dilo.
- **Tareas aprobadas** → ✅ Aprobadas, con `- Validada: AAAA-MM-DD` y los cambios pedidos ya aplicados (estimación, semana…).
- **Aparcadas o descartadas** → ❌, con `- Motivo: …` (pregunta el motivo solo si no es obvio).
- **Capacidad:** si las aprobadas de una semana suman más de 16 h, avisa y propón qué mover (P3 primero); no lo muevas sin confirmación.
- Actualiza `empresa/estado.md`: plan de la semana actual (aprobadas de esta semana, en orden sugerido por dependencias y prioridad), pendiente de validar y decisiones recientes.
- Si en «Salud del comité» está la fila de la reunión de origen, completa «Elegida ≠ recomendada» con el número de decisiones en las que se eligió otra opción.

## 5. Cerrar

Resumen breve: decisiones tomadas, horas aprobadas por semana y las 3 primeras tareas por las que empezar.
