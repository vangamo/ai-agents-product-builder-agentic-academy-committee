import datetime as dt
import os
import unittest

from ayudas import OficinaTemporal, pba, tarea

S1 = dt.date(2026, 10, 5)


class TestNumeroSemana(unittest.TestCase):
    def test_s1_va_de_lunes_a_domingo(self):
        self.assertEqual(pba.numero_semana(dt.date(2026, 10, 5), S1), 1)
        self.assertEqual(pba.numero_semana(dt.date(2026, 10, 11), S1), 1)
        self.assertEqual(pba.numero_semana(dt.date(2026, 10, 12), S1), 2)

    def test_semanas_posteriores(self):
        self.assertEqual(pba.numero_semana(dt.date(2026, 11, 5), S1), 5)
        self.assertEqual(pba.numero_semana(dt.date(2027, 1, 11), S1), 15)

    def test_semanas_anteriores_a_s1(self):
        self.assertEqual(pba.numero_semana(dt.date(2026, 10, 4), S1), 0)
        self.assertEqual(pba.numero_semana(dt.date(2026, 9, 28), S1), 0)
        self.assertEqual(pba.numero_semana(dt.date(2026, 8, 24), S1), -5)


class TestRangoSemana(unittest.TestCase):
    def test_mismo_mes(self):
        self.assertEqual(pba.rango_semana(1, S1), "5–11 oct")

    def test_cruza_de_mes(self):
        self.assertEqual(pba.rango_semana(4, S1), "26 oct–1 nov")

    def test_semana_cero(self):
        self.assertEqual(pba.rango_semana(0, S1), "28 sep–4 oct")


class TestFormatoHoras(unittest.TestCase):
    def test_coma_decimal_sin_ceros(self):
        self.assertEqual(pba.formato_horas(15.25), "15,25")
        self.assertEqual(pba.formato_horas(16.0), "16")
        self.assertEqual(pba.formato_horas(0.5), "0,5")


class TestComandoSemana(OficinaTemporal):
    def test_usa_pba_hoy(self):
        os.environ["PBA_HOY"] = "2026-11-05"
        codigo, salida = self.pba("semana")
        self.assertEqual(codigo, 0)
        self.assertIn("jueves 2026-11-05", salida)
        self.assertIn("S5 · 2–8 nov", salida)

    def test_antes_de_s1(self):
        codigo, salida = self.pba("semana", "--fecha", "2026-09-28")
        self.assertEqual(codigo, 0)
        self.assertIn("S0", salida)
        self.assertIn("Faltan 7 días", salida)

    def test_numero(self):
        codigo, salida = self.pba("semana", "--numero", "7")
        self.assertEqual(codigo, 0)
        self.assertEqual(salida.strip(), "S7 · 16–22 nov")

    def test_sin_config_falla_con_mensaje(self):
        (self.raiz / "empresa" / "config.toml").unlink()
        codigo, salida = self.pba("semana")
        self.assertEqual(codigo, 2)
        self.assertIn("No existe", salida)


class TestParser(OficinaTemporal):
    def test_lee_campos_y_estado(self):
        self.backlog_con(propuestas=tarea(3, horas="0,75", semana=2, prioridad="P2"), ultimo=3)
        tareas = pba.cargar_tareas(self.raiz)
        self.assertEqual(len(tareas), 1)
        t = tareas[0]
        self.assertEqual((t.id, t.estado, t.horas, t.semana, t.prioridad), ("T-003", "propuestas", 0.75, 2, "P2"))
        self.assertEqual(t.campo("Área"), "operaciones")
        self.assertEqual(t.campo("Hecho cuando"), "está hecho")

    def test_reconoce_hechas_con_selector_de_variacion(self):
        self.backlog_con(hechas=tarea(1), ultimo=1)
        self.assertEqual(pba.cargar_tareas(self.raiz)[0].estado, "hechas")


class TestComandoIds(OficinaTemporal):
    def test_siguiente_id(self):
        self.backlog_con(propuestas=tarea(1) + "\n" + tarea(2), ultimo=2)
        codigo, salida = self.pba("ids")
        self.assertEqual(codigo, 0)
        self.assertIn("siguiente T-003", salida)
        self.assertIn("siguiente D-001", salida)

    def test_avisa_si_ultimo_id_esta_desfasado(self):
        self.backlog_con(propuestas=tarea(7), ultimo=2)
        codigo, salida = self.pba("ids")
        self.assertEqual(codigo, 1)
        self.assertIn("contiene T-007", salida)
        self.assertIn("siguiente T-008", salida)


if __name__ == "__main__":
    unittest.main()
