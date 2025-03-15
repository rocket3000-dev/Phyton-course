print("ingrese un texto")
texto=input()

a=0
e=0
i=0
o=0
u=0

for m in texto:
    if m == "a":
        a+=1
    elif m == "e":
        e+=1
    elif m == "i":
        i+=1
    elif m == "o":
        o+=1
    elif m == "u":
        u+=1

print("el total de a es ",a)
print("el total de e es ",e)
print("el total de i es ",i)
print("el total de o es ",o)
print("el total de u es ",u)


