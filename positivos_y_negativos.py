#solicita al usuario numeros(positivos y negatvos) hasta que escriba "fin"
#despues crea una lista donde este al principio los positivos y negativos
#2,4,5,7,-4,-8,-1

number=0
list_positivo=[]
list_negativo=[]

while number != -999:
    print("ingrese un numero (positivo y negativo) o escribe -999 para finalizar")
    number=int(input())

    if number != -999 and number >= 0:
        list_positivo.append(number)
    elif number != -999 and number < 0:
            list_positivo.append(number)
print(list_positivo)
