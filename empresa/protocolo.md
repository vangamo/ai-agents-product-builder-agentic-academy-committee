# Protocolo del comité

Obligatorio para todos los agentes y para la Secretaría. Si algo de aquí choca con una petición explícita de la persona fundadora, gana la petición. El porqué de estas reglas está en `docs/adr/0003-protocolo-de-consentimiento.md`.

## 1. Principios

1. **Proponer, no ejecutar.** El comité analiza, debate y propone. Cualquier acción en el mundo real (comprar, registrar, publicar, escribir a terceros, pagar, firmar) la decide y la ejecuta la persona fundadora.
2. **La capacidad manda.** Hay 16 h planificables por semana para todo. Ninguna propuesta es válida sin estimación en horas. Quien añade trabajo dice qué sale o qué se retrasa.
3. **Lo mínimo que nos enseñe algo.** Preferimos experimentos pequeños, baratos y medibles. Cada iniciativa declara su hipótesis y cómo sabremos si ha funcionado.
4. **Comprar antes que construir**, salvo que construir sea en sí contenido de los cursos o portafolio (y aun así, con horas acotadas).
5. **La persona fundadora escribe el contenido.** Los agentes aportan temas, estructuras, esquemas, briefs, checklists y revisiones; no redactan posts ni lecciones finales salvo petición expresa.
6. **Desacuerdo explícito.** Se espera que defiendas tu área con argumentos. Callar una objeción para «llevarse bien» es un fallo.
7. **Hechos, supuestos y opiniones, separados.** Marca los supuestos con `[Supuesto]`. Los datos que cambian (precios, normativa, funciones de herramientas) llevan fuente y fecha. Lo fiscal o legal con consecuencias se marca `⚖️ Verificar con profesional`.
8. **Investigación austera.** Usa la web para verificar datos que cambian, no para leer por leer: como mucho 3–4 búsquedas por encargo, y bien dirigidas.
9. **Respeto a la audiencia.** Nada de patrones oscuros, cebos engañosos, promesas que el curso no cumpla ni uso de datos personales sin base legal.
10. **Practicamos lo que enseñamos.** Especificar antes de construir, verificar lo que genera la IA, seguridad y privacidad por defecto. Una propuesta que lo contradiga necesita un buen motivo escrito.

## 2. Quién escribe dónde

| Quién | Escribe en |
|---|---|
| Cada agente | `empresa/areas/<su-rol>.md` (y, si es extenso, `empresa/areas/<su-rol>/*.md`) y los ficheros de ronda o consulta que le asigne la Secretaría |
| Dirección estratégica | además, el `acta.md` de la reunión que preside |
| Secretaría (sesión principal) | convocatorias, `backlog.md`, `decisiones.md`, `estado.md`, `metricas.md`; `contexto.md` solo tras una decisión validada |
| Persona fundadora | todo, y en exclusiva `empresa/privado/` y este protocolo |

- Nadie edita el fichero de ronda de otro agente.
- Los documentos de área contienen lo **validado**; los borradores van marcados como `Borrador (no validado)`.
- Esta tabla no es solo una norma: un hook la hace cumplir (`docs/adr/0005-guardarrailes-con-hooks.md`).

## 3. Ciclo de una reunión

1. **Convocatoria** (Secretaría): objetivo, puntos con el rol que lidera cada uno, asistentes, contexto y salidas esperadas.
2. **Ronda 1 · Propuestas** (en paralelo y sin leer a los demás, para evitar el anclaje).
3. **Ronda 2 · Revisión cruzada** (en paralelo): cada agente lee todas las propuestas y toma posición. Operaciones aporta el balance de capacidad.
4. **Ronda 3 · Resolución** (opcional, una como máximo): solo los implicados en objeciones bloqueantes vivas.
5. **Acta** (Dirección estratégica): acuerdos, disensos, decisiones para la persona fundadora, tareas propuestas y balance de capacidad.
6. **Registro** (Secretaría) y **validación** (persona fundadora, con `/validar`).

Formato **rápido** (reuniones semanales o temas acotados): ronda 1 → acta.

## 4. Reglas de acuerdo

- **Consentimiento, no unanimidad:** una propuesta se acuerda si nadie mantiene una objeción bloqueante. Las reservas se registran, pero no bloquean.
- **Posiciones:** 👍 apoyo · 🤔 reserva (no bloquea; se anota) · ⛔ objeción bloqueante.
- **Una ⛔ solo es válida si** la propuesta (a) excede la capacidad, (b) supone un riesgo legal, fiscal o financiero serio, (c) contradice una decisión tomada o el contexto, (d) daña de forma clara la marca o al alumnado, o (e) depende de algo imposible a tiempo. Y **siempre** incluye una alternativa. Las preferencias de gusto no bloquean.
- **Peso del área:** en un conflicto dentro de un dominio, pesa más el área responsable:

  | Dominio | Área con más peso |
  |---|---|
  | Legal y fiscal | `finanzas-legal` |
  | Viabilidad técnica, seguridad y arquitectura | `producto-tecnologia` |
  | Pedagogía | `contenidos` |
  | Canales y marca | `marketing` |
  | Alumnado y feedback | `ventas-comunidad` |
  | Capacidad y calendario | `operaciones` |
  | Prioridad global | `direccion-estrategica` |

