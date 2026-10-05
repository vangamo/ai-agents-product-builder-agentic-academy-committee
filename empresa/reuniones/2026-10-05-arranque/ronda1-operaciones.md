# Ronda 1 · operaciones · Reunión de arranque (2026-10-05)

> Máximo 200 líneas. Escrita sin leer las rondas de otros roles.

## Resumen

- 8 semanas = **128 h planificables**. Las reparto ya por carriles (6.1): lo que un área proponga fuera de su sobre tiene que desplazar algo.
- Hitos: web en staging en **S2** · web pública en **S3** (si la consulta ⚖️ lo permite) · beta del curso 1 en **S6 (9-nov)**, 6 semanas, hasta el 20-dic · login en staging en **S8** · pagos en modo test en S9–S10.
- S1 y S2 cerradas a 16 h cada una (6.3). Rutina de 4 bloques + colchón fijo, WIP ≤ 3 y un lote semanal de redes.
- Regla clave: **una unidad por delante**. No se promete una cadencia en público sin stock: la web abre con 2 posts y la beta con el módulo 1 completo.

## Diagnóstico

**Hechos**
- `pba.py capacidad` (2026-10-05): 0 h comprometidas en todas las semanas y backlog vacío. No hay horas reales: estimo con la tabla de referencia del rol.
- Coste fijo del comité en S1–S8: 2 h (validar el arranque) + 1 h × 7 semanales + 1 h de retro en S8 = **10 h**.
- Calendario: el lunes 12-oct es festivo nacional (S2). El 1-nov cae en domingo y varias CCAA lo trasladan al **lunes 2-nov (S5)**. El martes 8-dic cae en S10 y las Navidades en S12–S13.
- Todo depende de una persona, y el trámite pendiente ⚖️ condiciona qué se hace público y cuándo.

**Supuestos**
- [Supuesto] Es la primera vez con Astro i18n, la newsletter y el vídeo: las tareas de montaje llevan un +25 % sobre la referencia.
- [Supuesto] Una lección escrita del curso 1 con ejercicio ≈ 3–3,5 h en ES; un módulo = 3 lecciones.
- [Supuesto] Los festivos no restan capacidad (lo pregunto abajo).

**Opinión**
- El mayor riesgo no es arrancar tarde. Es prometer en público un ritmo (posts semanales, entregas semanales de la beta) que en S5 ya no se sostenga. Por eso el plan acumula stock antes de cada apertura.

## Propuestas por punto de la agenda

### Punto 6 · Plan de 8 semanas (lidero)

#### 6.1 Presupuesto de capacidad por carriles (h)

| Carril | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | Total |
|---|---|---|---|---|---|---|---|---|---|
| Comité, plan y horas | 2,5 | 1 | 1 | 1,5 | 1 | 1 | 1 | 2 | 11 |
| Web y tecnología | 6,5 | 4,5 | 4 | 2 | 2 | 3 | 2 | 3 | 27 |
| Curso 1 | 2 | 0 | 3 | 7 | 6 | 6 | 6 | 6 | 36 |
| Blog (ES + EN) | 1,5 | 4,5 | 4,5 | 0 | 4,5 | 0 | 4,5 | 0 | 19,5 |
| Redes y marca | 1 | 1,5 | 2,5 | 2,5 | 1,5 | 2 | 1,5 | 2 | 14,5 |
| Captación y beta | 0 | 2 | 0,5 | 2 | 1 | 3 | 1 | 3 | 12,5 |
| Legal, finanzas y admin | 1,5 | 2,5 | 0,5 | 0,5 | 0 | 0,5 | 0 | 0 | 5,5 |
| Sin asignar | 1 | 0 | 0 | 0,5 | 0 | 0,5 | 0 | 0 | 2 |
| **Total** | **16** | **16** | **16** | **16** | **16** | **16** | **16** | **16** | **128** |

