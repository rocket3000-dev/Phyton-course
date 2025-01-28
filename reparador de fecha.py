#01--------05------25
#01-05-25
list_final=[]
index=2
print("Ingrese una fecha descompuesta (01-----05--25 -> 01-05-25)")
list_fecha="01----05--25"
list_final.append(list_fecha[0] + list_fecha[1] + "-")

for indice in range(2, len(list_fecha)-2):
    #print("valor de fecha ", list_fecha[indice])
    if list_fecha[indice] != "-":
        list_final.append(list_fecha[indice])

list_final.append("-")
list_final.append(list_fecha[len(list_fecha)-2] + list_fecha[len(list_fecha)-1])

for m in list_final:
    print(m, end="")

print()