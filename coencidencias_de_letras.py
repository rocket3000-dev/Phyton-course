#ingresa un texto y despues solicita letras hasta que coloque ñ
#imprime verdadero y falso si la letra esta contenida en el texto
#ejemplo : perrogato
#letras = aaaaaaaaaaao
#resultado = perrogato contiene las letras

flag=False
letra=""
list_letras=[]

print("Ingrese un texto")
texto_principal=input()

while letra != "ñ":
    print("ingrese una letra o escriba ñ para finalizar")
    letra=input()

    if letra != "ñ":
        list_letras.append(letra)

print(list_letras)
index=len(texto_principal)-1

for ch in list_letras:
    if ch == texto_principal[index]:
        flag=True
        print("okey")

print(index)
print(flag)