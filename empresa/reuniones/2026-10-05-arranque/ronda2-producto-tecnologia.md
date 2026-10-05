# Ronda 2 · producto-tecnologia · Arranque (2026-10-05)

> Leídas la convocatoria y las 7 rondas 1. Máximo 120 líneas.

## Objeciones bloqueantes (⛔)

**⛔ 1 · operaciones (6.1–6.2): un carril web de 27 h que reparte «v1 en 15 h (S1–S3) + login en 10 h (S5–S8)», con el hito «login en staging en S8».**
- **Motivo (§4 e · viabilidad técnica):** la beta de S6 necesita la zona de cursos en abierto (F1), que piden contenidos, ventas y dirección. Con ese reparto, F1 solo tiene las 2 h de S4: el hito de S6 depende de algo que no tiene horas. F0 + F1 + login no caben en 27 h.
- **Alternativa (el mismo sobre de 27 h, sin ampliar la capacidad):** F0 en 15 h (S1–S3) · **F1 mínima en 4 h (S4–S5)** · en S6–S8 (8 h), el modelo de amenazas, la spec de F2 y un prototipo de login con timebox. **Login en staging en S10 y pagos en modo test en S11–S12.** La beta no se toca y D-003 se cumple, porque login y pagos avanzan durante la beta. Detalle en «Ajustes».

## Posiciones sobre las propuestas de otras áreas

