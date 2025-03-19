contador=-1
carro=0

fila = 0    #fila representa la lista en donde se colocara el carro
columna = 0 

"""0 = _ _ _ _ _
1 = * _ _ _ _
2 = _ _ _ _ _
3 = _ _ _ _ _
4 = _ _ _ _ _"""

while dir != "stop":
    print("l = izquierda u = arriba r = derecha b = abajo cuando quiera acabar ingrese stop")
    dir=input()
    #se limpia el mapa 
    lista_0=["_","_","_","_","_"]
    lista_1=["_","_","_","_","_"]
    lista_2=["_","_","_","_","_"]
    lista_3=["_","_","_","_","_"]
    lista_4=["_","_","_","_","_"]

    #esta seccion de if nos ayuda a actualizar la fila o la columna donde se encuentre el carro

    if dir == "l":      #aqui se decide si ira hacia la izquierda el coche
        columna-=1
    elif dir == "u":    #aqui se decide si ira hacia arriba el coche
        fila-=1
    elif dir == "r":    #aqui se decide si ira hacia la derecha el coche
        columna+=1
    elif dir == "b":    #aqui se decide si ira abajo el coche
        fila+=1
    
    #esta seccion de if nos ayuda a decidir que listas alterar   

    if fila == 0:
        lista_0[columna] = "🚗"
    elif fila == 1:
        lista_1[columna] = "🚗"
    elif fila == 2:
        lista_2[columna] = "🚗"
    elif fila == 3:
        lista_3[columna] = "🚗"
    elif fila == 4:
        lista_4[columna] = "🚗"
    
    print(lista_0)
    print(lista_1)
    print(lista_2) 
    print(lista_3)
    print(lista_4)