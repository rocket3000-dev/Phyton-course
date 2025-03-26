list_final=[]

print("Ingrese un numero")
number=int(input())
number *=2

for m in range(0,number):

    if m %2 == 0:
        list_final.append(m)

print(list_final)