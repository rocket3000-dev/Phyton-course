#utiliza una matriz de 5x4
#el jugador iniciara en la cordenada 0,0
# a = izquierda
# w = arriba
# d = derecha
# s = abajo

matriz=[
    ['🚶','⬜','⬜','⬜','⬜'],
    ['⬜','⬜','⬜','⬜','⬜'],
    ['⬜','⬜','⬜','⬜','⬜'],
    ['⬜','⬜','⬜','⬜','⬜']
]

def valida_columna(columna):
    return columna >= 0 and columna <= 4

def valida_fila(fila):
    return fila >= 0 and fila <= 3

def up(fila_actual):
    es_valido=valida_fila(fila_actual-1)
    if es_valido:
        fila_actual-=1
    else:
        print("error")

    return fila_actual  



def down(fila_actual):
    es_valido=valida_fila(fila_actual+1)
    if es_valido:
        fila_actual+=1
    else:
        print("error")

    return fila_actual



def left(columna_actual):
    es_valido=valida_columna(columna_actual-1)
    if es_valido:
        columna_actual-=1 
    else:
        print("error")

    return columna_actual



def right(columna_actual):
    es_valido=valida_columna(columna_actual+1)
    if es_valido:
        columna_actual+=1
    else:
        print("error")
    
    return columna_actual







############################################


direccion=""
fila_jugador=0
columna_jugador=0

for map in range(0,4):
    print(matriz[map])

while direccion != "-1":
    print("Ingrese que direccion ira / a , w , s , d ")
    direccion=input()

    if direccion == "a":
        columna_anterior = columna_jugador
        columna_jugador = left(columna_jugador)

        matriz[fila_jugador][columna_anterior] = "⬜"
        matriz[fila_jugador][columna_jugador] = "🚶"

        print(columna_jugador)



    elif direccion == "d":
        columna_anterior= columna_jugador
        columna_jugador = right(columna_jugador)

        matriz[fila_jugador][columna_anterior] = "⬜"
        matriz[fila_jugador][columna_jugador] = "🚶"
        print(columna_jugador)



    elif direccion == "w":
        fila_anterior = fila_jugador
        fila_jugador = up(fila_jugador)

        if(valida_fila(fila_anterior)):
            matriz[fila_anterior][columna_jugador] = "⬜"#borrar la casilla anterior
            matriz[fila_jugador][columna_jugador] = "🚶"#mover el jugador a la nueva casilla
        print(fila_jugador)



    elif direccion == "s":
        fila_anterior = fila_jugador
        fila_jugador = down(fila_jugador)
        
        if valida_fila(fila_anterior):
            matriz[fila_anterior][columna_jugador] = "⬜"
            matriz[fila_jugador][columna_jugador] = "🚶"   
        
        print(fila_jugador)

    for map in range(0,4):
        print(matriz[map])
