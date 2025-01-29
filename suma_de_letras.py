#solicita un texto al usuario e imprime la suma de las letras ascii
contador=0
print("Ingrese un texto")
text=input()

for letras in text:
    number = ord(letras)
    contador+=number

print(contador)