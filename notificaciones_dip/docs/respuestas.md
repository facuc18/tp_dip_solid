# Respuestas

## Parte 1
- **¿Qué pasa si queremos WhatsApp?** El servicio solo conoce `EmailService`; habría que agregar una clase `WhatsAppService` y cambiar `NotificacionService` para usarla.

- **¿Qué clase modificamos?** `NotificacionService` (la clase principal que difine la logica).

- **¿Problema?** este diseño hace que cada clase nueva se deba agregar a la principal para funcionar lo que puede causar que algo deje de andar y hace que la clase se vuelva mas larga y dificil de testear

## Parte 4
1. **DIP:** los módulos de alto nivel no deben depender de los de bajo nivel; ambos deben depender de abstracciones. Y las abstracciones no deben depender de los detalles, sino los detalles de las abstracciones.

2. **Clase concreta vs interfaz:** depender de una clase concreta ata el código a esa funcionalidad en concreto; depender de una interfaz solo exige que se cumpla algo en especifico como un boton de enviar por lo que cualquier clase que lo implemente puede remplazalo

3. **Inyección de dependencias:** es algo que permite que una clase o funcion use parametro u otras cosas que vengan de otro lado y no solo las que vienen de si mismo

4. **Ventajas de inyección por constructor:** la dependencia es obligatoria por lo que una clase no puede crear un objeto sin esta y ademas es facil ver lo que una clase nesecita para crear un objeto y remplazarlo por una falsa dependencia para testeo 

5. **Facilidad para extender:** agregar un canal es crear una clase que implemente `Mensajeria` y inyectarla; `NotificacionService` no cambia (así se agregó Push y MultiCanal).

6. **DIP y OCP:** DIP es el mecanismo que hace posible OCP. Al depender de una abstracción, el sistema queda abierto a extensión (nuevas implementaciones) y cerrado a modificación (el servicio no se toca).
