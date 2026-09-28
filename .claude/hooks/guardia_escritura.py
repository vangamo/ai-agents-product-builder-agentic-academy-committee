#!/usr/bin/env python3
"""Hook PreToolUse: aplica la matriz «quién escribe dónde» del protocolo (§2).

Claude Code lo ejecuta antes de cada Write, Edit, MultiEdit o NotebookEdit y
le pasa por la entrada estándar un JSON con `tool_name`, `tool_input`, `cwd` y,
si la llamada viene de un subagente, `agent_type`. El hook responde con una
decisión de permiso (`deny` o `ask`) o no dice nada, y entonces se aplica el
flujo normal de permisos. Ver docs/adr/0005-guardarrailes-con-hooks.md.

Modo mantenimiento: con PBA_MANTENIMIENTO=1 el hook no interviene (para
trabajar en la configuración de la oficina sin avisos).
"""

from __future__ import annotations

import json
import os
import sys
from fnmatch import fnmatch
from pathlib import Path

ROLES = {
    "direccion-estrategica",
    "contenidos",
    "marketing",
    "ventas-comunidad",
    "finanzas-legal",
    "producto-tecnologia",
    "operaciones",
}

# Ficheros de hechos: solo cambian por petición de la persona fundadora o tras
# una decisión validada, así que la Secretaría siempre pide confirmación.
HECHOS = {"empresa/contexto.md", "empresa/config.toml"}
SOLO_PERSONA = {"empresa/protocolo.md"}


def permitidos_para(rol: str) -> list[str]:
    patrones = [
        f"empresa/areas/{rol}.md",
        f"empresa/areas/{rol}/*",
        f"empresa/reuniones/*/ronda[123]-{rol}.md",
        f"empresa/consultas/*-{rol}-*.md",
    ]
    if rol == "direccion-estrategica":
        patrones.append("empresa/reuniones/*/acta.md")
    return patrones


# Subagentes que no son un rol (p. ej., general-purpose haciendo de rol cuando
# los subagentes del comité no están cargados): solo zonas de agentes.
PERMITIDOS_GENERICO = [
    "empresa/areas/*",
    "empresa/reuniones/*/ronda[123]-*.md",
    "empresa/reuniones/*/acta.md",
    "empresa/consultas/*.md",
]


def ruta_del_tool(tool_input: dict) -> str | None:
    return tool_input.get("file_path") or tool_input.get("notebook_path")


def relativa(ruta: str, raiz: Path, cwd: Path) -> str | None:
    """Ruta relativa a la raíz en formato POSIX, o None si está fuera."""
    p = Path(ruta)
    if not p.is_absolute():
        p = cwd / p
    try:
        return Path(os.path.realpath(p)).relative_to(os.path.realpath(raiz)).as_posix()
    except ValueError:
        return None


def coincide(rel: str, patrones: list[str]) -> bool:
    return any(fnmatch(rel, patron) for patron in patrones)


def decidir(entrada: dict, raiz: Path) -> tuple[str, str] | None:
    """Devuelve (decisión, motivo) o None si el hook no interviene."""
    ruta = ruta_del_tool(entrada.get("tool_input") or {})
    if not ruta:
        return None
    cwd = Path(entrada.get("cwd") or raiz)
    agente = entrada.get("agent_type") or None
    rel = relativa(ruta, raiz, cwd)

    # --- Subagentes: lista blanca estricta -------------------------------
    if agente:
        if rel is None:
            return "deny", f"Un subagente no escribe fuera del repositorio ({ruta})."
        if rel.startswith("empresa/privado/"):
            return "deny", "empresa/privado/ solo lo escribe la persona fundadora (protocolo §10)."
        permitidos = permitidos_para(agente) if agente in ROLES else PERMITIDOS_GENERICO
        if coincide(rel, permitidos):
            return None
        quien = f"El rol {agente}" if agente in ROLES else f"El subagente {agente}"
        return "deny", (
            f"{quien} no puede escribir en {rel} (protocolo §2). Puede escribir en: "
            + ", ".join(permitidos)
            + ". Si necesitas que cambie otro fichero, dilo en tu respuesta y lo hará quien corresponda."
        )

    # --- Sesión principal (Secretaría) ----------------------------------
    if rel is None:
        return "ask", f"Vas a escribir fuera de la oficina ({ruta}). ¿Seguro?"
    if rel.startswith("empresa/privado/"):
        return "ask", "empresa/privado/ es de la persona fundadora. Confirma que te ha pedido este cambio."
    if rel in HECHOS:
        return "ask", f"{rel} recoge hechos: solo cambia por petición de la persona fundadora o tras una decisión validada."
    if rel in SOLO_PERSONA:
        return "ask", f"{rel} lo mantiene la persona fundadora. Confirma que te ha pedido este cambio."
    if fnmatch(rel, "empresa/reuniones/*/ronda*.md"):
        return "deny", "La Secretaría no edita los ficheros de ronda: son de cada agente (protocolo §2)."
    if rel.startswith("empresa/areas/"):
        return "deny", "Los documentos de área los edita su rol (protocolo §2). Lanza al rol con el encargo."
    if rel.startswith("empresa/"):
        return None
    return "ask", (
        f"{rel} es configuración de la oficina, no estado del comité. "
        "Para trabajar en ella sin avisos, arranca Claude Code con PBA_MANTENIMIENTO=1."
    )


def responder(decision: str, motivo: str) -> str:
    return json.dumps(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": decision,
                "permissionDecisionReason": motivo,
            }
        },
        ensure_ascii=False,
    )


def main() -> int:
    if os.environ.get("PBA_MANTENIMIENTO") == "1":
        return 0
    try:
        entrada = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        # Sin entrada legible no hay nada que decidir: se aplica el flujo normal.
        print(f"guardia_escritura: entrada no válida ({e})", file=sys.stderr)
        return 0
    raiz = Path(os.environ.get("CLAUDE_PROJECT_DIR") or entrada.get("cwd") or ".")
    resultado = decidir(entrada, raiz)
    if resultado:
        print(responder(*resultado))
    return 0


if __name__ == "__main__":
    sys.exit(main())
