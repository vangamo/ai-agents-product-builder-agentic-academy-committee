# Ronda 2 · finanzas-legal · Reunión de arranque (2026-10-05)

> Leídas la convocatoria, las 7 rondas 1 y las rondas 2 ya escritas (marketing, producto-tecnologia y ventas-comunidad). Máximo 120 líneas.

## Objeciones bloqueantes (⛔)

**⛔ 1 · Hacer público el proyecto antes de tener la respuesta escrita de la consulta.** Afecta a ventas (R2, fila 17: post de «La oficina» en S2 que enlaza a la landing alojada por el proveedor) y a producto y dirección (repositorio de la web público desde S1, opción A).
- **Motivo (§4 b):** según `contexto.md`, hay un trámite pendiente al que podrían afectar la actividad y la forma de presentar el proyecto en público ⚖️. Un error ahí costaría más que cualquier ingreso previsible en 2026, y esperar una semana no cuesta nada. Es justo la pregunta 1 del dossier de la consulta.
- **Alternativa (0 h extra; como mucho, 1 semana de retraso):** en S1–S2 todo se prepara en privado: el repo privado (la opción B de producto), la landing y el post en borrador, y los perfiles reservados, sin publicar y con una bio neutra. En S3 se abre todo a la vez, con la misma condición que operaciones pone a la web y que marketing ya acepta. Si la consulta da luz verde antes, se adelanta. Si se retrasa, se aplica el plan B de ventas (invitaciones privadas, con el texto revisado por mí).

**⛔ 2 · contenidos: licencia «textos CC BY-NC-SA», si incluye las lecciones de los cursos.**
- **Motivo (§4 b y c):** una licencia CC no se puede retirar de lo ya publicado ⚖️. Cualquiera podría copiar y redistribuir gratis, y para siempre, el curso 1 que queremos vender (D-003).
- **Alternativa:** la opción A de mi D-? sobre licencias: el blog con CC BY-NC-SA 4.0; las lecciones con todos los derechos reservados (uso personal del alumnado); y el código y las plantillas con MIT, para que el alumnado pueda reutilizarlos en sus proyectos. Encaja con los dos repos que propone producto. **Si contenidos se refería solo al blog, el ⛔ decae.**

## Posiciones sobre las propuestas de otras áreas

