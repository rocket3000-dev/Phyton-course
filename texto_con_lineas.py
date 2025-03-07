#texto = hola
#print : h-o-l-a

print("Ingrese un texto el que sea")
text=input()
contador=len(text)

for m in text:

    print(m, end="")
    if contador > 1:
        print("-",end="")
    contador-=1

print()




