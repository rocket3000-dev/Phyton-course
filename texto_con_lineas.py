#texto = hola
#print : h-o-l-a
list_text=[]
print("Ingrese un texto el que sea")
text=input()
contador=len(text)

for m in text:

    list_text.append(m)
    if contador > 1:
        list_text.append("-")
    contador-=1

print(list_text)    # h-o-l-a
