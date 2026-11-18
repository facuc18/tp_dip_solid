import sys

from src.controllers.main_controller import MainController
from src.models.email_mensajeria import EmailMensajeria
from src.models.multicanal_mensajeria import MultiCanalMensajeria
from src.models.push_mensajeria import PushMensajeria
from src.models.sms_mensajeria import SmsMensajeria
from src.models.whatsapp_mensajeria import WhatsAppMensajeria
from src.views.main_view import MainView


def main() -> None:
    # RAÍZ DE COMPOSICIÓN: único lugar que conoce las clases concretas.
    # Para agregar un canal nuevo solo se agrega una línea acá.
    email, whatsapp, sms, push = (
        EmailMensajeria(), WhatsAppMensajeria(), SmsMensajeria(), PushMensajeria()
    )
    canales = {
        "Email": email,
        "WhatsApp": whatsapp,
        "SMS": sms,
        "Push": push,
        "Multicanal (todos)": MultiCanalMensajeria([email, whatsapp, sms, push]),
    }
    controlador = MainController(MainView(), canales)

    if "--demo" in sys.argv:
        controlador.demo("Tu pedido fue enviado")
    else:
        controlador.ejecutar()


if __name__ == "__main__":
    main()
