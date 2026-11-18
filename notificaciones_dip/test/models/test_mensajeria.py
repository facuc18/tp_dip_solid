import unittest

from src.models.email_mensajeria import EmailMensajeria
from src.models.mensajeria import Mensajeria
from src.models.multicanal_mensajeria import MultiCanalMensajeria
from src.models.push_mensajeria import PushMensajeria
from src.models.sms_mensajeria import SmsMensajeria
from src.models.whatsapp_mensajeria import WhatsAppMensajeria


class TestMensajeria(unittest.TestCase):
    def test_abstraccion_no_se_instancia(self):
        with self.assertRaises(TypeError):
            Mensajeria()

    def test_cada_canal_envia(self):
        casos = [(EmailMensajeria(), "EMAIL"), (WhatsAppMensajeria(), "WHATSAPP"),
                 (SmsMensajeria(), "SMS"), (PushMensajeria(), "PUSH")]
        for canal, etiqueta in casos:
            with self.subTest(canal=etiqueta):
                self.assertIsInstance(canal, Mensajeria)
                self.assertIn(f"[{etiqueta}]", canal.enviar("hola"))

    def test_multicanal(self):
        r = MultiCanalMensajeria([EmailMensajeria(), SmsMensajeria()]).enviar("hola")
        self.assertIn("[EMAIL]", r)
        self.assertIn("[SMS]", r)


if __name__ == "__main__":
    unittest.main()
