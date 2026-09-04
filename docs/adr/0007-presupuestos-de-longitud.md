# ADR-0007 · Cada fichero de reunión tiene un presupuesto de longitud

- **Estado:** aceptada
- **Fecha:** 2026-09-04

## Contexto

En el prototipo, la reunión de arranque produjo siete rondas 1 de 330–575 líneas (unas 3.000 en total), siete rondas 2 de 140–300 líneas y un acta de casi 800. El coste crece de forma casi cuadrática: en la ronda 2, **cada** agente lee **todas** las rondas 1, y dirección lee todo para redactar el acta.

Además, un acta de 800 líneas no la lee nadie con atención, y la persona fundadora tiene 20 h/semana.

## Decisión

1. **Presupuestos de longitud** por tipo de fichero en el protocolo (§9), más generosos solo en la reunión de arranque.
2. **Formato rápido** (ronda 1 → acta) por defecto para las reuniones semanales.
3. **Asistentes mínimos:** dirección y operaciones siempre; el resto, solo si tienen algo que decidir o aportar.
4. **Modo económico** opcional en `/reunion` (`--economica`): las rondas se ejecutan con un modelo más barato y el acta con el modelo por defecto.
5. Se mide: la tabla «Salud del comité» de `metricas.md` registra ejecuciones y líneas por reunión.

## Alternativas consideradas

| Alternativa | Por qué no |
|---|---|
| Resumir las rondas 1 antes de la ronda 2 | Otro paso que puede perder matices o las objeciones; el presupuesto ataca la causa |
| Que la ronda 2 lea solo las rondas «relevantes» | Lo relevante no se sabe hasta leerlo: las tensiones aparecen donde no se esperan |
| Bajar a un modelo pequeño todas las reuniones | El acta y los desempates necesitan el mejor criterio disponible |

## Consecuencias

- **Positivas:** coste más predecible; actas que se pueden leer en 10 minutos; obliga a los agentes a priorizar.
- **Negativas y riesgos:** se pierde detalle. → Los anexos van a `empresa/areas/<rol>/` como borrador, y el acta enlaza.
- **Cómo sabremos si fue un error:** si una decisión se toma mal porque el detalle que hacía falta no cabía, se sube el presupuesto de ese fichero.
