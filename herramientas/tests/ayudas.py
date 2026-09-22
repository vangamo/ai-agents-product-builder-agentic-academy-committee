"""Utilidades comunes de los tests: una oficina mínima en un directorio temporal."""

from __future__ import annotations

import contextlib
import io
import os
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

HERRAMIENTAS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERRAMIENTAS))

import pba  # noqa: E402

CONFIG = """\
[calendario]
inicio_s1 = 2026-10-05

[capacidad]
total_h = 20
planificable_h = 16
max_horas_tarea = 4
"""

BACKLOG_VACIO = """\
# Backlog

> Último ID usado: T-000

## 🟡 Propuestas (pendientes de validar)

_(ninguna)_

## ✅ Aprobadas (por hacer)

_(ninguna)_

## 🔵 En curso

_(ninguna)_

## ✔️ Hechas

_(ninguna)_

## ❌ Descartadas o aparcadas

_(ninguna)_
"""

DECISIONES_VACIO = """\
# Registro de decisiones

> Último ID usado: D-000

## 🟡 Pendientes (requieren a la persona fundadora)

_(ninguna)_

## ✅ Tomadas
"""


def tarea(numero: int, titulo: str = "Hacer algo", horas: str = "1", semana: int = 1, prioridad: str = "P1", extra: str = "") -> str:
    """Bloque de tarea con el formato del protocolo §5."""
    bloque = f"""\
    ### T-{numero:03d} · {titulo}

    - Área: operaciones · Propuesta por: operaciones
    - Estimación: {horas} h · Prioridad: {prioridad} · Semana: S{semana}
    - Depende de: —
    - Hecho cuando: está hecho
    - Por qué: porque sí
    """
    return textwrap.dedent(bloque) + (textwrap.dedent(extra) if extra else "")


class OficinaTemporal(unittest.TestCase):
    """Crea empresa/ con config, backlog y decisiones en un directorio temporal."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.raiz = Path(self._tmp.name)
        (self.raiz / "empresa" / "reuniones").mkdir(parents=True)
        self.escribir("empresa/config.toml", CONFIG)
        self.escribir("empresa/backlog.md", BACKLOG_VACIO)
        self.escribir("empresa/decisiones.md", DECISIONES_VACIO)
        self._entorno = dict(os.environ)

    def tearDown(self) -> None:
        os.environ.clear()
        os.environ.update(self._entorno)
        self._tmp.cleanup()

    def escribir(self, relativa: str, contenido: str) -> Path:
        ruta = self.raiz / relativa
        ruta.parent.mkdir(parents=True, exist_ok=True)
        ruta.write_text(contenido, encoding="utf-8")
        return ruta

    def leer(self, relativa: str) -> str:
        return (self.raiz / relativa).read_text(encoding="utf-8")

    def backlog_con(self, propuestas: str = "", aprobadas: str = "", hechas: str = "", ultimo: int = 0) -> None:
        texto = BACKLOG_VACIO.replace("T-000", f"T-{ultimo:03d}")
        partes = texto.split("_(ninguna)_")
        # Orden de las secciones: propuestas, aprobadas, en curso, hechas, descartadas.
        rellenos = [propuestas, aprobadas, "", hechas, ""]
        resultado = partes[0]
        for relleno, resto in zip(rellenos, partes[1:]):
            resultado += (relleno.strip() if relleno else "_(ninguna)_") + resto
        self.escribir("empresa/backlog.md", resultado)

    def pba(self, *args: str) -> tuple[int, str]:
        """Ejecuta pba con esta raíz y devuelve (código, salida estándar + error)."""
        salida = io.StringIO()
        with contextlib.redirect_stdout(salida), contextlib.redirect_stderr(salida):
            codigo = pba.main(["--raiz", str(self.raiz), *args])
        return codigo, salida.getvalue()
