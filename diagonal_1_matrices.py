matris=[
    [0, 1, 2, 3, 4]  ,  #fila 0
    [5, 6, 7, 8, 9]  ,  #fila 1
    [10,11,12,13,14] ,  #fila 2
    [15,16,17,18,19] ,  #fila 3
    [20,21,22,23,24]    #fila 4
]    

fila=5
columna=0

for diagonal in range(0,fila):
    print(f"fila numero {columna} : {matris[columna][diagonal]}")
    
    columna+=1