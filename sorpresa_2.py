contador=0
print("Ingrese un texto")
text=input()

for m in text:
    if m == "a":
        contador+=1
print("el total de a en tu texto es",contador)
