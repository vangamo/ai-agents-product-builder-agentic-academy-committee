# Ronda 1 · contenidos · Arranque 2026-10-05

## Resumen

- Mantengo los dos cursos en su orden (1 = del chatbot al primer agente; 2 = agente con especificaciones y tests). Curso 1: 4 módulos × 3 lecciones y un proyecto (web personal de una página, publicada), en HTML y CSS sin framework para que se vea lo que hay debajo.
- Beta por entregas: M1–M2 listos al cierre de S5, así que la beta puede abrir como pronto en S6; M3 en S7 y M4 en S9–S10. Contenidos cuesta ≈ 6,2 h/semana (49,25 h en S1–S8).
- Blog: 4 pilares y 12 ideas; quincenal mientras se produce el curso, con la mitad de los posts derivados de lecciones. Primero texto; infografía en S8; vídeo corto solo para demos.
- Bilingüe: original en ES; blog en ES+EN desde el primer post; curso en EN tras la beta. Guía de estilo y glosario en borrador.

## Diagnóstico

- **Hecho:** no hay contenido ni plantillas. La fundadora escribe (D-005) y su punto fuerte es el texto. **Opinión:** la capacidad es la restricción que manda; en 8 semanas no caben a la vez 12 lecciones, un blog semanal y la versión EN, así que hay que elegir.
- **Hecho** (búsqueda del 2026-10-05): la oferta de «web con IA» en español promete «sin programar» o «en minutos» (Platzi, Udemy, Alison). No encontré ningún curso gratuito en ES que enseñe a revisar lo que genera la IA ni a trabajar con agentes de código. Ahí está el hueco del enfoque «con criterio».
- **Hecho** (fuentes secundarias del 2026-10-05, con cifras contradictorias): los planes gratuitos de agentes de código cambiaron en junio de 2026. Copilot pasó a créditos con poca asignación gratuita y se recortó el acceso gratuito a Gemini CLI. **Consecuencia:** el curso 1 no puede depender de ningún agente gratuito concreto.
- [Supuesto] Una lección de texto con práctica cuesta 3 h en ES, y adaptarla a EN, ≈ 25 % de ese tiempo. Se calibra con la lección piloto de S1.
- [Supuesto] Público prioritario: personas que empiezan a construir con IA (producto, diseño, reconversión profesional, estudiantes) y quieren entender lo que hacen. Si dirección elige desarrolladores con experiencia, el curso 1 se queda corto y habrá que subirle el nivel.

## Propuestas por punto de la agenda

### Punto 2 · Catálogo, cursos y blog (lidero)

#### 2.1 Los cursos 1 y 2 se mantienen, en ese orden

- **Propuesta:** curso 1 de iniciación, sin programación previa. Curso 2 de iniciación-intermedio: pide el curso 1 o HTML y CSS básicos. El curso 1 incluye Git y un primer contacto con un agente, para que el curso 2 empiece ya en «delegar con especificaciones».
- **Por qué:** es la escalera chatbot → agente. El curso 1 llega al público más amplio y su proyecto, una web personal, sirve de portafolio al alumnado (y a la fundadora).
- **Alternativas descartadas:** invertir el orden (el curso 2 exige JavaScript); fusionarlos (más de 25 lecciones y peor finalización); hacer el curso 1 con Astro o con un constructor sin código (taparía lo que hay debajo; Astro tendrá su propio curso futuro).

#### 2.2 Temario del curso 1 · «Tu web personal con IA, con criterio»

Títulos alternativos: «Tu primera web con IA (entendiendo lo que haces)» · «De la idea a tu web publicada, con IA y criterio». 12 lecciones de 10–15 min, cada una con una práctica de ≤ 20 min: ≈ 8–10 h de trabajo del alumnado en 4 semanas. 🔧 marca los momentos de «abrir el capó».