| Área · propuesta (resumen) | Posición | Motivo | Alternativa / condición |
|---|---|---|---|
| operaciones · #3 pedir la consulta en S1 (1,5 h) y #12 textos legales en S2 (2,5 h) | 👍 | Es el camino crítico hacia S3 | Reestimo: 1 h en S1 (incluida la búsqueda de marca) y 2,5 h en S2, ya con la consulta dentro (Ajustes) |
| operaciones · web pública en S3 si la consulta lo permite; si tarda, staging y stock | 👍 | Es mi condición 1 aplicada a todo lo público | Que la condición valga para todo lo público (⛔ 1) |
| operaciones / producto · dominio en S1, en este orden: TMview → registro → Email Routing → cuentas | 👍 | Cloudflare Registrar cobra a precio de coste e incluye la privacidad WHOIS | ≈ 10–12 €/año: es un gasto recurrente y va en el D-? de presupuesto |
| marketing · «La oficina» y el perfil de LinkedIn pasan a S3, condicionados ⚖️ | 👍 | Resuelve lo que habría sido otro ⛔ | Siguiendo la pauta de abajo |
| marketing · perfiles reservados sin publicar y con bio neutra | 👍 | Riesgo bajo | La bio de marca, después de la consulta |
| marketing / producto · campo oculto `origen` rellenado desde `utm_source` | 👍 | No guarda nada en el dispositivo, así que no le aplica el art. 22.2 de la LSSI | La privacidad lo menciona como finalidad: «saber por qué canal te suscribiste» |
| ventas · post en S2 que enlaza a la landing alojada del proveedor (fila 17) | ⛔ | §4 b | ⛔ 1 |
| ventas · la cohorte conserva el C1 y el −40 % pasa al C2 y al pack (fila 21) | 👍 | Retiro mi código de descuento sobre el C1 | ⚖️ El acceso se da a toda la cohorte y no depende del feedback, para que no parezca un pago en especie. Lo llevo a la consulta |
| ventas · nota prudente: «quienes participen conservarán el acceso al curso 1» | 👍 | No anuncia en público ningún pago futuro | Las condiciones de la beta (S4) precisan el alcance: el curso 1 y sus actualizaciones, mientras se publique |
| ventas · demanda medida entre quienes terminan y en la lista; el mínimo de la lista lo fija finanzas (fila 10) | 👍 | Es una cuestión de caja | Umbrales en Conflictos 1 |
| ventas · 2 directos (kickoff en S6 y demo day en S11) | 👍 | — | Aviso de grabación, cámara opcional y permiso por escrito para mostrar la imagen, la voz o la web de cada persona (n.º 8 de la checklist) |
| ventas / producto · newsletter en Brevo | 👍 | Está en la UE y, según su FAQ oficial, el plan gratuito admite 100.000 contactos y 300 envíos/día: no nos obligará a pagar antes de abrir la puerta para cobrar | DPA aceptado, doble opt-in, formulario propio sin reCAPTCHA de Google y exportación mensual |
| producto · Kit o MailerLite como alternativas | 🤔 | Kit: transferencia a EE. UU. (legal con el Marco de Privacidad) y recomendaciones de terceros ante nuestra audiencia. MailerLite: está en la UE, pero con 250 contactos obliga a pagar antes de tener ingresos | Solo como plan B |
| producto · repo de la web público desde S1 (opción A) | ⛔ | §4 b | ⛔ 1. Al abrirlo: `LICENSE`, ningún dato personal y el email *noreply* de GitHub en los commits |
| producto · dos repos (web pública y cursos privados) | 👍 | Protege el curso de pago y encaja con las licencias | — |
| producto · sin scripts de terceros, analítica sin cookies, vídeo tras una fachada y fuentes autoalojadas | 👍 | Así la web no necesita banner (n.º 3) ⚖️ | En la revisión de apertura (S3), comprobar en DevTools que no se escribe ninguna cookie ni nada en `localStorage` (0,25 h, dentro de esa tarea) |
| producto · login en staging en S10, pagos en test en S11–S12 y 4 criterios más para elegir el MoR | 👍 | El cobro no hace falta antes | MoR en S9–S10 (no en S6); las condiciones de venta se revisan en el checkout alojado, en modo test |
| producto · Tally para el feedback y las entregas; Jitsi o Meet para los directos | 👍 | Son encargados del tratamiento | DPA y mención en la privacidad (S4); formularios con código (B01…), sin email |
| dirección · cobrar según criterios, en 3 bloques, con revisión en S14 | 👍 | Es mi puerta, mejor ordenada | Mis condiciones 1, 3 y 4 forman el bloque 3 |
| dirección · lista ≥ 150 para empezar a cobrar | 🤔 | 150 × 3 % `[Supuesto]` ≈ 4–5 ventas, por debajo del equilibrio (≈ 7 ventas del C1 al mes para cubrir la cuota) | Lista ≥ 200 y ≥ 15 intenciones explícitas (Conflictos 1) |
| dirección · firmar con nombre y construir en público | 👍 | El aviso legal ya exige el nombre (LSSI art. 10) | Después de la consulta. Como titular: nombre y email del dominio, sin domicilio hasta el alta (pregunta 7) |
| contenidos · licencia «textos CC BY-NC-SA y código MIT» | ⛔ | §4 b y c | ⛔ 2 |
| contenidos · uso de capturas de herramientas de terceros ⚖️ | 👍 | Derecho de cita con fines docentes (LPI art. 32): solo el fragmento necesario para explicar o analizar, con la fuente | Las marcas, solo para identificar; sin logos decorativos ni nada que sugiera un patrocinio |
| contenidos · prácticas a 0 € para el alumnado | 👍 | En la beta no se cobra nada ni se pide tarjeta | — |

## Pauta de comunicación pública (provisional; la piden marketing y dirección)

- **Cuándo:** nada público hasta tener la respuesta escrita de la consulta (⛔ 1). Después, la pauta se confirma o se ajusta.
- **Sí:** «proyecto educativo personal», «gratuito», «en construcción», «beta gratuita», «blog siempre gratis». Firma con nombre propio.
- **Nunca (hasta abrir la puerta para cobrar):** precios, «comprar», «reserva tu plaza», «empresa», «negocio», «clientes», «facturar», ingresos, donaciones o «invítame a un café», afiliados, patrocinios, fechas de cobro ni «curso de pago».
- **Construir en público:** se cuenta el mecanismo, nunca la situación fiscal, laboral o administrativa, ni que exista un trámite. Ninguna captura de `contexto.md`, de `areas/finanzas-legal*` ni de actas que la mencionen.

## Conflictos y solapamientos detectados

