list_number=[]
number=0
index=0
result=0

while number != -1:
    print("Ingrese un numero o escriba -1 para finalizar")
    number=int(input())

    if number != -1:
        list_number.append(number)
                                 #0,1,2,3,4,5
#aqui la lista tiene los valores [1,2,3,4,5,6]
result = 1
for n in list_number:
    if index % 2 == 0:
        result *= list_number[index]

    index+=1
print(result)