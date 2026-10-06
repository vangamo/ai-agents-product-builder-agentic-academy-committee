# Backlog

> Lo mantiene la Secretaría (sesión principal). Las tareas nacen en las reuniones como **Propuestas**, pasan a **Aprobadas** cuando la persona fundadora las valida (`/validar`) y se actualizan con `/progreso`. Formato de tarea: `empresa/protocolo.md` §5.
>
> Último ID usado: T-018

## 🟡 Propuestas (pendientes de validar)

### T-001 · Validar el acta de arranque y bloquear la rutina semanal hasta S8
- Área: operaciones · Propuesta por: operaciones
- Estimación: 2,5 h · Prioridad: P1 · Semana: S1
- Depende de: —
- Hecho cuando: D-008 a D-012 y las tareas de esta acta han pasado por `/validar`; has respondido a las preguntas de «Pendiente»; la rutina, con el colchón de 4 h, está en tu calendario hasta el 29-nov, y la hoja de horas, lista para `/progreso`.
- Por qué: arrancar con un plan validado y medir horas reales desde S1.
- Origen: reuniones/2026-10-05-arranque

### T-002 · Comprobar la marca en TMview y la OEPM, revisar el dossier y pedir la cita de la consulta
- Área: finanzas-legal · Propuesta por: finanzas-legal
- Estimación: 1 h · Prioridad: P1 · Semana: S1
- Depende de: D-008 (para la cita)
- Hecho cuando: el resultado para «Product Builder Academy» y «Product Builder» en las clases 41 y 9 está en `/progreso`, con luz verde o roja para el dominio y los nombres; el dossier incluye la pregunta sobre el acceso gratuito de la cohorte ⚖️; la cita está pedida para S2, con el compromiso de una respuesta escrita (vale un email) a la pregunta 1.
- Por qué: no invertir en un nombre ocupado; la respuesta escrita abre la puerta pública (A2).
- Origen: reuniones/2026-10-05-arranque

### T-003 · Asegurar las cuentas técnicas y crear el repositorio privado de la web
- Área: producto-tecnologia · Propuesta por: producto-tecnologia, finanzas-legal
- Estimación: 1 h · Prioridad: P1 · Semana: S1
- Depende de: D-010 (para `LICENSE`)
- Hecho cuando: GitHub, Cloudflare y el gestor de contraseñas tienen 2FA con llave o TOTP, con los códigos de recuperación fuera del repo; el repo `web` es privado, usa el email *noreply* de GitHub desde el primer commit y tiene `LICENSE`, ningún dato personal y gitleaks en *pre-commit* y en la CI.
- Por qué: el robo de cuentas es el riesgo más probable, y el historial se publicará entero en la apertura.
- Origen: reuniones/2026-10-05-arranque

### T-004 · Registrar el dominio y activar el reenvío del correo de la marca
- Área: producto-tecnologia · Propuesta por: producto-tecnologia, operaciones
- Estimación: 0,5 h · Prioridad: P1 · Semana: S1
- Depende de: T-002 · T-003 · D-008
- Hecho cuando: `productbuilderacademy.com` está registrado en Cloudflare Registrar con bloqueo de transferencia y la renovación anotada; el reenvío del alias de la marca está probado hacia un buzón con 2FA; el gasto consta en `/progreso`.
- Por qué: del dominio dependen el correo, los alias de las cuentas, el handle de Bluesky, el remitente y el SEO.
- Origen: reuniones/2026-10-05-arranque

### T-005 · Escribir la especificación de la web mínima (F0)
- Área: producto-tecnologia · Propuesta por: producto-tecnologia
- Estimación: 2 h · Prioridad: P1 · Semana: S1
- Depende de: T-003
- Hecho cuando: `specs/001-web-minima.md` está en el repo con el alcance, las rutas `/es/` y `/en/`, el modelo de contenido, los criterios de aceptación de calidad y seguridad de E5, el staging no público y lo que queda fuera.
- Por qué: especificar antes de construir desde el día 1; es materia del curso 2 y del portafolio.
- Origen: reuniones/2026-10-05-arranque

### T-006 · Crear el proyecto Astro bilingüe y desplegarlo en un staging no indexado
- Área: producto-tecnologia · Propuesta por: producto-tecnologia
- Estimación: 3 h · Prioridad: P1 · Semana: S1
- Depende de: T-005
- Hecho cuando: la plantilla oficial de blog de Astro está adaptada a `/es/` y `/en/`, con TypeScript estricto y la colección `blog` con esquema; la CI (build, `astro check` y gitleaks) pasa en una PR; el despliegue automático en `*.workers.dev` funciona con `noindex`, sin enlaces desde ningún sitio y con texto provisional (sin tu nombre ni la oferta); hay un README de arranque.
- Por qué: desbloquea F0 sin publicar nada antes de la luz verde.
- Origen: reuniones/2026-10-05-arranque

