# Ronda 1 · finanzas-legal · Reunión de arranque (2026-10-05)

## Resumen

- Presupuesto S1–S8: **≈ 60–95 € comprometidos** (dominio ≈ 12 €/año + una consulta profesional ≈ 50–80 €), el resto en reserva. Todo lo demás, con planes gratuitos. Coste fijo ≈ 1 €/mes.
- **Ni alta, ni ingresos, ni donaciones** hasta pasar la «puerta para cobrar»: trámite pendiente aclarado ⚖️ + demanda que cubra la cuota (≈ 205 €/mes, sin tarifa plana) + cobro probado en test + textos legales listos.
- Cobro con **Merchant of Record** (≈ 5 % + 0,50 $ por venta, sin cuota). Proveedor concreto en S6, integración solo en modo test (D-007). Stripe directo, descartado.
- Legal del día 1: aviso legal, privacidad, web sin cookies no técnicas (sin banner) y newsletter con doble opt-in. Yo preparo los borradores; la persona fundadora los revisa (2 h).

## Diagnóstico

**Hechos** (fuentes al final, consultadas el 2026-10-05)
- 0 € gastados, 0 ingresos, dominio sin registrar; presupuesto total < 150 € (`contexto.md`).
- Sin alta y probablemente sin tarifa plana ⚖️ → cuota mínima de 2026 (tramo 1, rendimientos ≤ 670 €/mes) ≈ **205,88 €/mes** (base 653,59 €; Orden PJC/297/2026). Es más que el presupuesto total, **cada mes**.
- Hay un trámite pendiente que cualquier actividad o ingreso podría afectar, quizá incluso sin alta ⚖️. Equivocarse ahí cuesta más que cualquier ingreso previsible en 2026.
- Donativos: según prensa, la DGT (V5110-26, jul-2026) trata al creador de contenido como **empresario o profesional**; el donativo voluntario y sin contrapartida no lleva IVA, pero se enmarca en una actividad (IRPF sin aclarar) ⚖️. Activar donaciones **no** es neutro.
- VeriFactu: vigente el 1-jul-2027 para autónomos (RDL 15/2025); Hacienda ha anunciado otro aplazamiento a 2028, aún sin norma publicada ⚖️. No nos afecta antes del alta.
- MoR en 2026 (fuentes secundarias): Lemon Squeezy, Paddle y Polar Starter ≈ 5 % + 0,50 $ sin cuota mensual. Stripe lanzó su propio MoR (Stripe Managed Payments) y el futuro de Lemon Squeezy es incierto.

**Supuestos**
- [Supuesto] Publicar contenido gratis, sin ingresos ni contraprestación, no obliga por sí solo al alta ⚖️ (la consulta debe confirmarlo, junto con el efecto en el trámite).
- [Supuesto] Primeras ventas posibles hacia mediados de diciembre de 2026 o enero de 2027 (beta de 1–2 meses); conversión de lista a compra del 2–4 % por lanzamiento.

**Opinión:** el riesgo financiero no es gastar 150 €, sino darse de alta sin demanda (≈ 207 €/mes de coste fijo) o cobrar algo que perjudique el trámite.

## Propuestas por punto de la agenda

### Punto 5 · Finanzas y cumplimiento (lidero)

**5.1 Presupuesto inicial y reglas de gasto**

| Concepto | Propuesta | Coste | ¿Recurrente? | Semana |
|---|---|---|---|---|
| Dominio `.com` | Registrador a precio de coste, privacidad WHOIS incluida, renovación sin subida | ≈ 11–15 €/año [verificar al comprar] | Sí, anual → escalar | S1 |
| Consulta fiscal y de Seguridad Social (45–60 min) | Gestoría o asesoría, con el dossier ya preparado | ≈ 50–80 € [Supuesto] | No (> 20 € → escalar) | S2 |
| Hosting, analítica, newsletter, formularios, email del dominio (reenvío), vídeo, diseño | Planes gratuitos | 0 € | — | S1–S4 |
| Reserva | Imprevistos | ≈ 55–90 € | — | — |

