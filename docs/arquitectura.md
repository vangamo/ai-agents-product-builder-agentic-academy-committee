# Arquitectura de la oficina

> Cómo está montado el comité de agentes y por qué. Las decisiones de diseño, con sus alternativas, están en [`docs/adr/`](adr/).

## Componentes

```
                        Persona fundadora
               valida · ejecuta · escribe el contenido
                              │
                              │  /reunion · /validar · /progreso · /estado
                              ▼
        ┌──────────── Sesión principal = Secretaría ────────────┐
        │  facilita, registra y lleva el backlog; no opina       │
        └──────┬──────────────────────────────────┬─────────────┘
               │ lanza en paralelo                │ lee y escribe
               ▼                                  ▼
   Subagentes del comité (.claude/agents/)   empresa/  · estado en Markdown
   ─ direccion-estrategica (preside)          contexto · protocolo
   ─ contenidos     ─ marketing               backlog · decisiones
   ─ ventas-comunidad                         estado · metricas
   ─ finanzas-legal ─ producto-tecnologia     areas/ · reuniones/
   ─ operaciones (veto de capacidad)
               │                                  ▲
               └──── escriben sus rondas y ───────┘
                     su documento de área
```

| Componente | Dónde | Responsabilidad |
|---|---|---|
| Persona fundadora | — | Decide, valida, ejecuta en el mundo real y escribe el contenido |
| Secretaría | sesión principal de Claude Code (`CLAUDE.md`) | Convoca, lanza a los agentes, registra resultados y mantiene el estado. No opina |
| Comité | `.claude/agents/*.md` | Siete roles con mandato, intereses y métricas propias. Proponen, no ejecutan |
| Comandos | `.claude/skills/*/SKILL.md` | Procedimientos repetibles: reunión, validación, progreso y estado |
| Estado | `empresa/` | Memoria compartida y auditable del comité |

## Los roles y sus tensiones

Cada rol defiende un interés que choca de forma natural con los de otros. Esa fricción es el producto: obliga a justificar.

| Rol | Defiende | Choca sobre todo con |
|---|---|---|
| `direccion-estrategica` | Foco y diferenciación | marketing (todos los canales), producto (construir de más) |
| `contenidos` | Calidad pedagógica | marketing (frecuencia), ventas (prometer lo que no existe) |
| `marketing` | Distribución y constancia | contenidos, operaciones, finanzas (herramientas) |
| `ventas-comunidad` | Validar con personas reales | dirección (foco), finanzas (gratis frente a cobrar) |
| `finanzas-legal` | Caja y cumplimiento | producto (servicios de pago), ventas (cuándo cobrar) |
| `producto-tecnologia` | Simplicidad, seguridad y dogfooding | finanzas (coste), operaciones (horas) |
| `operaciones` | Sostenibilidad | todas: tiene el veto de capacidad |

Ningún rol tiene terminal (`Bash`): leen, buscan en la web y escriben en sus propios ficheros.

## Flujo de una reunión

```
Convocatoria ─► Ronda 1 ─────────► Ronda 2 ───────────► [Ronda 3] ─────────► Acta ──────► Registro ──► /validar
(Secretaría)    propuestas,        revisión cruzada:     solo si quedan      (Dirección   (Secretaría)  (persona
                en paralelo        👍 · 🤔 · ⛔ con       objeciones          estratégica)               fundadora)
                y a ciegas         alternativa           bloqueantes
```

1. **Convocatoria.** La Secretaría fija objetivo, puntos, quién lidera cada uno, asistentes y el contexto que todos deben conocer.
2. **Ronda 1.** Cada asistente propone sin leer a los demás. Así se evita que la primera propuesta ancle al resto.
3. **Ronda 2.** Cada asistente lee todas las propuestas y se posiciona. Una objeción bloqueante solo vale por motivos tasados y siempre trae una alternativa. Operaciones añade el balance de capacidad.
4. **Ronda 3** (opcional, una como máximo). Solo los implicados en bloqueos vivos.
5. **Acta.** Dirección estratégica consolida acuerdos, disensos, decisiones para la persona fundadora y tareas.
6. **Registro y validación.** La Secretaría pasa tareas y decisiones al backlog como propuestas, y la persona fundadora las aprueba, ajusta o descarta.

Formato **rápido** para reuniones semanales y temas acotados: ronda 1 → acta.

## Modelo de datos

Todo el estado vive en Markdown con un formato fijo, para que lo lean igual las personas, los agentes y las herramientas (ADR-0002).

**Tarea** (`backlog.md`): `T-NNN`, área responsable, estimación (≤ 4 h), prioridad (P1–P3), semana, dependencias, criterio de hecho y motivo.

```
🟡 Propuesta ──/validar──► ✅ Aprobada ──/progreso──► 🔵 En curso ──/progreso──► ✔️ Hecha
      │                        │
      └──────────/validar──────┴──────────────► ❌ Descartada o aparcada (con motivo)
```

**Decisión** (`decisiones.md`): `D-NNN`, pregunta cerrada, contexto, opciones, recomendación del comité, quién discrepa, coste de no decidir y tareas afectadas.

```
🟡 Pendiente ──/validar──► ✅ Tomada (fecha y opción elegida)
```

Una decisión tomada solo se cambia con otra decisión que diga a cuál sustituye.

**Semana:** S1 es la semana del lunes 2026-10-05. Las semanas van de lunes a domingo.

## Decisiones de diseño

| ADR | Decisión |
|---|---|
| [0001](adr/0001-comite-de-subagentes.md) | Un comité de subagentes de Claude Code en lugar de un único prompt o un framework de agentes |
| [0002](adr/0002-estado-en-markdown.md) | El estado compartido vive en ficheros Markdown versionados |
| [0003](adr/0003-protocolo-de-consentimiento.md) | Las reuniones siguen un protocolo de consentimiento con rondas a ciegas |
