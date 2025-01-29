#Un alfa numerico se compone con letras y numeros como por ejemplo ( hd7dt6bg4 )

print("Ingrese algo que contenga letras y numeros")
alfa_number=input()
result = 0

for m in alfa_number:
    if m == "1" or m == "2" or m == "3" or m == "4" or m == "5" or m == "6" or m == "7" or m == "8" or m == "9":
        result += ord(m) - ord('0')
    
print(result)