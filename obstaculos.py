#5 listas de tamaño 5
#un jugador inicia en la esquina superior
#en la lista existira _ que ese es camino libre
#en la lista existira $ que significa bloqueado

direcion = ""
fila = 0
columna = 0
fila_peon =  0
columna_peon = 0

while direcion != "stop":
    print("l = izquierda / u = arriba / r = derecha / b = abajo / stop = finaliza todo")
    direcion=input()

    list_0=["_","_","_","_","_"]
    list_1=["_","0","_","0","_"]
    list_2=["_","_","_","_","_"]
    list_3=["_","0","_","0","_"]
    list_4=["_","_","_","_","_"]

    #para saber a donde se dirigira el coche

    if direcion == "l":
        if columna_peon > 0:
            columna_peon-=1

    elif direcion == "u":
        if fila_peon > 0:
            fila_peon-=1

    elif direcion == "r":
        if columna_peon < 4:
            columna_peon+=1

    elif direcion == "b":
        if fila_peon < 4:
            fila_peon+=1

    #abajo es para cambiar el coche a otro lugar del mapa

    print(columna_peon)
    print(fila_peon)

    if fila_peon == 0:
        if list_0[columna_peon] != "0": #cuando el peon este en una posicion valida el rey se mueve a donde esta el peon    
            columna = columna_peon
            fila = fila_peon
            list_0[columna_peon] = "🚗"
        else:  #cuando el peon este en una posicion bloqueada debe regresar a donde esta el rey    
            fila_peon = fila
            columna_peon = columna
            print("No puedes pasar")

    elif fila_peon == 1:
        if list_1[columna_peon] != "0":
            columna = columna_peon
            fila = fila_peon       
            list_1[columna_peon] = "🚗"
        else:
            fila_peon = fila
            columna_peon = columna
            print("No puedes pasar")

    elif fila_peon == 2:
        if list_2[columna_peon] != "0":
            columna = columna_peon
            fila = fila_peon
            list_2[columna_peon] = "🚗"
        else:
            fila_peon = fila
            columna_peon = columna
            print("No puedes pasar")

    elif fila_peon == 3:
        if list_3[columna_peon] != "0":
            columna = columna_peon
            fila = fila_peon
            list_3[columna_peon] = "🚗"
        else:
            fila_peon = fila
            columna_peon = columna
            print("No puedes pasar")

    elif fila_peon == 4:
        if list_4[columna_peon] != "0":
            columna = columna_peon
            fila = fila_peon
            list_4[columna_peon] = "🚗"
        else:
            fila_peon = fila
            columna_peon = columna
            print("No puedes pasar")

    print(list_0)
    print(list_1)
    print(list_2)
    print(list_3)
    print(list_4)