| Lección | Al terminar, serás capaz de… | Práctica |
|---|---|---|
| **M1 · Entender antes de construir** | | |
| L1.1 Qué vas a construir y cómo trabajarás con la IA | describir el proyecto y el método (especificar → pedir → revisar) | Objetivo de tu web y 3 webs de referencia |
| L1.2 🔧 Qué pasa desde que escribes una URL | explicar qué hacen el navegador, el servidor, el HTML, el CSS y el JS | Inspeccionar una web con DevTools y cambiar un texto en local |
| L1.3 🔧 Qué es un modelo de lenguaje y por qué se equivoca | anticipar los errores típicos de la IA | Pedir el mismo HTML dos veces, comparar y localizar un error |
| **M2 · Construir con un chatbot** | | |
| L2.1 Especificar antes de pedir: el brief | escribir el brief de una página de tu web | Brief con plantilla |
| L2.2 HTML semántico con IA | generar el HTML, leerlo y explicar cada bloque | index.html a partir del brief, sin errores en el validador del W3C |
| L2.3 CSS con criterio: primero el móvil | pedir y ajustar estilos responsive y legibles | La web se ve bien en 3 anchos de pantalla |
| **M3 · Revisar lo que genera la IA** | | |
| L3.1 Accesibilidad esencial | detectar y corregir problemas de accesibilidad | Lighthouse y navegación con teclado; corregir 3 fallos |
| L3.2 UI/UX para una web personal | mejorar la jerarquía, la legibilidad y la llamada a la acción | Test de 5 segundos con una persona y una iteración |
| L3.3 Rendimiento, SEO básico y privacidad | optimizar imágenes y metadatos y evitar rastreadores innecesarios | Lighthouse ≥ 90 en rendimiento; Open Graph |
| **M4 · Delegar y publicar** | | |
| L4.1 Git: tu botón de deshacer | versionar cambios y revertirlos | Repositorio con 3 commits; revertir uno |
| L4.2 🔧 Del chatbot al agente de código | delegar un cambio acotado, revisar el diff y decidir, conociendo los permisos y los riesgos | Un cambio hecho con el agente y revisado; sin agente, con el chatbot y un diff a mano |
| L4.3 🔧 Publicar en Internet | publicar con HTTPS y explicar qué pasa en un despliegue | La web con URL pública en un hosting gratuito |

- **Proyecto final:** web personal de una página publicada, con su repositorio y su brief. Debe superar la checklist: validador sin errores, accesibilidad en Lighthouse ≥ 90, 3 anchos, texto alternativo en todas las imágenes y ningún secreto en el repositorio. Se acompaña de un «diario de 3 prompts»: qué pediste, qué revisaste y qué corregiste.
- **Autoevaluación y materiales:** 4 preguntas por módulo y autoevaluación del proyecto con la checklist. Repositorio plantilla, plantilla de brief, prompts comentados (buenos y malos), checklist de revisión y anexo de herramientas fechado. El anexo es la única capa que caduca: se revisa en S5 y después cada trimestre.
- **0 € para el alumnado:** todas las prácticas funcionan con cualquier chatbot gratuito. L4.2 usa ≈ 10 peticiones al agente como máximo y tiene una alternativa sin agente.
- **Cómo sabremos si funciona (beta):** ≥ 60 % de quienes empiecen L1.2 terminan la práctica de L2.3; ≥ 30 % de las personas inscritas publican su web; valoración por módulo ≥ 4/5. Si una lección acumula ≥ 3 preguntas repetidas, se reescribe.

#### 2.3 Esquema del curso 2 · «Un juego de memoria con IA: especifica, delega y prueba»