1. **Tres criterios distintos para empezar a cobrar** (dirección, ventas y el mío). Propongo una sola tabla con los 3 bloques de dirección:
   - **Bloque 2 · demanda** (el mínimo lo fijo yo, como pide ventas): **≥ 15 personas que dicen «lo compraría a 39 €»** (quienes terminan la beta y las 3 preguntas de la newsletter de S10) **y una lista ≥ 200**. Con una conversión de 15 × 50 % `[Supuesto]` salen ≈ 7–8 ventas en el mes de lanzamiento, que es el equilibrio con la cuota (≈ 206 €/mes).
   - **Bloque 3 · habilitación ⚖️:** mis condiciones 1, 3 y 4: trámite aclarado por escrito; cobro probado en test; y condiciones de venta, privacidad y alta listas antes de la primera venta.
   - Con solo el C1 en S14, lo realista es una **ventana de lanzamiento** (alta alineada con la apertura de las ventas y evaluación a los 3 meses), no unos ingresos mensuales estables ⚖️ (pregunta 7 del dossier).
2. **Fechas de los pagos:** mi revisión de la puerta pasa de S8 a S14, como propone dirección. El MoR pasa de S6 a S9–S10, justo antes de los pagos en test (S11–S12, según el calendario de producto). Las condiciones de venta se revisan esa misma semana en el checkout alojado.
3. **Textos de consentimiento (ventas), #12 de operaciones y mi tarea de textos legales:** se fusionan en una sola tarea en S2. Preparo yo los borradores, también los consentimientos de la newsletter, los formularios, los testimonios y las entrevistas.
4. **El hueco «sin asignar» de S1** lo piden ventas (1 h) y marketing (0,5 h). Mi reestimación libera 0,5 h en S1.
5. **Presupuesto:** ninguna área propone más gasto que el dominio (≈ 10–12 €/año) y la consulta (≤ 80 €): **≤ 92 € comprometidos** y un coste fijo de ≈ 1 €/mes. Los posibles gastos recurrentes futuros (correo transaccional de F2, una newsletter por encima del plan gratuito) se escalan antes de contratarlos.

## Ajustes a mi propuesta

En S1–S8 bajo de 9 h a **4,5 h**, dentro del carril legal de operaciones (5,5 h):

| Semana | Tarea | h | Carril de operaciones |
|---|---|---|---|
| S1 | Búsqueda de marca en TMview y la OEPM (0,5) · revisar el dossier y pedir la cita (0,5; es la #3) | 1 | 1,5 (libero 0,5) |
| S2 | Consulta (1,5) · revisar los textos legales en ES y los consentimientos (1; es la #12) | 2,5 | 2,5 |
| S3 | Revisar la versión EN de los textos y el registro de actividades (borradores míos) | 0,5 | 0,5 |
| S4 | Condiciones de la beta, casilla de testimonios y privacidad de Tally y de los directos (antes, 1 h) | 0,5 | 0,5 |
| S6 | — | 0 | 0,5 (libero 0,5) |

- **Fuera de S1–S8:** elegir el MoR (1,5 h, S9–S10) · revisar las condiciones de venta en el checkout de test (1 h, la misma semana) · revisar la puerta (1 h, S14).
- **Precios:** mantengo como referencia para la encuesta C1 a 39 €, C2 a 49 € y el pack a 69 €. La cohorte conserva gratis el C1 (ventas) y el −40 % pasa al C2 y al pack, para toda la cohorte y sin condiciones.
- **Lista mínima para cobrar:** baja de 300 a 200, porque ahora la previsión se apoya en las 15 intenciones explícitas.
- **Dossier de la consulta:** añadiré una pregunta: dar acceso gratuito y permanente a una cohorte que además aporta feedback y testimonios, ¿puede verse como una contraprestación? ⚖️ La presencia pública ya la cubre la pregunta 1.

## Mi top 3 para el comité

1. **Nada público hasta tener la respuesta escrita de la consulta** (cita pedida en S1 y consulta en S2), y apertura conjunta en S3: web, landing, perfiles, primer post y repo.
2. **Licencias según la opción A, validadas en S1** (blog CC BY-NC-SA, lecciones con derechos reservados, código MIT) y lecciones en un repo privado: protege lo que se va a vender y desbloquea a producto y a contenidos.
3. **Una sola puerta para cobrar** (3 bloques, revisión en S14): suelo de demanda (≥ 15 intenciones y lista ≥ 200), donaciones apagadas, cobro con un MoR y alta alineada con el lanzamiento ⚖️.

## Fuentes consultadas

- https://help.brevo.com/hc/en-us/articles/208580669 (FAQ oficial) · consultada el 2026-10-05 · plan gratuito: hasta 100.000 contactos, 300 envíos/día, 2.000 contactos en automatizaciones y el sello «Sent with Brevo» en los envíos. Algunas webs de terceros dan otras cifras.
- Normativa de referencia, sin consulta web hoy (verificar en el BOE y en la AEPD): LSSI arts. 10 y 22.2 (este último cubre cualquier almacenamiento en el dispositivo, no solo las cookies) · LPI art. 32 (cita con fines docentes) · RGPD arts. 28 y 30.
