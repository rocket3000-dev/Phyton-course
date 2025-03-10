#solicita una cifra y suma sus digitos
#ejemplo : 585
#resultado = 5 + 8 + 5 = 18
result=0
print("Ingrese un numero")
numbers=input() # 5 8 5

for digito in numbers:
    print(digito)
    result+=int(digito)
    
print(result)