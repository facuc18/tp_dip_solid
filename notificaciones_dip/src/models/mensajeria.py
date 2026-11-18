from abc import ABC, abstractmethod


class Mensajeria(ABC):
    """Abstracción de la que dependen los módulos de alto nivel (DIP)."""

    @abstractmethod
    def enviar(self, mensaje: str) -> str:
        """Envía el mensaje y devuelve el detalle de lo enviado."""
