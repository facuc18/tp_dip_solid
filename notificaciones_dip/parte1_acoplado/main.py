


class EmailService:
    def enviar_email(self, mensaje):
        print(f"[EMAIL] Enviando correo: {mensaje}")


class NotificacionService:
    def __init__(self):
        self.email = EmailService()  # dependencia directa a una clase concreta

    def notificar(self, mensaje):
        self.email.enviar_email(mensaje)


if __name__ == "__main__":
    NotificacionService().notificar("Bienvenido al sistema")
