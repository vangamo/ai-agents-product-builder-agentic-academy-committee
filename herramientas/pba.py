#!/usr/bin/env python3
"""pba · herramientas deterministas de la oficina del comité.

Resuelven con código lo que no debe calcular un modelo de lenguaje: fechas
y semanas, IDs y sumas de horas (docs/adr/0004). Solo usan la librería
estándar de Python (3.11 o superior).

Uso:
    python3 herramientas/pba.py semana [--fecha AAAA-MM-DD] [--numero N]
    python3 herramientas/pba.py ids

Opción global: --raiz <directorio> (por defecto, la raíz del repositorio).
La fecha de hoy se puede fijar con la variable de entorno PBA_HOY=AAAA-MM-DD.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path

RAIZ_POR_DEFECTO = Path(__file__).resolve().parent.parent

DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]


class ErrorPBA(Exception):
    """Error esperado (fichero ausente, formato roto…): se muestra sin traza."""


# --------------------------------------------------------------------------
# Configuración
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Config:
    inicio_s1: dt.date
    capacidad_h: float
    max_horas_tarea: float


def cargar_config(raiz: Path) -> Config:
    ruta = raiz / "empresa" / "config.toml"
    try:
        with open(ruta, "rb") as f:
            datos = tomllib.load(f)
        inicio = datos["calendario"]["inicio_s1"]
        if not isinstance(inicio, dt.date):
            inicio = dt.date.fromisoformat(str(inicio))
        capacidad = datos["capacidad"]
        return Config(
            inicio_s1=inicio,
            capacidad_h=float(capacidad["planificable_h"]),
            max_horas_tarea=float(capacidad["max_horas_tarea"]),
        )
    except FileNotFoundError as e:
        raise ErrorPBA(f"No existe {ruta}") from e
    except (KeyError, ValueError, tomllib.TOMLDecodeError) as e:
        raise ErrorPBA(f"{ruta} no tiene el formato esperado: {e}") from e


def hoy() -> dt.date:
    valor = os.environ.get("PBA_HOY")
    return dt.date.fromisoformat(valor) if valor else dt.date.today()


def leer(raiz: Path, nombre: str) -> str:
    ruta = raiz / "empresa" / nombre
    try:
        return ruta.read_text(encoding="utf-8")
    except FileNotFoundError as e:
        raise ErrorPBA(f"No existe {ruta}") from e


def formato_horas(horas: float) -> str:
    """15.25 → '15,25'; 16.0 → '16'. Coma decimal, como en el protocolo."""
    texto = f"{horas:.2f}".rstrip("0").rstrip(".")
    return texto.replace(".", ",")


# --------------------------------------------------------------------------
# Calendario
# --------------------------------------------------------------------------


def numero_semana(fecha: dt.date, inicio_s1: dt.date) -> int:
    """S1 es la semana que empieza en inicio_s1. Antes de S1: 0, -1, -2…"""
    return (fecha - inicio_s1).days // 7 + 1


def lunes_de(numero: int, inicio_s1: dt.date) -> dt.date:
    return inicio_s1 + dt.timedelta(weeks=numero - 1)


def rango_semana(numero: int, inicio_s1: dt.date) -> str:
    """Rango corto de una semana: '5–11 oct' o '26 oct–1 nov'."""
    lunes = lunes_de(numero, inicio_s1)
    domingo = lunes + dt.timedelta(days=6)
    if lunes.month == domingo.month:
        return f"{lunes.day}–{domingo.day} {MESES[domingo.month - 1]}"
    return f"{lunes.day} {MESES[lunes.month - 1]}–{domingo.day} {MESES[domingo.month - 1]}"


def describir_fecha(fecha: dt.date) -> str:
    return f"{DIAS[fecha.weekday()]} {fecha.isoformat()}"


def describir_semana(numero: int, inicio_s1: dt.date) -> str:
    texto = f"S{numero} · {rango_semana(numero, inicio_s1)}"
    if numero < 1:
        texto += " (antes de S1: montaje de la oficina)"
    return texto


# --------------------------------------------------------------------------
# Lectura del backlog y del registro de decisiones
# --------------------------------------------------------------------------

# Emoji del encabezado «## …» de cada sección → estado. Se compara sin el
# selector de variación (✔️ = ✔ + U+FE0F).
ESTADOS_TAREA = {"🟡": "propuestas", "✅": "aprobadas", "🔵": "en-curso", "✔": "hechas", "❌": "descartadas"}
ESTADOS_DECISION = {"🟡": "pendientes", "✅": "tomadas"}

RE_ENCABEZADO = re.compile(r"^###\s+([TD])-(\d{3,})\s+·\s+(.*\S)\s*$")
RE_ULTIMO_ID = re.compile(r"Último ID usado:\s*([TD])-(\d+)")


@dataclass
class Item:
    """Una tarea (T-NNN) o una decisión (D-NNN) con las líneas de su bloque."""

    tipo: str
    numero: int
    titulo: str
    estado: str
    linea: int
    lineas: list[str]

    @property
    def id(self) -> str:
        return f"{self.tipo}-{self.numero:03d}"

    @property
    def texto(self) -> str:
        return "\n".join(self.lineas)

    def campo(self, nombre: str) -> str | None:
        """Valor de «Nombre: valor» (admite negrita y varios campos por línea con «·»)."""
        m = re.search(rf"{re.escape(nombre)}\**\s*:\s*\**\s*([^·\n]*)", self.texto)
        return m.group(1).strip() if m else None

    @property
    def horas(self) -> float | None:
        m = re.search(r"Estimación\**\s*:\s*\**\s*(\d+(?:[.,]\d+)?)\s*h", self.texto)
        return float(m.group(1).replace(",", ".")) if m else None

    @property
    def prioridad(self) -> str | None:
        m = re.search(r"Prioridad\**\s*:\s*\**\s*(P\d)", self.texto)
        return m.group(1) if m else None

    @property
    def semana(self) -> int | None:
        m = re.search(r"Semana\**\s*:\s*\**\s*S(-?\d+)", self.texto)
        return int(m.group(1)) if m else None


def parsear_items(texto: str, tipo: str, estados: dict[str, str]) -> list[Item]:
    items: list[Item] = []
    estado = "?"
    actual: Item | None = None
    for n, linea in enumerate(texto.splitlines(), start=1):
        if linea.startswith("## "):
            actual = None
            estado = next((v for k, v in estados.items() if k in linea), "?")
            continue
        m = RE_ENCABEZADO.match(linea)
        if m and m.group(1) == tipo:
            actual = Item(tipo, int(m.group(2)), m.group(3), estado, n, [linea])
            items.append(actual)
            continue
        if linea.startswith("#"):
            actual = None
            continue
        if actual is not None:
            actual.lineas.append(linea)
    for item in items:
        while item.lineas and not item.lineas[-1].strip():
            item.lineas.pop()
    return items


def cargar_tareas(raiz: Path) -> list[Item]:
    return parsear_items(leer(raiz, "backlog.md"), "T", ESTADOS_TAREA)


def cargar_decisiones(raiz: Path) -> list[Item]:
    return parsear_items(leer(raiz, "decisiones.md"), "D", ESTADOS_DECISION)


def ultimo_id_declarado(texto: str, tipo: str) -> int | None:
    for m in RE_ULTIMO_ID.finditer(texto):
        if m.group(1) == tipo:
            return int(m.group(2))
    return None


def siguiente_id(texto: str, items: list[Item], tipo: str) -> int:
    declarado = ultimo_id_declarado(texto, tipo) or 0
    encontrado = max((i.numero for i in items), default=0)
    return max(declarado, encontrado) + 1


# --------------------------------------------------------------------------
# Comandos
# --------------------------------------------------------------------------


def cmd_semana(args: argparse.Namespace, raiz: Path) -> int:
    config = cargar_config(raiz)
    if args.numero is not None:
        print(describir_semana(args.numero, config.inicio_s1))
        return 0
    fecha = dt.date.fromisoformat(args.fecha) if args.fecha else hoy()
    numero = numero_semana(fecha, config.inicio_s1)
    print(f"Hoy: {describir_fecha(fecha)}")
    print(f"Semana: {describir_semana(numero, config.inicio_s1)}")
    if numero < 1:
        dias = (config.inicio_s1 - fecha).days
        print(f"Faltan {dias} días para S1 ({describir_fecha(config.inicio_s1)}).")
    return 0


def cmd_ids(args: argparse.Namespace, raiz: Path) -> int:
    codigo = 0
    for tipo, fichero, cargar, nombre in (
        ("T", "backlog.md", cargar_tareas, "Tareas"),
        ("D", "decisiones.md", cargar_decisiones, "Decisiones"),
    ):
        texto = leer(raiz, fichero)
        items = cargar(raiz)
        declarado = ultimo_id_declarado(texto, tipo)
        encontrado = max((i.numero for i in items), default=0)
        siguiente = siguiente_id(texto, items, tipo)
        print(f"{nombre + ':':<12} último declarado {tipo}-{(declarado or 0):03d} · siguiente {tipo}-{siguiente:03d}")
        if declarado is None:
            print(f"  ⚠️ {fichero} no tiene la línea «Último ID usado».")
            codigo = 1
        elif encontrado > declarado:
            print(f"  ⚠️ {fichero} contiene {tipo}-{encontrado:03d}, pero «Último ID usado» dice {tipo}-{declarado:03d}.")
            codigo = 1
    return codigo


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pba", description="Herramientas deterministas de la oficina del comité.")
    parser.add_argument("--raiz", type=Path, default=RAIZ_POR_DEFECTO, help="raíz del repositorio")
    sub = parser.add_subparsers(dest="comando", required=True)

    p = sub.add_parser("semana", help="semana actual (o de una fecha) y su rango")
    p.add_argument("--fecha", help="fecha AAAA-MM-DD (por defecto, hoy o PBA_HOY)")
    p.add_argument("--numero", type=int, help="muestra el rango de la semana SN")
    p.set_defaults(func=cmd_semana)

    p = sub.add_parser("ids", help="último ID usado y siguiente libre de tareas y decisiones")
    p.set_defaults(func=cmd_ids)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = construir_parser().parse_args(argv)
    try:
        return args.func(args, args.raiz.resolve())
    except ErrorPBA as e:
        print(f"pba: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
