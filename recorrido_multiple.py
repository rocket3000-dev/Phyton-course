import os
import time

#mapa 10x10
#solicita la direccion y despues el numero de casillas a moverse
#si el muñeco no se puede mover tantas casillas como se le indico marca error

def valida_si_puedes_moverte_a_la_siguiente_casilla(posicion):
    return posicion >= 0 and posicion <= 9


def up(fila):
    if valida_si_puedes_moverte_a_la_siguiente_casilla(fila-1):
        fila-=1
    else:
        print("Error")

    return fila


def down(fila):
    if valida_si_puedes_moverte_a_la_siguiente_casilla(fila+1):
        fila+=1
    else:   
        print("Error")

    return fila


def left(columna):
    if valida_si_puedes_moverte_a_la_siguiente_casilla(columna-1):
        columna-=1
    else:
        print("Error")    

    return columna


def right(columna):
    if valida_si_puedes_moverte_a_la_siguiente_casilla(columna+1):
        columna+=1
    else:
        print("Error")    

    return columna


def mostrar_matriz(matriz):
    fila = len(matriz)
    for index in range (0,fila):
        print(matriz[index])


def regresa_matriz_limpia():
    matriz=[
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
]

    return  matriz  
#el codigo que esta arriba no es conocido por el codigo de abajo 
#aqui ya comienza el programa

fila_jugador=0
columna_jugador=0
opcion=""
numero_de_pasos=0
matriz= regresa_matriz_limpia()
   
mostrar_matriz(matriz)

while opcion != "-1":
    print("pa donde ira / a izquierda , w arriba , s abajo , d derecha ")
    opcion=input()
    print("Ingrese el numero de pasos a mover")
    numero_de_pasos=int(input())

    if opcion == "a":
        for pasos in range(0,numero_de_pasos):
            columna_jugador = left(columna_jugador)
            matriz = regresa_matriz_limpia()
            matriz[fila_jugador][columna_jugador] = "🐒"
            mostrar_matriz(matriz)
            print("")
            print("")
            time.sleep(1)


    elif opcion == "w":
       for pasos in range(0,numero_de_pasos):
            fila_jugador = up(fila_jugador)
            matriz = regresa_matriz_limpia()
            matriz[fila_jugador][columna_jugador] = "🐒"
            mostrar_matriz(matriz)
            print("")
            print("")
            time.sleep(1)


    elif opcion == "s":
        for pasos in range(0,numero_de_pasos):
            fila_jugador = down(fila_jugador)
            matriz = regresa_matriz_limpia()
            matriz[fila_jugador][columna_jugador] = "🐒"
            mostrar_matriz(matriz)
            print("")
            print("")
            time.sleep(1)


    elif opcion == "d":
        for pasos in range(0,numero_de_pasos):
            columna_jugador = right(columna_jugador)
            matriz = regresa_matriz_limpia()
            matriz[fila_jugador][columna_jugador] = "🐒"
            mostrar_matriz(matriz)
            print("")
            print("")
            time.sleep(1)
