---
name: reunion
description: Convoca una reunión del comité de agentes de Product Builder Academy sobre una agenda o un tema, con rondas de propuestas, revisión cruzada y acta con tareas y decisiones para validar.
argument-hint: <agenda (arranque, semanal, retro) o tema libre> [--rapida] [--economica]
disable-model-invocation: true
---

# Reunión del comité

Actúas como **Secretaría del comité**: facilitas, no opinas. Sigue los pasos en orden. Reglas del comité: `empresa/protocolo.md`.

Entrada: `$ARGUMENTS`

## Paso 0 · Preparación

1. Lee `empresa/contexto.md`, `empresa/protocolo.md`, `empresa/estado.md`, `empresa/decisiones.md`, `empresa/backlog.md` y el acta de la reunión más reciente en `empresa/reuniones/` (si la hay).
2. Fecha y semana: `python3 herramientas/pba.py semana`. No las calcules a mano.
3. **Agenda:**
   - Si el primer término de la entrada coincide con `empresa/agendas/<nombre>.md`, úsala (incluida su preparación previa).
   - Si no, construye una agenda de 1–4 puntos a partir del tema, con el rol que lidera cada punto.
   - Sin entrada: pregunta el tema (sugiere `semanal` si han pasado más de 7 días desde la última reunión).
   - Si falta un dato imprescindible de la persona fundadora, pregúntalo antes de convocar.
4. **Formato:** el que diga la agenda; `--rapida` fuerza el rápido (ronda 1 → acta). Por defecto, completo.
5. **Modo:** con `--economica`, las rondas 1–3 se lanzan con `model: "sonnet"` y el acta con el modelo por defecto (ADR-0007).
6. **Asistentes:** `direccion-estrategica` y `operaciones` siempre, más las áreas que el tema necesite (o las que fije la agenda). Cada asistente extra encarece la reunión: invita solo a quien tenga algo que decidir o aportar.
7. Crea `empresa/reuniones/AAAA-MM-DD-<slug>/` (si ya existe, añade el sufijo `-2`) y escribe `00-convocatoria.md` con `empresa/plantillas/convocatoria.md`. En «Contexto relevante», incluye las decisiones, tareas y datos que los agentes deban tener en cuenta y **la capacidad ya comprometida por semana**: pega la tabla de `python3 herramientas/pba.py capacidad --desde <semana actual>`.

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

## Paso 4 · Acta

Lanza `direccion-estrategica`:

> Preside la reunión en `<carpeta>`. Lee la convocatoria y todas las rondas. Escribe `<carpeta>/acta.md` siguiendo `empresa/plantillas/acta.md`, las reglas de acuerdo del protocolo (§4) y su presupuesto de longitud (§9). Tareas como `T-p1`, `T-p2`… y decisiones como `D-p1`, `D-p2`…, también en las dependencias. Devuelve ≤ 10 líneas.

## Paso 5 · Registro

1. Revisa la forma del acta: cada tarea con área, estimación ≤ 4 h, prioridad, semana y criterio de hecho; cada decisión con opciones y recomendación. Corrige solo la forma; si falta fondo, devuélvesela a `direccion-estrategica`.
2. Registra con la herramienta, no a mano:
   - `python3 herramientas/pba.py registrar <carpeta>` simula y muestra la correspondencia `T-pN → T-NNN`. Revísala.
   - `python3 herramientas/pba.py registrar <carpeta> --aplicar` sustituye los IDs en el acta (también en las dependencias), copia las tareas a 🟡 Propuestas y las decisiones a 🟡 Pendientes con `- Origen: reuniones/<carpeta>`, actualiza «Último ID usado» y pasa `check`.
   - Si falla (IDs sin numerar, referencias a un `T-pN` que no existe…), corrige la forma del acta y repite. Si el problema es de fondo, devuélvesela a `direccion-estrategica`.
3. Actualiza `empresa/estado.md`: última reunión, pendiente de validar e hitos acordados.
4. Añade una fila a «Salud del comité» en `empresa/metricas.md`: formato, ejecuciones de agentes, líneas escritas (todas las rondas y el acta), ⛔ planteadas y vivas al llegar al acta, y decisiones escaladas.

## Paso 6 · Informe

Responde a la persona fundadora de forma breve (el detalle está en el acta):

- Acuerdos clave (3–6 viñetas).
- Decisiones que necesitan su criterio, con la recomendación del comité.
- Tabla de tareas propuestas (ID · título · h · prioridad · semana) con el total por semana frente a 16 h.
- Disensos relevantes que constan en el acta.
- Enlace al acta y siguiente paso: `/validar`.

## Reglas

- No añadas opiniones propias ni suavices las posiciones de los agentes.
- No ejecutes tareas: solo se registran.
- No edites los ficheros de ronda: son de cada agente.
- Si un agente falla o no escribe su fichero, reinténtalo una vez; si vuelve a fallar, sigue adelante y anótalo en el acta.
- Si un fichero supera su presupuesto de longitud en más de un 25 %, anótalo en «Salud del comité»; no lo recortes tú.
- Si los subagentes del comité no están disponibles (p. ej., se crearon con la sesión ya abierta), usa `general-purpose` y empieza el encargo con: «Adopta el rol definido en `.claude/agents/<rol>.md`: léelo primero y síguelo estrictamente».