### T-007 · Crear la plantilla de lección y escribir la lección piloto L1.2 «Qué pasa desde que escribes una URL» (ES)
- Área: contenidos · Propuesta por: contenidos
- Estimación: 3,5 h · Prioridad: P1 · Semana: S1
- Depende de: T-001
- Hecho cuando: la plantilla de lección en Markdown tiene su estructura tipo y el frontmatter de E5; el borrador de L1.2 está completo, con práctica, comprobación de criterio y caja 🔧, y revisado con la checklist de la guía; las horas reales constan en `/progreso`.
- Por qué: calibrar el coste real por lección (hipótesis: ≤ 3,5 h); si pasa de 4 h, la semanal de S2 baja el curso a 10 lecciones.
- Origen: reuniones/2026-10-05-arranque

### T-008 · Preparar el guion, concertar 5 entrevistas de descubrimiento y hacer la primera
- Área: ventas-comunidad · Propuesta por: ventas-comunidad, direccion-estrategica
- Estimación: 1 h · Prioridad: P1 · Semana: S1
- Depende de: T-001
- Hecho cuando: el guion une las preguntas de ventas-comunidad, las 5 de dirección y las 2 de contenidos; hay 5 citas (≥ 2 de A temprano, ≥ 1 junior y ≥ 1 de B; ≥ 2 de fuera del círculo cercano) concertadas con mensajes 1:1 que siguen la pauta pública, sin oferta ni enlace; la primera entrevista está anotada solo con nombre de pila y perfil.
- Por qué: validar el público con personas reales antes de cerrar la landing y los módulos 2–4.
- Origen: reuniones/2026-10-05-arranque

### T-009 · Reservar los nombres de usuario de la marca en Bluesky, X e Instagram
- Área: marketing · Propuesta por: marketing
- Estimación: 1 h · Prioridad: P1 · Semana: S1
- Depende de: T-002 · T-004
- Hecho cuando: las 3 cuentas existen sin publicar, con los nombres de E4 (o sus alternativas), nombre visible, avatar provisional y bio neutra; usan el alias de la marca, 2FA y contraseñas en el gestor; Bluesky usa el handle del dominio verificado por DNS (si el dominio no está listo, el handle pasa a S5).
- Por qué: que nadie ocupe el nombre, sin presencia pública antes de la luz verde.
- Origen: reuniones/2026-10-05-arranque

### T-010 · Validar la guía de marca v0: tono, paleta, tipografías y logotipo
- Área: marketing · Propuesta por: marketing
- Estimación: 0,5 h · Prioridad: P2 · Semana: S1
- Depende de: T-001
- Hecho cuando: cada elemento de la marca v0 (E4) está marcado «sí» o «cambiar» y el contraste de la paleta está comprobado con un verificador WCAG; los mensajes y la bio se cierran con el perfil de LinkedIn (S3).
- Por qué: el layout y las plantillas de S3 la necesitan.
- Origen: reuniones/2026-10-05-arranque

### T-011 · Celebrar la semanal de S2 y registrar las horas reales de S1
- Área: operaciones · Propuesta por: operaciones
- Estimación: 0,5 h · Prioridad: P1 · Semana: S2
- Depende de: T-001
- Hecho cuando: las horas reales de S1 (también las de la piloto) están en `/progreso`, consta si el C1 sigue con 12 lecciones o baja a 10, y lo que salga ha pasado por `/validar`.
- Por qué: aplicar a tiempo la válvula del curso y empezar la recalibración.
- Origen: reuniones/2026-10-05-arranque

### T-012 · Celebrar la consulta profesional y revisar los textos legales y los consentimientos en ES
- Área: finanzas-legal · Propuesta por: finanzas-legal, operaciones
- Estimación: 2,5 h · Prioridad: P1 · Semana: S2
- Depende de: T-002 · D-009 · D-010
- Hecho cuando: hay respuesta escrita al menos a la pregunta 1 del dossier y sus consecuencias (no los datos) están en `/progreso`, con la pauta pública confirmada o ajustada; el aviso legal, la privacidad y el texto de cookies en ES (borradores de finanzas-legal) llevan los encargados reales (Cloudflare, Brevo y Tally), y están listos los consentimientos de newsletter, formularios, testimonios y entrevistas; la fila «Antes de abrir» de la checklist de E6 está marcada.
- Por qué: es la condición de la apertura (RGPD y LSSI desde el primer visitante).
- Origen: reuniones/2026-10-05-arranque

