matris=[
    ["_","_","_","_","_"],   #fila 0
    ["_","_","_","_","_"],   #fila 1
    ["_","_","_","_","_"],   #fila 2
    ["_","_","_","_","_"],   #fila 3
    ["_","_","_","_","_"]   #fila 4
]
#🚗
fila=0
columna=0
direccion=""

while direccion != "stop":

    for fila_item in range(0, 5):
        print(matris[fila_item])

    print("l / izquierda : r / derecha : u / arriba : b / abajo : stop / finish ")
    direccion=input()


    if direccion == "l": 
        matris[fila][columna] ="_"      
        columna-=1

    elif direccion == "r":
        matris[fila][columna] ="_"
        columna+=1

    elif direccion == "u":
        matris[fila][columna] ="_"
        fila+=1

    elif direccion == "b":
        matris[fila][columna] ="_"
        fila-=1

    matris[fila][columna]="🚗"