from src.models.mensajeria import Mensajeria


class NotificacionService:
    """Depende de la abstracción Mensajeria, inyectada por constructor."""

    def __init__(self, mensajeria: Mensajeria):
        self._mensajeria = mensajeria

    def notificar(self, mensaje: str) -> str:
        return self._mensajeria.enviar(mensaje)
