# Planning · Oficina del comité de agentes

> Documento de trabajo: lo actualizo al cerrar cada fase. Empecé el lunes 2026-08-24 y el objetivo es tener la oficina lista para la reunión de arranque del **lunes 2026-10-05 (S1)**.

## Objetivo

Construir la «oficina» de Product Builder Academy: un sistema de siete agentes de Claude Code que hacen de comité de dirección de una academia de cursos sobre IA y programación agéntica. Los agentes analizan, debaten y proponen. Yo, como persona fundadora, valido y ejecuto.

La academia enseña a construir software y productos con IA **con criterio**: entender la tecnología que hay debajo, la arquitectura y las buenas prácticas que garantizan la seguridad y la calidad del producto. La oficina tiene que predicar con el ejemplo: si enseñamos especificación, tests y guardarraíles, el sistema que dirige la academia debe tenerlos.

## Punto de partida: el prototipo

Antes de esto hice un prototipo con _vibe coding_ para ver hasta dónde llegaba. Funcionó lo bastante como para tomarlo en serio, y me dejó una lista clara de problemas.

### Lo que funciona y se conserva

- **Siete roles con intereses en tensión:** foco, calidad pedagógica, distribución, validación con personas reales, caja y cumplimiento, simplicidad técnica y capacidad. La tensión es lo que hace útil al comité.
- **Rondas:** propuestas en paralelo y a ciegas (contra el anclaje), revisión cruzada y una resolución solo si quedan bloqueos.
- **Acuerdo por consentimiento:** objeciones bloqueantes tasadas y siempre con alternativa, peso del área experta, veto de capacidad y escalado obligatorio de lo que tenga consecuencias.
- **Estado en ficheros Markdown:** cada reunión parte de lo que se decidió en la anterior y todo queda auditado.
- **Autoría humana:** la persona fundadora escribe el contenido y ejecuta todo lo que ocurre en el mundo real.

### Lo que falla y cómo lo resuelvo

| # | Problema en el prototipo | Consecuencia | Solución |
|---|---|---|---|
| 1 | Rondas de 300–575 líneas y un acta de casi 800 | Reuniones caras, lentas y difíciles de leer | Presupuestos de longitud por fichero (ADR-0007) |
| 2 | El modelo calcula semanas, IDs y sumas de horas | Errores de fecha y de capacidad que no se ven | `herramientas/pba.py`, determinista y con tests (ADR-0004) |
| 3 | El paso de tareas del acta al backlog es manual | IDs duplicados y dependencias rotas | IDs provisionales `T-p1`, `D-p1`… y `pba.py registrar` |
| 4 | «Quién escribe dónde» solo está en los prompts | Nada impide que un agente edite el backlog | Hook `PreToolUse` que aplica la matriz de permisos (ADR-0005) |
| 5 | Datos fiscales y personales en `contexto.md`, versionado | Se publicarían si el repositorio se hace público | `empresa/privado/` fuera de git y detector de términos sensibles (ADR-0006) |
| 6 | Las mismas instrucciones copiadas en los siete agentes | Deriva entre roles al cambiar una regla | Reglas comunes en el protocolo (§8); cada agente solo define su rol |
| 7 | Sin pruebas ni CI | Un cambio de formato rompe el sistema sin avisar | Tests de las herramientas y del hook, y GitHub Actions |
| 8 | No hay forma de saber si el comité se comporta bien | Confianza ciega en las salidas | Escenarios de evaluación en `evals/` |

## Principios de diseño

1. **Determinista donde se pueda, modelo donde aporte.** Fechas, IDs, sumas y formatos los resuelve código. El modelo delibera, redacta y juzga.
2. **Guardarraíles en código, no solo en prompts.** Si una regla importa, se hace cumplir con un hook o una comprobación.
3. **Privacidad por diseño.** Lo personal no entra en git.
4. **Coste acotado.** Cada fichero tiene un presupuesto de longitud; hay formato rápido y modo económico.
5. **Trazabilidad.** Cada decisión de diseño tiene su ADR. Cada decisión de negocio, su entrada en `decisiones.md` y su acta.
6. **Evaluable.** Lo que el comité debe hacer está escrito como escenarios comprobables.
7. **Simple.** Sin frameworks de agentes ni servicios externos: Claude Code, Markdown y Python con la librería estándar.

## Fases y pasos

### Fase 0 · Diseño (24–28 ago) ✅

- [x] Repositorio, README y `.gitignore`
- [x] `planning.md` con el análisis del prototipo (este documento)
- [x] `docs/arquitectura.md`: componentes, flujo de una reunión y modelo de datos
- [x] ADR-0001 comité de subagentes · ADR-0002 estado en Markdown · ADR-0003 protocolo de consentimiento
- [x] `CLAUDE.md` v1: la sesión principal como Secretaría del comité

