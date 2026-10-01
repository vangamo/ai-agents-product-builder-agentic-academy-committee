# Evaluación del comité

¿El comité hace lo que dice el protocolo? Los tests de `herramientas/tests/` comprueban el código. Aquí se comprueba el **comportamiento de los agentes**, que no es determinista.

- `escenarios.md`: casos con una entrada concreta, el comportamiento esperado y cómo verificarlo.
- Los marcados como **automático** ya están cubiertos por un test; los **manuales** se ejecutan en una sesión de prueba y se revisa la salida.

## Cómo ejecutar un escenario manual

1. Trabaja en una rama o en una copia del repositorio: los escenarios escriben en `empresa/`.
2. Lanza la entrada del escenario tal cual.
3. Revisa la salida con la lista «Se espera» y anota el resultado en la tabla de `escenarios.md` (fecha, modelo, ✅/❌ y una nota si falla).
4. Descarta los cambios de `empresa/` (`git restore empresa/ && git clean -fd empresa/reuniones empresa/consultas`).

## Cuándo

- Antes de la reunión de arranque, una pasada completa.
- Tras cambiar un rol, el protocolo o una skill: los escenarios afectados.
- En cada retrospectiva (`empresa/agendas/retro.md`): los que fallaron la última vez.

Un fallo repetido se convierte en un cambio de prompt, de regla o, si se puede, en un guardarraíl en código.
