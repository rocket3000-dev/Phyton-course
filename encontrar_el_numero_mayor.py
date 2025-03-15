
number=0
max=0
list_number=[]

while number != -1:
    print("Ingrese un numero o escriba -1 para finalizar")
    number=int(input())

    if number != -1:
        list_number.append(number)

for m in list_number:
    if max < m:
        max = m

print(max)