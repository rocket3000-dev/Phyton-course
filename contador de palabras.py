#solicita al usuario dos textos
#texto1=saosoxoo
#palabra=oso
#retorna cuantas veces puede formar la palabra con texto1
list_abc=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
index=0
contador=0
flag=False
print("Ingrese un texto")
texto=input()
print("Ingrese otro texto")
palabra=input()
for m in palabra:
    index = ord(m) - ord('a')
    list_abc[index]+=1

for n in texto:
    index = ord(n) - ord('a')
    list_abc[index]-=1

for item in list_abc:
    if item > 0:
        flag=True

print(list_abc)

if flag:
    print("No se puede crear la palabra:",palabra)
else:
    print("Si se puede crear la palabra:",palabra)
#oso
#o=2
#s=1
#o in text1 = 10
#s in text2 = 2