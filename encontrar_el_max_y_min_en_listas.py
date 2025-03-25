number=0
list_number=[]
max=0
min=100
while number != -1:
    print("Ingrese un numero o escriba -1 para finalizar")
    number=int(input())

    if number != -1:
        list_number.append(number)

print(list_number)

for m in list_number:
    
    if m > max:
        max=m

for n in list_number:

    if n < min:
        min=n

print(min)
print(max)

