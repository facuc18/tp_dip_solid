from src.models.mensajeria import Mensajeria


class MultiCanalMensajeria(Mensajeria):
    """DESAFÍO OPCIONAL (patrón Composite): envía por varios canales a la vez."""

    def __init__(self, canales: list[Mensajeria]):
        self._canales = list(canales)

    def enviar(self, mensaje: str) -> str:
        return "\n".join(canal.enviar(mensaje) for canal in self._canales)