Lo que da cada sobre:
- **Curso 1:** 36 h ≈ 10 lecciones escritas hasta S8. Al empezar la beta (fin de S5) hay 16 h ≈ 4–5 lecciones: el módulo 1 y 1–2 lecciones del 2.
- **Blog:** 4 posts bilingües (escritos en S2, S3, S5 y S7). La web abre con 2 y después va cada quince días.
- **Web:** la v1 en 15 h (S1–S3) y el login en 10 h (S5–S8). Los pagos quedan fuera del horizonte.
- **Redes:** ~2 h/semana, es decir, un lote semanal de ≤ 1 h y una pieza visual reutilizada.
- **Beta:** 1–3 h/semana de gestión (altas, comunidad, encuestas y 2 entrevistas en S8).

#### 6.2 Hitos S1–S8

| Semana | Hito | Hecho cuando |
|---|---|---|
| S1 · 5–11 oct | Plan validado y cimientos | acta validada; consulta ⚖️ pedida; dominio y perfiles reservados (si se aprueban); spec de la web v1 escrita |
| S2 · 12–18 oct | Web en staging | Astro ES/EN con blog, legal v1 y lista de espera en staging `noindex`; post 1 listo en ES y EN |
| S3 · 19–25 oct | 🚀 Web pública | dominio en producción con 2 posts y lista de espera; perfiles activos. **Condicionado** a la respuesta ⚖️ |
| S4 · 26 oct–1 nov | Inscripción a la beta abierta | página y formulario de la beta; módulo 1 en borrador (3 lecciones); estimaciones recalibradas |
| S5 · 2–8 nov | Grupo beta confirmado | personas de la beta confirmadas; módulo 1 revisado y 1 lección del 2; spec del login |
| S6 · 9–15 nov | 🎓 Arranca la beta (6 semanas, hasta el 20-dic) | módulo 1 entregado; encuesta de entrada enviada |
| S7 · 16–22 nov | Ritmo de beta sostenido | 2.ª entrega a tiempo con stock ≥ 1 lección; post 4 |
| S8 · 23–29 nov | Revisión y retro | encuesta de mitad de beta; login en staging; retro del comité; plan S9–S16 (pagos en modo test en S9–S10) |

#### 6.3 Plan de S1 y S2 (cada fila es una tarea `T-?`; `#n` numera esta tabla; el «por qué» es el hito de su semana)

**S1 · 5–11 oct · 16 h** · orden: #1 → (#2, #3, #4, #5) → #6 → #7; #8 → #9 en paralelo

| # | Tarea | Área | h | P | Depende de | Hecho cuando |
|---|---|---|---|---|---|---|
| 1 | Validar el acta de arranque y sus decisiones | operaciones | 2 | P1 | — | todo el acta ha pasado por `/validar` |
| 2 | Bloquear la rutina S1–S8 en el calendario y abrir el registro de horas | operaciones | 0,5 | P1 | #1 | bloques hasta el 29-nov y hoja de horas lista |
| 3 | Solicitar la consulta profesional sobre publicar la web y la beta gratuita ⚖️ | finanzas-legal | 1,5 | P1 | #1 | consulta pedida con preguntas cerradas y plazo de respuesta conocido |
| 4 | Registrar el dominio | producto-tecnologia | 0,5 | P1 | D-? (gasto recurrente) | dominio registrado y renovación anotada |
| 5 | Reservar los nombres de usuario en LinkedIn, Bluesky, Instagram y X | marketing | 1 | P2 | D-? (nombre) | 4 perfiles creados sin publicar, con 2FA |
| 6 | Escribir la especificación de la web v1 (SDD) | producto-tecnologia | 2 | P1 | #1 | spec con páginas, i18n, blog, legal, lista de espera y criterios de aceptación |
| 7 | Crear el esqueleto Astro ES/EN y desplegarlo en staging no indexado | producto-tecnologia | 4 | P1 | #6 | URL de staging con `noindex`, rutas /es y /en y despliegue automático |
| 8 | Cerrar el temario del curso 1 y el esquema del curso 2 | contenidos | 2 | P2 | #1 | temario con módulos, lecciones y proyecto final, aprobado por ti |
| 9 | Escribir los briefs de los posts 1 y 2 | contenidos | 1,5 | P2 | #8 | 2 briefs con tesis, esquema y enlace a un curso |
| — | Sin asignar (para lo que añadan otras áreas) | — | 1 | — | — | — |

