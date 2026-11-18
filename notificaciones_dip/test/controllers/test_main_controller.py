import unittest

from src.controllers.main_controller import MainController
from src.models.mensajeria import Mensajeria


class FakeCanal(Mensajeria):
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta

    def enviar(self, mensaje):
        return f"{self.etiqueta}:{mensaje}"


class ViewSpy:
    def __init__(self, respuestas):
        self.respuestas = iter(respuestas)   # canal elegido, mensaje, canal, ...
        self.notificaciones = []
        self.inyecciones = []

    def mostrar_titulo(self, titulo): pass
    def elegir_canal(self, nombres): return next(self.respuestas)
    def pedir_mensaje(self): return next(self.respuestas)
    def mostrar_inyeccion(self, clase): self.inyecciones.append(clase)
    def mostrar_notificacion(self, canal, resultado):
        self.notificaciones.append((canal, resultado))


class TestMainController(unittest.TestCase):
    def setUp(self):
        self.canales = {"A": FakeCanal("a"), "B": FakeCanal("b")}

    def test_interactivo_usa_el_canal_elegido(self):
        view = ViewSpy(["B", "hola", "A", "chau", None])
        MainController(view, self.canales).ejecutar()
        self.assertEqual(view.notificaciones, [("B", "b:hola"), ("A", "a:chau")])
        self.assertEqual(view.inyecciones, ["FakeCanal", "FakeCanal"])

    def test_demo_envia_por_todos(self):
        view = ViewSpy([])
        MainController(view, self.canales).demo("x")
        self.assertEqual([c for c, _ in view.notificaciones], ["A", "B"])


if __name__ == "__main__":
    unittest.main()