### Fase 1 · Fuente de verdad (31 ago – 4 sep) ✅

- [x] `empresa/contexto.md`: hechos y restricciones
- [x] `empresa/privado/` fuera de git (ADR-0006)
- [x] `empresa/protocolo.md` §1–7: principios, permisos, ciclo, reglas de acuerdo, formatos y calendario
- [x] `empresa/decisiones.md` con las decisiones fundacionales
- [x] `backlog.md`, `estado.md` y `metricas.md` vacíos, con su formato
- [x] Protocolo §8–9: reglas comunes de los agentes y presupuestos de longitud (ADR-0007)

### Fase 2 · Los siete roles (7–11 sep) ✅

- [x] `direccion-estrategica` · `operaciones` · `producto-tecnologia` · `contenidos` · `marketing` · `ventas-comunidad` · `finanzas-legal`, cada uno con su documento de área
- [x] Revisión cruzada de los roles: tensiones, pesos y métricas coherentes con el protocolo

### Fase 3 · Reuniones (14–18 sep) ✅

- [x] Plantillas: convocatoria, rondas 1–3 y acta (con IDs provisionales)
- [x] Agendas: arranque y semanal
- [x] Skill `/reunion`
- [x] Skill `/validar`

### Fase 4 · Ciclo semanal y herramientas deterministas (21–25 sep) ✅

- [x] Skills `/progreso`, `/estado` y `/consulta`
- [x] `herramientas/pba.py`: `semana`, `ids`, `capacidad`, `check` y `registrar`, con tests (ADR-0004)
- [x] Las skills usan `pba.py` en lugar de calcular a mano

### Fase 5 · Guardarraíles y calidad (28 sep – 2 oct) ✅

- [x] Hook de guardia de escritura por rol (ADR-0005) y `settings.json`
- [x] Contexto de sesión automático (fecha, semana y pendientes)
- [x] `pba.py privacidad`: términos sensibles en ficheros versionados
- [x] CI en GitHub Actions
- [x] Agenda de retrospectiva del comité
- [x] Escenarios de evaluación (`evals/`)
- [x] README completo

### Fase 6 · Arranque (5 oct)

Comprobación previa (2 oct):

- [x] 77 tests en verde y `pba.py check` sin errores ni avisos
- [x] `empresa/privado/situacion-personal.md` y `terminos-sensibles.txt` creados en local; `pba.py privacidad` sin coincidencias y el historial de git limpio
- [x] Hooks de git activos (`core.hooksPath .githooks`)
- [x] Escenarios automáticos de `evals/` (E02, E11, E12, E13) en verde
- [ ] Escenarios manuales de `evals/`: se ejecutan tras la primera reunión real, con datos (E09, E10 y E13 ya se comprobaron en el arranque)

Reunión:

- [x] Reunión de arranque completa con los siete roles
- [x] Registro de tareas y decisiones con `pba.py registrar`, y estado actualizado

## Balance de la construcción

| Fase | Commits | Entregado |
|---|---|---|
| 0 · Diseño | 7 | Análisis del prototipo, arquitectura, ADR 0001–0003, `CLAUDE.md` |
| 1 · Fuente de verdad | 7 | Contexto, privacidad (ADR-0006), protocolo §1–10, registros, ADR-0007 |
| 2 · Roles | 8 | Siete agentes con su documento de área y revisión cruzada |
| 3 · Reuniones | 7 | Plantillas con IDs provisionales, agendas, `/reunion`, `/validar` |
| 4 · Herramientas | 7 | `/progreso`, `/estado`, `/consulta`; `pba.py` con 5 comandos y tests (ADR-0004) |
| 5 · Guardarraíles | 9 | Hook de guardia (ADR-0005), contexto de sesión, privacidad, CI, retro, evals, docs |
| 6 · Arranque | 3 | Reunión completa con los siete roles (22 ejecuciones, ~2.550 líneas), acta y registro con `pba.py registrar`: 18 tareas y 5 decisiones para `/validar` |

Lo que más ha cambiado respecto al plan inicial: probar `pba.py check` contra el backlog del prototipo destapó un campo que el parser no reconocía («Recomendación del comité»), y la primera pasada de `pba.py privacidad` encontró términos reales en mis propios tests. Las dos cosas confirman la idea de partida: lo que no se comprueba en código acaba fallando sin que se note.

## Fuera de alcance (por ahora)

- Ejecutar el comité sin supervisión (cron o agentes en la nube): primero quiero ver cómo se comporta con datos reales.
- Una interfaz web para el backlog: los ficheros Markdown bastan mientras trabaje una sola persona.
- Evaluaciones automáticas con un modelo como juez: llegarán cuando haya varias reuniones reales con las que comparar.
