number=0
max=int(0)
big=0
list_number=[]
while number != -1:
    print("Ingrese un numero o escriba a para finalizar")
    number=int(input())

    if number != -1:
        list_number.append(number)

for m in list_number:
    if m > max:
        max=m

for n in list_number:
    if n > big:
        if n <= max:
            big=n
print(m)
print(n)