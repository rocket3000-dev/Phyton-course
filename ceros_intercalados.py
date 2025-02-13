number=0
contador=0
list_numbers=[]
#0,8,7,6,0,0,1
while number != -1:
    print("Ingrese numeros")
    number=int(input())

    if number != -1 and number != 0:
        list_numbers.append(number) #una lista sin ceros

    if number == 0:
        contador+=1
#------
for m in list_numbers:
    print(m, end="")
    print(",", end ="")
    if contador > 0:
        print(0, end="")
        print(",", end ="")
        contador-=1


for n in range(contador):
    print(0, end = ",")

print()
