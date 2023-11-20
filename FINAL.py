"""
-----------------------------------------------------------------------------------------------
Título: VAQUITA V1.0

Fecha: 21/11/2023

Autor: Joaquin Monsalvo, Nicolas Tombolan, Luciano Dominguez

Descripción:

Videojuego que presenta un mapa de juego en donde:
-La "P" representa plantas que come la vaquita,
-"I" es pasto que no come
-"T" son tranqueras que la vaquita salta
- "&" es la vaquita que movemos de la siguiente manera:
|W + enter|  =  arriba ;
|A + enter|  =  izquierda ;
|S + enter|  = abajo ;
|D + enter|  = derecha.

El objetivo es que la vaquita llegue a "E" (establo) una vez que ha saltado 7 tranqueras.
Se utiliza una matriz de 5 x 5 para representar el mapa en donde las tranqueras se cargan
aleatoriamente (7 tranqueras). El establo siempre estará en el último casillero (el 4,4).
Aparecen en misma proporcion (pasto y plantitas) al inicio del juego (8 y 8)
No se marcará que el juego está ganado hasta que la vaquita haya saltado las 7 tranqueras.
Si la vaquita ya comió la plantita o saltó la tranquera ese casillero queda con "I". 

Mejora para el  8:

La vaquita gasta energía si se mueve (score de calorías/ energia).
La vaquita inicia con 100 de energía
Si la vaquita come una planta + 250 score de energia
Si se llega a destino + 500 score de energia
Saltar cada tranquera le consume energia - 25
Cada movimiento le cuesta - 10 de energia independientemente de que tenga el casillero destino
Si la vaquita se queda sin energía se muestra GAME OVER

Mejora para el  10:

Se crean 3 partidas con diferentes niveles de dificultad (7 tranqueras, 9 tranqueras, 11 tranqueras)
Si la vaquita no logra cumplir con algun nivel se muestra game over y se pregunta si se quiere volver
a jugar. Si se pasan los tres niveles se muestra que ganamos y se pregunta si queremos volver a jugar



-----------------------------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------
# MÓDULOS IMPORTADOS
#----------------------------------------------------------------------------------------------

import random
import colorama
from colorama import Fore as c_fore;
from colorama import Style as c_style;
colorama.init();

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------


def crearMapaNuevo(mapa, dificultad):
    
    """
    Método de creación del nuevo mapa.
    1- Se crea matriz vacía del tamaño especificado
    2- Se carga con el pasto, las plantitas, el establo, la vaquita y las tranqueras
    (vaquita empieza en [0][0])
    3- Se retorna el mapa al menú principal
    """

    vaquita = "&"
    pastoComun = "I"
    pastoComestible = "P"
    tranquera = "T"
    establo = "E"

    mapa = [[0 for cero in range(5)] for ceros in range(5)]
    mapa[0][0] = vaquita  # Establecer posicion vaquita
    mapa[4][4] = establo  # Establecer posicion establo

    if dificultad == 1:
        ntranqueras = 7
        nPastoComun = 8
        nPastoComestible = 8

        # Distribucion de Tranqueras
        for t in range(ntranqueras):
            while True:
                fila = random.randint(0, 4)
                columna = random.randint(0, 4)
                if mapa[fila][columna] == 0:
                    mapa[fila][columna] = tranquera
                    break

        # Distribucion de Pasto Comun
        for p in range(nPastoComun):
            while True:
                fila = random.randint(0, 4)
                columna = random.randint(0, 4)
                if mapa[fila][columna] == 0:
                    mapa[fila][columna] = pastoComun
                    break

        # Distribucion de Pasto Comestible
        for c in range(nPastoComestible):
            while True:
                fila = random.randint(0, 4)
                columna = random.randint(0, 4)
                if mapa[fila][columna] == 0:
                    mapa[fila][columna] = pastoComestible
                    break

        return mapa


def mostrarMapa(mapa):
    for fila in mapa:
        for columna in fila:
            if columna == "&":
                print(f"{c_fore.RED}{columna}	{c_style.RESET_ALL}", end="")
            elif columna == "P":
                print(f"{c_fore.LIGHTGREEN_EX}{columna}	{c_style.RESET_ALL}", end="")
            elif columna == "T":
                print(f"{c_fore.WHITE}{columna}	{c_style.RESET_ALL}", end="")
            elif columna == "I":
                print(f"{c_fore.GREEN}{columna}	{c_style.RESET_ALL}", end="")
            elif columna == "E":
                print(f"{c_fore.LIGHTCYAN_EX}{columna}	{c_style.RESET_ALL}", end="")
            else:
                print(f"{c_fore.CYAN}{columna}	{c_style.RESET_ALL}", end="")
        print()
    

def hallarCoordenadas(mapa):
    """
    Método de búsqueda de una coordenada esfecífica
    (es decir, ¿donde se encuentra la vaquita '&' ? ¿Qué fila y qué columna? )
    retorna el valor de fila y el valor de columna
    """
    
    for f in range(len(mapa)):
        for c in range(len(mapa[f])):
            if mapa[f][c] == "&":
                return f, c

    return f,c
    

def irDerecha(mapa, tranqueras, llegoAlDestino, score):
    """
    Primer método para mover la vaquita a derecha. Para ello:
    1- llama al método hallarCoordenadas para ver en dónde está la vaquita. Recibe dos enteros (fila y columna)
    2- A esa posición la reemplaza por "I".
    3- Identifica la posición a derecha de esa y le asiga la vaquita.
    4-  retorna mapa, _colisiones, _llegoAlDestino
    
    Casos a tener en cuenta:
        a) Si está en la última columna y queremos correr a la derecha debemos volver a la columna 0
        b) Si  en esa posición a la que se mueve tiene "T" de tranquera sumará una tranquera al contador
        c) Si en esa posición a la que se mueve tiene "X" de llegada se cambia _llegoAlDestino por True
    """
    f, c = hallarCoordenadas(mapa)

    if c < len(mapa[0]) - 1:
        lugarSiguiente = mapa[f][c + 1]
        score -= 10

        if lugarSiguiente == "T":
            tranqueras += 1
            score -= 25
        elif lugarSiguiente == "E" and tranqueras == 7:
            llegoAlDestino = True
            score += 500
        elif lugarSiguiente == "P":
            score += 250

        mapa[f][c] = "I"
        mapa[f][c + 1] = "&"

    return mapa, tranqueras, llegoAlDestino, score


def irArriba(mapa, tranqueras, llegoAlDestino, score):
    """
    Segundo método para mover la vaquita para arriba. Para ello:
    1- llama al método hallarCoordenadas para ver en dónde está la vaquita. Recibe dos enteros (fila y columna)
    2- A esa posición la reemplaza por "I".
    3- Identifica la posición a arriba de esa y le asiga la vaquita.
    4-  retorna mapa, _colisiones, _llegoAlDestino
    
    Casos a tener en cuenta:
        a) Si está en la primera fila (0)  y queremos correr arriba debemos irnos a la última fila.
        b) Si  en esa posición a la que se mueve tiene "T" de tranquera sumará una tranquera al contador
        c) Si en esa posición a la que se mueve tiene "X" de llegada se cambia _llegoAlDestino por True
    """
    f, c = hallarCoordenadas(mapa)

    if f > 0:
        lugarSiguiente = mapa[f - 1][c]
        score -= 10

        if lugarSiguiente == "T":
            tranqueras += 1
            score -= 25
        elif lugarSiguiente == "E" and tranqueras == 7:
            llegoAlDestino = True
            score += 500
        elif lugarSiguiente == "P":
            score += 250

        mapa[f][c] = "I"
        mapa[f - 1][c] = "&"

    return mapa, tranqueras, llegoAlDestino, score
    

def irAbajo(mapa, tranqueras, llegoAlDestino, score):
    """
    Tercer método para mover la vaquita para abajo. Para ello:
    1- llama al método hallarCoordenadas para ver en dónde está la vaquita. Recibe dos enteros (fila y columna)
    2- A esa posición la reemplaza por "I".
    3- Identifica la posición a arriba de esa y le asiga la vaquita.
    4-  retorna mapa, _colisiones, _llegoAlDestino
    
    Casos a tener en cuenta:
        a) Si está en la última fila   y queremos correr hacia abajo debemos irnos a la primera fila (0).
        b) Si  en esa posición a la que se mueve tiene "T" de tranquera sumará una tranquera al contador
        c) Si en esa posición a la que se mueve tiene "X" de llegada se cambia _llegoAlDestino por True
    """
    f, c = hallarCoordenadas(mapa)

    if f < len(mapa) - 1:
        lugarSiguiente = mapa[f + 1][c]
        score -= 10

        if lugarSiguiente == "T":
            tranqueras += 1
            score -= 25
        elif lugarSiguiente == "E" and tranqueras == 7:
            llegoAlDestino = True
            score += 500
        elif lugarSiguiente == "P":
            score += 250

        mapa[f][c] = "I"
        mapa[f + 1][c] = "&"

    return mapa, tranqueras, llegoAlDestino, score


def irIzquierda(mapa, tranqueras, llegoAlDestino, score):
    """
    Cuarto método para mover la vaquita para arriba. Para ello:
    1- llama al método hallarCoordenadas para ver en dónde está la vaquita. Recibe dos enteros (fila y columna)
    2- A esa posición la reemplaza por "I".
    3- Identifica la posición a arriba de esa y le asiga la vaquita.
    4-  retorna mapa, _colisiones, _llegoAlDestino
    
    Casos a tener en cuenta:
        a) Si está en la primera columna (0)  y queremos ir a izquierda debemos irnos a la última fila.
        b) Si  en esa posición a la que se mueve tiene "T" de tranquera sumará una tranquera al contador
        c) Si en esa posición a la que se mueve tiene "X" de llegada se cambia _llegoAlDestino por True
    """
    f, c = hallarCoordenadas(mapa)

    if c > 0:
        lugarSiguiente = mapa[f][c - 1]
        score -= 10

        if lugarSiguiente == "T":
            tranqueras += 1
            score -= 25
        elif lugarSiguiente == "E" and tranqueras == 7:
            llegoAlDestino = True
            score += 500
        elif lugarSiguiente == "P":
            score += 250

        mapa[f][c] = "I"
        mapa[f][c - 1] = "&"

    return mapa, tranqueras, llegoAlDestino, score



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
# Declaración de variables

"""
Se crea el mapa y se llama al método crearMapaNuevo.
Se cargan las tranqueras en 0
Se carga la booleana llegoAlDestino como falso
"""

score = 100
dificultad = 1
tranqueras = 0
mapa = []
mapa = crearMapaNuevo(mapa, dificultad)
llegoAlDestino = False
    
#----------------------------------------------------------------------------------------------
# Bloque de cursor
#----------------------------------------------------------------------------------------------        

while llegoAlDestino == False and score > 0 :
    print(f"{c_fore.BLUE} Level: {dificultad} {c_style.RESET_ALL}")
    print(f"{c_fore.GREEN} Score: {score} {c_style.RESET_ALL}")
    print(f"{c_fore.YELLOW} Tranqueras: {tranqueras} {c_style.RESET_ALL}")
    print(f"{c_fore.WHITE} ___________________________________ {c_style.RESET_ALL}")
    print()
    
    mostrarMapa(mapa)
    cursor = input("->")
    if cursor.upper() == "W":
        mapa , tranqueras, llegoAlDestino, score = irArriba(mapa, tranqueras, llegoAlDestino, score)
    elif cursor.upper() == "D":
        mapa , tranqueras, llegoAlDestino, score = irDerecha(mapa, tranqueras, llegoAlDestino, score)
    elif cursor.upper() == "S":
        mapa , tranqueras, llegoAlDestino, score = irAbajo(mapa, tranqueras, llegoAlDestino, score)
    elif cursor.upper() == "A":
        mapa , tranqueras, llegoAlDestino, score = irIzquierda(mapa, tranqueras, llegoAlDestino, score)

    if llegoAlDestino == True:
        print(f"{c_fore.BLUE} Level: {dificultad} {c_style.RESET_ALL}")
        print(f"{c_fore.GREEN} Score: {score} {c_style.RESET_ALL}")
        print(f"{c_fore.YELLOW} Tranqueras: {tranqueras} {c_style.RESET_ALL}")
        print(f"{c_fore.WHITE} ___________________________________ {c_style.RESET_ALL}")
        print()
        mostrarMapa(mapa)

        print("GANASTE")

    if score <= 0:
        print("GAME OVER")
        jugarSiNo = input("\nQueres jugar de nuevo? SI o No? ").upper()
        
        if jugarSiNo == "SI":
                llegoAlDestino == False
                score = 100
                continue

        elif jugarSiNo == "NO":
            break

#----------------------------------------------------------------------------------------------
# Fin del juego
#----------------------------------------------------------------------------------------------

