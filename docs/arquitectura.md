# Arquitectura de la oficina

> Cómo está montado el comité de agentes y por qué. Las decisiones de diseño, con sus alternativas, están en [`docs/adr/`](adr/).

## Componentes

```
                        Persona fundadora
               valida · ejecuta · escribe el contenido
                              │
                              │  /reunion · /validar · /progreso · /estado · /consulta
                              ▼
        ┌──────────── Sesión principal = Secretaría ────────────┐
        │  facilita, registra y lleva el backlog; no opina       │◄── SessionStart: fecha, semana,
        └──────┬───────────────────┬──────────────┬─────────────┘    pendientes (pba.py)
               │ lanza en paralelo │ invoca       │ lee y escribe
               ▼                   ▼              ▼
   Subagentes del comité    herramientas/pba.py   empresa/  · estado en Markdown
   (.claude/agents/)        semana · ids          contexto · config.toml · protocolo
   ─ direccion-estrategica  capacidad · check     backlog · decisiones · estado
   ─ contenidos ─ marketing registrar             metricas · areas/ · reuniones/
   ─ ventas-comunidad       privacidad            consultas/ · privado/ (fuera de git)
   ─ finanzas-legal                                       ▲
   ─ producto-tecnologia                                  │
   ─ operaciones                                          │
               │                                          │
               └── escriben rondas y áreas ──► guardia_escritura.py (PreToolUse)
                                               aplica «quién escribe dónde»
```

| Componente | Dónde | Responsabilidad |
|---|---|---|
| Persona fundadora | — | Decide, valida, ejecuta en el mundo real y escribe el contenido |
| Secretaría | sesión principal de Claude Code (`CLAUDE.md`) | Convoca, lanza a los agentes, registra resultados y mantiene el estado. No opina |
| Comité | `.claude/agents/*.md` | Siete roles con mandato, intereses y métricas propias. Proponen, no ejecutan |
| Comandos | `.claude/skills/*/SKILL.md` | Procedimientos repetibles: reunión, validación, progreso, estado y consulta |
| Estado | `empresa/` | Memoria compartida y auditable del comité |
| Herramientas | `herramientas/pba.py` | Lo determinista: fechas, IDs, capacidad, validación, registro de actas y privacidad |
| Guardarraíles | `.claude/hooks/`, `.githooks/`, `.github/workflows/` | Hacen cumplir en código las reglas que importan |

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

## Capas de control

Las reglas importantes no dependen solo de que el modelo las siga. De la más blanda a la más dura:

| Capa | Mecanismo | Qué garantiza |
|---|---|---|
| 1 · Instrucciones | Roles, protocolo, plantillas y skills | El comportamiento esperado, con su porqué |
| 2 · Formato | Plantillas con campos fijos y presupuestos de longitud | Salidas comparables y baratas de leer |
| 3 · Cálculo determinista | `pba.py semana`, `ids`, `capacidad`, `registrar` | Fechas, IDs y sumas correctos y reproducibles |
| 4 · Permisos en tiempo de ejecución | Hook `guardia_escritura.py` + `settings.json` | Cada rol escribe solo en sus ficheros; los hechos piden confirmación |
| 5 · Validación antes de versionar | `pre-commit` → `pba.py check` (formato, IDs, capacidad, privacidad) | Nada roto ni sensible entra en git |
| 6 · Integración continua | GitHub Actions: tests + `check` | El contrato se mantiene en cada cambio |
| 7 · Persona fundadora | `/validar` | Nada se aprueba ni se ejecuta sin ella |

## Matriz de escritura

Lo que dice el protocolo §2 y aplica el hook (ADR-0005):

| Fichero | Rol del comité | Dirección | Secretaría | Persona fundadora |
|---|---|---|---|---|
| `areas/<su-rol>.md`, `areas/<su-rol>/*` | ✍️ | ✍️ (la suya) | ⛔ | ✍️ |
| `reuniones/*/ronda[123]-<su-rol>.md` | ✍️ | ✍️ (la suya) | ⛔ | ✍️ |
| `reuniones/*/acta.md` | ⛔ | ✍️ | ✍️ (forma e IDs) | ✍️ |
| `reuniones/*/00-convocatoria.md` | ⛔ | ⛔ | ✍️ | ✍️ |
| `consultas/*-<su-rol>-*.md` | ✍️ | ✍️ (la suya) | ✍️ | ✍️ |
| `backlog`, `decisiones`, `estado`, `metricas` | ⛔ | ⛔ | ✍️ | ✍️ |
| `contexto.md`, `config.toml`, `protocolo.md` | ⛔ | ⛔ | ❓ confirma | ✍️ |
| `privado/` | ⛔ (solo lee) | ⛔ (solo lee) | ❓ confirma | ✍️ |
| Fuera de `empresa/` | ⛔ | ⛔ | ❓ confirma (o `PBA_MANTENIMIENTO=1`) | ✍️ |

## Coste de una reunión

| Formato | Ejecuciones de agentes | Lectura dominante |
|---|---|---|
| Rápido (semanal, 3–5 asistentes) | 4–6 | El acta lee 3–5 rondas 1 |
| Completo (7 asistentes) | 15–17 | Cada ronda 2 lee las 7 rondas 1 (≈ 7 × 7 lecturas) |

Por eso hay presupuestos de longitud (ADR-0007), asistentes mínimos y `--economica` para las rondas. La tabla «Salud del comité» de `empresa/metricas.md` registra el coste real de cada reunión.

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
| [0004](adr/0004-herramientas-deterministas.md) | Lo calculable (fechas, IDs, horas, formato) lo resuelve `herramientas/pba.py`, no el modelo |
| [0005](adr/0005-guardarrailes-con-hooks.md) | La matriz «quién escribe dónde» la hace cumplir un hook `PreToolUse` |
| [0006](adr/0006-datos-personales-fuera-de-git.md) | Los datos personales viven en `empresa/privado/`, fuera de git |
| [0007](adr/0007-presupuestos-de-longitud.md) | Cada fichero de reunión tiene un presupuesto de longitud |
