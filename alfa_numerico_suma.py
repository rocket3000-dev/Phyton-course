#Un alfa numerico se compone con letras y numeros como por ejemplo ( hd7dt6bg4 )

print("Ingrese algo que contenga letras y numeros")
alfa_number=input()
result=0

for m in alfa_number:
    if m == "1":
        result+=1
    if m == "2":
        result+=2
    if m == "3":
        result+=3
    if m == "4":
        result+=4
    if m == "5":
        result+=5
    if m == "6":
        result+=6
    if m == "7":
        result+=7
    if m == "8":
        result+=8
    if m == "9":
        result+=9
    
print(result)
