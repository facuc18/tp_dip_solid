# Sistema de notificaciones – DIP e Inyección de Dependencias

Programación Orientada a Objetos · Python 3.9+ · sin dependencias externas.

## Estructura (MVC)
```
src/
├── main.py                      # raíz de composición (arma e inyecta objetos)
├── controllers/main_controller.py
├── models/                      # abstracción + canales
│   ├── mensajeria.py            # interfaz Mensajeria
│   ├── email_mensajeria.py / whatsapp_mensajeria.py / sms_mensajeria.py
│   ├── push_mensajeria.py       # PARTE 3 (agregado sin tocar el service)
│   └── multicanal_mensajeria.py # DESAFÍO OPCIONAL
├── services/notificacion_service.py
└── views/main_view.py
test/                            # espejo de src/
parte1_acoplado/main.py          # PARTE 1 (diseño que viola DIP)
docs/                            # respuestas.md y uml.md
```

## Ejecutar
```bash
python -m src.main                              # interactivo: elegís canal y mensaje
python -m src.main --demo                       # mismo mensaje por todos los canales
python parte1_acoplado/main.py                  # parte 1
python -m unittest discover -s test -t . -v     # tests
```
(Ejecutar siempre desde la raíz del proyecto.)

## UML
Ver `docs/uml.md` (Mermaid; se renderiza en GitHub/VS Code).
Respuestas conceptuales: `docs/respuestas.md`.

## ¿Dónde está la inyección de dependencias?
1. `src/models/mensajeria.py`: la abstracción (`Mensajeria.enviar`).
2. `src/services/notificacion_service.py`: `__init__(self, mensajeria)` recibe la dependencia, no la crea.
3. `src/controllers/main_controller.py`: `NotificacionService(canal)` inyecta el canal elegido.
4. `src/main.py`: raíz de composición, único lugar que conoce las clases concretas.

Al ejecutar, el programa imprime una línea `[DI] NotificacionService(mensajeria=...)` cada vez que inyecta un canal.

## Agregar un canal nuevo (ej. Telegram)
1. Crear `src/models/telegram_mensajeria.py` con `class TelegramMensajeria(Mensajeria)`.
2. Agregar una línea al diccionario `canales` de `src/main.py`.
`NotificacionService` no se modifica.
