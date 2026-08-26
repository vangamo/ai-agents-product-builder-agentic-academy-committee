# ADR-0002 · El estado compartido vive en ficheros Markdown versionados

- **Estado:** aceptada
- **Fecha:** 2026-08-26

## Contexto

Los subagentes no recuerdan nada entre ejecuciones. Para que cada reunión parta de lo que se decidió en la anterior, el comité necesita una memoria compartida que:

- lean igual de bien las personas, los agentes y las herramientas;
- deje rastro de quién cambió qué y cuándo;
- no cueste dinero ni mantenimiento.

## Decisión

Todo el estado vive en `empresa/` como Markdown, con **formatos fijos** (tarea, decisión, acta) definidos en el protocolo y **un único responsable de escritura** por fichero:

| Fichero | Qué contiene | Quién escribe |
|---|---|---|
| `contexto.md` | Hechos y restricciones (fuente de verdad) | Persona fundadora, o Secretaría tras una decisión validada |
| `protocolo.md` | Reglas del comité | Persona fundadora |
| `backlog.md`, `decisiones.md`, `estado.md`, `metricas.md` | Estado operativo | Secretaría |
| `areas/<rol>.md` | Documento vivo de cada área | Ese rol |
| `reuniones/<fecha-tema>/` | Convocatoria, rondas y acta | Secretaría, cada rol y Dirección (acta) |

El historial de git hace de registro de auditoría.

## Alternativas consideradas

| Alternativa | Por qué no |
|---|---|
| Base de datos (SQLite, Notion, Airtable) | Los agentes necesitarían herramientas o MCP para leerla; se pierde el diff legible |
| Memoria del propio modelo o de la sesión | No es auditable, se pierde al compactar y no la comparten los subagentes |
| Un único fichero de estado | Se convierte en un cuello de botella y cualquier error de edición lo rompe todo |

## Consecuencias

- **Positivas:** cero infraestructura, diffs revisables, y cualquier persona entiende el estado abriendo un fichero.
- **Negativas y riesgos:**
  - El Markdown no valida nada: un formato roto pasa desapercibido. → Lo valida `pba.py check` (ADR-0004).
  - El versionado expone todo lo que se escribe. → Lo personal va fuera de git (ADR-0006).
- **Cómo sabremos si fue un error:** si `backlog.md` supera ~1.000 líneas o leerlo empieza a dominar el coste de cada reunión, habrá que archivar las tareas hechas por trimestre.