### T-013 · Crear la cuenta de Brevo y configurar DNSSEC, CAA y la autenticación del remitente
- Área: producto-tecnologia · Propuesta por: producto-tecnologia
- Estimación: 0,5 h · Prioridad: P1 · Semana: S2
- Depende de: T-004
- Hecho cuando: la cuenta de Brevo tiene 2FA y el alias de la marca, el DPA aceptado y los límites del plan gratuito comprobados en su web oficial; DNSSEC, CAA, SPF, DKIM y DMARC `p=none` están publicados y un correo de prueba sale autenticado.
- Por qué: sin un remitente con dominio autenticado no llega la confirmación del doble opt-in `[Supuesto]`.
- Origen: reuniones/2026-10-05-arranque

### T-014 · Implementar el blog bilingüe con SEO técnico
- Área: producto-tecnologia · Propuesta por: producto-tecnologia, marketing
- Estimación: 3 h · Prioridad: P1 · Semana: S2
- Depende de: T-006
- Hecho cuando: hay listado y post por idioma, RSS por idioma, sitemap con `hreflang` recíproco y `x-default`, canonical, JSON-LD `Article` y una imagen OG por defecto por idioma; un post de prueba ES/EN emparejado por `translationKey` pasa la validación de datos estructurados; el staging sigue con `noindex`.
- Por qué: el blog es el canal gratuito de captación (D-002), y el SEO cuesta más arreglarlo después.
- Origen: reuniones/2026-10-05-arranque

### T-015 · Configurar la lista en Brevo con doble opt-in, etiquetas, bienvenida y landing alojada, sin publicar
- Área: ventas-comunidad · Propuesta por: ventas-comunidad, operaciones
- Estimación: 2 h · Prioridad: P1 · Semana: S2
- Depende de: T-012 · T-013 · D-011
- Hecho cuando: un alta de prueba privada recorre sin errores la confirmación, las etiquetas (`beta-curso1`, `interes-curso2`), los campos de idioma y `origen`, las bienvenidas en ES y en EN y la baja en un clic; el formulario tiene la casilla sin marcar, la edad mínima de 14 años y la primera capa de privacidad; la landing alojada queda despublicada (activarla es parte de la apertura).
- Por qué: que cada visita, desde la apertura, pueda convertirse en suscriptor.
- Origen: reuniones/2026-10-05-arranque

### T-016 · Hacer 4 entrevistas de descubrimiento y sintetizar las 5
- Área: ventas-comunidad · Propuesta por: ventas-comunidad, direccion-estrategica
- Estimación: 2,5 h · Prioridad: P1 · Semana: S2
- Depende de: T-008
- Hecho cuando: hay una síntesis de una página (patrones, 3 citas sin datos personales, el veredicto «¿≥ 3 de 5 confirman los dos dolores, con ≥ 2 de A temprano?: sí o no» y 3 cambios para el C1 y la beta) registrada con `/progreso`.
- Por qué: la semanal de S3 confirma o revisa el público con evidencia.
- Origen: reuniones/2026-10-05-arranque

### T-017 · Validar la guía de estilo y el glosario y escribir el post «Qué pasa desde que escribes una URL» (ES+EN)
- Área: contenidos · Propuesta por: contenidos
- Estimación: 3 h · Prioridad: P1 · Semana: S2
- Depende de: T-007
- Hecho cuando: la guía y el glosario están aceptados o con los cambios anotados; existe la plantilla de post (frontmatter, palabra clave, título de ≤ 60 caracteres, slugs ES/EN y recuadro «Lo esencial»); el post, derivado de L1.2, está listo en ES y en EN para publicarse en la apertura, con texto alternativo y el glosario aplicado; las horas de la versión EN están anotadas.
- Por qué: la web abre con este post, que además mide lo que cuestan un derivado y la versión EN (hipótesis: ≤ 25 %).
- Origen: reuniones/2026-10-05-arranque

### T-018 · Escribir el brief de la web de referencia I y crear su repositorio plantilla
- Área: contenidos · Propuesta por: contenidos
- Estimación: 1,5 h · Prioridad: P2 · Semana: S2
- Depende de: T-017 · D-009 · D-010
- Hecho cuando: el brief de una página está escrito con la plantilla que usará L2.1 (sobre tu web personal real si D-009 es A; si no, sobre una ficticia) y el repositorio plantilla del C1 existe en privado con su `LICENSE`.
- Por qué: es la primera parte de la web de referencia I (4 h en total con el HTML y el CSS de S3) y libera S3, que va a 16 h.
- Origen: reuniones/2026-10-05-arranque

## ✅ Aprobadas (por hacer)

_(ninguna)_

## 🔵 En curso

_(ninguna)_

## ✔️ Hechas

_(ninguna)_

## ❌ Descartadas o aparcadas

_(ninguna)_
