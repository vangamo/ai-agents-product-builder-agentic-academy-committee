import unittest

from ayudas import OficinaTemporal, tarea

VALIDADA = "- Validada: 2026-10-06\n"


class TestCheck(OficinaTemporal):
    def test_oficina_vacia_es_valida(self):
        codigo, salida = self.pba("check")
        self.assertEqual(codigo, 0, salida)
        self.assertIn("0 errores", salida)

    def test_backlog_correcto(self):
        self.backlog_con(propuestas=tarea(2), aprobadas=tarea(1, extra=VALIDADA), ultimo=2)
        codigo, salida = self.pba("check", "--estricto")
        self.assertEqual(codigo, 0, salida)

    def test_tarea_de_mas_de_4_horas(self):
        self.backlog_con(propuestas=tarea(1, horas="5"), ultimo=1)
        codigo, salida = self.pba("check")
        self.assertEqual(codigo, 1)
        self.assertIn("T-001 estima 5 h", salida)

    def test_falta_un_campo_obligatorio(self):
        self.backlog_con(propuestas=tarea(1).replace("- Hecho cuando: está hecho\n", ""), ultimo=1)
        codigo, salida = self.pba("check")
        self.assertEqual(codigo, 1)
        self.assertIn("T-001 no tiene «Hecho cuando»", salida)

    def test_prioridad_invalida(self):
        self.backlog_con(propuestas=tarea(1, prioridad="P7"), ultimo=1)
        codigo, salida = self.pba("check")
        self.assertEqual(codigo, 1)
        self.assertIn("prioridad", salida)

    def test_id_duplicado(self):
        self.backlog_con(propuestas=tarea(1) + "\n" + tarea(1, titulo="Otra"), ultimo=1)
        codigo, salida = self.pba("check")
        self.assertEqual(codigo, 1)
        self.assertIn("T-001 está duplicado", salida)

    def test_ultimo_id_desfasado(self):
        self.backlog_con(propuestas=tarea(4), ultimo=2)
        codigo, salida = self.pba("check")
        self.assertEqual(codigo, 1)
        self.assertIn("existe T-004", salida)

    def test_id_provisional_sin_registrar(self):
        self.backlog_con(propuestas=tarea(1).replace("Depende de: —", "Depende de: T-p2"), ultimo=1)
        codigo, salida = self.pba("check")
        self.assertEqual(codigo, 1)
        self.assertIn("ID provisional", salida)

    def test_referencia_inexistente_es_solo_aviso(self):
        self.backlog_con(propuestas=tarea(1).replace("Depende de: —", "Depende de: T-009 · D-012"), ultimo=1)
        codigo, salida = self.pba("check")
        self.assertEqual(codigo, 0)
        self.assertIn("T-001 cita T-009, que no existe", salida)
        self.assertIn("T-001 cita D-012, que no existe", salida)
        codigo, _ = self.pba("check", "--estricto")
        self.assertEqual(codigo, 1)

    def test_aprobada_sin_fecha_de_validacion(self):
        self.backlog_con(aprobadas=tarea(1), ultimo=1)
        codigo, salida = self.pba("check")
        self.assertEqual(codigo, 0)
        self.assertIn("no consta «Validada", salida)

    def test_capacidad_comprometida_excedida(self):
        tareas = "\n".join(tarea(n, horas="4", semana=1, extra=VALIDADA) for n in range(1, 6))
        self.backlog_con(aprobadas=tareas, ultimo=5)
        codigo, salida = self.pba("check")
        self.assertIn("S1 tiene 20 h comprometidas", salida)

    def test_decision_pendiente_incompleta(self):
        self.escribir(
            "empresa/decisiones.md",
            "# Registro\n\n> Último ID usado: D-001\n\n## 🟡 Pendientes\n\n### D-001 · ¿Algo?\n\n- **Contexto:** x\n\n## ✅ Tomadas\n",
        )
        codigo, salida = self.pba("check")
        self.assertEqual(codigo, 1)
        self.assertIn("D-001 no tiene «Opciones»", salida)
        self.assertIn("D-001 no tiene «Recomendación del comité»", salida)

    def test_decision_pendiente_completa_con_negritas(self):
        decision = (
            "### D-001 · ¿Qué handle usamos?\n\n"
            "- **Contexto:** no cabe en X.\n"
            "- **Opciones:** A) uno · B) otro\n"
            "- **Recomendación del comité:** A · **Discrepa:** nadie\n"
            "- **Coste de no decidir:** se ocupa el handle.\n"
        )
        self.escribir("empresa/decisiones.md", f"# Registro\n\n> Último ID usado: D-001\n\n## 🟡 Pendientes\n\n{decision}\n## ✅ Tomadas\n")
        codigo, salida = self.pba("check", "--estricto")
        self.assertEqual(codigo, 0, salida)

    def test_decision_tomada_sin_fecha(self):
        self.escribir(
            "empresa/decisiones.md",
            "# Registro\n\n> Último ID usado: D-001\n\n## 🟡 Pendientes\n\n## ✅ Tomadas\n\n### D-001 · Marca\n\n- Decisión: sí\n",
        )
        codigo, salida = self.pba("check")
        self.assertEqual(codigo, 1)
        self.assertIn("D-001 está tomada pero no tiene «Fecha»", salida)


if __name__ == "__main__":
    unittest.main()
