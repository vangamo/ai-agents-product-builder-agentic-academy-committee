---
name: reunion
description: Convoca una reunión del comité de agentes de Product Builder Academy sobre una agenda o un tema, con rondas de propuestas, revisión cruzada y acta con tareas y decisiones para validar.
argument-hint: <agenda (arranque, semanal…) o tema libre> [--rapida] [--economica]
disable-model-invocation: true
---

# Reunión del comité

Actúas como **Secretaría del comité**: facilitas, no opinas. Sigue los pasos en orden. Reglas del comité: `empresa/protocolo.md`.

Entrada: `$ARGUMENTS`

## Paso 0 · Preparación

1. Lee `empresa/contexto.md`, `empresa/protocolo.md`, `empresa/estado.md`, `empresa/decisiones.md`, `empresa/backlog.md` y el acta de la reunión más reciente en `empresa/reuniones/` (si la hay).
2. Calcula la semana actual con la fórmula del protocolo §7.
3. **Agenda:**
   - Si el primer término de la entrada coincide con `empresa/agendas/<nombre>.md`, úsala (incluida su preparación previa).
   - Si no, construye una agenda de 1–4 puntos a partir del tema, con el rol que lidera cada punto.
   - Sin entrada: pregunta el tema (sugiere `semanal` si han pasado más de 7 días desde la última reunión).
   - Si falta un dato imprescindible de la persona fundadora, pregúntalo antes de convocar.
4. **Formato:** el que diga la agenda; `--rapida` fuerza el rápido (ronda 1 → acta). Por defecto, completo.
5. **Modo:** con `--economica`, las rondas 1–3 se lanzan con `model: "sonnet"` y el acta con el modelo por defecto (ADR-0007).
6. **Asistentes:** `direccion-estrategica` y `operaciones` siempre, más las áreas que el tema necesite (o las que fije la agenda). Cada asistente extra encarece la reunión: invita solo a quien tenga algo que decidir o aportar.
7. Crea `empresa/reuniones/AAAA-MM-DD-<slug>/` (si ya existe, añade el sufijo `-2`) y escribe `00-convocatoria.md` con `empresa/plantillas/convocatoria.md`. En «Contexto relevante», incluye las decisiones, tareas y datos que los agentes deban tener en cuenta y **la capacidad ya comprometida por semana** (horas de las tareas aprobadas y en curso).

## Paso 1 · Ronda de propuestas

Lanza a **todos los asistentes en un solo mensaje** (llamadas a Agent en paralelo, `subagent_type` = nombre del rol). Encargo:

> Reunión en `<carpeta>`. Lee `00-convocatoria.md`. RONDA 1 (propuestas): escribe tu aportación en `<carpeta>/ronda1-<rol>.md` siguiendo `empresa/plantillas/ronda1.md` y el presupuesto de longitud del protocolo §9. Desarrolla a fondo los puntos que lideras; en el resto, aporta solo lo que afecte a tu área. No leas las aportaciones de otros roles. Devuelve un resumen de ≤ 8 líneas.

Espera a que terminen todos y comprueba que cada fichero existe.

## Paso 2 · Revisión cruzada (solo formato completo)

Lanza de nuevo a todos en paralelo:

> Reunión en `<carpeta>`. RONDA 2 (revisión cruzada): lee `00-convocatoria.md` y **todos** los `ronda1-*.md`. Escribe `<carpeta>/ronda2-<rol>.md` siguiendo `empresa/plantillas/ronda2.md` y el presupuesto del protocolo §9. Posiciónate (👍/🤔/⛔) sobre las propuestas de otras áreas que afecten a tu dominio o al plan; cada ⛔ con un motivo admitido por el protocolo (§4) y una alternativa. Devuelve ≤ 8 líneas, empezando por tus ⛔.

A `operaciones` añádele: «Incluye el balance de capacidad por semana, partiendo de la capacidad ya comprometida de la convocatoria, y la propuesta de recorte si no cabe».

## Paso 3 · Resolución (opcional, una como máximo)

Si quedan ⛔ cuya alternativa no ha aceptado el área proponente en su ronda 2, lanza solo a los roles implicados (quien objeta y quien propone):

> Reunión en `<carpeta>`. RONDA 3 (resolución): lee las rondas 1 y 2. Para cada objeción bloqueante en la que estés implicado, escribe en `<carpeta>/ronda3-<rol>.md` (plantilla `empresa/plantillas/ronda3.md`) si aceptas la alternativa, propones un compromiso o mantienes tu posición, y por qué. Devuelve ≤ 5 líneas.

Lo que siga bloqueado lo resuelve el acta (desempate) o se escala a la persona fundadora.
