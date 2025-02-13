number=0
contador=0
list_number=[]
list_zero=[]
while number != -1:
    print("Ingrese numeros")
    number=int(input())

    if number != -1 and number != 0:
        list_number.append(number)  #los ceros no se toman en cuenta 

    if number == 0:
        contador+=1
        list_zero.append(number)
        list_final=list_number+list_zero

print(list_number)
print(list_zero)
print(contador)
print(list_final)