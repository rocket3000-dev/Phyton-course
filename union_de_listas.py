#solicita dos listas de caracteres 
#ejemplo : lista 1 = 1,2,3
#ejemplo : lista 2 = a,b,c,d
#resultado = 3,2,1,d,c,b,a

caracter_1=0
caracter_2=0 
list_1=[]
lista_2=[]
contador_1=-2
contador_2=-2

while caracter_1 != "ñ":
    print("Ingrese un caracter para la primer lista o escriba ñ para finalizar")
    caracter_1=input()

    if caracter_1 != "ñ":
        list_1.append(caracter_1)
    contador_1+=1

print("okey ahora pasaremos a la segunda lista")

while caracter_2 != "ñ":
    print("Ingrese un caracter para la segunda lista o escriba ñ para finalizar")
    caracter_2=input()

    if caracter_2 != "ñ":
        lista_2.append(caracter_2)
    contador_2+=1

for ch in list_1:
    print(list_1[contador_1],end="")
    contador_1-=1

for ch in lista_2:
    print(lista_2[contador_2],end="")
    contador_2-=1

print()





