# Ronda 1 · producto-tecnologia · Arranque (2026-10-05)

> Detalle técnico (esquemas, cabeceras, modelo de amenazas): `empresa/areas/producto-tecnologia/arranque-detalle-tecnico.md` · Borrador (no validado).

## Resumen

- **Web estática con Astro 6 + islas React en Cloudflare**, a 0 € salvo el dominio. Sin servidores ni base de datos hasta F2.
- **F0 abre en S3** (≤ 25 oct) y **F1 queda lista técnicamente en S5**. La beta es abierta y no necesita login. F2 llega a staging en S8 y F3 se prueba en modo test en S9–S10 (D-003, D-007).
- **Construir F0–F1** (es el contenido de los cursos y el portafolio). **Comprar el cobro** a un *Merchant of Record* (MoR), y también el login si no cabe.
- **Seguridad desde el día 1:** 2FA, cabeceras, PR obligatoria para el código de agentes y CI con presupuestos de calidad. Modelo de amenazas en S5.
- **Coste:** 7 h en S1 y 8 h en S2; 51 h en S1–S8, o 37 h si F2 y F3 pasan a S9+.

## Diagnóstico

**Hechos**
- No hay nada técnico creado: ni dominio (D-001), ni repositorio de la web, ni hosting `[Supuesto: confírmalo]`. Lo que manda: < 150 € en total, cualquier gasto recurrente se escala, pagos solo en modo test (D-007) y login y pagos en paralelo a la beta (D-003).
- El equipo de Astro se unió a Cloudflare (ene-2026). Astro 6 es estable desde mar-2026, con soporte de primera para Workers (fuentes secundarias).
- Workers sirve los ficheros estáticos gratis y sin límite; el plan gratuito da 100.000 peticiones/día a la parte dinámica. Newsletter: MailerLite recortó su plan gratuito a 250 suscriptores y 2.500 envíos/mes (jun-2026); Kit es gratis hasta 10.000, con un hueco de recomendación que gestiona Kit; Buttondown, hasta 100.
- MoR: la referencia es ≈ 5 % + 0,50 $ por venta (Paddle, Lemon Squeezy); Polar habría subido su tarifa en may-2026. Las cifras vienen de blogs comparativos y hay que verificarlas en la web de cada proveedor.

**Opinión**
- El mayor riesgo técnico no es la dificultad, sino que construir se coma las horas de contenido. El riesgo de seguridad más probable es el robo de cuentas (dominio, GitHub), no un fallo del código.

## Propuestas por punto de la agenda

### Punto 4 · Producto y tecnología (lidero)

**4.1 Arquitectura**
- **Propuesta:**
  - **Astro 6 en salida estática** en F0–F1; SSR solo en las rutas de F2–F3. *Content collections* `blog` y `lecciones` con esquema validado; MDX solo en las lecciones con componentes.
  - **i18n y URLs:** `/es/` y `/en/` siempre con prefijo; slugs traducidos y emparejados por `translationKey`, con `hreflang` solo cuando existe la pareja. URLs estables y sin fechas (`/es/blog/<slug>/`, `/en/courses/<course>/<lesson>/`), con 301 si algo cambia.
  - **Islas: React, solo donde hagan falta** (progreso, quiz y tema). Tiene más peso en el empleo y en los SDK de login y pagos `[Supuesto]`. Vue también valdría; lo que importa es **uno solo**.
  - **Estilos y SEO:** CSS moderno sin framework, coherente con el curso 1. Tipografía del sistema o autoalojada, nunca Google Fonts remoto ⚖️. Sitemap, canonical, RSS por idioma, JSON-LD e imagen OG.
  - **Presupuestos de calidad en cada PR:** Lighthouse en móvil ≥ 95 en las cuatro categorías; 0 incidencias graves en axe; ≤ 30 KB de JS por página de contenido; LCP < 2,5 s, CLS < 0,1 e INP < 200 ms; WCAG 2.2 AA.
- **Por qué:** una web estática cuesta 0 €, se mantiene en ~1 h/mes y se lleva a cualquier hosting.
- **Cómo sabremos si funciona:** la CI pasa con estos presupuestos y el mantenimiento real es ≤ 2 h/mes (en `metricas.md`).
- **Alternativas descartadas:** WordPress (mantenimiento y superficie de ataque), Next.js (demasiado para un sitio de contenido) y React y Vue a la vez.

**4.2 Herramientas** (todo en plan gratuito salvo el dominio)

