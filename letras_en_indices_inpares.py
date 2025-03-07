#ingresa un texto e imprime las letras que estan en posiciones inpares
#ejemplo : h o l a
#          0 1 2 3

index=0
print("Ingrese un texto")
text=input()

for m in text:
    if index %2 != 0:
        print(m)
    index+=1

