#solicita una letra e imprime el resto del abecedario incluyendo la letra
list_abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
contador1=-1
contador2=1

print("Ingrese una letra")
letra=input()

for a in list_abc:
    contador1+=contador2

    if ord(letra)-ord('a') == 0:
        contador2-=1

contador3=len(list_abc)

for m in list_abc[contador1:contador3]:
    print(m)

print()