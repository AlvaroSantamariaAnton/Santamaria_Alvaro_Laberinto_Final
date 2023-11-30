# Laberinto
Este programa en Python simula un juego en el que debes recorrer un laberinto desde la entrada (E) hasta la salida (S).
## Descripción del Código
### Dimensiones y Muros
* Se define la estructura del laberinto con un tamaño de **filas** por **columnas**.
* Los muros se establecen mediante las coordenadas de las celdas bloqueadas con 'X'.
### Inicialización del Laberinto
* La matriz del laberinto se inicializa con espacios en blanco.
* Los muros se colocan en sus respectivas posiciones.
### Funciones de Imprimir
* limpiar_terminal(): Limpia la terminal para una mejor presentación.
* imprimir_caracteres(coordenadas, caracteres): Coloca caracteres en las coordenadas especificadas.
* imprimir_laberinto(): Muestra el estado actual del laberinto en la terminal.
### Función de Movimiento
* mover_cursor(direccion): Permite mover el cursor (jugador) en el laberinto, evitando muros. Retorna verdadero si se llega a la salida.
### Inicialización del Juego
* Coordenadas y caracteres deseados para la entrada y salida.
* El cursor se coloca en la entrada.
* Se imprime el laberinto inicial.
### Bucle Principal del Juego
* Se solicita al jugador introducir direcciones (W/S/A/D).
* Los movimientos son validados y se actualiza el estado del laberinto.
* El juego continúa hasta que el jugador alcanza la salida.
### Mensaje de Finalización
* Se imprime el laberinto final con la posición del jugador.
* Se felicita al jugador por llegar a la salida.
* Se muestra la lista de movimientos realizados.
## Instrucciones del Juego
* Utiliza las teclas W, S, A y D para moverte arriba, abajo, izquierda y derecha respectivamente.
* Encuentra la salida (S) comenzando desde la entrada (E).
## Link al repositorio
https://github.com/AlvaroSantamariaAnton/Santamaria_Alvaro_Laberinto_Final.git