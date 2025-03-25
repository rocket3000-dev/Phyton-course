number=0
list_number=[]
max=0
index=0
flag=False

while number != -1:
    print("Ingrese un numero o pon -1 para acabar")
    number=int(input())

    if number != -1:
        list_number.append(number)

for m in list_number:
    if max < m[index]:
        max = m
        flag=True

    index+=1

print(flag)
