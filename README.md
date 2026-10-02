# Product Builder Academy · Oficina del comité de agentes

Siete agentes de Claude Code hacen de equipo directivo de **Product Builder Academy**, una academia de cursos que enseña a construir software y productos con IA **con criterio**: entender la tecnología que hay debajo, la arquitectura y las buenas prácticas que garantizan la seguridad y la calidad. Los agentes debaten, llegan a acuerdos y proponen tareas; **tú validas y ejecutas**. Todo queda escrito en `empresa/`, así que cada reunión parte de lo que se decidió en la anterior.

La oficina aplica lo que enseña la academia: especificación antes de construir, código determinista donde el modelo podría equivocarse, guardarraíles en lugar de buenas intenciones, privacidad por diseño y tests.

## Cómo se ponen de acuerdo

```
Convocatoria ─► Ronda 1: propuestas ─► Ronda 2: revisión cruzada ─► [Ronda 3: resolución] ─► Acta ─► Tú validas
                (en paralelo y a ciegas,   (👍 apoyo · 🤔 reserva ·        (solo si quedan        (Dirección
                 contra el anclaje)          ⛔ objeción bloqueante)          bloqueos)              estratégica)
```

- **Consentimiento, no unanimidad:** se acuerda lo que nadie bloquea. Las reservas constan en el acta.
- **Bloquear cuesta:** una ⛔ solo vale por motivos tasados (capacidad, riesgo legal o financiero, contradice una decisión, daña la marca o al alumnado, imposible a tiempo) y **siempre trae una alternativa**.
- **Peso del área experta:** en lo legal manda finanzas-legal; en lo técnico, producto; en pedagogía, contenidos…
- **Veto de capacidad:** operaciones tumba cualquier semana que pase de 16 h.
- **Desempate y escalado:** dirección estratégica desempata; lo que implique dinero, compromisos públicos, temas legales o cambios de alcance **te llega a ti** como pregunta cerrada con recomendación.

Detalle: [`empresa/protocolo.md`](empresa/protocolo.md) · Por qué así: [`docs/adr/0003`](docs/adr/0003-protocolo-de-consentimiento.md).

## El equipo

| Rol | Área | Defiende |
|---|---|---|
| `direccion-estrategica` | Posicionamiento, objetivos y hoja de ruta; preside y redacta actas | Foco y diferenciación |
| `contenidos` | Catálogo de cursos, línea editorial, formatos, flujo ES/EN | Calidad pedagógica |
| `marketing` | Marca, redes, SEO, reutilización | Distribución y constancia |
| `ventas-comunidad` | Embudo, newsletter, beta, feedback, comunidad | Validar con personas reales |
| `finanzas-legal` | Presupuesto, precios, cobro, fiscalidad, RGPD | Caja y cumplimiento |
| `producto-tecnologia` | Arquitectura Astro, herramientas, seguridad, login y pagos | Simplicidad, seguridad y dogfooding |
| `operaciones` | Capacidad, estimaciones, plan semanal | Sostenibilidad (veto de capacidad) |

## Puesta en marcha