- Reglas: cada gasto se registra (proveedor, importe, ¿recurrente?) con `/progreso`. Nada de planes anuales «para ahorrar» ni de pruebas que pidan tarjeta. Un plan gratuito solo vale si permite **exportar** los datos y el **uso comercial** futuro.
- **Por qué:** caja intacta para el momento del alta. **Cómo sabremos:** gasto acumulado ≤ 100 € en S8 y coste fijo ≤ 2 €/mes hasta la puerta para cobrar.
- **Descartadas:** herramientas de pago para analítica, newsletter o cursos (coste fijo sin ingresos); registrar la marca ahora (tasa ≈ 130–150 € [Supuesto], fuera de presupuesto).

**5.2 Alta fiscal: «puerta para cobrar»** (respuesta también al criterio del punto 1)

Cuatro condiciones, todas necesarias, antes de alta e ingresos:
1. **Trámite aclarado:** resuelto, o dictamen profesional por escrito de que la actividad no lo afecta ⚖️.
2. **Demanda:** ≥ 15 personas que dicen que comprarían al precio propuesto (≈ 2 × el equilibrio si cumple la mitad) y lista ≥ 300 suscriptores [Supuesto].
3. **Cobro probado** de extremo a extremo en modo test (checkout → webhook → acceso).
4. **Legal y alta listos:** condiciones de venta, privacidad actualizada y alta en Hacienda y Seguridad Social **antes** de la primera venta. El alta y la baja surten efectos por días (hasta 3 veces al año) ⚖️ → alinear el alta con el lanzamiento.

- Si la condición 2 falla en S8–S10: ampliar la beta o abrir lista de espera; **no** darse de alta «para ver».
- Tras el alta, previsiblemente ⚖️: IRPF en estimación directa simplificada con pago fraccionado trimestral; IVA trimestral (con MoR se factura **solo al MoR**: pocas facturas, con o sin IVA español según su sede) y, si el MoR está en la UE, declaración de operaciones intracomunitarias. Epígrafe IAE a confirmar. Facturas con software VeriFactu cuando toque (la AEAT tiene una aplicación gratuita para volúmenes bajos).
- Mito a evitar: «por debajo del SMI no hace falta alta». No es una regla de la Seguridad Social: no contar con ello ⚖️.
- **Por qué:** cada mes de alta sin ventas consume más que el presupuesto entero. **Cómo sabremos:** en S8, las 4 condiciones en verde o rojo, con evidencias.
- **Descartadas:** alta al acabar la beta pase lo que pase (caja); vender «poco» sin alta (riesgo legal y para el trámite); vender en plataformas de terceros para evitar el alta (sigue siendo actividad ⚖️).

**5.3 Donaciones (seguimiento de D-007)**
- **Propuesta:** desactivadas en S1–S8; se revisan con la puerta para cobrar. Si algún día se activan: importe libre, sin recompensas ni contenido exclusivo (con contrapartida deja de ser donativo) y declaradas como indique la gestoría ⚖️.
- **Por qué:** no evitan la «actividad» ante Hacienda, pueden afectar al trámite y con audiencia cero rendirían ≈ 0 €. Riesgo alto, beneficio nulo. **Descartada:** un botón de Ko-fi o similar «solo para probar».

**5.4 Plataforma de cobro**

| Opción | Comisión (referencia 2026) | IVA del cliente y factura | Esfuerzo | Encaje |
|---|---|---|---|---|
| Lemon Squeezy / Stripe Managed Payments (MoR) | 5 % + 0,50 $ (LS); SMP: tarifa Stripe + recargo [verificar] | Los gestiona el MoR | Bajo: checkout alojado + webhook | ✅ finalista |
| Polar (MoR) | 5 % + 0,50 $ en Starter tras su cambio de 2026 | MoR | Bajo; API abierta, buen material de curso | ✅ finalista |
| Paddle (MoR) | 5 % + 0,50 $ | MoR | Medio; orientado a software: ¿acepta cursos? [Supuesto] | 🤔 |
| Gumroad (MoR) | ≈ 10 % + 0,50 $ [verificar] | MoR | Mínimo | Plan B |
| Stripe directo | ≈ 1,5 % + 0,25 € tarjetas UE [Supuesto] + Stripe Tax | **Nosotros:** IVA UE (OSS > 10.000 €/año), Reino Unido sin umbral ⚖️, una factura por venta | Alto y continuo | ❌ |
| Plataformas de cursos con cuota (Teachable, Podia…) | Cuota mensual | Varía | Bajo | ❌ coste fijo, no usa Astro |

