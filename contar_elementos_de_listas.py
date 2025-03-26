list_number=[]
number=0
contador=0

while number != -1:
    print("pon un numero o escriba -1")
    number=int(input())

    if number != -1:
        list_number.append(number)

print("Ingrese un numero mediano a tu lista")
number_secret=int(input())

for m in list_number:

    if number_secret < m:
        contador+=1

print(contador)