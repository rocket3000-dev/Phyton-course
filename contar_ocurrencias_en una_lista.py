number=0
list_number=[]
contador=0

while number != -1:
    print("Ingrese un numero o escriba -1")
    number=int(input())

    if number != -1:
        list_number.append(number)

print("de los tantos numeros que ingresaste cual de ellos quieres saber cuantas veces fue ingresado")        
number_secret=int(input())

for m in list_number:

    if m == number_secret:
        contador+=1

print("El total de veces de",number_secret,"fue",contador)