Margen por venta con MoR (IVA 21 % incluido; comisión sobre el total [Supuesto]; 0,50 $ ≈ 0,45 €), antes de IRPF y cuota:

| PVP | IVA | Comisión | Neto |
|---|---|---|---|
| 39 € | 6,77 € | 2,40 € | **29,83 €** (76 %) |
| 49 € | 8,50 € | 2,90 € | **37,60 €** (77 %) |
| 69 € | 11,98 € | 3,90 € | **53,12 €** (77 %) |

- **Propuesta:** decidir ya el **modelo MoR** y elegir proveedor en S6 con sus páginas oficiales. Criterios: acepta cursos; ≤ 5 % + 0,50 $ sin cuota; paga a una persona física con cuenta española; modo test y webhooks; reembolsos; exportación de clientes. Integración fina (un adaptador de webhooks) para poder cambiar de proveedor.
- **Por qué:** un curso pregrabado es un servicio electrónico (IVA del país del comprador, sin exención educativa ⚖️) y el MoR es el vendedor ante el cliente: IVA mundial, facturas y reembolsos quedan fuera de nuestras 16 h. **Descartado:** Stripe directo; ~3 puntos de comisión no compensan las horas de cumplimiento.

**5.5 Precios y escenarios** (hipótesis, con ventas-comunidad)
- C1 (iniciación) **39 €**, C2 (intermedio) **49 €**, pack **69 €**, IVA incluido. Código permanente −40 % para quien complete la beta y dé feedback, sin cuentas atrás falsas. Sin suscripción hasta tener ≥ 4 cursos.
- Validación: 3 preguntas de precio en la encuesta beta (¿caro?, ¿barato?, ¿lo comprarías a X?). **No publicar precios** hasta pasar la puerta.

| Escenario mensual (coste fijo ≈ 207 €: cuota + dominio) | Ventas/mes | Neto | Resultado antes de IRPF |
|---|---|---|---|
| Pesimista | 3 C1 | 89 € | −118 €/mes |
| Base | 5 C1 + 2 C2 + 1 pack | 277 € | +70 €/mes |
| Optimista | 12 C1 + 5 C2 + 3 pack | 705 € | +498 €/mes |

- Equilibrio ≈ **7 ventas de C1 al mes**. **Cómo sabremos:** ≥ 60 % de quienes respondan la encuesta ven el precio aceptable y ≥ 15 intenciones de compra.

**5.6 Checklist legal por fases**

