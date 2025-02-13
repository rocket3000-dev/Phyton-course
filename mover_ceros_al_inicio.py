number=0
list_zeros=[]
list_numeros=[]
list_final=[]

while number != -1:
    print("Ingrese numeros")
    number=int(input())

    if number != -1 and number == 0:
        list_zeros.append(number)

    if number != -1 and number != 0:    
        list_numeros.append(number)
    list_final=list_zeros+list_numeros

print(list_zeros)
print(list_numeros)
print(list_final)
