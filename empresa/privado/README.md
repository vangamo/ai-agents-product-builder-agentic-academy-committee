# empresa/privado/ · datos que no se versionan

Esta carpeta está en `.gitignore`: **solo este README se sube al repositorio**. Aquí van los datos personales y administrativos que el comité necesita para razonar, pero que no deben acabar en git (ver `docs/adr/0006-datos-personales-fuera-de-git.md`).

## Ficheros esperados

| Fichero | Contenido | Quién lo lee |
|---|---|---|
| `situacion-personal.md` | Residencia fiscal, altas anteriores, trámites o prestaciones pendientes, comunidad autónoma… | finanzas-legal, direccion-estrategica y la Secretaría |
| `terminos-sensibles.txt` | Un término por línea (las líneas con `#` son comentarios). Palabras que nunca deben aparecer en ficheros versionados | `pba.py privacidad` |

## Reglas

- Solo la persona fundadora escribe aquí.
- Los agentes pueden leer estos ficheros, pero en los ficheros versionados escriben **la consecuencia, no el dato**. Por ejemplo: «hay un trámite pendiente que cualquier ingreso podría afectar ⚖️», y no el nombre del trámite.
- Si clonas el repositorio en otra máquina, copia esta carpeta a mano.