| # | Qué | Cuándo | Criterio mínimo |
|---|---|---|---|
| 1 | Aviso legal (ES/EN) | Antes de abrir la web | Titular con nombre y apellidos y email del dominio; completo (NIF, domicilio) tras el alta (LSSI art. 10) ⚖️ |
| 2 | Privacidad (ES/EN) | Ídem | RGPD art. 13: responsable, finalidades (newsletter, contacto, beta), bases, encargados, transferencias, plazos, derechos, reclamación a la AEPD. Base: mi borrador + Facilita RGPD |
| 3 | Cookies sin banner | Ídem | Solo técnicas; analítica sin cookies; fuentes alojadas en el sitio; vídeos que cargan al hacer clic; sin píxeles de redes |
| 4 | Newsletter | Al activar el formulario | Doble opt-in; casilla sin marcar; primera capa junto al formulario; baja en un clic; nada de importar contactos sin consentimiento (LSSI arts. 21–22); el lead magnet dice claramente que implica suscribirse ⚖️ |
| 5 | Encargados del tratamiento | Al elegir herramientas | DPA aceptado; sede UE o adhesión al Marco de Privacidad UE-EE. UU. |
| 6 | Registro de actividades de tratamiento | S3 | Una página: newsletter, contacto, beta |
| 7 | Edad mínima | Con el n.º 2 | ≥ 14 años para newsletter y beta (LOPDGDD art. 7); ≥ 18 para comprar |
| 8 | Condiciones de la beta | Antes de la beta | Gratis, duración, sin garantías, uso del feedback; testimonios solo con consentimiento expreso y revocable; en directos, avisar de la grabación y pedir permiso para publicar imagen o voz |
| 9 | Propiedad intelectual | Antes del primer post | Licencias (pregunta 5); imágenes con IA solo de herramientas que permitan uso comercial, sin imitar marcas, personajes ni personas reales, y etiquetadas; marcas de terceros solo para identificar |
| 10 | Marca | S1, antes del dominio | Búsqueda gratuita en TMview y OEPM. «Product Builder Academy» es muy descriptiva: marca débil sin logotipo distintivo ⚖️. Registro aplazado |
| 11 | Condiciones de venta | Antes de cobrar | Desistimiento de 14 días; excepción del contenido digital solo con consentimiento expreso, reconocimiento de la pérdida y confirmación en soporte duradero (TRLGDCU arts. 98 y 103 m) ⚖️. Propongo garantía voluntaria de 14 días (decidir en S7) |
| 12 | Login y pagos | Antes del login | Minimización; plan de brechas (aviso a la AEPD en 72 h, RGPD art. 33); ningún dato de tarjeta propio |

- Mientras la puerta esté cerrada, en público: «proyecto personal, beta gratuita», sin precios, sin «comprar» ni «reserva tu plaza» ⚖️.

### Punto 4 · Producto y tecnología (aporto)

- **Hosting:** plan gratuito que permita uso comercial más adelante (algunos planes «Hobby», como el de Vercel, lo prohíben [verificar términos]).
- **Analítica:** gratuita y sin cookies; nada de Google Analytics (banner y transferencias).
- **Newsletter y formularios:** DPA, exportación, doble opt-in, plan gratuito para ≥ 300 contactos [verificar límites]; mejor con sede en la UE.
- **Beta:** cursos en abierto sin cuentas → menos datos y menos textos legales. Las cuentas, solo cuando aporten algo y siempre antes de los pagos.
- **Pagos:** MoR en modo test; nunca almacenar datos de pago. **Contenido:** «Privacidad por diseño en Astro: web sin banner de cookies» es un buen post (practicamos lo que enseñamos).

### Puntos 1, 2, 3 y 6 · Lo que afecta a mi área

- **P1 · Criterio para empezar a cobrar:** la puerta de 5.2.
- **P2 · Licencias:** contenidos pide la pregunta 5; código de ejemplo bajo MIT para que el alumnado lo reutilice; los textos legales también en EN.
- **P3 · Canales y beta:** nombres de usuario después de la búsqueda de marca; sin píxeles de seguimiento; n.º 4 y 8 de la checklist en las tareas de newsletter y beta.
- **P6 · Hitos:** checklist 1–7 lista antes de abrir la web; el resto, en las tareas de abajo (S1–S8).

## Tareas propuestas

### T-? · Comprobar anterioridades de la marca en TMview y OEPM
- Área: finanzas-legal · Propuesta por: finanzas-legal
- Estimación: 0,5 h · Prioridad: P1 · Semana: S1
- Depende de: —
- Hecho cuando: resultado para «Product Builder Academy» y «Product Builder» en las clases 41 y 9 registrado con `/progreso`, con luz verde o roja para el dominio
- Por qué: no invertir en dominio, perfiles y marca ya ocupados

### T-? · Celebrar la consulta profesional con el dossier preparado
- Área: finanzas-legal · Propuesta por: finanzas-legal
- Estimación: 1,5 h · Prioridad: P1 · Semana: S2 (pedir la cita en S1)
- Depende de: D-? consulta profesional
- Hecho cuando: respuestas por escrito a las preguntas 1–4 de `empresa/areas/finanzas-legal/consulta-profesional.md` (borrador ya preparado) y sus consecuencias, no los datos, registradas con `/progreso`
- Por qué: condición 1 de la puerta; aclarar el trámite antes de que la web sea pública

