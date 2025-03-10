#una cifra e imprimela al revez sin usar texto
#738 = 837
print("Ingrese un numero")
number=int(input())

while number != 0:
    print(number%10,end="")
    number=int(number/10)

print("")