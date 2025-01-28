#1,2
#2
list_number=[]
number=0
contador=0

while number != -1:
    print("Ingrese un digito positivo o -1 para finalizar")
    number=int(input()) #10
    
    for n in list_number: #10,20,30
        if number == n:
            contador += 1

    if contador == 0 and number != -1:
        list_number.append(number)

    contador=0

print(list_number)