### T-? · Revisar y adaptar el aviso legal, la privacidad y el texto de cookies (ES/EN)
- Área: finanzas-legal · Propuesta por: finanzas-legal
- Estimación: 2 h · Prioridad: P1 · Semana: S2 (o la semana anterior a abrir la web)
- Depende de: herramientas elegidas por producto-tecnologia · D-? licencias
- Hecho cuando: los 3 textos, con los encargados reales, están listos en el repositorio de la web y los puntos 1–7 de la checklist marcados
- Por qué: cumplir RGPD y LSSI desde el primer visitante; los borradores los preparo yo, sin horas de la fundadora

Siguientes, para el plan S3–S8 (todas de finanzas-legal; formato completo en el acta si se aprueban):
- T-? · Completar el registro de actividades de tratamiento · 0,5 h · P2 · S3 · depende de los textos legales · hecho cuando: una página (newsletter, contacto, beta), fuera del repositorio público si tiene datos personales (RGPD art. 30) ⚖️
- T-? · Revisar las condiciones de la beta y la casilla de testimonios · 1 h · P2 · S4 · depende del diseño de la beta (ventas-comunidad) · hecho cuando: publicadas en el formulario de alta a la beta
- T-? · Elegir el Merchant of Record con sus páginas oficiales · 1,5 h · P2 · S6 · depende de D-? modelo de cobro; con producto-tecnologia · hecho cuando: tabla de 3 finalistas con los criterios de 5.4, fuentes fechadas, proveedor elegido y cuenta en modo test
- T-? · Revisar las condiciones de venta y la renuncia al desistimiento en el checkout de test · 1 h · P2 · S7 · depende de T-? (MoR) · hecho cuando: el checkout de test cumple el punto 11 de la checklist
- T-? · Revisar la puerta para cobrar con los datos de la beta · 1 h · P1 · S8 · depende de T-? (consulta), T-? (MoR) y la encuesta beta · hecho cuando: 4 condiciones evaluadas con evidencias y propuesta (fecha de alta o ampliación de la beta) en la reunión semanal

## Coste de mis propuestas

| S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | Total |
|---|---|---|---|---|---|---|---|---|
| 0,5 h | 3,5 h | 0,5 h | 1 h | 0 h | 1,5 h | 1 h | 1 h | 9 h |

## Dependencias y peticiones a otras áreas

- A **producto-tecnologia** (fin de S1): proveedores de hosting, analítica, newsletter y formularios, para listarlos como encargados; que cumplan 5.1 y el punto 4. Estimación de la integración del MoR en modo test (S7–S8).
- A **ventas-comunidad** (antes de S4): las 3 preguntas de precio en la encuesta beta; los puntos 4 y 8 de la checklist en el «Hecho cuando» de sus tareas.
- A **marketing:** mensajes públicos sin precios ni llamadas a comprar hasta pasar la puerta; sin píxeles; nombres de usuario después de T-? (marca).
- A **operaciones:** reservar 3,5 h en S2 y situar la revisión de la puerta en S8. A **direccion-estrategica:** usar la puerta de 5.2 como criterio para empezar a cobrar.

## Riesgos

- Una actividad o un ingreso afecta al trámite pendiente ⚖️ → consulta en S2, donaciones apagadas y mensaje público de «proyecto personal».
- Alta sin ventas (≈ 207 €/mes) → puerta con condición de demanda; alinear el alta con el lanzamiento.
- Suscripciones «pequeñas» que se acumulan → todo recurrente se escala y se registra.
- Un plan gratuito cambia o encierra los datos → exportación como requisito; revisión en cada reunión semanal.
- El MoR cambia condiciones (incertidumbre de Lemon Squeezy) → elegir en S6 con datos frescos; integración fácil de sustituir. Textos legales de plantilla genérica → borrador propio + Facilita RGPD + repaso en la consulta.

