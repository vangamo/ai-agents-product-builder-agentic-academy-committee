import unittest
from pathlib import Path

from ayudas import OficinaTemporal, pba, tarea

ACTA = (Path(__file__).parent / "datos" / "acta-prueba.md").read_text(encoding="utf-8")
CARPETA = "empresa/reuniones/2026-10-05-prueba"


class TestRegistrar(OficinaTemporal):
    def setUp(self):
        super().setUp()
        self.escribir(f"{CARPETA}/acta.md", ACTA)

    def test_simulacion_no_escribe(self):
        antes = self.leer("empresa/backlog.md")
        codigo, salida = self.pba("registrar", "2026-10-05-prueba")
        self.assertEqual(codigo, 0, salida)
        self.assertIn("T-p1   → T-001 · Registrar el dominio", salida)
        self.assertIn("D-p1   → D-001", salida)
        self.assertIn("Simulación", salida)
        self.assertEqual(self.leer("empresa/backlog.md"), antes)
        self.assertEqual(self.leer(f"{CARPETA}/acta.md"), ACTA)

    def test_aplicar_registra_y_resuelve_dependencias(self):
        codigo, salida = self.pba("registrar", "2026-10-05-prueba", "--aplicar")
        self.assertEqual(codigo, 0, salida)
        backlog = self.leer("empresa/backlog.md")
        self.assertIn("### T-001 · Registrar el dominio", backlog)
        self.assertIn("- Depende de: T-001 · D-001", backlog)
        self.assertIn("- Depende de: T-002", backlog)
        self.assertIn("- Origen: reuniones/2026-10-05-prueba", backlog)
        self.assertIn("Último ID usado: T-003", backlog)
        self.assertNotIn("_(ninguna)_\n\n### T-001", backlog)
        decisiones = self.leer("empresa/decisiones.md")
        self.assertIn("### D-001 · ¿Qué herramienta de email usamos?", decisiones)
        self.assertIn("- Tareas afectadas: T-002", decisiones)
        self.assertIn("Último ID usado: D-001", decisiones)
        acta = self.leer(f"{CARPETA}/acta.md")
        self.assertNotRegex(acta, r"\b[TD]-p\d")
        self.assertIn("lista de espera en S2 (T-002)", acta)
        # El resultado pasa la validación completa.
        codigo, salida = self.pba("check", "--estricto")
        self.assertEqual(codigo, 0, salida)

    def test_las_tareas_quedan_como_propuestas(self):
        self.pba("registrar", "2026-10-05-prueba", "--aplicar")
        tareas = pba.cargar_tareas(self.raiz)
        self.assertEqual([(t.id, t.estado) for t in tareas], [("T-001", "propuestas"), ("T-002", "propuestas"), ("T-003", "propuestas")])

    def test_continua_la_numeracion_existente(self):
        self.backlog_con(aprobadas=tarea(25, extra="- Validada: 2026-10-01\n"), ultimo=25)
        codigo, salida = self.pba("registrar", "2026-10-05-prueba", "--aplicar")
        self.assertEqual(codigo, 0, salida)
        backlog = self.leer("empresa/backlog.md")
        self.assertIn("### T-026 · Registrar el dominio", backlog)
        self.assertIn("- Depende de: T-026 · D-001", backlog)
        self.assertIn("Último ID usado: T-028", backlog)
        # La tarea aprobada sigue en su sección.
        estados = {t.id: t.estado for t in pba.cargar_tareas(self.raiz)}
        self.assertEqual(estados["T-025"], "aprobadas")

    def test_no_registra_dos_veces(self):
        self.pba("registrar", "2026-10-05-prueba", "--aplicar")
        codigo, salida = self.pba("registrar", "2026-10-05-prueba", "--aplicar")
        self.assertEqual(codigo, 2)
        self.assertIn("ya se registró", salida)

    def test_referencia_sin_definir_no_escribe_nada(self):
        self.escribir(f"{CARPETA}/acta.md", ACTA.replace("- Depende de: T-p2\n", "- Depende de: T-p9\n"))
        antes = self.leer("empresa/backlog.md")
        codigo, salida = self.pba("registrar", "2026-10-05-prueba", "--aplicar")
        self.assertEqual(codigo, 2)
        self.assertIn("T-p9", salida)
        self.assertEqual(self.leer("empresa/backlog.md"), antes)

    def test_rechaza_ids_sin_numerar(self):
        self.escribir(f"{CARPETA}/acta.md", ACTA.replace("### T-p3 ·", "### T-? ·"))
        codigo, salida = self.pba("registrar", "2026-10-05-prueba")
        self.assertEqual(codigo, 2)
        self.assertIn("Numera los IDs provisionales", salida)

    def test_rechaza_ids_provisionales_duplicados(self):
        self.escribir(f"{CARPETA}/acta.md", ACTA.replace("### T-p3 ·", "### T-p2 ·"))
        codigo, salida = self.pba("registrar", "2026-10-05-prueba")
        self.assertEqual(codigo, 2)
        self.assertIn("T-p2 aparece dos veces", salida)

    def test_acta_inexistente(self):
        codigo, salida = self.pba("registrar", "no-existe")
        self.assertEqual(codigo, 2)
        self.assertIn("No encuentro", salida)


if __name__ == "__main__":
    unittest.main()
