import unittest

from src.models.mensajeria import Mensajeria
from src.models.push_mensajeria import PushMensajeria
from src.models.sms_mensajeria import SmsMensajeria
from src.services.notificacion_service import NotificacionService


class FakeMensajeria(Mensajeria):
    def __init__(self):
        self.recibidos = []

    def enviar(self, mensaje):
        self.recibidos.append(mensaje)
        return "ok"


class TestNotificacionService(unittest.TestCase):
    def test_delega_en_la_abstraccion_inyectada(self):
        fake = FakeMensajeria()
        self.assertEqual(NotificacionService(fake).notificar("hola"), "ok")
        self.assertEqual(fake.recibidos, ["hola"])

    def test_canales_intercambiables_sin_modificar_el_service(self):
        self.assertIn("[SMS]", NotificacionService(SmsMensajeria()).notificar("x"))
        self.assertIn("[PUSH]", NotificacionService(PushMensajeria()).notificar("x"))


if __name__ == "__main__":
    unittest.main()
