from src.models.mensajeria import Mensajeria


class WhatsAppMensajeria(Mensajeria):
    def enviar(self, mensaje: str) -> str:
        return f"[WHATSAPP] Enviando WhatsApp: {mensaje}"