| Necesidad | Propuesta | Coste | Alternativas descartadas |
|---|---|---|---|
| Hosting y CDN | Cloudflare Workers (ficheros estáticos) | 0 € | Netlify (plan por créditos `[Supuesto]`); Vercel Hobby (prohíbe el uso comercial `[Supuesto]`, choca con F3); GitHub Pages (no admite cabeceras propias) |
| Dominio y DNS | Cloudflare Registrar + DNSSEC | ≈ 10–12 €/año `[Supuesto]` · **recurrente: se escala** | Registradores con renovación cara |
| Correo de contacto | Cloudflare Email Routing (reenvío) | 0 € | Buzón de pago |
| Analítica | Cloudflare Web Analytics (sin cookies `[Supuesto]`) | 0 € | Plausible (≈ 9 $/mes); GA4 (obliga a un banner de consentimiento) |
| Newsletter | MailerLite gratis (proveedor en la UE) | 0 € hasta 250 suscriptores | Kit (hueco de recomendación ajeno); Buttondown (100 gratis, luego 9 $/mes) |
| Feedback | Tally gratis `[Supuesto]` | 0 € | Google Forms (datos fuera de la UE) |
| Vídeo | YouTube no listado tras una fachada `youtube-nocookie` (no carga nada hasta el clic) | 0 € | Bunny o Cloudflare Stream, solo si hay vídeo de pago en F3 |
| Repositorio y CI/CD | GitHub + Actions + Dependabot | 0 € | — |
| Login (F2) | Better Auth + Cloudflare D1, solo enlace mágico | 0 € + correo transaccional `[Supuesto]` | Clerk (más rápido, menos control); Supabase (pausa los proyectos inactivos `[Supuesto]`) |
| Pagos (F3) | Un MoR (lo elige finanzas-legal) | ≈ 5 % + 0,50 $ por venta | Stripe directo: comisión menor, pero el IVA OSS corre de tu cuenta ⚖️ |

**4.3 Construir frente a comprar**

| Criterio | Plataforma (Teachable, Podia, Thinkific, Gumroad) | Astro + servicios gestionados |
|---|---|---|
| Horas hasta la beta | ~6–8 h `[Supuesto]` | ~22 h (F0) + ~10 h (F1) |
| Coste | Comisión de ~8–10 % + un fijo, o 30–60 $/mes `[Supuesto: sin verificar]` | 0 € hasta F3; después, la comisión del MoR |
| Blog bilingüe y SEO | Limitado: suele hacer falta otro sitio | Completo |
| Portabilidad | Exportación parcial y URLs ajenas | Markdown en git y URLs propias |
| Mantenimiento | ~0 h | ~1–2 h/mes; ~3 h/mes con login y pagos `[Supuesto]` |
| Valor didáctico y de portafolio | Nulo | Alto: es el proyecto de los cursos 1 y 2 |

- **Veredicto:** construir F0–F1; en F2–F3, comprar el cobro (MoR) y construir solo el control de acceso. **Revisión en S5:** si F0 + F1 han costado más de 40 h reales, valorar una plataforma solo para los cursos de pago.

**4.4 Roadmap por fases**

| Fase | Semanas | Hecho cuando |
|---|---|---|
| F0 · Web mínima | S1–S3 (abre ≤ 25 oct) | Inicio, sobre mí y blog ES/EN con ≥ 1 post; newsletter con doble opt-in; aviso legal, privacidad y cookies; analítica; presupuestos de calidad en CI; nota A en Mozilla Observatory |
| F1 · Cursos en abierto | S4–S5 (lista ≤ 8 nov; la apertura la fija contenidos) | Índice de cursos; lección con anterior/siguiente; progreso en `localStorage`; feedback por lección; vídeo con fachada. Sin cuentas |
| F2 · Cuentas | S6–S8, en staging (no pública) | Modelo de amenazas validado; login por enlace mágico; progreso por usuario; acceso por curso con tests; límite de intentos |
| F3 · Pagos | Diseño en S8; modo test en S9–S10 | Compra en sandbox → webhook firmado → acceso; el reembolso revoca el acceso; recibos del MoR. Producción solo tras el alta ⚖️ |

- **Por qué este orden:** F1 es abierta, así que la beta no espera al login, y F2–F3 avanzan en paralelo (D-003) sin bloquearla.

