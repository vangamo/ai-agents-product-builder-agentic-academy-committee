# Guía de estilo y glosario ES/EN · Borrador (no validado)

> Propuesta de `contenidos` para la reunión de arranque (2026-10-05). Pasa a `empresa/areas/contenidos.md` cuando la persona fundadora la valide.

## Tono

- ES: de tú, español neutro (sin regionalismos marcados), lenguaje inclusivo sin desdoblamientos («el alumnado», «la persona que…»). EN: «you», directo.
- Honesto y sin bombo: nada de «en 5 minutos» ni «sin saber nada». Solo se promete lo que la lección cumple.
- Se enseña el proceso real: prompts tal como se escribieron, errores incluidos e iteraciones.

## Estructura tipo de lección (10–15 min · 1.200–1.800 palabras)

1. **Objetivo:** «Al terminar, serás capaz de…» (un resultado observable).
2. **Por qué importa:** 2–3 frases con una situación real.
3. **Concepto:** lo duradero.
4. **Proceso real:** prompt → resultado → revisión → corrección.
5. **🔧 Abrir el capó** (si toca): cómo funciona por dentro, a la altura del alumnado.
6. **Práctica** (≤ 20 min) con su «hecho cuando».
7. **Comprobación:** checklist de 3–5 puntos.
8. **Capa que caduca:** caja con herramientas, versiones y fecha de prueba.
9. **Resumen** en 3 viñetas y enlace a la siguiente lección.

## Estructura tipo de post

- Título con un problema o una pregunta concreta.
- Gancho de un párrafo → desarrollo con un ejemplo real → «qué puedes hacer mañana».
- Una sola llamada a la acción, hacia la lección o el curso relacionado.
- Fecha de vigencia si cita herramientas.

## Frontmatter común (lecciones y posts)

`title`, `objetivo`, `duracion`, `lang` (`es` | `en`), `traduccion_de`, `capa_caduca` (lista de herramientas), `ultima_revision` (AAAA-MM-DD). Producto-tecnologia confirma que encaja con las colecciones de contenido de Astro.

## Código y prompts

- Bloques de código con el lenguaje indicado; fichero completo o diff claro, nunca fragmentos ambiguos.
- Código, nombres, comentarios y mensajes de commit en **inglés en ambas versiones**: un solo repositorio por curso.
- Los prompts se muestran en el idioma de la versión; si un prompt se ha editado para la lección, se indica.
- «Probado con <herramienta> el AAAA-MM» dentro de la caja de capa que caduca.

## Accesibilidad

- Texto alternativo en toda imagen: qué muestra y para qué sirve. El texto importante de una captura también va en el cuerpo.
- Infografías: contraste AA (≥ 4,5:1 en texto normal), nada que dependa solo del color y versión en texto debajo.
- Vídeo: subtítulos revisados (no solo automáticos) y transcripción.
- Encabezados jerárquicos y enlaces descriptivos (nunca «aquí»).

## Vigencia

- Cada lección separa el núcleo duradero de la capa que caduca.
- El anexo de herramientas de cada curso es el único sitio con nombres de planes, límites y versiones. Se revisa antes de abrir cada edición o beta y cada trimestre.

## Flujo ES → EN

1. Original en ES cerrado y revisado con la checklist.
2. Borrador EN asistido por IA, con el glosario dentro del prompt.
3. Revisión humana con la checklist de localización: términos del glosario, ejemplos y referencias culturales adaptados, enlaces a recursos en inglés, alt text traducido, título, slug y meta description propios (no literales).
4. Publicación con enlace cruzado entre versiones.

## Glosario inicial

| ES | EN | Nota |
|---|---|---|
| agente de código | coding agent | |
| chatbot | chatbot | |
| modelo de lenguaje | language model (LLM) | |
| prompt | prompt | No se traduce en ES |
| especificación | spec / specification | |
| desarrollo guiado por especificaciones | Spec-Driven Development (SDD) | La sigla SDD también en ES |
| abrir el capó | under the hood | Nombre de la caja 🔧 |
| construir en público | building in public | |
| con criterio | with judgment | Evitar «with criteria» |
| publicar / despliegue | deploy / deployment | |
| repositorio | repository (repo) | |
| commit | commit | No se traduce |
| revisión de código | code review | |
| hosting / alojamiento | hosting | «hosting» aceptado en ES |
| accesibilidad | accessibility (a11y) | |
| test / prueba | test | «test» aceptado en ES |
| ventana de contexto | context window | |
| alucinación | hallucination | Explicarla como «invención plausible» |
