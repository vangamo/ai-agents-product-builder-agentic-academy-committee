#!/usr/bin/env python3
"""pba · herramientas deterministas de la oficina del comité.

Resuelven con código lo que no debe calcular un modelo de lenguaje: fechas
y semanas, IDs y sumas de horas, validación de formato y paso de las tareas de un acta
al backlog (docs/adr/0004). Solo usan la librería
estándar de Python (3.11 o superior).

Los comandos que escriben (registrar) simulan por defecto y solo escriben
con --aplicar.

Uso:
    python3 herramientas/pba.py semana [--fecha AAAA-MM-DD] [--numero N]
    python3 herramientas/pba.py ids
    python3 herramientas/pba.py capacidad [--desde N]
    python3 herramientas/pba.py check [--estricto]
    python3 herramientas/pba.py registrar <carpeta-de-reunión> [--aplicar]

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


def plural(n: int, singular: str, plural_: str) -> str:
    return f"{n} {singular if n == 1 else plural_}"


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
# Capacidad
# --------------------------------------------------------------------------

# Lo comprometido es lo que la persona fundadora ya ha aceptado hacer.
COMPROMETIDO = {"aprobadas", "en-curso", "hechas"}


@dataclass
class Balance:
    semana: int
    comprometido: float = 0.0
    propuesto: float = 0.0

    @property
    def total(self) -> float:
        return self.comprometido + self.propuesto


def balance_capacidad(tareas: list[Item]) -> tuple[list[Balance], list[Item]]:
    """Horas por semana. Devuelve también las tareas que no se pueden contar
    (sin semana o sin estimación) para que no desaparezcan en silencio."""
    por_semana: dict[int, Balance] = {}
    sin_contar: list[Item] = []
    for t in tareas:
        if t.estado not in COMPROMETIDO | {"propuestas"}:
            continue
        if t.semana is None or t.horas is None:
            sin_contar.append(t)
            continue
        b = por_semana.setdefault(t.semana, Balance(t.semana))
        if t.estado == "propuestas":
            b.propuesto += t.horas
        else:
            b.comprometido += t.horas
    return [por_semana[s] for s in sorted(por_semana)], sin_contar


# --------------------------------------------------------------------------
# Validación del formato (check)
# --------------------------------------------------------------------------

RE_REFERENCIA = re.compile(r"\b([TD])-(\d{3,})\b")
RE_PROVISIONAL = re.compile(r"\b([TD])-(?:p\d+\b|\?)")

CAMPOS_TAREA_OBLIGATORIOS = ("Área", "Estimación", "Prioridad", "Hecho cuando")
CAMPOS_TAREA_RECOMENDADOS = ("Semana", "Depende de", "Por qué")
# Un campo puede tener variantes: la primera es la del protocolo.
CAMPOS_DECISION_PENDIENTE = ("Contexto", "Opciones", ("Recomendación del comité", "Recomendación"))


@dataclass
class Hallazgo:
    nivel: str  # "error" | "aviso"
    fichero: str
    linea: int
    mensaje: str

    def __str__(self) -> str:
        icono = "❌" if self.nivel == "error" else "⚠️"
        return f"{icono} {self.fichero}:{self.linea} · {self.mensaje}"


def _comprobar_ids(items: list[Item], texto: str, fichero: str, tipo: str) -> list[Hallazgo]:
    hallazgos = []
    vistos: dict[str, Item] = {}
    for item in items:
        if item.id in vistos:
            hallazgos.append(Hallazgo("error", fichero, item.linea, f"{item.id} está duplicado (también en la línea {vistos[item.id].linea})"))
        vistos.setdefault(item.id, item)
    declarado = ultimo_id_declarado(texto, tipo)
    maximo = max((i.numero for i in items), default=0)
    if declarado is None:
        hallazgos.append(Hallazgo("error", fichero, 1, "falta la línea «Último ID usado»"))
    elif maximo > declarado:
        hallazgos.append(Hallazgo("error", fichero, 1, f"«Último ID usado» dice {tipo}-{declarado:03d}, pero existe {tipo}-{maximo:03d}"))
    for n, linea in enumerate(texto.splitlines(), start=1):
        if RE_PROVISIONAL.search(linea):
            hallazgos.append(Hallazgo("error", fichero, n, "queda un ID provisional (T-?, T-pN, D-?, D-pN): hay que registrarlo con un ID definitivo"))
    return hallazgos


def _comprobar_referencias(item: Item, fichero: str, existentes: set[str]) -> list[Hallazgo]:
    hallazgos = []
    for m in RE_REFERENCIA.finditer("\n".join(item.lineas[1:])):
        ref = f"{m.group(1)}-{int(m.group(2)):03d}"
        if ref != item.id and ref not in existentes:
            hallazgos.append(Hallazgo("aviso", fichero, item.linea, f"{item.id} cita {ref}, que no existe"))
    return hallazgos


def comprobar(raiz: Path, config: Config) -> list[Hallazgo]:
    texto_b = leer(raiz, "backlog.md")
    texto_d = leer(raiz, "decisiones.md")
    tareas = parsear_items(texto_b, "T", ESTADOS_TAREA)
    decisiones = parsear_items(texto_d, "D", ESTADOS_DECISION)
    existentes = {i.id for i in tareas} | {i.id for i in decisiones}
    hallazgos: list[Hallazgo] = []

    hallazgos += _comprobar_ids(tareas, texto_b, "backlog.md", "T")
    for t in tareas:
        if t.estado == "?":
            hallazgos.append(Hallazgo("aviso", "backlog.md", t.linea, f"{t.id} está fuera de una sección conocida (🟡 ✅ 🔵 ✔️ ❌)"))
        if t.estado != "descartadas":
            for campo in CAMPOS_TAREA_OBLIGATORIOS:
                if t.campo(campo) is None:
                    hallazgos.append(Hallazgo("error", "backlog.md", t.linea, f"{t.id} no tiene «{campo}»"))
        if t.estado in {"propuestas", "aprobadas", "en-curso"}:
            for campo in CAMPOS_TAREA_RECOMENDADOS:
                if t.campo(campo) is None:
                    hallazgos.append(Hallazgo("aviso", "backlog.md", t.linea, f"{t.id} no tiene «{campo}»"))
        if t.horas is not None and t.horas > config.max_horas_tarea:
            hallazgos.append(Hallazgo("error", "backlog.md", t.linea, f"{t.id} estima {formato_horas(t.horas)} h: el máximo es {formato_horas(config.max_horas_tarea)} h, hay que descomponerla"))
        if t.campo("Prioridad") is not None and t.prioridad not in {"P1", "P2", "P3"}:
            hallazgos.append(Hallazgo("error", "backlog.md", t.linea, f"{t.id} tiene una prioridad que no es P1, P2 ni P3"))
        if t.estado in {"aprobadas", "en-curso"} and t.campo("Validada") is None:
            hallazgos.append(Hallazgo("aviso", "backlog.md", t.linea, f"{t.id} está aprobada pero no consta «Validada: AAAA-MM-DD»"))
        if t.estado == "hechas" and t.campo("Hecha") is None:
            hallazgos.append(Hallazgo("aviso", "backlog.md", t.linea, f"{t.id} está hecha pero no consta «Hecha: AAAA-MM-DD»"))
        hallazgos += _comprobar_referencias(t, "backlog.md", existentes)

    hallazgos += _comprobar_ids(decisiones, texto_d, "decisiones.md", "D")
    for d in decisiones:
        if d.estado == "pendientes":
            for campo in CAMPOS_DECISION_PENDIENTE:
                variantes = campo if isinstance(campo, tuple) else (campo,)
                if all(d.campo(v) is None for v in variantes):
                    hallazgos.append(Hallazgo("error", "decisiones.md", d.linea, f"{d.id} no tiene «{variantes[0]}»"))
            if d.campo("Coste de no decidir") is None:
                hallazgos.append(Hallazgo("aviso", "decisiones.md", d.linea, f"{d.id} no tiene «Coste de no decidir»"))
        elif d.estado == "tomadas" and d.campo("Fecha") is None:
            hallazgos.append(Hallazgo("error", "decisiones.md", d.linea, f"{d.id} está tomada pero no tiene «Fecha»"))
        elif d.estado == "?":
            hallazgos.append(Hallazgo("aviso", "decisiones.md", d.linea, f"{d.id} está fuera de una sección conocida (🟡 ✅)"))
        hallazgos += _comprobar_referencias(d, "decisiones.md", existentes)

    balances, _ = balance_capacidad(tareas)
    for b in balances:
        if b.comprometido > config.capacidad_h:
            hallazgos.append(Hallazgo("aviso", "backlog.md", 1, f"S{b.semana} tiene {formato_horas(b.comprometido)} h comprometidas, por encima de {formato_horas(config.capacidad_h)} h"))
    return hallazgos


# --------------------------------------------------------------------------
# Registro de un acta (registrar)
# --------------------------------------------------------------------------

RE_ENCABEZADO_PROVISIONAL = re.compile(r"^###\s+([TD])-(p\d+|\?)\s+·\s+(.*\S)\s*$")
RE_REF_PROVISIONAL = re.compile(r"\b([TD])-p(\d+)\b")
MARCAS_VACIO = {"_(ninguna)_", "_(ninguno)_"}


@dataclass
class Bloque:
    """Tarea o decisión del acta, todavía con su ID provisional."""

    tipo: str
    provisional: str  # "p1", "p2"… o "?" si el acta no los numeró
    titulo: str
    linea: int
    lineas: list[str]

    @property
    def clave(self) -> str:
        return f"{self.tipo}-{self.provisional}"


@dataclass
class PlanRegistro:
    mapa: dict[str, str]  # "T-p1" → "T-026"
    tareas: list[Bloque]
    decisiones: list[Bloque]
    acta: str  # el acta con los IDs definitivos


def extraer_bloques(texto: str) -> list[Bloque]:
    bloques: list[Bloque] = []
    actual: Bloque | None = None
    en_codigo = False
    for n, linea in enumerate(texto.splitlines(), start=1):
        if linea.lstrip().startswith("```"):
            en_codigo = not en_codigo
        m = None if en_codigo else RE_ENCABEZADO_PROVISIONAL.match(linea)
        if m:
            actual = Bloque(m.group(1), m.group(2), m.group(3), n, [])
            bloques.append(actual)
            continue
        if not en_codigo and linea.startswith("#"):
            actual = None
            continue
        if actual is not None:
            actual.lineas.append(linea)
    for b in bloques:
        while b.lineas and not b.lineas[-1].strip():
            b.lineas.pop()
    return bloques


def _sustituir(texto: str, mapa: dict[str, str]) -> str:
    return RE_REF_PROVISIONAL.sub(lambda m: mapa[f"{m.group(1)}-p{m.group(2)}"], texto)


def planificar_registro(texto_acta: str, siguiente_t: int, siguiente_d: int) -> PlanRegistro:
    """Asigna IDs definitivos en orden de aparición. No escribe nada."""
    bloques = extraer_bloques(texto_acta)
    sin_numerar = [b for b in bloques if b.provisional == "?"]
    if sin_numerar:
        lineas = ", ".join(str(b.linea) for b in sin_numerar)
        raise ErrorPBA(
            f"El acta usa T-?/D-? (líneas {lineas}). Numera los IDs provisionales "
            "(T-p1, T-p2…, D-p1…) para poder resolver las dependencias."
        )
    if not bloques:
        raise ErrorPBA("El acta no tiene tareas ni decisiones con ID provisional: ¿ya está registrada?")
    mapa: dict[str, str] = {}
    vistos: dict[str, Bloque] = {}
    for b in bloques:
        if b.clave in vistos:
            raise ErrorPBA(f"{b.clave} aparece dos veces en el acta (líneas {vistos[b.clave].linea} y {b.linea})")
        vistos[b.clave] = b
        if b.tipo == "T":
            mapa[b.clave] = f"T-{siguiente_t:03d}"
            siguiente_t += 1
        else:
            mapa[b.clave] = f"D-{siguiente_d:03d}"
            siguiente_d += 1
    citados = {f"{m.group(1)}-p{m.group(2)}" for m in RE_REF_PROVISIONAL.finditer(texto_acta)}
    sin_definir = sorted(citados - mapa.keys())
    if sin_definir:
        raise ErrorPBA(f"El acta cita {', '.join(sin_definir)}, pero no define ningún bloque con ese ID")
    return PlanRegistro(
        mapa=mapa,
        tareas=[b for b in bloques if b.tipo == "T"],
        decisiones=[b for b in bloques if b.tipo == "D"],
        acta=_sustituir(texto_acta, mapa),
    )


def bloque_definitivo(bloque: Bloque, mapa: dict[str, str], origen: str) -> str:
    lineas = [f"### {mapa[bloque.clave]} · {_sustituir(bloque.titulo, mapa)}", *bloque.lineas]
    texto = _sustituir("\n".join(lineas), mapa)
    if not re.search(r"Origen\**\s*:", texto):
        texto += f"\n- Origen: {origen}"
    return texto


def insertar_en_seccion(texto: str, emoji: str, bloques: list[str]) -> str:
    """Añade los bloques al final de la sección «## <emoji> …», quitando «_(ninguna)_»."""
    lineas = texto.splitlines()
    inicio = next((i for i, l in enumerate(lineas) if l.startswith("## ") and emoji in l), None)
    if inicio is None:
        raise ErrorPBA(f"No encuentro la sección «## {emoji} …»")
    fin = next((i for i in range(inicio + 1, len(lineas)) if lineas[i].startswith("## ")), len(lineas))
    cuerpo = [l for l in lineas[inicio + 1 : fin] if l.strip() not in MARCAS_VACIO]
    while cuerpo and not cuerpo[0].strip():
        cuerpo.pop(0)
    while cuerpo and not cuerpo[-1].strip():
        cuerpo.pop()
    seccion = [""] + (cuerpo + [""] if cuerpo else [])
    for b in bloques:
        seccion += [*b.splitlines(), ""]
    final = "\n" if texto.endswith("\n") else ""
    return "\n".join(lineas[: inicio + 1] + seccion + lineas[fin:]) + final