**4.5 Seguridad y calidad desde el día 1** (checklist completa en el borrador)
- **Propuesta:**
  - **Cuentas:** 2FA con llave o TOTP en GitHub, Cloudflare, el registrador y la newsletter; bloqueo de transferencia del dominio y DNSSEC.
  - **Cabeceras:** CSP sin `unsafe-inline` en los scripts, HSTS, `frame-ancestors 'none'`, `Referrer-Policy` y `Permissions-Policy`. Correo con SPF, DKIM y DMARC.
  - **Secretos y dependencias:** ningún secreto en F0; *secret scanning* y *push protection*; pocas dependencias, Dependabot semanal y Actions fijadas por SHA.
  - **Código de agentes:** siempre en rama + PR, con checklist (spec, secretos, dependencias, accesibilidad y tests); la persona fundadora revisa el diff antes de fusionar. `astro check`, axe y Lighthouse CI en cada PR; tests obligatorios en el acceso, los webhooks y los pagos.
- **Modelo de amenazas** (1 página, S5, antes de F2): activos (cuentas, emails, progreso, lecciones de pago y claves del MoR) y amenazas STRIDE (robo de sesión, IDOR, webhook falsificado, fuga de lecciones de pago y secreto filtrado por un agente).
- **Cómo sabremos si funciona:** 0 incidencias, nota A en Observatory y ninguna alerta crítica de Dependabot abierta más de 7 días.

**4.6 La construcción como contenido**
- **Especificar antes de construir:** cada funcionalidad nace de `specs/NNN-*.md` (especificación → plan → tareas → revisión) y deja un ADR si decide algo. El repo es el ejemplo vivo del curso 2 y el resultado del curso 1.
- **Bitácora por tarea:** el prompt clave, qué falló en la revisión y el tiempo real. Son 10 minutos, ya incluidos en cada estimación. Es materia prima: los posts los escribe la persona fundadora (D-005).
- **Briefs de posts para contenidos:** (1) «Especifica tu web antes de pedírsela a un agente»; (2) «Mi checklist para revisar el código que genera la IA»; (3) «Cabeceras de seguridad para una web estática en 30 minutos»; (4) «Web bilingüe con Astro: `hreflang` sin dolor»; (5) «Un comité de 7 agentes dirige mi academia».
- **Sobre el comité:** se publica la arquitectura, nunca `empresa/privado/`. Cómo se presenta en público, lo deciden dirección y finanzas-legal (prudencia de `contexto.md` ⚖️).

### Punto 1 · Posicionamiento (aporte)
- La web es la prueba del «con criterio»: repo y specs visibles, un enlace a «cómo está hecha esta página» y notas A en seguridad y accesibilidad.

### Punto 2 · Catálogo y blog (aporte)
- Lecciones en MDX con cuatro componentes (aviso, ejercicio, solución plegable y quiz) e infografías en SVG accesible, que se traducen sin rehacer la imagen. Flujo bilingüe: un fichero por idioma, sin obligación de tener ambos; si falta la traducción, el conmutador lleva al índice.

### Punto 3 · Canales y beta (aporte)
- **Newsletter:** formulario HTML nativo (sin JS), con doble opt-in, segmentos ES/EN y exportación mensual. Si ventas-comunidad quiere captar antes de abrir, la landing gratuita del proveedor puede estar en S2 (≈ 1 h).
- **Bluesky:** usuario `@productbuilderacademy.com`, verificado por DNS (0 €, 0,25 h) cuando exista el dominio.

### Punto 5 · Finanzas y cumplimiento (aporte)
- **Coste en S1–S8:** solo el dominio; el primer coste recurrente probable es la newsletter, si pasa de 250 suscriptores. **Cookies:** F0–F1 no ponen ninguna, así que posiblemente no haga falta banner ⚖️ Verificar con profesional; en F2, solo la de sesión, estrictamente necesaria.
- **MoR:** necesito sandbox, webhooks firmados, checkout ES/EN y facturas automáticas. La integración son ≈ 8 h.
- **Punto 6 · Plan:** los hitos y las horas están en «Coste de mis propuestas».

## Tareas propuestas

### T-? · Asegurar las cuentas técnicas y crear el repositorio de la web
- Área: producto-tecnologia · Propuesta por: producto-tecnologia
- Estimación: 1 h · Prioridad: P1 · Semana: S1
- Depende de: D-? (repositorio público o privado)
- Hecho cuando: GitHub y Cloudflare tienen 2FA y los códigos de recuperación están fuera del repo; el repo tiene *secret scanning*, *push protection* y PR obligatoria en `main`.
- Por qué: el robo de cuentas es el riesgo más probable y el más caro.

