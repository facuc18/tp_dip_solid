class MainView:
    """Solo se encarga de entrada/salida por consola."""

    def mostrar_titulo(self, titulo: str) -> None:
        print(f"\n=== {titulo} ===")

    def elegir_canal(self, nombres: list[str]):
        """Muestra el menú y devuelve el nombre elegido, o None para salir."""
        print("\nElegí el canal de notificación:")
        for i, nombre in enumerate(nombres, start=1):
            print(f"  {i}. {nombre}")
        print("  0. Salir")
        while True:
            opcion = input("Opción: ").strip()
            if opcion == "0":
                return None
            if opcion.isdigit() and 1 <= int(opcion) <= len(nombres):
                return nombres[int(opcion) - 1]
            print("Opción inválida, probá de nuevo.")

    def pedir_mensaje(self) -> str:
        return input("Mensaje a enviar: ").strip()

    def mostrar_inyeccion(self, clase_inyectada: str) -> None:
        print(f"[DI] NotificacionService(mensajeria={clase_inyectada}())  <- inyección por constructor")

    def mostrar_notificacion(self, canal: str, resultado: str) -> None:
        print(f"-> Canal {canal}:")
        print(resultado)