def actualizar_ultimo_id(texto: str, tipo: str, numero: int) -> str:
    patron = re.compile(rf"(Último ID usado:\s*){tipo}-\d+")
    if not patron.search(texto):
        raise ErrorPBA(f"Falta la línea «Último ID usado: {tipo}-…»")
    return patron.sub(lambda m: f"{m.group(1)}{tipo}-{numero:03d}", texto, count=1)


def resolver_carpeta(argumento: str, raiz: Path) -> Path:
    for candidato in (Path(argumento), raiz / argumento, raiz / "empresa" / "reuniones" / argumento):
        if (candidato / "acta.md").is_file():
            return candidato.resolve()
    raise ErrorPBA(f"No encuentro «{argumento}/acta.md» (ni en empresa/reuniones/)")


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


def cmd_capacidad(args: argparse.Namespace, raiz: Path) -> int:
    config = cargar_config(raiz)
    balances, sin_contar = balance_capacidad(cargar_tareas(raiz))
    if args.desde is not None:
        balances = [b for b in balances if b.semana >= args.desde]
    cap = config.capacidad_h
    print("| Semana | Fechas | Comprometido | Propuesto | Total | Capacidad | Holgura |")
    print("|---|---|---|---|---|---|---|")
    excedidas = []
    for b in balances:
        holgura = cap - b.total
        marca = " ⚠️" if holgura < 0 else ""
        if holgura < 0:
            excedidas.append(b.semana)
        print(
            f"| S{b.semana} | {rango_semana(b.semana, config.inicio_s1)} | {formato_horas(b.comprometido)} "
            f"| {formato_horas(b.propuesto)} | {formato_horas(b.total)} | {formato_horas(cap)} "
            f"| {formato_horas(holgura)}{marca} |"
        )
    if not balances:
        print("| — | — | 0 | 0 | 0 | " + formato_horas(cap) + " | — |")
    print()
    print("Comprometido = aprobadas + en curso + hechas. Propuesto = pendiente de /validar.")
    for t in sin_contar:
        print(f"⚠️ {t.id} no cuenta: le falta la semana o la estimación.")
    if excedidas:
        semanas = ", ".join(f"S{s}" for s in excedidas)
        print(f"⚠️ Por encima de {formato_horas(cap)} h: {semanas}. Operaciones debe proponer recorte o reprogramación.")
        return 1
    return 0