- **M1 · Especificar el juego (SDD):** reglas, criterios de aceptación y casos límite; 🔧 cómo lee un agente tu repositorio. **M2 · El JavaScript que necesitas para revisar:** estado, eventos, DOM y módulos.
- **M3 · Construir por incrementos** (una tarea = un diff = un commit) y revisión de código; 🔧 el agujero XSS de usar `innerHTML` con el nombre del jugador. **M4 · Tests de la lógica** (barajar, emparejar, fin de partida): TDD con el agente y por qué un test generado puede no probar nada. **M5 · Calidad:** accesibilidad del juego (teclado, lector de pantalla, movimiento reducido) e integración continua que ejecuta los tests.
- **Proyecto:** el juego publicado, con la especificación en el repositorio y los tests en verde en la CI. Unas 15 lecciones; se produce a partir de S10.

#### 2.4 Ideas de cursos futuros (sin detallar)

1) **Tu blog con Astro y un agente de código** (dogfooding de la web de la academia) · 2) **Un equipo de agentes con Spec-Driven Development** (el caso real de esta oficina, con su protocolo y sus guardarraíles) · 3) **Seguridad para quien construye con IA** (secretos, dependencias, OWASP básico, inyección de instrucciones en agentes) · 4) **DevOps mínimo para proyectos personales** (Git en serio, CI/CD, entornos, despliegues sin miedo) · 5) **Abrir el capó de un agente** (construir uno mínimo: herramientas, bucle, contexto, MCP).

#### 2.5 Pilares del blog y 12 ideas priorizadas

Pilares: **P1 · Abrir el capó** (conceptos duraderos, buenos para el SEO) · **P2 · Construir con criterio** (tutoriales y casos) · **P3 · Construyendo en público** (la web y la oficina: prompts, errores y decisiones; también portafolio) · **P4 · Opinión y comparativas** (con fecha de vigencia). Cada post enlaza a una lección o a un curso, con una sola llamada a la acción.

| # | Título provisional | Pilar · tipo | Conecta con | h (ES+EN) |
|---|---|---|---|---|
| 1 | Qué pasa desde que escribes una URL hasta que ves una web | P1 · concepto | C1 L1.2 (derivado) | 2 |
| 2 | Siete agentes proponen, yo decido: así dirijo mi academia | P3 · construyendo en público | Curso futuro 2 | 3,75 |
| 3 | Por qué la IA se inventa cosas (y cómo notarlo cuando programas) | P1 · concepto | C1 L1.3 (derivado) | 2 |
| 4 | Especifica antes de pedir: el brief de una página que uso | P2 · tutorial | C1 L2.1 (derivado) | 2 |
| 5 | 5 errores que comete la IA al generar HTML y cómo cazarlos | P2 · caso práctico | C1 M3 y lead magnet | 3,75 |
| 6 | Chatbot o agente de código: qué cambia cuando la IA toca tus ficheros | P1 · concepto con infografía | C1 L4.2 → C2 | 3,75 |
| 7 | Accesibilidad mínima de una web hecha con IA: 10 comprobaciones | P2 · checklist | C1 L3.1 (derivado) | 2 |
| 8 | La arquitectura de la web de la academia con Astro, y por qué | P3 · construyendo en público | Curso futuro 1 | 3,75 |
| 9 | Git para quien trabaja con agentes: tu botón de deshacer | P2 · tutorial | C1 L4.1 (derivado) | 2 |
| 10 | Cómo elijo herramienta de IA para programar sin casarme con ninguna | P4 · comparativa por criterios | Anexo de herramientas | 3,75 |
| 11 | Spec-Driven Development explicado con un juego de memoria | P2 · tutorial | C2 M1 (prelanzamiento) | 3,75 |
| 12 | El test que escribió la IA pasa… y el juego sigue roto | P4 · opinión fundamentada | C2 M4 | 3,75 |

- **Cadencia:** quincenal mientras se produce el curso 1 (posts 1–4 en S2–S8), siempre con un post de colchón ya escrito. Semanal cuando el curso esté terminado. Un post «derivado» condensa una lección ya escrita: ≈ 2 h frente a 3,75 h de uno original.
- **Cómo sabremos si funciona:** el coste real de cada post queda dentro de ± 25 % de la estimación; cada post da al menos 2 piezas para redes (marketing); los clics hacia el curso se miden con la analítica que elija producto-tecnologia. **Alternativa descartada:** blog semanal desde S2. Añade 12–15 h en S2–S8 y retrasa la beta unas 2 semanas.

