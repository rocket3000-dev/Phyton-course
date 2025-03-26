number=0
list_number=[]
index=0  

while number != -1:
    print("Ingrese un numero o pon -1 para acabar")
    number=int(input())

    if number != -1:
        list_number.append(number)

print("De los tantos numeros que ingresaste cual quieres saber")
number_secret=int(input())

for m in list_number:

    if m == number_secret:
        print("Numero encontrado en la posicion ",index)

    index+=1