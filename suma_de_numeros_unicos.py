numero=0
list_mappeo=[]
contador=0
max=0
result =0
lista_numero=[]
while numero != -1:
    print("Ingrese un numero entero o escriba a para acabar")
    numero=int(input())
    if numero != -1:
        lista_numero.append(numero)
    
    if numero != -1 and numero > max:
        max = numero

for i in range(0, max +1):
    list_mappeo.append(0)

#[0,0,0,0]
for m in lista_numero:#[3,2,1,1,3,4]
    list_mappeo[m]+=1

ind =0 
for n in list_mappeo:#[0,2,1,2,1]
    if n == 1:
        result+=ind
    
    ind+=1

print(result)