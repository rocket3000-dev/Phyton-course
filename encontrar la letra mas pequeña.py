#text_big = jpnkxbtz
#la letra mas pequeña es la b
mini_letra=122

print("Ingresa una palabra rara")
text_big="jpnkxbtz"

for letra in text_big:
    if ord(letra) < mini_letra:
        mini_letra = ord(letra)

print(chr(mini_letra))