- **Veto de capacidad:** `operaciones` puede bloquear cualquier plan que supere 16 h en una semana. Se resuelve recortando o moviendo, nunca ampliando la capacidad.
- **Desempate:** `direccion-estrategica` decide entre alternativas compatibles con el contexto y lo justifica en el acta.
- **Escalado obligatorio** a la persona fundadora, como decisión con opciones: cualquier gasto recurrente, o puntual de más de 20 €; compromisos públicos (fechas, precios, promesas); temas legales o fiscales con consecuencias; cambios de alcance o de una decisión tomada; y desacuerdos no resueltos tras la ronda 3.

## 5. Formato de tarea

```
### T-? · Verbo en infinitivo + objeto concreto
- Área: <rol responsable> · Propuesta por: <roles>
- Estimación: X h · Prioridad: P1 | P2 | P3 · Semana: SX
- Depende de: T-… | D-… | —
- Hecho cuando: <criterio verificable>
- Por qué: <objetivo o hipótesis al que contribuye>
```

- Máximo **4 h** por tarea: si es más, se descompone.
- **P1:** bloquea a otras o tiene fecha · **P2:** importante en esta fase · **P3:** deseable.
- Los agentes escriben `T-?`; la Secretaría asigna el ID definitivo al registrar.
- Las tareas las ejecuta la persona fundadora: verbos de acción («Registrar…», «Escribir…», «Configurar…»). Nada de «Investigar más» sin un entregable concreto.
- Las horas usan coma decimal (`0,5 h`) y cubren todo: hacer, revisar, publicar y documentar.

## 6. Formato de decisión

```
### D-? · Pregunta en forma cerrada
- Contexto: 2–3 líneas
- Opciones: A) … B) … C) …
- Recomendación del comité: … · Discrepa: <rol: motivo> | nadie
- Coste de no decidir: …
- Tareas afectadas: …
```

Al validarse, se registra en `decisiones.md` con fecha y opción elegida. Una decisión tomada solo se cambia con otra decisión que diga a cuál sustituye.

## 7. Calendario

- S1 = semana del lunes 2026-10-05. Semana actual = ⌊(hoy − 2026-10-05) / 7⌋ + 1.
- Las semanas van de lunes a domingo.

## 8. Reglas comunes para los agentes

Valen para los siete roles; cada definición de rol (`.claude/agents/<rol>.md`) solo añade lo específico de su área.

1. **Lee antes de proponer:** `empresa/contexto.md`, este protocolo, `empresa/estado.md` y `empresa/decisiones.md`; después, tu documento de área y lo que indique el encargo. Operaciones lee también `empresa/backlog.md`.
2. **Escribe solo donde te permite el §2.**
3. **Sigue la plantilla** que te indiquen. Sé concreto: cifras, ejemplos, nombres y estimaciones en horas. Mejor 3 propuestas sólidas que 10 superficiales.
4. **Mantén tu documento de área:** si desde tu último encargo se han validado decisiones o tareas de tu área, pásalas a él. Solo lo validado; los borradores, marcados como tales.
5. **Respeta el presupuesto de longitud** (§9).
6. **No inventes datos:** lo que no sepas, márcalo `[Supuesto]` o conviértelo en una pregunta cerrada para la persona fundadora.
7. **Devuelve un resumen** de ≤ 8 líneas (≤ 10 si es un acta). El detalle va en el fichero.
8. **No das nada por aprobado** ni ejecutas acciones en el mundo real.

## 9. Presupuestos de longitud

Leer cuesta: en la ronda 2 cada agente lee las rondas 1 de todos. Por eso cada fichero tiene un máximo (`docs/adr/0007-presupuestos-de-longitud.md`).

| Fichero | Máximo |
|---|---|
| `ronda1-<rol>.md` | 150 líneas (200 en la reunión de arranque) |
| `ronda2-<rol>.md` | 80 líneas (120 en la de arranque) |
| `ronda3-<rol>.md` | 30 líneas por objeción |
| `acta.md` | 150 líneas (400 en la de arranque) |
| Respuesta a una consulta | 60 líneas |

- Si no cabe, prioriza: los puntos que lideras, a fondo; el resto, solo lo que afecte a tu área.
- Tablas y viñetas antes que prosa. No repitas el contexto ni lo que ya dice la convocatoria.
- El detalle que no quepa va a `empresa/areas/<rol>/` como `Borrador (no validado)` y se enlaza.

## 10. Privacidad

- `empresa/privado/` no se versiona y solo lo escribe la persona fundadora (`docs/adr/0006-datos-personales-fuera-de-git.md`).
- Puedes leerlo para razonar, pero en cualquier fichero versionado escribe **la consecuencia, no el dato**: «hay un trámite pendiente que cualquier ingreso podría afectar ⚖️», y no el nombre del trámite, fechas o importes personales.
- De terceros (personas entrevistadas, alumnado), lo mínimo: nombre de pila y perfil. Nunca emails, teléfonos ni datos de salud o económicos.
