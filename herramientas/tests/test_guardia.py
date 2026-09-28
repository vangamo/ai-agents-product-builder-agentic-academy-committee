"""Tests del hook .claude/hooks/guardia_escritura.py (matriz del protocolo §2)."""

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

RUTA_HOOK = Path(__file__).resolve().parents[2] / ".claude" / "hooks" / "guardia_escritura.py"
spec = importlib.util.spec_from_file_location("guardia_escritura", RUTA_HOOK)
guardia = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guardia)


class TestDecidir(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.raiz = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def decidir(self, ruta, agente=None, herramienta="Write"):
        entrada = {"tool_name": herramienta, "tool_input": {"file_path": str(self.raiz / ruta)}, "cwd": str(self.raiz)}
        if agente:
            entrada["agent_type"] = agente
        resultado = guardia.decidir(entrada, self.raiz)
        return resultado[0] if resultado else None

    # --- Roles del comité -------------------------------------------------

    def test_rol_escribe_su_area_y_sus_rondas(self):
        self.assertIsNone(self.decidir("empresa/areas/marketing.md", "marketing"))
        self.assertIsNone(self.decidir("empresa/areas/marketing/plan-canales.md", "marketing"))
        self.assertIsNone(self.decidir("empresa/reuniones/2026-10-05-arranque/ronda1-marketing.md", "marketing"))
        self.assertIsNone(self.decidir("empresa/reuniones/2026-10-05-arranque/ronda3-marketing.md", "marketing"))
        self.assertIsNone(self.decidir("empresa/consultas/2026-10-07-marketing-handles.md", "marketing"))

    def test_rol_no_escribe_lo_de_otros(self):
        self.assertEqual(self.decidir("empresa/areas/contenidos.md", "marketing"), "deny")
        self.assertEqual(self.decidir("empresa/reuniones/2026-10-05-arranque/ronda1-contenidos.md", "marketing"), "deny")
        self.assertEqual(self.decidir("empresa/reuniones/2026-10-05-arranque/acta.md", "marketing"), "deny")

    def test_rol_no_escribe_ficheros_de_secretaria_ni_hechos(self):
        for ruta in ("empresa/backlog.md", "empresa/decisiones.md", "empresa/estado.md", "empresa/metricas.md",
                     "empresa/contexto.md", "empresa/protocolo.md", "CLAUDE.md", ".claude/agents/operaciones.md"):
            with self.subTest(ruta=ruta):
                self.assertEqual(self.decidir(ruta, "operaciones"), "deny")

    def test_solo_direccion_escribe_el_acta(self):
        self.assertIsNone(self.decidir("empresa/reuniones/2026-10-05-arranque/acta.md", "direccion-estrategica"))

    def test_nadie_del_comite_escribe_en_privado(self):
        self.assertEqual(self.decidir("empresa/privado/situacion-personal.md", "finanzas-legal"), "deny")
        self.assertEqual(self.decidir("empresa/privado/notas.md", "general-purpose"), "deny")

    def test_subagente_fuera_del_repositorio(self):
        entrada = {"tool_name": "Write", "tool_input": {"file_path": "/etc/passwd"}, "cwd": str(self.raiz), "agent_type": "marketing"}
        self.assertEqual(guardia.decidir(entrada, self.raiz)[0], "deny")

    def test_rutas_relativas_y_con_puntos(self):
        self.assertEqual(self.decidir("empresa/areas/../backlog.md", "marketing"), "deny")
        entrada = {"tool_name": "Edit", "tool_input": {"file_path": "empresa/areas/marketing.md"}, "cwd": str(self.raiz), "agent_type": "marketing"}
        self.assertIsNone(guardia.decidir(entrada, self.raiz))

    def test_subagente_generico_solo_zonas_de_agentes(self):
        self.assertIsNone(self.decidir("empresa/reuniones/x/ronda2-contenidos.md", "general-purpose"))
        self.assertEqual(self.decidir("empresa/backlog.md", "general-purpose"), "deny")

    # --- Sesión principal (Secretaría) -----------------------------------

    def test_secretaria_escribe_su_estado(self):
        for ruta in ("empresa/backlog.md", "empresa/decisiones.md", "empresa/estado.md", "empresa/metricas.md",
                     "empresa/reuniones/2026-10-05-arranque/00-convocatoria.md"):
            with self.subTest(ruta=ruta):
                self.assertIsNone(self.decidir(ruta))

    def test_secretaria_pide_confirmacion_para_hechos_y_protocolo(self):
        self.assertEqual(self.decidir("empresa/contexto.md"), "ask")
        self.assertEqual(self.decidir("empresa/config.toml"), "ask")
        self.assertEqual(self.decidir("empresa/protocolo.md"), "ask")
        self.assertEqual(self.decidir("empresa/privado/situacion-personal.md"), "ask")

    def test_secretaria_no_edita_rondas_ni_areas(self):
        self.assertEqual(self.decidir("empresa/reuniones/2026-10-05-arranque/ronda1-marketing.md"), "deny")
        self.assertEqual(self.decidir("empresa/areas/marketing.md"), "deny")

    def test_configuracion_de_la_oficina_pide_confirmacion(self):
        self.assertEqual(self.decidir(".claude/agents/marketing.md"), "ask")
        self.assertEqual(self.decidir("README.md"), "ask")

    def test_herramientas_sin_ruta_no_intervienen(self):
        self.assertIsNone(guardia.decidir({"tool_name": "Write", "tool_input": {}}, self.raiz))


class TestEjecucion(unittest.TestCase):
    """El hook como lo ejecuta Claude Code: JSON por stdin, JSON por stdout."""

    def ejecutar(self, entrada, **entorno):
        env = {k: v for k, v in os.environ.items() if k != "PBA_MANTENIMIENTO"}
        env.update({"CLAUDE_PROJECT_DIR": "/proyecto", **entorno})
        r = subprocess.run([sys.executable, str(RUTA_HOOK)], input=entrada, capture_output=True, text=True, env=env)
        return r.returncode, r.stdout

    def test_responde_con_el_formato_de_claude_code(self):
        entrada = json.dumps({"tool_name": "Write", "tool_input": {"file_path": "/proyecto/empresa/backlog.md"}, "cwd": "/proyecto", "agent_type": "marketing"})
        codigo, salida = self.ejecutar(entrada)
        self.assertEqual(codigo, 0)
        datos = json.loads(salida)["hookSpecificOutput"]
        self.assertEqual(datos["hookEventName"], "PreToolUse")
        self.assertEqual(datos["permissionDecision"], "deny")
        self.assertIn("protocolo §2", datos["permissionDecisionReason"])

    def test_permitido_no_imprime_nada(self):
        entrada = json.dumps({"tool_name": "Write", "tool_input": {"file_path": "/proyecto/empresa/areas/marketing.md"}, "cwd": "/proyecto", "agent_type": "marketing"})
        self.assertEqual(self.ejecutar(entrada), (0, ""))

    def test_modo_mantenimiento(self):
        entrada = json.dumps({"tool_name": "Write", "tool_input": {"file_path": "/proyecto/empresa/backlog.md"}, "cwd": "/proyecto", "agent_type": "marketing"})
        self.assertEqual(self.ejecutar(entrada, PBA_MANTENIMIENTO="1"), (0, ""))

    def test_entrada_invalida_no_rompe(self):
        self.assertEqual(self.ejecutar("esto no es json"), (0, ""))


if __name__ == "__main__":
    unittest.main()
