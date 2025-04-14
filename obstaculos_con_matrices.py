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

dir = repr(input())
print(dir)

#if(dir == repr('\x1b[D')):
#if(dir == repr('\x1b[C')):

#if(dir == repr('\x1b[A')):
#if(dir == repr('\x1b[B')):

while direccion != repr("stop"):

    for fila_item in range(0, 5):
        print(matris[fila_item])

    print(" <- / izquierda : -> / derecha : flecha arriba / arriba : flecha abajo / abajo : stop / finish ")
    direccion= repr(input())



    if direccion == repr('\x1b[D'):            # Izquierda
        if columna_futura > 0:
            matris[fila_futura][columna_futura] = "_"      
            columna_futura-=1    



    elif direccion == repr('\x1b[C'):          # Derecha
        if columna_futura < 4:     
            matris[fila_futura][columna_futura] = "_"
            columna_futura+=1



    elif direccion == repr('\x1b[A'):          # Arriba
        if fila_futura > 0:
            matris[fila_futura][columna_futura] = "_"
            fila_futura-=1



    elif direccion == repr('\x1b[B'):          # Abajo
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