#solicita al usuario un texto y cambia las letras en la posicion inpar a una pocision par
#ejemplo:  a b c d
#letras pares a , c
#letras inpares b , d
# b a d c
index=0
list_final=[]
list_par=[]
list_impar=[]

print("Ingrese un texto")
text=input()

for l in text:
    list_final.append("-")

for m in text:
    if index %2 == 0:
        list_par.append(m)
    else:
        list_impar.append(m)
    
    index+=1

#lista_par=[g , t]
#lista_impar=[a , o]
index = 1
for n in list_par:
    list_final.pop(index)
    list_final.insert(index, n)
    index+=2

index = 0
for j in list_impar:
    list_final.pop(index)
    list_final.insert(index, j)
    index+=2

print(list_final)