#### 2.6 Formatos y coste

| Formato | Uso en S1–S8 | Coste estimado |
|---|---|---|
| Lección de texto con práctica | Curso 1 completo | 3 h (ES) |
| Post original / derivado | 4 posts en S2–S8 | 3 h / 1,5 h en ES + 0,75 h / 0,5 h en EN |
| Infografía (1 concepto, plantilla reutilizable) | Plantilla y 1 infografía en S8 | 1,5 h la plantilla; 1 h cada infografía |
| Vídeo corto de pantalla (2–4 min, subtitulado) | 1, para L4.2, en S9 | 2 h |
| Directo «revisión en vivo» (45 min) | Quincenal desde S7 | 2,5 h (preparación, directo y resumen) |
| Lección completa en vídeo · ejercicio interactivo (React o Vue) | No en esta fase | 5–8 h · ≥ 4 h de desarrollo |

- **Propuesta:** primero texto. Infografía para los 4 conceptos de «abrir el capó». Vídeo solo donde ver el proceso aporta algo (el agente y la publicación). Directo: 15 min de concepto, 30 min revisando 2–3 webs del alumnado (con su permiso) y 15 min de preguntas. Cada lección termina con un reto opcional para compartir. **Alternativa descartada:** curso en vídeo; cuesta 2–3 veces más y hoy no es el punto fuerte de la fundadora.

#### 2.7 Flujo bilingüe ES/EN

- **Propuesta:** original en ES [Supuesto: es el idioma más cómodo y el público prioritario es hispanohablante]. La versión EN parte de un borrador asistido por IA, con el glosario en el prompt, y pasa una revisión humana con la checklist de localización (términos, ejemplos, enlaces, texto alternativo, título, slug y meta propios). Código, nombres y commits en inglés en las dos versiones, para tener un solo repositorio por curso. Blog: EN la misma semana. Curso: EN tras cerrar la beta (S10 en adelante), porque el feedback cambiará las lecciones.
- **Cómo sabremos si funciona:** la versión EN cuesta ≤ 25 % del tiempo del original; la revisión no encuentra ningún término fuera del glosario.
- **Alternativas descartadas:** hacerlo todo a la vez (se traduciría dos veces lo que la beta va a cambiar); traducción literal sin revisión (calidad y SEO pobres).
- La guía de estilo, la estructura tipo de lección y de post, el flujo detallado y el glosario están en `empresa/areas/contenidos/guia-estilo-glosario.md` (borrador, no validado).

### Puntos 1, 3 y 4 · Lo que afecta a contenidos (aporto)

- **P1 · Cómo se nota el criterio:** en el curso 1, 4 momentos 🔧, la checklist de revisión, los permisos del agente y ningún secreto en el repositorio. En el curso 2, la especificación antes que el código, la revisión de diffs, el XSS, los tests y la integración continua.
- **P1 · Diferenciación frente a «sin programar» o «en minutos»:** prometemos entender y revisar, no velocidad. Nunca prometemos que se pueda «sin saber nada». El nivel del catálogo depende del público que elija dirección.
- **P3 · Lead magnet:** «Checklist de revisión de webs hechas con IA», en ES+EN, 2 h en S5. Es la base de M3 y del post 5.
- **P3 · Beta por entregas:** abre con M1–M2 y publica un módulo cada ≈ 2 semanas. Solo se anuncia lo que ya está producido, con 1 semana de margen. Necesito una valoración por lección (una pregunta de 1 a 5 y un campo libre) y el registro de las preguntas repetidas.
- **P4 · Formato:** plantillas en Markdown con frontmatter (`title`, `objetivo`, `duracion`, `lang`, `capa_caduca`, `ultima_revision`), compatibles con las colecciones de contenido de Astro. L4.3 usa el mismo tipo de hosting gratuito que la academia (dogfooding).
- **P4 · Construyendo en público:** un diario de construcción de 3–5 líneas por sesión (prompt clave, error, decisión), unos 10 min por sesión. Es la materia prima de los posts 2 y 8 y del curso futuro 2.

