from src.models.mensajeria import Mensajeria


class EmailMensajeria(Mensajeria):
    def enviar(self, mensaje: str) -> str:
        return f"[EMAIL] Enviando correo: {mensaje}"
