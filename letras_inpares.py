#solicita un texto al usuario un texto e imprime las letras que esten en el indice impar
index=0
list_impar=[]

print("Ingrese un texto")
text=input()

for letra in text:
    if index %2 != 0:
        list_impar.append(letra)
    index+=1
    
print(list_impar)