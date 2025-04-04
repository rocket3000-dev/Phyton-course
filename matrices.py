matris=[
    [0, 1, 2, 3, 4] ,           #fila 0
    [5, 6, 7, 8, 9] ,           #fila 1
    [10,11,12,13,14] ,           #fila 2
    [15,16,17,18,19] ,           #fila 3
    [20,21,22,23,24]             #fila 4
]

fila = 5
columna = 5
fila_decrementa = 4
columna_decrementa = 4

for fila_item in range (0,fila):

    for columna_item in range(0,columna):
        print("el numero es",matris[fila_decrementa][columna_decrementa])
        columna_decrementa-=1
    fila_decrementa-=1

    columna_decrementa = 4

#print(matris)

#matris [fila][columna]
#el numero 13 esta en la fila 2 y en la columna 3
#el numero 24 esta en la fila 4 y en la columna 4
#el numero 9 esta en la fila 1 y en la columna 4
#el numero 3 esta en la fila 0 y en la columna 3

#print(matris[2][4])

"""print(matris[0][0])
print(matris[1][1])
print(matris[2][2])
print(matris[3][3])
print(matris[4][4])"""

"""print(matris[0][4])
print(matris[1][3])
print(matris[2][2])
print(matris[3][1])
print(matris[4][0])"""

"""print(matris[0][0])
print(matris[0][1])
print(matris[0][2])
print(matris[0][3])
print(matris[0][4])
print(matris[1][4])
print(matris[2][4])
print(matris[3][4])
print(matris[4][4])
print(matris[4][3])
print(matris[4][2])
print(matris[4][1])
print(matris[4][0])
print(matris[3][0])
print(matris[2][0])
print(matris[1][0])"""

"""fila = 5
columna = 5

#asi se recorre una matris

for fila_item in range(0,fila):
    #print("fila",fila_item,matris[fila_item])

    for columna_item in range(0,columna):
        print("el numero es",matris[fila_item][columna_item])"""