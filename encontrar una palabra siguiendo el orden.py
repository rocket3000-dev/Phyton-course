#text_big=xpnerrenrsrt
#text_litle=perro
index=0
frase_finally=""
flag=False

text_big=input("Ingrese una palabra (ejemplo=xpesvrmgvo)")
text_min=input("Inrese una palabra (ejemplo=perro)")
l = len(text_min)#2

#abcd
#be
for letra_text_largo in text_big:    
    if l > 0 and letra_text_largo == text_min[index]:        
        index+=1
        l-=1

    if l == 0:
        flag = True

if flag:
    print("Si se puede crear la palabra", text_min)
else:
    print("No se puede crear la palabra", text_min)