"""Contrato de la configuración de Claude Code: agentes, skills y hooks."""

import json
import re
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
ROLES = {
    "direccion-estrategica", "contenidos", "marketing", "ventas-comunidad",
    "finanzas-legal", "producto-tecnologia", "operaciones",
}


def frontmatter(ruta: Path) -> dict[str, str]:
    texto = ruta.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
    if not m:
        return {}
    datos = {}
    for linea in m.group(1).splitlines():
        if ":" in linea:
            clave, valor = linea.split(":", 1)
            datos[clave.strip()] = valor.strip()
    return datos


class TestAgentes(unittest.TestCase):
    def test_estan_los_siete_roles(self):
        nombres = {p.stem for p in (RAIZ / ".claude" / "agents").glob("*.md")}
        self.assertEqual(nombres, ROLES)

    def test_frontmatter_coherente_y_sin_terminal(self):
        for ruta in (RAIZ / ".claude" / "agents").glob("*.md"):
            with self.subTest(agente=ruta.stem):
                fm = frontmatter(ruta)
                self.assertEqual(fm.get("name"), ruta.stem)
                self.assertTrue(fm.get("description"))
                herramientas = {h.strip() for h in fm.get("tools", "").split(",")}
                self.assertNotIn("Bash", herramientas, "ningún rol tiene terminal (ADR-0001)")
                self.assertIn("Write", herramientas)

    def test_cada_rol_tiene_documento_de_area_y_remite_al_protocolo(self):
        for rol in ROLES:
            with self.subTest(rol=rol):
                self.assertTrue((RAIZ / "empresa" / "areas" / f"{rol}.md").is_file())
                texto = (RAIZ / ".claude" / "agents" / f"{rol}.md").read_text(encoding="utf-8")
                self.assertIn("protocolo.md` §8", texto)

    def test_la_tabla_de_peso_del_protocolo_nombra_a_los_siete_roles(self):
        protocolo = (RAIZ / "empresa" / "protocolo.md").read_text(encoding="utf-8")
        tabla = protocolo.split("| Dominio | Área con más peso |", 1)[1].split("\n\n", 1)[0]
        citados = set(re.findall(r"\| `([a-z-]+)` \|", tabla))
        self.assertEqual(citados, ROLES)


class TestSkills(unittest.TestCase):
    def test_nombre_coincide_con_la_carpeta(self):
        for ruta in (RAIZ / ".claude" / "skills").glob("*/SKILL.md"):
            with self.subTest(skill=ruta.parent.name):
                fm = frontmatter(ruta)
                self.assertEqual(fm.get("name"), ruta.parent.name)
                self.assertTrue(fm.get("description"))

    def test_las_agendas_citadas_existen(self):
        for nombre in ("arranque", "semanal", "retro"):
            self.assertTrue((RAIZ / "empresa" / "agendas" / f"{nombre}.md").is_file())


class TestSettings(unittest.TestCase):
    def setUp(self):
        self.settings = json.loads((RAIZ / ".claude" / "settings.json").read_text(encoding="utf-8"))

    def test_los_scripts_de_los_hooks_existen(self):
        for evento, grupos in self.settings["hooks"].items():
            for grupo in grupos:
                for hook in grupo["hooks"]:
                    with self.subTest(evento=evento):
                        rutas = re.findall(r"\$CLAUDE_PROJECT_DIR/([^\"\s]+)", hook["command"])
                        self.assertTrue(rutas, hook["command"])
                        for ruta in rutas:
                            self.assertTrue((RAIZ / ruta).is_file(), ruta)

    def test_la_guardia_cubre_todas_las_herramientas_de_escritura(self):
        matchers = [g["matcher"] for g in self.settings["hooks"]["PreToolUse"]]
        cubiertas = {h for m in matchers for h in m.split("|")}
        self.assertLessEqual({"Write", "Edit", "MultiEdit", "NotebookEdit"}, cubiertas)


class TestPrivado(unittest.TestCase):
    def test_privado_esta_ignorado_salvo_el_readme(self):
        gitignore = (RAIZ / ".gitignore").read_text(encoding="utf-8")
        self.assertIn("empresa/privado/*", gitignore)
        self.assertIn("!empresa/privado/README.md", gitignore)


if __name__ == "__main__":
    unittest.main()
