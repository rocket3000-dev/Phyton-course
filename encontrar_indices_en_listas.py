number=0
list_number=[]
index=0

while number != -1:
    print("ingrese un numero o -1 para acabar")
    number=int(input())

    if number != -1:
        list_number.append(number)

print("de los numeros que ingresaste pon uno")
number_star=int(input())

for m in list_number:

    if m == number_star:
        print(index)

    index+=1