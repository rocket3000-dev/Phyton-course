#text1 = abcthgangtopqat 
#text2 = gato

list_abc=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
flag=False
contador=0

print("Ingrese un texto")
text=input()
print("Ingrese un ultimo texto")
word=input()

for palabra in text:
    index=ord(palabra) - ord('a')
    list_abc[index]+=2

for textos in word:
    index=ord(textos) - ord('a')
    list_abc[index]-=1

for pro in list_abc:
    if pro > 0:
        flag=True

print(list_abc)

if flag:
    print("No se puede repetir la palabra")

else:
    print("Se puede repetir dos veces")
    #Este es un cambio"