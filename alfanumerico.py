#ingrese un texto y debe imprimirse solamente las letras

list_letras=[]

print("Ingrese un texto")
text=input()

for letra in text:
    if ord(letra) - ord('a') >= 0 or ord(letra) - ord('A') >= 0:
        list_letras.append(letra)

print(list_letras)