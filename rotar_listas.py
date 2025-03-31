number=0
list_number=[]
lista_invertida=[]
k=-1

while number != -1:
    print("Ingrese un numero o pon -1  para acabar")
    number=int(input())

    if number != -1:
        list_number.append(number)
        k+=1
print("Escribe un numero para que rote")
contador=int(input())

for a in list_number:

    if contador == k:
        contador=0

    lista_invertida.append(list_number[contador])
    contador+=1
    
print(lista_invertida)    
print(list_number)