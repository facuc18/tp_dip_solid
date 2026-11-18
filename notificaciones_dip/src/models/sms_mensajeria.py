from src.models.mensajeria import Mensajeria


class SmsMensajeria(Mensajeria):
    def enviar(self, mensaje: str) -> str:
        return f"[SMS] Enviando SMS: {mensaje}"
