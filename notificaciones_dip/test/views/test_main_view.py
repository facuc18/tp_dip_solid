import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from src.views.main_view import MainView


class TestMainView(unittest.TestCase):
    def test_muestra_notificacion(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            MainView().mostrar_notificacion("SMS", "[SMS] hola")
        self.assertIn("[SMS] hola", buf.getvalue())

    def test_elegir_canal_valido(self):
        with patch("builtins.input", return_value="2"), redirect_stdout(io.StringIO()):
            self.assertEqual(MainView().elegir_canal(["A", "B"]), "B")

    def test_elegir_canal_reintenta_y_sale(self):
        with patch("builtins.input", side_effect=["9", "0"]), redirect_stdout(io.StringIO()):
            self.assertIsNone(MainView().elegir_canal(["A", "B"]))


if __name__ == "__main__":
    unittest.main()
