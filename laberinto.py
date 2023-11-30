import os

# Definir las dimensiones del laberinto
filas = 5
columnas = 5

# Definir las corrdenadas de los muros
muro = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))

# Inicialización del laberinto
laberinto = [[' ' for _ in range(columnas)] for _ in range(filas)]

# Creación de muros
for coordenada in muro:
    fila, columna = coordenada
    laberinto[fila][columna] = 'X'


def limpiar_terminal():
    # Función para limpiar la terminal
    os.system('cls' if os.name == 'nt' else 'clear')


def imprimir_caracteres(coordenadas, caracteres):
    # Función para imprimir caracteres en coordenadas
    for i in range(len(coordenadas)):
        fila, columna = coordenadas[i]
        laberinto[fila][columna] = caracteres[i]


def imprimir_laberinto():
    # Función para imprimir el laberinto
    limpiar_terminal()
    titulo = "LABERINTO"
    print(titulo + "\n" + len(titulo) * "-")
    print("\nTu misión es encontrar la salida (S), empezarás por la entrada (E)" + "\n")
    imprimir_caracteres(coordenadas_deseadas, caracteres_deseados)
    for fila in laberinto:
        print(' '.join(fila))


def mover_cursor(direccion):
    # Función para mover el cursor
    nueva_fila, nueva_columna = cursor[0], cursor[1]

    if direccion == 'W' and cursor[0] > 0:
        nueva_fila -= 1
    elif direccion == 'S' and cursor[0] < filas - 1:
        nueva_fila += 1
    elif direccion == 'A' and cursor[1] > 0:
        nueva_columna -= 1
    elif direccion == 'D' and cursor[1] < columnas - 1:
        nueva_columna += 1

    if (nueva_fila, nueva_columna) not in muro:
        laberinto[cursor[0]][cursor[1]] = ' '
        cursor[0], cursor[1] = nueva_fila, nueva_columna
        laberinto[cursor[0]][cursor[1]] = 'J'

        return (cursor[0], cursor[1]) == coordenadas_deseadas[1]  # Verificar si el cursor llegó a la posición de salida

    return False


# Caracteres deseados junto con sus respectivas coordenadas
coordenadas_deseadas = [(0, 0), (4, 4)]
caracteres_deseados = ['E', 'S']

# Llamar a la función para imprimir los caracteres en las coordenadas deseadas
imprimir_caracteres(coordenadas_deseadas, caracteres_deseados)

# Iniciar el cursor en la posición inicial
cursor = [0, 0]
laberinto[cursor[0]][cursor[1]] = 'J'

# Lista para almacenar los movimientos realizados
movimientos_realizados = []

# Imprimir el laberinto inicial
imprimir_laberinto()

juego_terminado = False

# Bucle principal del juego
while not juego_terminado:
    # Capturar la entrada del teclado
    direccion = input("Introduce una dirección (W-arriba, S-abajo, A-izquierda, D-derecha): ").upper()

    if direccion in ['W', 'S', 'A', 'D']:
        juego_terminado = mover_cursor(direccion)
        if not juego_terminado:
            imprimir_laberinto()
        movimientos_realizados.append(direccion)
    else:
        print("Dirección no válida (W/S/A/D). Inténtalo de nuevo.")

# Mensaje de felicitaciones y lista de movimientos
coordenadas_deseadas = [(0, 0), (4, 4)]
caracteres_deseados = ['E', 'J']
imprimir_laberinto()
print("\n¡Felicidades! Has llegado a la salida.")
print("\nMovimientos realizados:", ', '.join(movimientos_realizados))