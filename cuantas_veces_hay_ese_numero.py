number=0
number_star=0
list_number=[]
contador=0

print("ingrese un numero solamente uno")
number_star=int(input())

while number != -1:
    print("ingrese un numero o escriba -1 para acabar")
    number=int(input())

    if number != -1:
        list_number.append(number)

for m in list_number:
    if m == number_star:
        contador+=1

print("el total de ",number_star ,"en tu lista de numeros es de",contador)