**S2 · 12–18 oct · 16 h** · orden: #10 → (#11, #12) → #13 → #14; #15 → #16 → #17

| # | Tarea | Área | h | P | Depende de | Hecho cuando |
|---|---|---|---|---|---|---|
| 10 | Celebrar la reunión semanal y registrar las horas de S1 | operaciones | 1 | P1 | #1 | acta rápida validada; horas reales en `/progreso` |
| 11 | Maquetar el blog bilingüe (listado, post, RSS, sitemap, hreflang) | producto-tecnologia | 3 | P1 | #7 | un post de prueba visible en ES y EN en staging |
| 12 | Adaptar los textos legales v1 (aviso legal, privacidad, cookies) ⚖️ | finanzas-legal | 2,5 | P1 | checklist legal | los 3 textos, revisados contra el checklist |
| 13 | Configurar la lista de espera con doble opt-in y email de bienvenida | ventas-comunidad | 2 | P1 | #12 | un alta de prueba completa el doble opt-in |
| 14 | Integrar los textos legales y el formulario en la web | producto-tecnologia | 1,5 | P1 | #11, #12, #13 | enlaces en el pie y formulario operativo en staging |
| 15 | Escribir el post 1 en ES | contenidos | 3,5 | P1 | #9 | post revisado y listo para publicar |
| 16 | Adaptar el post 1 al inglés con IA y revisarlo | contenidos | 1 | P2 | #15 | versión EN revisada por ti |
| 17 | Crear las plantillas de carrusel e imagen OG y el checklist de publicación | marketing | 1,5 | P2 | #5 | 2 plantillas y el checklist, ya usados con el post 1 |

WIP: como máximo 3 tareas abiertas a la vez (una técnica, una de contenido y una corta de gestión).

#### 6.4 Rutina semanal (plantilla; los días los eliges tú)

| Bloque | h | Para qué |
|---|---|---|
| Arranque del lunes | 1 | `/progreso` de la semana anterior, reunión semanal y `/validar` |
| Bloque profundo 1 | 3,5 | escritura (curso o post), sin redes ni correo |
| Bloque profundo 2 | 3,5 | escritura (curso o post) |
| Bloque de construcción | 3,5 | web y tecnología, con timebox |
| Bloque de producción | 2 | infografías, vídeo y grabación por lotes |
| Lote de distribución | 1 | adaptar y programar las publicaciones de la semana siguiente |
| Ventanas de comunidad | 1 | 4 × 15 min a hora fija |
| Cierre | 0,5 | anotar horas reales y preparar la reunión |
| **Total** | **16** | + **4 h de colchón** en un bloque fijo que no se planifica |

Los bloques se reparten cada semana según los carriles de 6.1 (por ejemplo, en S4 los dos bloques profundos van al curso).

#### 6.5 Reglas de operación

1. **WIP ≤ 3 y terminar antes de empezar:** una tarea nueva solo entra cuando otra cumple su criterio de «hecho».
2. **Timebox** en las tareas técnicas y en todo lo que se hace por primera vez: al agotar la estimación +25 %, se para y la reunión semanal decide si se parte, se simplifica o se mueve. Nada se alarga en silencio.
3. **Una unidad por delante:** la web abre con ≥ 2 posts y la beta con el módulo 1 completo y ≥ 1 lección del 2. Durante la beta, el stock nunca baja de 1 entrega; si se agota, se avisa y se pausa una semana.
4. **Orden de recorte** (cuando el colchón no basta): ① P3 ② lo sin asignar ③ redes al mínimo (1 publicación por red) ④ la adaptación EN se retrasa una semana ⑤ el post de la quincena vuelve a la cola. Nunca se recortan las entregas comprometidas con la beta ni la reunión semanal (mínimo 0,5 h). Lo recortado vuelve a la cola y no se acumula a la semana siguiente.
5. **Semana de mínimos (≈ 8 h)**, para semanas de muchas entrevistas: reunión 0,5 · curso o beta 5 · redes 1 · comunidad 1 · cierre 0,5.
6. **Datos reales:** cada tarea anota sus horas al cerrarse. Recalibro las referencias en S4 y aviso si la desviación media supera el 30 %.
7. **Bitácora de construcción:** cada bloque técnico acaba con 10 min de notas (qué se pidió al agente, qué falló, qué se verificó). Es materia prima para posts y para el curso sin horas extra (ya va en las estimaciones).

