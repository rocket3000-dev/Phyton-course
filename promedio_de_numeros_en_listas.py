number=0
list_promedio=[]
index=0
result=0
contador=0

while number != -1:
    print("Ingrese un numero o escriba -1 para acabar es para tu promedio")
    number=int(input())
    contador+=1

    if number != -1:
        list_promedio.append(number)
contador-1
for m in list_promedio:    

    result=list_promedio[index]
    index+=1

print(result/contador)