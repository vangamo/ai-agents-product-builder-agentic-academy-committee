---
name: consulta
description: Pregunta a un rol concreto del comité de Product Builder Academy fuera de una reunión (p. ej., «pregúntale a finanzas-legal si necesito alta para aceptar donaciones»). Deja la respuesta por escrito y registra como propuestas las tareas o decisiones que salgan.
argument-hint: <rol> <pregunta>
---

# Consulta a un rol

Actúas como **Secretaría del comité**. Entrada: `$ARGUMENTS`

1. **Identifica el rol** (primer término o el que mejor encaje con la pregunta: tabla «Equipo» de `CLAUDE.md`). Si la pregunta cruza varias áreas o pide decidir algo con consecuencias para varias, sugiere `/reunion <tema> --rapida` en su lugar.
2. **Crea el fichero de respuesta** con el nombre `empresa/consultas/AAAA-MM-DD-<rol>-<slug>.md` (no lo escribas tú: lo escribe el agente).
3. **Lanza al rol** (`subagent_type` = nombre del rol) con este encargo:

   > CONSULTA de la persona fundadora: «<pregunta literal>». Lee lo que necesites según el protocolo §8 y responde en `<fichero>` (máx. 60 líneas, protocolo §9) con: **Respuesta** (directa, en 3–5 líneas), **Fundamento** (fuentes con fecha si hay datos que cambian; ⚖️ si aplica), **Opciones** (si hay más de una vía) y, si procede, **Tareas propuestas** (formato §5, con `T-?`) y **Decisiones propuestas** (formato §6, con `D-?`). Devuelve un resumen de ≤ 6 líneas.

4. **Registra:** si la respuesta trae tareas o decisiones, pásalas como 🟡 Propuestas y 🟡 Pendientes con `- Origen: consultas/<fichero>`. No se aprueba nada sin `/validar`.
5. **Responde** a la persona con el resumen del rol (sin suavizarlo), el enlace al fichero y, si hay propuestas, la sugerencia de `/validar`.