- **Por qué:** es un ritmo que se puede mantener seis meses, con los hitos públicos detrás de un stock y no delante.
- **Cómo sabremos si funciona:** ≥ 80 % de las tareas planificadas, hechas cada semana; ninguna semana > 20 h reales; desviación media de las estimaciones ≤ 25 % desde S4; hitos S3 y S6 con ≤ 1 semana de retraso.
- **Alternativas descartadas:** beta en S4–S5 (sin stock ni datos de cuánto cuesta una lección real) · post semanal bilingüe desde S3 (+9 h en S3–S8 que solo saldrían del curso o del login) · login y pagos completos en S1–S8 (sin alta no se pueden activar, D-007) · beta de 8 semanas desde S6 (acabaría el 3-ene, con las Navidades dentro).

### Puntos 2–5 · Lo que afecta a capacidad y calendario

- **P2 · Cursos:** propongo producir el curso **primero en ES** y pasarlo a EN tras el feedback de la beta, para no traducir dos veces lo que va a cambiar. El blog sí sale bilingüe desde el post 1 (~1 h por post). Vídeo: como máximo 1 corto por módulo, dentro del sobre del curso, y el primero con timebox de 3 h. Curso 2: solo esquema (0 h de producción en S1–S8).
- **P3 · Redes:** hay ~2 h/semana para 4 redes, y solo cabe con un lote semanal y reutilizando posts y lecciones. Si se propone más, hay que decir qué carril cede.
- **P3 · Directos y beta:** un directo cuesta 3 h y no cabe en S1–S8 salvo que sustituya a un post; propongo el primero en S9. La gestión de la beta cabe en 1–3 h/semana, y el cupo tiene que ser coherente con eso.
- **P4 · Tecnología:** web v1 en ≤ 15 h (S1–S3) y login en ≤ 10 h (S5–S8), en tareas de ≤ 4 h con timebox. Las herramientas que exijan verificación de cuenta se dan de alta en S2 para absorber la espera.
- **P5 · Cumplimiento:** la consulta ⚖️ (#3) es P1 en S1 porque condiciona el hito S3. Si la respuesta tarda más de 2 semanas, la web sigue en staging y S3–S4 acumulan stock: se mueven los hitos, no las 16 h.

## Tareas propuestas

Las de S1–S2 están en la tabla 6.3 (las de operaciones son #1, #2 y #10; la reunión semanal se repite con 1 h cada semana hasta S8). Sus responsables detallan las de otras áreas. Fuera de la tabla, propongo solo esta:

### T-? · Recalibrar las referencias de estimación con las horas reales de S1–S3
- Área: operaciones · Propuesta por: operaciones
- Estimación: 0,5 h · Prioridad: P2 · Semana: S4
- Depende de: #10 (reunión semanal y horas registradas cada semana)
- Hecho cuando: `empresa/areas/operaciones.md` tiene la tabla de referencias con datos reales y la desviación por tipo de tarea.
- Por qué: si una lección real supera 4 h, la beta de S6 se replanifica en S4, no en S6.

## Coste de mis propuestas

| Semana | Tareas de operaciones | Plan completo propuesto (todas las áreas) |
|---|---|---|
| S1 | 2,5 | 16 (15 asignadas + 1 sin asignar) |
| S2 | 1 | 16 |
| S3 | 1 | 16 |
| S4 | 1,5 | 16 (15,5 + 0,5 sin asignar) |
| S5–S7 | 1 por semana | 16 (S6: 15,5 + 0,5 sin asignar) |
| S8 | 2 (reunión semanal + retro) | 16 |

## Dependencias y peticiones a otras áreas

- A direccion-estrategica: que confirme S3 (web) y S6 (beta) como prioridad global; si prioriza otra cosa, que diga qué carril cede.
- A producto-tecnologia: la web v1 en ≤ 15 h y el login en ≤ 10 h, en tareas de ≤ 4 h; mejor herramientas con alta inmediata.
- A contenidos: una plantilla de lección que quepa en 3–3,5 h; que confirme el curso en ES primero.
- A marketing: un plan de redes en ≤ 2 h/semana y el blog quincenal tras la apertura.
- A ventas-comunidad: un cupo y un diseño de la beta cuya gestión quepa en 1–3 h/semana.
- A finanzas-legal: el checklist legal antes del martes 13-oct (para #12) y las preguntas de la consulta ⚖️ (#3) en S1.

## Riesgos

- La respuesta ⚖️ es lenta o restrictiva → la web sigue en staging, S3–S4 producen stock y los hitos se desplazan sin tocar las 16 h.
- Los perfiles en redes ya son presencia pública → se crean sin publicar; si finanzas-legal ve riesgo, #5 espera a la respuesta de #3.
- Sobreingeniería de la web (la tentación del portafolio) → timebox de 15 h para la v1; el resto va al backlog como P3.
- Una lección real supera las 4 h → se ve en S4 (recalibración); opciones: lecciones más cortas o beta en S7.
- Semanas con > 4 h de entrevistas → orden de recorte y semana de mínimos (6.5).
- Esperas externas (DNS, verificación de cuentas, alta en la herramienta de newsletter) → se inician en S1–S2.
- Festivos que no trabajes: 12-oct (S2) → #16 y #17 pasan a S3 y la lección piloto de S3 vuelve a la cola · 2-nov (S5) → el post 3 vuelve a la cola · 8-dic y Navidades → la beta cierra el 20-dic.
- El coste del propio comité crece → tope de 1 h/semana para la reunión semanal, en formato rápido por defecto.

## Preguntas para la persona fundadora

- ¿Abrimos la web en público en S3? · Opciones: A) S3, condicionada a la respuesta ⚖️ · B) S4 · C) cuando haya 3 posts · Mi recomendación: A.
- ¿Cuándo arranca la beta? · Opciones: A) S5 (2-nov) · B) S6 (9-nov), 6 semanas hasta el 20-dic · C) S7 (16-nov) · Mi recomendación: B.
- ¿Qué fecha de la beta anunciamos en público? (es un compromiso público, así que se escala) · Opciones: A) el 9-nov desde ya · B) «en noviembre» hasta tener el módulo 1 (S5) · C) nada hasta S5 · Mi recomendación: B.
- ¿Cómo repartes los bloques de la rutina? · Opciones: A) 4 días × 4 h + medio día fijo de colchón · B) 5 días × ~3,2 h · C) otro reparto · Mi recomendación: A (los bloques de escritura de 3,5 h necesitan días largos).
- ¿Trabajas los festivos (12-oct; 2-nov si aplica en tu comunidad)? · Opciones: A) sí, 16 h · B) no: esas semanas bajan a 11,5–13,5 h con el recorte ya previsto (ver Riesgos) · Mi recomendación: B, si quieres descanso real.

## Fuentes consultadas

- https://www.vozpopuli.com/actualidad/el-boe-confirma-el-1-de-noviembre-como-festivo-aunque-caiga-en-domingo-que-comunidades-autonomas-tienen-puente · consultada el 2026-10-05 · el 1-nov de 2026 cae en domingo y varias CCAA (≈ 9; las fuentes no coinciden) lo trasladan al lunes 2-nov. Compruébalo en tu calendario autonómico.
- `herramientas/pba.py capacidad` y `semana --numero N` · 2026-10-05 · 0 h comprometidas; rangos de S1–S13.
