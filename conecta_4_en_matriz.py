matriz=[
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ','x',' ',' '],
    [' ',' ',' ','x','0',' ',' ']
]   # 0   1   2   3   4   5   6

columna = 0
fila = 0


while columna != -1:
    print("ingrese en que columna desea poner la ficha va del 0 hasta el 6")
    columna=int(input())
    fila = 6

    while (fila >= 0 and matriz[fila][columna] != ' '):  # descubir en que fila hay espacio 
        fila-=1

    
    # hasta aqui ya se que fila y en que columna estara la ficha
    
    if (fila >= 0):
        matriz[fila][columna] = '0'
    else:
        print("error fila llena")
    
    #[0][0][0][o][][][][]
    

    
    # este codigo valida la ficha actual hacia la izquierda
    
    columna_peon = columna
    bolitas_izq=0

    while columna_peon > 0 and matriz[fila][columna_peon-1] != ' ':
        bolitas_izq+=1
        columna_peon -= 1

    # este codigo valida la ficha actual hacia la derecha
    columna_peon = columna 
    bolitas_der = 0

    while columna_peon < 6 and matriz[fila][columna_peon+1] == '0':
        bolitas_der+=1
        columna_peon+=1

    # este codigo valida la ficha actual hacia abajo
    fila_peon = fila
    bolitas_vertical= 0

    while fila_peon >= 0:
        bolitas_vertical+=1
        fila_peon-=1

    if bolitas_izq == 3:
        print("ya ganaste izq")
        columna = -1

    elif (bolitas_der == 3):
        print("ya ganaste der")
        columna = -1
    
    elif bolitas_izq + bolitas_der == 3:
        print("ya ganaste ambos lados")
        columna = -1

    elif bolitas_vertical == 4:
        print("Ya ganaste vert")  
        columna = -1  

    for m in range(0,7):
        print(matriz[m])
