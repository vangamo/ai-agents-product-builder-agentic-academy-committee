# Detalle técnico de la propuesta de arranque · Borrador (no validado)

> Anexo de `empresa/reuniones/2026-10-05-arranque/ronda1-producto-tecnologia.md`. Nada de esto está validado por la persona fundadora.

## Arquitectura (F0–F1)

- **Modo:** Astro 6 en salida estática. SSR solo en las rutas de F2–F3 (adaptador de Cloudflare para Workers).
- **Colecciones de contenido** (esquema validado en el build):
  - `blog`: `title`, `description`, `lang` (`es`|`en`), `translationKey`, `pubDate`, `updatedDate?`, `tags[]`, `draft`.
  - `lecciones`: los mismos campos, más `course`, `module`, `order`, `duration` (min) y `level`.
  - Markdown por defecto; MDX solo en las lecciones que usen componentes.
- **Componentes MDX de las lecciones:** `<Aviso>`, `<Ejercicio>`, `<Solucion>` (plegable, con `<details>`) y `<Quiz>` (isla React).
- **i18n:**
  - Prefijo siempre presente (`/es/`, `/en/`). `/` es una página estática que redirige a `/es/` y enlaza a `/en/`, sin detectar el idioma por IP ni con cookies.
  - Slugs traducidos y emparejados por `translationKey`. `hreflang` (con `x-default` → ES) solo cuando existe la pareja.
  - El conmutador de idioma lleva a la traducción si existe, y si no, al índice de la sección en el otro idioma.
- **URLs:**
  - `/es/blog/<slug>/` · `/en/blog/<slug>/`
  - `/es/cursos/<curso>/<leccion>/` · `/en/courses/<course>/<lesson>/`
  - Los segmentos traducidos se resuelven con páginas finas que reutilizan el mismo componente.
  - Sin fechas en la URL; los cambios se cubren con redirecciones 301 en `_redirects`.
- **Islas:** React, solo para el progreso, el quiz y el conmutador de tema. La newsletter usa un formulario HTML nativo, sin JS.
- **Estilos:** CSS moderno sin framework: *custom properties*, anidación, `clamp()` y *container queries*. Tipografía del sistema o autoalojada.
- **SEO:**
  - Sitemap con i18n y canonical.
  - RSS por idioma.
  - JSON-LD: `Article`, `Course`, `Person` y `BreadcrumbList`.
  - Imagen OG genérica por idioma en F0 y por post en F1.
- **Presupuestos de calidad** (criterio de «hecho» de cada PR):
  - Lighthouse en móvil ≥ 95 en las cuatro categorías.
  - 0 incidencias graves o críticas en axe.
  - ≤ 30 KB de JS en las páginas de contenido.
  - LCP < 2,5 s, CLS < 0,1 e INP < 200 ms.
  - WCAG 2.2 AA: foco visible, contraste y objetivos táctiles de 24 px.

## Por qué React y no Vue

- Más presencia en ofertas de empleo `[Supuesto]`: refuerza el portafolio.
- Los SDK de login y pagos suelen traer primero componentes React `[Supuesto]`.
- Los agentes de código lo generan con menos errores, por volumen de ejemplos `[Opinión]`.
- Vue sería igual de válido. La regla es usar **uno solo**.

## Seguridad y calidad desde el día 1

1. **Cuentas:**
   - 2FA con llave de acceso o TOTP en GitHub, Cloudflare, el registrador y la newsletter.
   - Códigos de recuperación fuera del repo.
   - Bloqueo de transferencia del dominio, DNSSEC y registro CAA.
2. **Cabeceras** (`_headers`):
   - `Content-Security-Policy` con `default-src 'self'`, scripts por hash (sin `unsafe-inline`), `frame-src https://www.youtube-nocookie.com`, `form-action` limitado al proveedor de newsletter y `frame-ancestors 'none'`.
   - `Strict-Transport-Security: max-age=31536000`, sin *preload* hasta que el sitio esté estable.
   - `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin` y una `Permissions-Policy` que niegue cámara, micrófono y geolocalización.
3. **Secretos:**
   - Ninguno en F0; `.env` en `.gitignore`.
   - *Secret scanning* y *push protection* de GitHub.
   - Los secretos de F2–F3, solo como secretos de Cloudflare.
4. **Dependencias:**
   - Pocas y justificadas, con *lockfile*.
   - Dependabot semanal, con las actualizaciones agrupadas.
   - Actions de GitHub fijadas por SHA y `npm audit` en CI.
5. **Código generado por agentes:**
   - Siempre en rama + PR.
   - Checklist en la plantilla de PR: spec enlazada, sin secretos, sin dependencias nuevas sin justificar, accesibilidad revisada y tests si hay lógica.
   - La persona fundadora revisa el diff antes de fusionar.
6. **Tests y CI:**
   - En cada PR: `astro check`, build, enlaces rotos, axe y Lighthouse CI.
   - Tests unitarios desde F1 (progreso), y obligatorios en el acceso, los webhooks y los pagos.
7. **Correo:** SPF y DKIM (los da el proveedor), y DMARC con `p=none` las dos primeras semanas y `p=quarantine` después.

## Esquema del modelo de amenazas (S5, 1 página, antes de F2)

- **Activos:** cuentas de alumnado, emails, progreso, lecciones de pago, claves y webhooks del MoR, y cuentas de administración.
- **Actores:** atacante anónimo, alumno o alumna curiosa, *bots* de relleno de credenciales y el propio agente de código (filtración accidental).
- **Amenazas (STRIDE) y mitigación:**
  - Robo de sesión → cookie `HttpOnly`, `Secure` y `SameSite=Lax`, y rotación de la sesión.
  - Acceso al progreso de otra persona (IDOR) → comprobar el propietario en el servidor.
  - Webhook falsificado → verificar la firma y la idempotencia.
  - Fuga de las lecciones de pago → las lecciones de pago no van en el repo público y se sirven tras comprobar el acceso.
  - Abuso del enlace mágico → límite de intentos, caducidad de 15 minutos y un solo uso.
  - Secreto filtrado por un agente → *push protection* y revisión de la PR.
- **Riesgo residual y revisión:** finanzas-legal revisa la parte de datos personales.

## Requisitos técnicos para elegir el MoR (F3)

- Sandbox o modo test (D-007).
- Webhooks firmados, incluidos los de reembolso.
- API para consultar compras.
- Checkout en ES y EN.
- Facturas o recibos automáticos.
- Exportación de datos de clientes.