Requisitos: [Claude Code](https://code.claude.com/docs) y Python 3.11 o superior (sin dependencias).

```bash
git clone <este repositorio> && cd <carpeta>
git config core.hooksPath .githooks          # validación antes de cada commit
python3 -m unittest discover -s herramientas/tests
claude                                       # acepta la confianza en la carpeta para activar los hooks
```

Antes de la primera reunión:

1. Revisa **`empresa/contexto.md`** (hechos y restricciones) y **`empresa/config.toml`** (inicio de S1 y capacidad).
2. Crea **`empresa/privado/situacion-personal.md`** y **`empresa/privado/terminos-sensibles.txt`**, que no se versionan. Ver [`empresa/privado/README.md`](empresa/privado/README.md).
3. Lanza `/reunion arranque`.

## Comandos

| Comando | Para qué |
|---|---|
| `/reunion arranque` | Reunión inicial completa (se hace una vez) |
| `/reunion semanal` | Revisión de la semana y plan de la siguiente (formato rápido) |
| `/reunion retro` | El comité revisa su propio funcionamiento (cada 8 semanas) |
| `/reunion <tema> [--rapida] [--economica]` | Reunión sobre cualquier tema, p. ej. `/reunion precio del curso 1 --rapida` |
| `/validar [IDs]` | Aprobar, ajustar o descartar las decisiones y tareas propuestas |
| `/progreso <texto>` | Contar qué has hecho: `/progreso T-003 hecha en 2,5 h; el post tuvo 40 reacciones` |
| `/estado` | ¿Cómo vamos y qué me toca? |
| `/consulta <rol> <pregunta>` | Preguntar a un área sin reunión: `/consulta finanzas-legal ¿necesito alta para aceptar donaciones?` |

## Ciclo semanal recomendado (≈ 1 h de tu tiempo)

1. **Lunes:** `/progreso` con lo de la semana anterior → `/reunion semanal` → `/validar`.
2. **Durante la semana:** ejecutas las tareas aprobadas; `/progreso` cuando termines algo.
3. **Cuando surja algo gordo** (una oportunidad, un problema, feedback que cambia planes): `/reunion <tema>`.
4. **Cada 8 semanas:** `/reunion retro`.

## Qué hay debajo

```
CLAUDE.md                 instrucciones de la sesión principal (la Secretaría)
planning.md               cómo se construyó la oficina, por fases
docs/                     arquitectura y decisiones de diseño (ADR-0001 a 0007)
.claude/agents/           los 7 roles
.claude/skills/           los comandos
.claude/hooks/            guardia de escritura por rol
.claude/settings.json     permisos y hooks
herramientas/pba.py       fechas, IDs, capacidad, validación, registro de actas y privacidad
herramientas/tests/       tests de las herramientas, del hook y de la configuración
evals/                    escenarios para evaluar el comportamiento del comité
empresa/                  el estado del comité (contexto, protocolo, backlog, decisiones, actas…)
```

**Guardarraíles** (detalle en [`docs/arquitectura.md`](docs/arquitectura.md#capas-de-control)):

- **Herramientas deterministas:** la Secretaría no calcula semanas, IDs ni sumas de horas; usa `herramientas/pba.py` ([ADR-0004](docs/adr/0004-herramientas-deterministas.md)).
- **Permisos por rol:** un hook `PreToolUse` impide que un agente escriba fuera de sus ficheros y pide confirmación antes de tocar los hechos ([ADR-0005](docs/adr/0005-guardarrailes-con-hooks.md)).
- **Privacidad:** los datos personales están en `empresa/privado/`, fuera de git, y `pba.py privacidad` vigila que no se cuelen en los ficheros versionados ([ADR-0006](docs/adr/0006-datos-personales-fuera-de-git.md)).
- **Validación continua:** `pre-commit` local y GitHub Actions ejecutan los tests y `pba.py check`.

## Ajustes

- **Coste:** una reunión completa con los 7 roles lanza unas 15–17 ejecuciones de agentes. Para abaratar: `--rapida`, `--economica` (rondas con un modelo más barato), menos asistentes o `model: sonnet` en `.claude/agents/*.md` ([ADR-0007](docs/adr/0007-presupuestos-de-longitud.md)).
- **Añadir un rol:** copia un fichero de `.claude/agents/`, crea su `empresa/areas/<rol>.md`, añádelo a las tablas de `CLAUDE.md` y del protocolo (§4) y al conjunto `ROLES` del hook y de `test_configuracion.py`.
- **Capacidad o calendario:** cambia `empresa/contexto.md` y `empresa/config.toml`, y registra la decisión en `decisiones.md`.
- **Trabajar en la configuración** (agentes, skills, herramientas) sin avisos del hook: `PBA_MANTENIMIENTO=1 claude`.
- **Tras crear o editar agentes o comandos**, reinicia Claude Code para que los cargue.

## Desarrollo

```bash
python3 -m unittest discover -s herramientas/tests -v   # tests
python3 herramientas/pba.py check                      # estado de la oficina
PBA_HOY=2026-11-05 python3 herramientas/pba.py semana  # simular otra fecha
```

Los cambios de diseño se documentan como ADR en `docs/adr/` (plantilla: `0000-plantilla.md`). Si un escenario de `evals/` falla de forma repetida, conviértelo en una regla en código cuando se pueda.
