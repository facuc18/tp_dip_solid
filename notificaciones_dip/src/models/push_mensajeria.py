from src.models.mensajeria import Mensajeria


class PushMensajeria(Mensajeria):
    def enviar(self, mensaje: str) -> str:
        return f"[PUSH] Enviando notificación push: {mensaje}"