## Preguntas para la persona fundadora

1. **D-? · ¿Apruebas el presupuesto inicial (≤ 95 €: dominio ≈ 12 €/año recurrente y consulta ≤ 80 €) y las reglas de gasto?** · Opciones: A) Sí · B) Solo el dominio · C) Nada todavía · Mi recomendación: A.
2. **D-? · ¿Cómo aclaramos el trámite y el alta?** · Opciones: A) Consulta con gestoría o asesoría fiscal y de Seguridad Social en S2 (≈ 50–80 €) · B) Primero vías gratuitas (Punto de Atención al Emprendedor y consulta escrita al organismo del trámite) y gestoría solo si queda duda · C) Esperar a que se resuelva · Mi recomendación: A; la duda mezcla fiscalidad, Seguridad Social y el trámite, y un error cuesta mucho más.
3. **D-? · ¿Adoptamos la puerta para cobrar (4 condiciones de 5.2) con las donaciones desactivadas mientras tanto?** · Opciones: A) Sí · B) Alta al acabar la beta en cualquier caso · C) Activar donaciones ya · Mi recomendación: A.
4. **D-? · ¿Cobraremos a través de un Merchant of Record?** · Opciones: A) MoR, con proveedor en S6 · B) Stripe directo · C) Gumroad · Mi recomendación: A.
5. **D-? · ¿Qué licencia usan los contenidos?** · Opciones: A) Blog CC BY-NC-SA 4.0, cursos con todos los derechos reservados y código MIT · B) Todo con derechos reservados · C) Blog CC BY 4.0 · Mi recomendación: A (se comparte con atribución y se protege lo que se venderá). Una licencia CC no se puede retirar de lo ya publicado ⚖️.
6. ¿Tienes una gestoría de confianza? · Opciones: Sí (consulta ahí) / No (busco una con consulta puntual ≤ 80 €). Y anota en `empresa/privado/situacion-personal.md` (no aquí) la comunidad autónoma y, si la sabes, la fecha prevista del trámite: afectan a impuestos autonómicos y a la puerta.
7. ¿Figurarás con nombre y apellidos y email del dominio como titular, sin domicilio hasta el alta? · Opciones: A) Sí · B) Prefiero tratarlo antes en la consulta · Mi recomendación: A ⚖️.

## Fuentes consultadas

- https://www.infoautonomos.com/blog/hacienda-retrasa-entrada-vigor-verifactu/ · consultada el 2026-10-05 · VeriFactu: 1-ene-2027 (sociedades) y 1-jul-2027 (resto), RDL 15/2025
- https://www.billeo.es/blog/retraso-verifactu-2028-que-hacer · consultada el 2026-10-05 · anuncio de aplazamiento a 2028, sin norma publicada
- https://guiafiscal.es/cuanto-pago/autonomos/670-euros-mes/ y https://www.wolterskluwer.com/es-es/expert-insights/cuotas-autonomos-2026 · consultadas el 2026-10-05 · tramo 1 de 2026: base 653,59 €, cuota ≈ 205,88 €/mes (Orden PJC/297/2026)
- https://fungies.io/merchant-of-record-pricing-guide-2026.md · consultada el 2026-10-05 · comisiones MoR 2026 (web de un competidor: verificar en páginas oficiales)
- https://alexcloudstar.com/blog/merchant-of-record-indie-saas-2026/ · consultada el 2026-10-05 · Stripe Managed Payments e incertidumbre de Lemon Squeezy
- https://www.merca2.es/2026/09/04/propinas-streamers-iva-hacienda-2448406/ · consultada el 2026-10-05 · DGT V5110-26 sobre donativos (resumen de prensa; texto original sin verificar)
- Normativa de referencia, sin consulta web hoy (verificar en BOE y AEPD): RGPD arts. 13, 30 y 33; LOPDGDD art. 7; LSSI arts. 10, 21 y 22; TRLGDCU arts. 98 y 103 m); guía de cookies y herramienta Facilita RGPD de la AEPD.
