"""Pruebas del MODELO con una base de datos temporal."""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from model import AlumnoModel  # noqa: E402


class TestAlumnoModel(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.modelo = AlumnoModel(os.path.join(self.tmp.name, "prueba.db"))

    def tearDown(self):
        self.tmp.cleanup()

    def test_agregar_y_obtener(self):
        id_nuevo = self.modelo.agregar("Ana Torres", "Contabilidad", 8.9)
        alumno = self.modelo.obtener_por_id(id_nuevo)
        self.assertEqual(alumno["nombre"], "Ana Torres")
        self.assertEqual(len(self.modelo.obtener_todos()), 1)

    def test_eliminar(self):
        id_nuevo = self.modelo.agregar("Luis Hernandez", "Software", 7.8)
        self.modelo.eliminar(id_nuevo)
        self.assertIsNone(self.modelo.obtener_por_id(id_nuevo))


if __name__ == "__main__":
    unittest.main()