### T-? · Escribir la especificación de la web mínima (F0)
- Área: producto-tecnologia · Propuesta por: producto-tecnologia
- Estimación: 2,5 h · Prioridad: P1 · Semana: S1
- Depende de: T-? (cuentas y repositorio)
- Hecho cuando: `specs/001-web-minima.md` está en el repo con alcance, rutas ES/EN, modelo de contenido, criterios de aceptación (§4.1 y §4.5) y lo que queda fuera de alcance.
- Por qué: aplicar SDD desde el día 1; además, es la base del post 1 y del curso 2.

### T-? · Crear el proyecto Astro bilingüe y desplegarlo en una URL provisional
- Área: producto-tecnologia · Propuesta por: producto-tecnologia
- Estimación: 3,5 h · Prioridad: P1 · Semana: S1
- Depende de: T-? (especificación F0) · D-? (islas) · D-? (hosting)
- Hecho cuando: la plantilla oficial de blog de Astro está adaptada a `/es/` y `/en/`, con TypeScript estricto y la colección `blog` con esquema; la CI (build + `astro check`) pasa en una PR; el despliegue automático en `*.workers.dev` funciona con `noindex`; hay un README de arranque.
- Por qué: desbloquea todo F0; la plantilla oficial aplica «comprar antes que construir».

### T-? · Registrar el dominio y configurar el DNS y el correo de contacto
- Área: producto-tecnologia · Propuesta por: producto-tecnologia
- Estimación: 1 h · Prioridad: P1 · Semana: S2
- Depende de: D-? (registro del dominio)
- Hecho cuando: el dominio tiene 2FA, bloqueo de transferencia, DNSSEC, CAA y DMARC `p=none`; el reenvío de `hola@` está probado; el dominio apunta a la web, que sigue con `noindex`.
- Por qué: del dominio dependen el correo, la newsletter, el usuario de Bluesky y el SEO.

### T-? · Maquetar el layout accesible y las páginas de inicio y sobre mí (ES/EN)
- Área: producto-tecnologia · Propuesta por: producto-tecnologia
- Estimación: 3 h · Prioridad: P2 · Semana: S2
- Depende de: T-? (proyecto Astro) · identidad visual mínima de marketing
- Hecho cuando: hay cabecera, pie, navegación y conmutadores de idioma y de tema, con texto provisional; esas páginas dan Lighthouse en móvil ≥ 95 y 0 errores graves en axe.
- Por qué: es el marco de todas las páginas; la accesibilidad cuesta menos desde el principio.

### T-? · Implementar el blog bilingüe con SEO técnico
- Área: producto-tecnologia · Propuesta por: producto-tecnologia
- Estimación: 4 h · Prioridad: P1 · Semana: S2
- Depende de: T-? (proyecto Astro)
- Hecho cuando: hay listado y post por idioma, RSS, sitemap con `hreflang`, canonical, JSON-LD `Article` e imagen OG; un post de prueba ES/EN emparejado pasa la validación de datos estructurados.
- Por qué: el blog es el canal gratuito de captación (D-002), y el SEO cuesta más arreglarlo después.

## Coste de mis propuestas

| Semana | Hito técnico | Horas |
|---|---|---|
| S1 | Cuentas seguras, spec F0 y proyecto en URL provisional | 7 |
| S2 | Dominio, layout y blog bilingüe con SEO | 8 |
| S3 | Cabeceras, Dependabot y CI de calidad (3 h); newsletter, analítica y páginas legales (3 h); revisión y **apertura de la web** (1,5 h) | 7,5 |
| S4 | Spec F1 (2 h); colección de cursos, índice y navegación (4 h); mantenimiento (0,5 h) | 6,5 |
| S5 | Progreso local, feedback y fachada de vídeo (4 h); modelo de amenazas (2 h); mantenimiento (0,5 h) | 6,5 |
| S6 | Spec F2 (2 h); prototipo de login con timebox (4 h); mantenimiento (0,5 h) | 6,5 |
| S7 | Progreso por usuario y acceso por curso con tests (4 h); mantenimiento (0,5 h) | 4,5 |
| S8 | Diseño de F3 con el MoR elegido (2 h); revisión de F2 en staging (2 h); mantenimiento (0,5 h) | 4,5 |
| **Total** | Plan mínimo: F2–F3 a S9+ (S6–S8 quedan en 0,5 h/semana) → 37 h. La beta no se ve afectada | **51** |

## Dependencias y peticiones a otras áreas

