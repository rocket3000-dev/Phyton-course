number=0
list_number=[]
list_final=[]

while number != -1:
    print("Ingrese un numero o escriba -1")
    number=int(input())

    if number != -1:
        list_number.append(number)

print("Ingrese un numero para que se multiplique con los de la lista")
multiplicar=int(input())

for m in list_number:

    result=m*multiplicar
    list_final.append(result)

print(list_final)