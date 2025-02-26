#solicita al usuario numeros o letras y pon numeros al inicio y letras al final
#recuerda que un numero puede contener uno o mas digitos
"""text1 ="3"
text2 ="h"

0 == 48
a == 97

ord('6') - ord('0')
54 - 48 = 6

ord('9') - ord('0')
57 - 48 = 9

ord('7') - ord('0')
55 - 48 = 7

ord('c') - ord('0')
99 - 48 = 51"""

caracter=""
list_final=[]
list_end=[]
while caracter != "idiota":
    print("Ingrese numeros o letras")
    caracter=input()

    if caracter != "idiota" and ord(caracter) > ord('9'):#esto valida si es una letra
        list_final.append(caracter)
    if caracter != "idiota" and ord(caracter) <= ord('9'):
        list_end.append(caracter)

print(list_final)  
print(list_end)
list_big=list_final + list_end
print(list_big)