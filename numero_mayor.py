number=0
list_number=[]
index=0
list_big=[]

while number != -1:
    print("Ingrese un numero o pon -1")
    number=int(input())

    if number != -1:
        list_number.append(number)

print("Ingrese un numero para que despues te imprima los numeros mas altos que el que ingresaste")
number_secret=0

for m in list_number:

    if  list_number[index] > number_secret :
        list_big.append(m)

    index+=1    

print(list_big)