# ADR-0004 · Lo calculable lo resuelve código, no el modelo

- **Estado:** aceptada
- **Fecha:** 2026-09-22

## Contexto

En el prototipo, la Secretaría y los agentes hacían a mano operaciones que tienen una única respuesta correcta:

- calcular en qué semana estamos a partir de la fecha;
- asignar el siguiente ID libre y sustituir los `T-?` del acta;
- sumar las horas por semana para aplicar el veto de capacidad;
- comprobar que cada tarea tiene sus campos y no pasa de 4 h.

Un modelo de lenguaje hace estas cosas bien casi siempre, y ese «casi» es el problema: un error de fecha o de suma no salta a la vista y contamina las decisiones siguientes. Además, cada cálculo a mano consume contexto.

## Decisión

Un único script, **`herramientas/pba.py`**, con la librería estándar de Python y tests, que la Secretaría y las skills invocan en lugar de calcular:

| Comando | Resuelve |
|---|---|
| `semana` | Semana actual (o de una fecha) y su rango |
| `ids` | Último ID usado y siguiente libre |
| `capacidad` | Horas comprometidas y propuestas por semana frente a la capacidad |
| `check` | Formato de tareas y decisiones, IDs, referencias y capacidad |
| `registrar` | Paso de tareas y decisiones del acta al backlog con IDs definitivos |

Los parámetros numéricos (inicio de S1, capacidad, máximo por tarea) salen de `empresa/config.toml`, para que no estén repetidos en varios sitios.

## Alternativas consideradas

| Alternativa | Por qué no |
|---|---|
| Seguir pidiéndoselo al modelo con instrucciones más detalladas | Reduce los errores, no los elimina, y no se puede testear |
| Un servidor MCP propio | Más piezas que mantener para cinco funciones; un script es más fácil de leer y de testear |
| Node o un lenguaje compilado | Python viene instalado en casi cualquier sistema y no necesita dependencias |

## Consecuencias

- **Positivas:**
  - Las respuestas son reproducibles y están cubiertas por tests.
  - El formato de los ficheros de `empresa/` pasa a ser un contrato verificable (la CI lo comprueba).
  - Es material de curso: «qué delegar en el modelo y qué no».
- **Negativas y riesgos:**
  - El formato Markdown se vuelve más rígido: un encabezado mal escrito hace que el parser no vea una tarea. → `check` avisa de lo que no entiende.
  - Requiere Python 3.11 o superior (`tomllib`).
- **Cómo sabremos si fue un error:** si mantener el parser al día con el formato cuesta más de 1 h al mes.
