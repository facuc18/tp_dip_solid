from src.models.mensajeria import Mensajeria
from src.services.notificacion_service import NotificacionService
from src.views.main_view import MainView


class MainController:
    """Recibe (inyectados) la vista y el catálogo de canales disponibles.
    Para cada envío, crea un NotificacionService INYECTÁNDOLE el canal elegido."""

    def __init__(self, view: MainView, canales: dict[str, Mensajeria]):
        self._view = view
        self._canales = canales

    def _notificar(self, nombre: str, mensaje: str) -> None:
        canal = self._canales[nombre]
        servicio = NotificacionService(canal)          # <-- INYECCIÓN DE DEPENDENCIA
        self._view.mostrar_inyeccion(type(canal).__name__)
        self._view.mostrar_notificacion(nombre, servicio.notificar(mensaje))

    def ejecutar(self) -> None:
        """Modo interactivo: el usuario elige el canal y el mensaje."""
        self._view.mostrar_titulo("Sistema de notificaciones")
        while True:
            nombre = self._view.elegir_canal(list(self._canales))
            if nombre is None:
                break
            self._notificar(nombre, self._view.pedir_mensaje())

    def demo(self, mensaje: str) -> None:
        """Modo demo: envía el mismo mensaje por todos los canales."""
        self._view.mostrar_titulo("Demo: mismo servicio, distintos canales")
        for nombre in self._canales:
            self._notificar(nombre, mensaje)
