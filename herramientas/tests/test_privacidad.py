import unittest

from ayudas import OficinaTemporal

# Términos ficticios: los reales viven en empresa/privado/ y nunca en un test.
TERMINOS = """\
# comentario
trámite secreto
=RAE
"""


class TestPrivacidad(OficinaTemporal):
    def test_sin_fichero_de_terminos_no_hay_nada_que_buscar(self):
        codigo, salida = self.pba("privacidad")
        self.assertEqual(codigo, 0)
        self.assertIn("no hay términos que buscar", salida)

    def test_detecta_sin_tildes_ni_mayusculas(self):
        self.escribir("empresa/privado/terminos-sensibles.txt", TERMINOS)
        self.escribir("empresa/reuniones/x/ronda1-finanzas-legal.md", "# Ronda\n\nOjo con el TRAMITE Secreto pendiente.\n")
        codigo, salida = self.pba("privacidad")
        self.assertEqual(codigo, 1)
        self.assertIn("empresa/reuniones/x/ronda1-finanzas-legal.md:3", salida)
        self.assertIn("trámite secreto", salida)

    def test_termino_exacto_distingue_mayusculas_y_palabras(self):
        self.escribir("empresa/privado/terminos-sensibles.txt", TERMINOS)
        self.escribir("docs/a.md", "Una raedera, un rae-algo en minúsculas y Rae.\n")
        codigo, salida = self.pba("privacidad")
        self.assertEqual(codigo, 0, salida)
        self.escribir("docs/b.md", "Según la RAE.\n")
        codigo, salida = self.pba("privacidad")
        self.assertEqual(codigo, 1)
        self.assertIn("docs/b.md:1", salida)

    def test_no_revisa_la_carpeta_privada(self):
        self.escribir("empresa/privado/terminos-sensibles.txt", TERMINOS)
        self.escribir("empresa/privado/situacion-personal.md", "Hay un trámite secreto pendiente.\n")
        codigo, salida = self.pba("privacidad")
        self.assertEqual(codigo, 0, salida)

    def test_check_incluye_la_privacidad(self):
        self.escribir("empresa/privado/terminos-sensibles.txt", TERMINOS)
        self.escribir("empresa/estado.md", "- Riesgo: el trámite secreto.\n")
        codigo, salida = self.pba("check")
        self.assertEqual(codigo, 1)
        self.assertIn("empresa/estado.md:1", salida)


if __name__ == "__main__":
    unittest.main()