| Área · propuesta (resumen) | Posición | Motivo | Alternativa / condición |
|---|---|---|---|
| operaciones · web v1 en ≤ 15 h (S1–S3) | 👍 | Cabe si se recorta lo que no hace falta para abrir | Recortes en «Ajustes» |
| operaciones · registrar el dominio en S1 (0,5 h) | 👍 | Dependen de él el correo, el remitente de la newsletter, Bluesky y los alias de las cuentas | Después de la búsqueda de marca de finanzas-legal (S1); cambia mi propuesta, que lo dejaba en S2 |
| operaciones · dar de alta en S2 las herramientas que piden verificación; timebox +25 %; bitácora de 10 min | 👍 | Coincide con mi R1 | La cuenta de newsletter, justo después de validar |
| direccion · beta sin login; medición mínima sin cookies; repo público de la web | 👍 | Es mi propuesta | Con las lecciones fuera del repo público (conflicto 2) |
| direccion · bloque 3 de cobro (login y pagos en test + modelo de amenazas) para revisar en S14 | 🤔 | Con la alternativa al ⛔ 1, la parte técnica llega a S13–S14 | Si S12–S13 (Navidades) no se trabajan, llega a S15. Que la revisión de S14 lo dé por posible, no por hecho |
| finanzas · MoR, proveedor en S6 con producto-tecnologia | 👍 | Quita IVA, facturas y reembolsos de nuestras horas | Añado 4 criterios: sandbox, webhooks firmados, checkout ES/EN y API para conceder y revocar el acceso |
| finanzas · revisar las condiciones de venta en el checkout de test en S7 | 🤔 | No hay integración propia hasta S11–S12 | Hacerlo en el **checkout alojado del MoR en modo test**, que no exige código (0 h técnicas). La condición 3 de la puerta saldrá en rojo en S8: ya está previsto |
| finanzas · newsletter con plan gratuito ≥ 300 contactos, DPA y exportación | 👍 | Descarta mi MailerLite (250) | Brevo (conflicto 1) |
| finanzas · web sin cookies no técnicas y sin banner (checklist n.º 3) | 👍 | Es el diseño de F0 | **Riesgo:** los formularios embebidos de los proveedores suelen cargar scripts o captchas de terceros que pueden poner cookies `[Supuesto]`. Requisito: formulario propio sin scripts de terceros, o la página alojada del proveedor. Lo compruebo en staging antes de abrir |
| finanzas · registro de actividades fuera del repo público; licencias opción A | 👍 | Correcto | Ningún dato personal en el repo de la web; las lecciones reservadas, en un repo privado |
| finanzas · plan de brechas antes del login (n.º 12) | 👍 | Encaja | Va dentro del modelo de amenazas de S6 |
| marketing · `hreflang` recíproco + `x-default`, canonical, sitemap, RSS por idioma, `Article` | 👍 | Todo cabe en la tarea del blog (S2) | `x-default` → `/es/`, sin redirección automática por idioma |
| marketing · imagen OG automática por post | 🤔 | Cuesta ≈ 1,5 h y duplica la plantilla de Canva (#17) | En F0, una OG por defecto por idioma + la plantilla de Canva; la automática, P3 desde S6 |
| marketing · `Course` en datos estructurados | 👍 | Barato cuando haya cursos | P3, con F1 |
| marketing · analítica sin cookies que lea los UTM | 🤔 | `[Supuesto, no verificado hoy]` Cloudflare Web Analytics no desglosa UTM | Suscripciones por canal: campo oculto `canal` en el formulario, que se rellena desde `utm_source` (0,25 h). Clics: referrer en la analítica y estadísticas de cada red. Sin analítica de pago |
| marketing · `/enlaces` y acceso DNS (Bluesky, Search Console, Bing) | 👍 | 0,25 h | En el layout (S3) |
| marketing · Atkinson Hyperlegible + JetBrains Mono autoalojadas; paleta AA | 👍 | OFL, sin CDN de terceros | Como mucho 2 pesos en `woff2` con subset; la paleta, como variables CSS; axe en la CI comprueba el contraste |
| marketing · reservar las cuentas con un alias de correo de la marca en S1 | 👍 | Email Routing cuesta 0 € | Requiere el dominio en Cloudflare antes. El buzón que recibe los reenvíos es la llave maestra: también con 2FA |
| contenidos · Markdown/MDX con frontmatter | 👍 | Encaja con las colecciones | Claves en inglés, como el código (`title`, `objective`, `duration`, `lang`, `lastReviewed`…) + `translationKey`, `course`, `module`, `order` y `draft`. Las valida un esquema: un error rompe el build, no la web |
| contenidos · zona de cursos en abierto antes de S6 | 👍 | Es F1 mínima (S4–S5) | Depende del ⛔ 1 |
| contenidos · L4.3 en el mismo hosting que la academia | 🤔 | Para iniciación, Cloudflare exige una cuenta más y más pasos `[Supuesto]` | **GitHub Pages:** ninguna cuenta nueva tras L4.1 y HTTPS automático. Cloudflare, como reto opcional. La decisión pedagógica es de contenidos |
| contenidos · revisión técnica de L4.2 (permisos del agente) en S9 | 👍 | Seguridad | 0,5 h en S9 |
| ventas · progreso medido con formularios por módulo y códigos B01 (seudónimos) | 👍 | Sin login y con datos mínimos | Por eso retiro el progreso en `localStorage` de F1 |
| ventas · newsletter gratis ≥ 500, doble opt-in, etiquetas, 1 automatización y DPA UE | 👍 | Requisitos correctos | Brevo (conflicto 1) |
| ventas · ¿enviar exige dominio propio? | 👍 | En la práctica, sí: los proveedores piden un remitente con dominio autenticado (SPF y DKIM) `[conocimiento estable, no verificado hoy]` | Otra razón para el dominio en S1 y la autenticación en S2 |
| ventas · herramienta para los 3 directos (me la pide) | — | Sin integración en la web | Jitsi Meet o Google Meet en plan gratuito `[Supuesto]`; grabar solo la propia pantalla con OBS en local. 0 € |
| ventas · acceso permanente al curso 1 para la beta | 👍 | Viable | Requisito de F2: conceder acceso a partir de una lista de la beta (+0,5 h en la spec de F2) |

## Conflictos y solapamientos detectados

1. **Proveedor de newsletter.** Mi R1 proponía MailerLite (250 gratis). Ventas pide ≥ 500 y finanzas ≥ 300; la puerta y el bloque de cobro piden 150–300 personas en la lista. **Propuesta para el D-?:** A) **Brevo** (UE; contactos de sobra en el plan gratuito y 300 envíos/día, según la fuente de ventas; con una newsletter quincenal basta hasta unos 300 contactos por día de envío) · B) Kit (EE. UU.; 10.000 gratis, pero el hueco de recomendación lo gestiona Kit: es promoción de terceros ante nuestra audiencia) · C) MailerLite. Recomiendo A, con los límites comprobados en su web oficial al darse de alta.
2. **Repo público + curso de pago con derechos reservados + beta abierta.** Si las lecciones del curso 1 entran en el repo público, el curso de pago queda en el historial de git para siempre. **Solución:** dos repos, `web` público (código, blog y legales) y `cursos` privado, que el build lee con un token de solo lectura. Es el primer secreto: va en Cloudflare, nunca en el repo. +0,5 h en F1.
3. **Calendario de login y pagos.** Operaciones (login en S8, pagos en S9–S10), dirección (bloque 3 en S14) y finanzas (checkout en S7 y puerta en S8) usan fechas distintas. **Calendario único:** modelo de amenazas en S6 · spec de F2 en S7 · prototipo en S8 · login en staging en S10 · pagos en test en S11–S12 · parte técnica del bloque 3 en S13–S14.
4. **Dominio:** S1 (operaciones), S2 (yo) y «después de la búsqueda de marca» (finanzas); además, marketing necesita alias para las cuentas y ventas un remitente. **Orden en S1:** TMview → registrar → Email Routing → reservar cuentas.
5. **Imagen OG:** la plantilla de Canva (#17) y la OG automática hacen lo mismo. Va Canva en F0; la automática, P3.
6. Fuera de mi dominio, pero afectan al plan: las **entrevistas** están duplicadas entre dirección y ventas (fusionarlas en las de ventas), y la **cadencia de la beta** no coincide (contenidos, un módulo cada ~2 semanas; ventas y dirección, uno por semana). Lo resuelven operaciones y contenidos.

## Ajustes a mi propuesta

- **Acepto el sobre de operaciones: 27 h en S1–S8** (antes 51 h, o 37 h en el plan mínimo), con el reparto de la alternativa al ⛔ 1:

| Semana | Tareas técnicas (h) | Total |
|---|---|---|
| S1 | Asegurar las cuentas y crear el repo (1) · spec F0 (2, antes 2,5) · proyecto Astro ES/EN en staging (3, antes 3,5: plantilla oficial y build de Cloudflare) · registrar el dominio (0,5) | 6,5 |
| S2 | Blog bilingüe con SEO técnico (3, antes 4: sin OG automática) · DNSSEC, CAA, Email Routing y autenticación del remitente (0,5) · integrar los legales y el formulario (1) | 4,5 |
| S3 | Layout accesible, inicio, sobre mí y `/enlaces` (1,5, antes 3: sin conmutador de tema) · cabeceras, Dependabot y CI de calidad (1,5) · revisión y **apertura**: analítica y quitar `noindex` (1) | 4 |
| S4 | Spec F1 corta (0,5) · colección de cursos en el repo privado, índice y anterior/siguiente (1,5) | 2 |
| S5 | Enlaces de feedback por módulo y formulario de entrega del proyecto (NSM) en Tally (1) · revisión antes de la beta (0,5) · mantenimiento (0,5) | 2 |
| S6 | Modelo de amenazas de 1 página, con el plan de brechas (2) · arreglos de la beta y mantenimiento (1) | 3 |
| S7 | Spec F2: enlace mágico, acceso por curso y concesión por lista de la beta (1,5) · mantenimiento (0,5) | 2 |
| S8 | Prototipo de login con timebox (2,5) · mantenimiento (0,5) | 3 |

- **Paso a P3 o fuera de S1–S8:** conmutador de tema, OG automática, `Course`, progreso en `localStorage`, fachada de vídeo (llega con el primer vídeo, S9) y **progreso por usuario en F2** (F2 queda en login + acceso por curso: menos datos personales y menos horas).
- **Cambio de recomendación:** newsletter → Brevo (era MailerLite). Dominio → S1 (era S2). La elección entre Better Auth y Clerk sigue después del modelo de amenazas, ahora en S7.
- **Intocable dentro de las 15 h de F0:** 2FA en todas las cuentas (también en el buzón que recibe los reenvíos), PR revisada para todo el código de agentes, cabeceras y Dependabot. Si F0 se pasa del timebox, lo primero que cae es el layout propio: se queda el de la plantilla.

## Mi top 3 para el comité

1. **Dar horas a F1 mínima en S4–S5 y mover el login en staging a S10** (⛔ 1): sin zona de cursos no hay beta en S6.
2. **Newsletter en Brevo con formulario sin scripts de terceros y dominio en S1:** cumple a la vez lo que piden ventas, finanzas y marketing.
3. **Seguridad mínima no negociable y lecciones en un repo privado:** protege las cuentas (el riesgo más probable) y el futuro curso de pago, por 0,5 h más.

> Fuentes: no he podido hacer búsquedas hoy (servicio no disponible). Límites de Brevo: fuente de ventas-comunidad (dreamlit.ai, consultada el 2026-10-05; es de terceros). UTM en Cloudflare Web Analytics y cookies de los formularios embebidos: `[Supuesto]`, a comprobar en staging (S2–S3).
