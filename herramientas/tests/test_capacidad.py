import unittest

from ayudas import OficinaTemporal, pba, tarea


class TestBalance(OficinaTemporal):
    def test_separa_comprometido_y_propuesto(self):
        self.backlog_con(
            propuestas=tarea(3, horas="2,5", semana=1),
            aprobadas=tarea(1, horas="4", semana=1) + "\n" + tarea(2, horas="1,25", semana=2),
            hechas=tarea(4, horas="3", semana=1),
            ultimo=4,
        )
        balances, sin_contar = pba.balance_capacidad(pba.cargar_tareas(self.raiz))
        s1, s2 = balances
        self.assertEqual((s1.semana, s1.comprometido, s1.propuesto, s1.total), (1, 7.0, 2.5, 9.5))
        self.assertEqual((s2.semana, s2.comprometido, s2.propuesto), (2, 1.25, 0.0))
        self.assertEqual(sin_contar, [])

    def test_tareas_sin_semana_no_desaparecen(self):
        bloque = tarea(1).replace(" · Semana: S1", "")
        self.backlog_con(aprobadas=bloque, ultimo=1)
        balances, sin_contar = pba.balance_capacidad(pba.cargar_tareas(self.raiz))
        self.assertEqual(balances, [])
        self.assertEqual([t.id for t in sin_contar], ["T-001"])


class TestComandoCapacidad(OficinaTemporal):
    def test_dentro_de_capacidad(self):
        self.backlog_con(aprobadas=tarea(1, horas="4", semana=1), ultimo=1)
        codigo, salida = self.pba("capacidad")
        self.assertEqual(codigo, 0)
        self.assertIn("| S1 | 5–11 oct | 4 | 0 | 4 | 16 | 12 |", salida)

    def test_avisa_si_se_pasa_de_16_horas(self):
        tareas = "\n".join(tarea(n, horas="4", semana=2) for n in range(1, 5))
        self.backlog_con(aprobadas=tareas, propuestas=tarea(5, horas="0,5", semana=2), ultimo=5)
        codigo, salida = self.pba("capacidad")
        self.assertEqual(codigo, 1)
        self.assertIn("| S2 | 12–18 oct | 16 | 0,5 | 16,5 | 16 | -0,5 ⚠️ |", salida)
        self.assertIn("Por encima de 16 h: S2", salida)

    def test_filtra_desde_una_semana(self):
        self.backlog_con(aprobadas=tarea(1, semana=1) + "\n" + tarea(2, semana=3), ultimo=2)
        codigo, salida = self.pba("capacidad", "--desde", "2")
        self.assertNotIn("| S1 |", salida)
        self.assertIn("| S3 |", salida)


if __name__ == "__main__":
    unittest.main()