### Punto 6 · Plan de 8 semanas (aporto)

| S | Lecciones (ES) | Blog (ES+EN) | Otros | h |
|---|---|---|---|---|
| S1 | L1.2 piloto (3) | — | Validar la guía y el glosario y crear las plantillas (1,5) | 4,5 |
| S2 | L1.3 (3) | Post 1 (2) | — | 5 |
| S3 | L2.1 (3) | — | Web de referencia I: brief, HTML y CSS (4) | 7 |
| S4 | L2.2 (3) | Post 2 (3,75) | — | 6,75 |
| S5 | L2.3 (3), L1.1 (2,5) | — | Checklist del lead magnet (2) | 7,5 |
| S6 | L3.1 (3) | Post 3 (2) | **Puede abrir la beta con M1–M2** | 5 |
| S7 | L3.2 (3), L3.3 (3) | — | Se publica M3 | 6 |
| S8 | — | Post 4 (2) | Web de referencia II: Git, agente y publicación (3); plantilla de infografía y la de L1.2 (2,5) | 7,5 |

- En S9–S10: M4 (9 h), el vídeo de L4.2 (2 h) y la guía del proyecto final. L1.1 se escribe al cerrar M2 porque necesita la web de referencia.
- Si la lección piloto supera las 4 h, el curso baja a 10 lecciones (L3.2 se integra en L2.3 y L3.3 pasa a lectura opcional) en lugar de retrasar la beta.

## Tareas propuestas

### T-? · Validar la guía de estilo y el glosario y crear con ellos las plantillas de lección y de post
- Área: contenidos · Propuesta por: contenidos
- Estimación: 1,5 h · Prioridad: P1 · Semana: S1
- Depende de: —
- Hecho cuando: la guía y el glosario quedan aceptados o con los cambios anotados, y existen las dos plantillas en Markdown con su frontmatter y su estructura tipo.
- Por qué: usar la misma estructura, el mismo tono y los mismos términos desde la primera pieza, y poder medir las horas por pieza.

### T-? · Escribir la lección piloto L1.2 «Qué pasa desde que escribes una URL» (ES)
- Área: contenidos · Propuesta por: contenidos
- Estimación: 3 h · Prioridad: P1 · Semana: S1
- Depende de: T-? (plantillas)
- Hecho cuando: el borrador está completo, con práctica, comprobación y caja 🔧, y revisado con la checklist de la guía; las horas reales están registradas con `/progreso`.
- Por qué: calibrar el coste real por lección (hipótesis: ≤ 3,5 h) antes de fijar la fecha de la beta.

### T-? · Escribir la lección L1.3 «Qué es un modelo de lenguaje y por qué se equivoca» (ES)
- Área: contenidos · Propuesta por: contenidos
- Estimación: 3 h · Prioridad: P1 · Semana: S2
- Depende de: T-? (lección piloto L1.2)
- Hecho cuando: el borrador está completo, con práctica, comprobación y caja 🔧, y aplica los ajustes que haya dejado la piloto.
- Por qué: completar M1 a tiempo para que la beta pueda abrir en S6.

### T-? · Escribir el post 1, derivado de L1.2, y adaptarlo a EN
- Área: contenidos · Propuesta por: contenidos
- Estimación: 2 h · Prioridad: P2 · Semana: S2
- Depende de: T-? (lección piloto L1.2)
- Hecho cuando: las versiones ES y EN están listas para publicar, con texto alternativo y el glosario aplicado, y están anotadas las horas de la adaptación a EN.
- Por qué: tener el primer post listo cuando abra la web y medir lo que cuestan de verdad un derivado y la adaptación (hipótesis: EN ≤ 25 %).