def cmd_check(args: argparse.Namespace, raiz: Path) -> int:
    config = cargar_config(raiz)
    hallazgos = comprobar(raiz, config)
    errores = [h for h in hallazgos if h.nivel == "error"]
    avisos = [h for h in hallazgos if h.nivel == "aviso"]
    for h in errores + avisos:
        print(h)
    tareas = cargar_tareas(raiz)
    decisiones = cargar_decisiones(raiz)
    print(
        f"{plural(len(tareas), 'tarea', 'tareas')} y {plural(len(decisiones), 'decisión', 'decisiones')} revisadas"
        f" · {plural(len(errores), 'error', 'errores')} · {plural(len(avisos), 'aviso', 'avisos')}"
    )
    if errores or (args.estricto and avisos):
        return 1
    return 0


def cmd_registrar(args: argparse.Namespace, raiz: Path) -> int:
    carpeta = resolver_carpeta(args.carpeta, raiz)
    origen = f"reuniones/{carpeta.name}"
    texto_b = leer(raiz, "backlog.md")
    texto_d = leer(raiz, "decisiones.md")
    if f"Origen: {origen}" in texto_b or f"Origen: {origen}" in texto_d:
        raise ErrorPBA(f"Ya hay tareas o decisiones con «Origen: {origen}»: esta acta ya se registró")
    sig_t = siguiente_id(texto_b, parsear_items(texto_b, "T", ESTADOS_TAREA), "T")
    sig_d = siguiente_id(texto_d, parsear_items(texto_d, "D", ESTADOS_DECISION), "D")
    ruta_acta = carpeta / "acta.md"
    plan = planificar_registro(ruta_acta.read_text(encoding="utf-8"), sig_t, sig_d)

    print(f"Acta: {ruta_acta.relative_to(raiz) if ruta_acta.is_relative_to(raiz) else ruta_acta}")
    for b in plan.decisiones + plan.tareas:
        print(f"  {b.clave:<6} → {plan.mapa[b.clave]} · {b.titulo}")
    if not args.aplicar:
        print("Simulación: no se ha escrito nada. Repite con --aplicar para registrar.")
        return 0

    if plan.tareas:
        texto_b = insertar_en_seccion(texto_b, "🟡", [bloque_definitivo(b, plan.mapa, origen) for b in plan.tareas])
        texto_b = actualizar_ultimo_id(texto_b, "T", sig_t + len(plan.tareas) - 1)
    if plan.decisiones:
        texto_d = insertar_en_seccion(texto_d, "🟡", [bloque_definitivo(b, plan.mapa, origen) for b in plan.decisiones])
        texto_d = actualizar_ultimo_id(texto_d, "D", sig_d + len(plan.decisiones) - 1)
    (raiz / "empresa" / "backlog.md").write_text(texto_b, encoding="utf-8")
    (raiz / "empresa" / "decisiones.md").write_text(texto_d, encoding="utf-8")
    ruta_acta.write_text(plan.acta, encoding="utf-8")

    print(
        f"Registradas {plural(len(plan.tareas), 'tarea', 'tareas')} y "
        f"{plural(len(plan.decisiones), 'decisión', 'decisiones')}; el acta ya usa los IDs definitivos."
    )
    errores = [h for h in comprobar(raiz, cargar_config(raiz)) if h.nivel == "error"]
    if errores:
        print(f"⚠️ check encuentra {len(errores)} errores tras registrar:")
        for h in errores:
            print(f"  {h}")
        return 1
    print("Siguiente paso: actualizar estado.md y validar con /validar.")
    return 0


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

    p = sub.add_parser("capacidad", help="horas comprometidas y propuestas por semana frente a la capacidad")
    p.add_argument("--desde", type=int, metavar="N", help="muestra solo desde la semana SN")
    p.set_defaults(func=cmd_capacidad)

    p = sub.add_parser("check", help="valida el formato del backlog y del registro de decisiones")
    p.add_argument("--estricto", action="store_true", help="los avisos también hacen fallar")
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("registrar", help="pasa las tareas y decisiones de un acta al backlog con IDs definitivos")
    p.add_argument("carpeta", help="carpeta de la reunión (p. ej., 2026-10-05-arranque)")
    p.add_argument("--aplicar", action="store_true", help="escribe los cambios (por defecto, solo simula)")
    p.set_defaults(func=cmd_registrar)

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
