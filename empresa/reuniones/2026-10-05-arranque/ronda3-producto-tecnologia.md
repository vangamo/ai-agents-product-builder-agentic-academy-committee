# Ronda 3 · producto-tecnologia · Arranque (2026-10-05)

> Máximo 30 líneas por objeción. Leídas las rondas 1 y 2.

## direccion-estrategica y finanzas-legal (⛔ 1 de sus R2) · repositorio de la web público desde S1

- **Posición final:** acepto la alternativa. Retiro la opción A del D-? del repositorio y recomiendo la B: el repo `web` es privado en S1–S2 y se hace público el mismo día que todo lo demás, en S3 o cuando haya luz verde por escrito. El repo `cursos` sigue privado siempre.
- **Condiciones técnicas para que funcione (0 h netas, el carril sigue en 27 h):**
  1. **El historial se hará público entero.** Por eso, desde el primer commit: el email *noreply* de GitHub (finanzas lo pedía al abrir; después costaría reescribir el historial), ningún dato personal, `LICENSE` y textos provisionales. Va dentro de la tarea de cuentas (1 h, S1).
  2. **Lo que GitHub Free no da en repos privados** (protección de `main` y escaneo de secretos con bloqueo de *push*) `[conocimiento estable, no verificado hoy: comprobar al crear el repo]` lo cubre en S1 **gitleaks** en *pre-commit* y en la CI. El tiempo es el mismo: el que no gasto en configurar esas protecciones. Dependabot y Actions sí funcionan en privado.
  3. **Apertura en S3:** hacer público el repo, activar la protección de `main` y el escaneo con bloqueo, y pasar gitleaks a todo el historial (+0,25 h en la tarea de apertura). Lo compensa el layout, que baja de 1,5 a 1,25 h porque aprovecha más la plantilla. S3 sigue en 16 h.
  4. **El staging no es «público»:** en `*.workers.dev`, con `noindex`, sin enlaces desde ningún sitio y con texto provisional, sin nombre real ni descripción de la oferta hasta la luz verde (0 h). Si finanzas-legal no lo ve suficiente, Cloudflare Access en esa URL (0 € `[Supuesto]`, ≈ 0,25 h).
  5. **Si la consulta se retrasa:** todo sigue en privado sin horas extra. El riesgo es que `main` queda sin protección forzada: reviso cada PR por disciplina y la CI la pasa igual. Si la espera pasa de S6, lo reviso en la semanal. No propongo pagar GitHub Pro.
- **Motivo:** la objeción cumple el §4 b y en lo legal pesa más finanzas-legal. A mí me cuesta poco: el dogfooding y el portafolio no se pierden, porque las specs, los ADR y todo el historial se publican en S3 con apenas dos semanas de retraso. Abrir todo a la vez, además, simplifica: una sola revisión de privacidad antes de abrir, en vez de una ahora y otra en S3.