## Coste de mis propuestas

| Semana | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | Total |
|---|---|---|---|---|---|---|---|---|---|
| Horas | 4,5 | 5 | 7 | 6,75 | 7,5 | 5 | 6 | 7,5 | 49,25 |

## Dependencias y peticiones a otras áreas

- **A direccion-estrategica (S1):** el público prioritario. Si son desarrolladores con experiencia, subo el nivel del curso 1.
- **A producto-tecnologia:** confirmar en S1 el formato del contenido (Markdown o MDX con frontmatter); tener lista antes de S6 la zona de cursos en abierto; recomendar el hosting de L4.3; revisar L4.2 (permisos y riesgos del agente) en S9.
- **A operaciones:** reservar ≈ 6–7 h/semana para contenidos en S2–S8 y recalibrar con las horas reales de la piloto.
- **A marketing:** sacar las piezas de redes de cada post y lección sin pedir texto nuevo; aceptar el blog quincenal hasta que el curso 1 esté completo; tener la marca lista para la plantilla de infografía antes de S8.
- **A ventas-comunidad:** beta por entregas, formulario de valoración por lección y consentimiento del alumnado para enseñar sus webs en los directos.
- **A finanzas-legal:** la licencia de los materiales (propuesta: textos CC BY-NC-SA y código MIT) y el uso de capturas de herramientas de terceros ⚖️.

## Riesgos

- Una lección cuesta más de 4 h → recortar a 10 lecciones antes que retrasar la beta; se decide en la semanal de S2 con los datos de la piloto.
- La capa de herramientas caduca (ya cambió en junio de 2026) → anexo fechado, prácticas que funcionan con cualquier chatbot gratuito y revisión en S5.
- Retrasos en la beta por entregas → anunciar solo lo producido, con 1 semana de margen.
- Perfeccionismo [Supuesto] → tope de horas por pieza y un «hecho cuando» verificable.
- Seguridad en L4.2 (un agente con permisos sobre los ficheros) → carpeta aislada, permisos mínimos y revisión de producto-tecnologia.

## Preguntas para la persona fundadora

- ¿En qué idioma escribes el original y en qué orden se produce lo bilingüe? · A) original en ES y todo en ES+EN a la vez · B) original en ES, blog en ES+EN desde el primer post y curso en EN tras la beta · C) original en ES y solo ES hasta S8 · D) original en EN con el mismo orden que B · Mi recomendación: B.
- ¿La web de referencia del curso 1 es tu web personal real (portafolio) o una ficticia? · Real / Ficticia · Mi recomendación: real, si te parece bien esa exposición (da autenticidad y te sirve de portafolio a la vez).
- ¿Beta por entregas (abre en S6 con M1–M2) o con el curso completo (≈ S10)? · Mi recomendación: por entregas.
- ¿Blog quincenal mientras se produce el curso 1, o semanal aunque la beta se retrase ≈ 2 semanas? · Mi recomendación: quincenal.

## Fuentes consultadas

- https://dupple.com/learn/is-github-copilot-free · consultada el 2026-10-05 · Copilot Free: 2.000 completados al mes; el chat y el agente gastan una asignación limitada de créditos desde el cambio de facturación del 2026-06-01 (fuente secundaria).
- https://www.tembo.io/blog/gemini-cli-pricing · consultada el 2026-10-05 · el acceso gratuito a Gemini CLI se recortó en junio de 2026; las cifras de distintas fuentes secundarias se contradicen.
- https://platzi.com/cursos/paginas-web-chatgpt/ · https://www.udemy.com/course/create-a-website-with-ai-in-minutes-no-coding/ · https://alison.com/es/curso/como-crear-un-sitio-web-gratuito-con-chatgpt-canva-y-ai · consultadas el 2026-10-05 · la oferta de «web con IA» se centra en no programar y en la rapidez.
