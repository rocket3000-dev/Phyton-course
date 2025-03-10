#solicita al usuario un numero e imprimelo de derecha a izquierda 
#ejemplo : 347 y como resultado : 743
list_final=[]
print("Ingrese un numero")
number=input()
index=len(number)   #esto es para saber su longitud
index-=1    #esto para que salga bien la canitdad de letra

while index >= 0:
    print(number[index],end="")
    index-=1

print()