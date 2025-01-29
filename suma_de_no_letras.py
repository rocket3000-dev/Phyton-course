#un texto puede contener de todo y van a sumar todos los caracteres que no sean letras (ascii)
result=0

print("Ingrese algo")
text=input()

for m in text:
    if m != "a" and m != "b" and m != "c" and m != "d" and m != "e" and m != "f" and m != "g" and m != "h" and m != "i" and m != "j" and m != "k" and m != "l" and m != "m" and m != "n" and m != "o" and m != "p" and m != "q" and m != "r" and m != "s" and m != "t" and m != "u" and m != "v" and m != "w" and m != "x" and m != "y" and m != "z":

        number=ord(m)
        result+=number

print(result)