# ADR-0001 · Un comité de subagentes de Claude Code

- **Estado:** aceptada
- **Fecha:** 2026-08-26

## Contexto

Product Builder Academy es un proyecto de una sola persona con 20 h/semana. Necesito el criterio de un equipo directivo (estrategia, contenidos, marketing, ventas, finanzas y legal, tecnología y operaciones) sin tenerlo. Un único asistente tiende a darme la razón y a mezclar puntos de vista: no aparecen las tensiones que en una empresa real frenan las malas ideas.

Restricciones: presupuesto < 150 €, nada de infraestructura que mantener y todo auditable por mí.

## Decisión

Cada área es un **subagente de Claude Code** (`.claude/agents/<rol>.md`) con un mandato, unos intereses que defender, unas métricas y unas herramientas limitadas (leer, escribir en sus ficheros y buscar en la web; sin terminal). La sesión principal hace de **Secretaría**: orquesta, pero no opina.

## Alternativas consideradas

| Alternativa | Por qué no |
|---|---|
| Un único prompt que «simule» a los siete roles | Un solo contexto se ancla en la primera opinión que escribe; los roles acaban sonando igual y no hay rondas a ciegas |
| Framework de agentes (LangGraph, CrewAI, AutoGen…) | Código, dependencias y claves de API que mantener. El valor está en el protocolo, no en el orquestador |
| Agentes en la nube o programados | Actuarían sin mí delante. Primero quiero ver cómo se comporta el comité con datos reales (ver `planning.md`, fuera de alcance) |

## Consecuencias

- **Positivas:**
  - Cada subagente tiene su propio contexto: en la ronda 1 nadie ve a los demás.
  - Los roles se editan como texto y se versionan con git.
  - Las herramientas de cada rol se limitan en su _frontmatter_: ninguno tiene terminal.
  - Montar el comité es material de los cursos de agentes: dogfooding.
- **Negativas y riesgos:**
  - Una reunión completa lanza ~15–17 ejecuciones de agentes: hay que acotar el coste (ADR-0007).
  - Las reglas escritas en un prompt se pueden incumplir: las importantes se hacen cumplir en código (ADR-0004 y ADR-0005).
  - Los agentes nuevos o editados solo se cargan al reiniciar Claude Code.
- **Cómo sabremos si fue un error:** si en tres reuniones seguidas las rondas de los siete roles dicen esencialmente lo mismo, el comité no aporta diversidad y conviene reducirlo.
