import os
import unittest

from ayudas import OficinaTemporal, tarea


class TestContextoSesion(OficinaTemporal):
    def test_antes_de_la_primera_reunion(self):
        os.environ["PBA_HOY"] = "2026-09-28"
        codigo, salida = self.pba("contexto-sesion")
        self.assertEqual(codigo, 0)
        self.assertIn("lunes 2026-09-28 · semana S0", salida)
        self.assertIn("la primera es /reunion arranque", salida)
        self.assertIn("Siguientes IDs: T-001 · D-001", salida)

    def test_con_pendientes_y_reunion_antigua(self):
        os.environ["PBA_HOY"] = "2026-10-15"
        (self.raiz / "empresa" / "reuniones" / "2026-10-05-arranque").mkdir()
        self.backlog_con(
            propuestas=tarea(3, horas="1,5", semana=2),
            aprobadas=tarea(1, horas="2", semana=2, extra="- Validada: 2026-10-06\n"),
            hechas=tarea(2, horas="1", semana=2, extra="- Hecha: 2026-10-13 · Horas reales: 1 h\n"),
            ultimo=3,
        )
        codigo, salida = self.pba("contexto-sesion")
        self.assertEqual(codigo, 0)
        self.assertIn("semana S2 · 12–18 oct", salida)
        self.assertIn("0 decisiones y 1 tarea (1,5 h)", salida)
        self.assertIn("Plan de S2: 1 h hechas de 3 h comprometidas", salida)
        self.assertIn("hace 10 días", salida)
        self.assertIn("toca /reunion semanal", salida)

    def test_nunca_falla(self):
        (self.raiz / "empresa" / "backlog.md").unlink()
        codigo, salida = self.pba("contexto-sesion")
        self.assertEqual(codigo, 0)
        self.assertIn("No se pudo preparar el contexto", salida)


if __name__ == "__main__":
    unittest.main()