- **A finanzas-legal:** licencias del código y del contenido antes de terminar S1. Para S3, los textos legales ES/EN y la confirmación ⚖️ de que una web sin cookies no necesita banner. Antes de S8, el MoR elegido y la revisión del DPA de la newsletter.
- **A marketing:** antes de S2, una identidad visual mínima (2–3 colores con contraste AA, tipografía y logo en SVG).
- **A contenidos:** 1–2 posts para la apertura en S3. Antes de S4, los campos de una lección y la estructura del curso 1.
- **A ventas-comunidad:** antes de S3, el flujo de la newsletter (doble opt-in, ES/EN). Antes de S5, las preguntas del feedback por lección.
- **A operaciones:** encajar 7 h en S1 y 8 h en S2, o decirme qué movemos. Si hay que recortar, el layout puede pasar a S3 antes que el blog.

## Riesgos

- **La web se come las horas de contenido** → timebox por tarea, plantilla oficial y F2–F3 deslizables sin tocar la beta.
- **Código de agente con fallos de seguridad o de accesibilidad** → PR obligatoria con checklist y CI con axe y Lighthouse.
- **Robo de cuentas o del dominio** → 2FA con llave, bloqueo de transferencia y DNSSEC.
- **Recortes de los planes gratuitos** (MailerLite ya bajó a 250) → formulario agnóstico del proveedor, exportación mensual y revisión trimestral.
- **Un login propio es responsabilidad de seguridad** → modelo de amenazas, solo enlace mágico, límite de intentos y tests; Clerk como salida. **Dependencia de Cloudflare** → la web estática es portable y el SSR queda en pocas rutas.

## Preguntas para la persona fundadora

- **¿Con qué framework se hacen las islas?** Opciones: A) React · B) Vue. Mi recomendación: A.
- **¿Dónde se aloja la web?** Opciones: A) Cloudflare Workers · B) Netlify · C) Vercel. Mi recomendación: A.
- **¿Registras el dominio en S2?** Cuesta ≈ 10–12 €/año y es un gasto recurrente. Opciones: A) Sí, en Cloudflare Registrar · B) Esperar a la apertura. Mi recomendación: A.
- **¿El repositorio de la web es público?** Opciones: A) Público desde S1 · B) Privado hasta la apertura. Mi recomendación: A, o B si prefieres no enseñar el trabajo a medias. Las lecciones de pago irán fuera del repo público en cualquier caso.
- **¿Qué proveedor de newsletter usamos?** Opciones: A) MailerLite · B) Kit · C) Buttondown. Mi recomendación: A, a confirmar con ventas-comunidad y finanzas-legal.
- **¿Dejamos la elección del login para S5, tras el modelo de amenazas?** Opciones: A) Sí · B) Decidir ya. Mi recomendación: A. Hoy prefiero Better Auth + D1 con un timebox de 4 h; si no cabe, Clerk.
- **¿Tienes ya cuenta en GitHub, en Cloudflare o algún dominio?** Opciones: A) Sí, alguna · B) No, ninguna. Sirve para ajustar la tarea de cuentas.

## Fuentes consultadas

Todas consultadas el 2026-10-05. Son resultados de búsqueda, la mayoría fuentes secundarias: verificar en la web oficial antes de decidir.
- https://doolpa.com/news/astro-6-stable-release-cloudflare-workers-vite-environment-api-march-2026 y https://engineered.at/articles/astro-is-joining-cloudflare · Astro 6 estable (mar-2026) con soporte de Workers; el equipo de Astro se une a Cloudflare (ene-2026)
- https://flaviocopes.com/cloudflare-workers-static-assets.md y https://eastondev.com/blog/ko/posts/dev/20260526-cloudflare-free-limits/ · los ficheros estáticos son gratis; plan gratuito de 100.000 peticiones/día
- https://blog.groupmail.io/mailerlite-free-plan-limits/ · MailerLite gratis: 250 suscriptores y 2.500 envíos (jun-2026)
- https://help.kit.com/en/articles/9053602-the-kit-newsletter-plan y https://toolradar.com/tools/buttondown/pricing · Kit gratis hasta 10.000, con un hueco de recomendación gestionado por Kit; Buttondown, 100 gratis y 9 $/mes por 1.000
- https://alexcloudstar.com/blog/merchant-of-record-indie-saas-2026/, https://fungies.io/?p=40299 (lo escribe un competidor) y https://dev.to/devtoolpicks/how-to-handle-eu-vat-as-a-solo-saas-founder-in-2026-jpd · comisiones de los MoR, subida de Polar y, con Stripe directo, IVA OSS a cargo de quien vende
- Sin verificar (marcados `[Supuesto]`): precio del dominio, Netlify, Vercel Hobby, Cloudflare Web Analytics, Tally, Clerk, Supabase y las comisiones de las plataformas de cursos.
