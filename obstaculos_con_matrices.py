matris=[
    ["_","_","_","_","_"],
    ["_","_","x","_","_"],
    ["_","_","_","_","_"],
    ["_","_","x","_","_"],
    ["_","_","_","_","_"]
]
direccion=""
fila=0
columna=0
fila_futura=0
columna_futura=0

while direccion != "stop":

    for fila_item in range(0, 5):
        print(matris[fila_item])
        
    print("l / izquierda : r / derecha : u / arriba : b / abajo : stop / finish ")
    direccion=input()



    if direccion == "l":            # Izquierda
        if columna_futura > 0:
            matris[fila_futura][columna_futura] = "_"      
            columna_futura-=1    



    elif direccion == "r":          # Derecha
        if columna_futura < 4:     
            matris[fila_futura][columna_futura] = "_"
            columna_futura+=1



    elif direccion == "u":          # Arriba
        if fila_futura > 0:
            matris[fila_futura][columna_futura] = "_"
            fila_futura-=1



    elif direccion == "b":          # Abajo
        if fila_futura < 4:
            matris[fila_futura][columna_futura] = "_"
            fila_futura+=1


    
    if(matris[fila_futura][columna_futura] != "x"):
        fila = fila_futura
        columna = columna_futura

    else:
        fila_futura = fila
        columna_futura = columna
    
    matris[fila][columna]="🚗"