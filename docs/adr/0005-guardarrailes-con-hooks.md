# ADR-0005 · La matriz «quién escribe dónde» la hace cumplir un hook

- **Estado:** aceptada
- **Fecha:** 2026-09-28

## Contexto

El protocolo (§2) dice quién puede escribir en cada fichero: cada rol en su área y en sus rondas, dirección además en el acta, la Secretaría en el estado operativo y nadie del comité en `empresa/privado/`. En el prototipo, esta regla solo existía como texto en los prompts.

Un agente con la herramienta `Write` puede escribir en cualquier ruta. Que lo haga por error (actualizar el backlog «para ayudar», retocar la ronda de otro rol) es poco probable, pero rompe dos garantías del sistema: la autoría de cada posición y que el estado solo cambie por el circuito de validación.

Claude Code permite ejecutar un script antes de cada uso de herramienta (hook `PreToolUse`). El script recibe la ruta y, si la llamada viene de un subagente, su tipo (`agent_type`).

## Decisión

Un hook, `.claude/hooks/guardia_escritura.py`, se ejecuta antes de cada `Write`, `Edit`, `MultiEdit` y `NotebookEdit`:

| Quién | Puede escribir sin preguntar | Pide confirmación | Bloqueado |
|---|---|---|---|
| Rol del comité | su área, sus rondas, sus consultas (dirección: también el acta) | — | todo lo demás |
| Otro subagente (p. ej., `general-purpose` haciendo de rol) | áreas, rondas, actas, consultas | — | todo lo demás |
| Sesión principal (Secretaría) | `empresa/` (convocatorias, backlog, decisiones, estado, métricas) | `contexto.md`, `config.toml`, `protocolo.md`, `privado/`, todo lo que está fuera de `empresa/` | rondas y documentos de área |

- Lo que el hook bloquea vuelve al agente con el motivo y lo que sí puede escribir, para que se corrija solo.
- **Modo mantenimiento:** con `PBA_MANTENIMIENTO=1` el hook no interviene, para trabajar en la configuración de la oficina.
- El hook tiene tests (`herramientas/tests/test_guardia.py`) con la matriz completa.

## Alternativas consideradas

| Alternativa | Por qué no |
|---|---|
| Solo instrucciones en los prompts | Es lo que tenía el prototipo: no se puede verificar |
| Reglas `permissions` de `settings.json` | No distinguen qué subagente hace la llamada: un rol podría escribir en el área de otro |
| Hooks en el _frontmatter_ de cada agente | Siete copias de la misma lógica; un único hook con la matriz es más fácil de revisar y testear |
| Quitar `Write` a los agentes y que la Secretaría copie sus respuestas | La Secretaría pasaría a reescribir las posiciones de los agentes, justo lo que no debe hacer |

## Consecuencias

- **Positivas:** la autoría de las rondas y el circuito de validación están garantizados en código; los agentes que se equivocan reciben un mensaje que les dice qué hacer.
- **Negativas y riesgos:**
  - Si el hook falla al leer la entrada, deja pasar la llamada (falla abierto) para no bloquear la sesión. Los tests cubren el formato que envía Claude Code.
  - Depende de que Claude Code siga enviando `agent_type`. Si deja de hacerlo, los roles se tratarían como sesión principal: se pedirían confirmaciones extra, pero no se abriría ningún permiso de los bloqueados para la Secretaría.
  - Los hooks de proyecto solo se ejecutan tras aceptar la confianza en la carpeta.
- **Cómo sabremos si fue un error:** si en el uso diario el hook bloquea más operaciones legítimas que errores reales.
