#5 opciones
#1 cuadrado
#2 triangulo
#3 circulo
#4 rectangulo
#5 rombo

def regresa_cuadrado():
    return [
        [' ',' ',' ',' ',' ',' '],
        [' ','#','#','#','#',' '],
        [' ','#',' ',' ','#',' '],
        [' ','#',' ',' ','#',' '],
        [' ','#',' ',' ','#',' '],
        [' ','#','#','#','#',' '],
        [' ',' ',' ',' ',' ',' ']
    ]


def regresa_triangulo():
    return[
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ','#',' ',' ',' '],
        [' ',' ','#',' ','#',' ',' '],
        [' ','#',' ',' ',' ','#',' '],
        [' ','#','#','#','#','#',' '],
        [' ',' ',' ',' ',' ',' ',' ']

    ]


def regresa_circulo():
    return[
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ','#','#',' ',' ',' '],
        [' ',' ','#',' ',' ','#',' ',' '],
        [' ','#',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ','#',' '],
        [' ',' ','#',' ',' ','#',' ',' '],
        [' ',' ',' ','#','#',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ']

    ]


def regresa_rectangulo():
    return[
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#','#','#','#','#','#','#',' '],
        [' ','#',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ','#',' '],
        [' ','#',' ',' ',' ',' ',' ','#',' '],
        [' ','#','#','#','#','#','#','#',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    ]


def regresa_rombo():
    return[
        [' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ','#',' ',' ',' ',' '],
        [' ',' ',' ','#',' ','#',' ',' ',' '],
        [' ',' ','#',' ',' ',' ','#',' ',' '],
        [' ','#',' ',' ',' ',' ',' ','#',' '],
        [' ',' ','#',' ',' ',' ','#',' ',' '],
        [' ',' ',' ','#',' ','#',' ',' ',' '],
        [' ',' ',' ',' ','#',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    ]

def imprime_matriz(matriz):
    filas = len(matriz)

    for index in range (0,filas):
        print(matriz[index])



matriz_original = []
opcion=0
while opcion != -1:
    print("que quiere ver 1 cuadrado o 2 triangulo o 3 circulo o 4 rectangulo o 5 rombo")
    opcion=int(input())

    if opcion == 1:
       matriz_original = regresa_cuadrado()
       imprime_matriz(matriz_original)


    elif opcion == 2:
        matriz_original = regresa_triangulo()
        imprime_matriz(matriz_original)

    
    elif opcion == 3:
        matriz_original = regresa_circulo()
        imprime_matriz(matriz_original)


    elif opcion == 4:
        matriz_original = regresa_rectangulo()
        imprime_matriz(matriz_original)


    elif opcion == 5:
        matriz_original = regresa_rombo()
        imprime_matriz(matriz_original)


    else:
        print("error")   