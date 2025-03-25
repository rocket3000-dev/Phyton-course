number=0
list_number=[]
index=0
result=0
while number != -1:
    print("ingrese un numero o escriba -1 para finalizar")
    number=int(input())

    if number != -1:
        list_number.append(number)

for m in list_number:
    result+=list_number[index]

    index+=1

print(list_number)
print(result)

