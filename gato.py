
matriz=[
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']

]

"""for m in range(0,3):   ejemplo: :v
    print(matriz[m])

print("Ingresa x en que fila pondra x")
fila_x=int(input())

print("ingresa en que columna ponra esa x")
columna_x=int(input())

matriz[fila_x][columna_x] == 'x'

print(fila_x)
print(columna_x)"""

#con este codigo se imprime la matriz

fila=0
columna=0
jugador=False #falso == x
#true == o 
contador=0
simbolo='x'
flag_win=False

while flag_win == False:
    for x in range(0,3):
        print(matriz[x])

    print("jugador ",simbolo)
    print("Ingresa la fila")
    fila=int(input())

    print("Ingresa la columna")
    columna=int(input())

    
    if  fila >= 0 and fila <= 2 and columna >= 0 and columna <= 2 and matriz[fila][columna] == ' ':
        matriz[fila][columna] = simbolo

        #valida la columna 0 
        if matriz[0][0] == simbolo and matriz[1][0] == simbolo and matriz[2][0] == simbolo:
            print("Gano",simbolo)
            flag_win=True

        #valida la columna 1
        elif matriz[0][1] == simbolo and matriz[1][1] == simbolo and matriz[2][1] == simbolo:
            print("Gano",simbolo)
            flag_win=True

        #valida la columna 2
        elif matriz[0][2] == simbolo and matriz[1][2] == simbolo and matriz[2][2] == simbolo:
            print("Gano",simbolo)
            flag_win=True

        #valida la fila 0
        elif matriz[0][0] == simbolo and matriz[0][1] == simbolo and matriz[0][2] == simbolo:
            print("Gano",simbolo)
            flag_win=True

        #valida la fila 1
        elif matriz[1][0] == simbolo and matriz[1][1] == simbolo and matriz[1][2] == simbolo:
            print("Gano",simbolo)
            flag_win=True

        #valida la fila 2
        elif matriz[2][0] == simbolo and matriz[2][1] == simbolo and matriz[2][2] == simbolo:
            print("Gano",simbolo)
            flag_win=True

        #valida en diagonal derecho
        elif matriz[0][0] == simbolo and matriz[1][1] == simbolo and matriz[2][2] == simbolo:
            print("Gano",simbolo)
            flag_win=True
    
        #valida en diagonal izquierdo
        elif matriz[0][2] == simbolo and matriz[1][1] == simbolo and matriz[2][0] == simbolo:
            print("Gano",simbolo)
            flag_win=True

        if jugador == True: #para cambiar de jugador de x a o
            jugador = False
            simbolo='x'
        else:
            jugador = True
            simbolo='o'    
    else:
        print("jugada invalida")   
        print("mal")

for x in range(0,3):
    print(matriz[x])