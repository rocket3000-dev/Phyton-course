#solicita un texto alfanumerico (mayusculas y minusculas) e imprime solo las consonantes

list_consonante=[]

print("ingrese un texto alfanumerico")
text=input()

for letra in text:  #para recorrer las letras
    if ord(letra) - ord('a') >= 0 or ord(letra) - ord('A') >= 0:    #para validar si es mayuscula o minuscula
        if ord(letra) - ord('a') >= 0:  #para saber si no es un numero
            if ord(letra) != ord('a') and ord(letra) != ord('e') and ord(letra) != ord('i') and ord(letra) != ord('o') and ord(letra) != ord('u'):  #para que no agrege vocales
                list_consonante.append(letra)
        else:
            if ord(letra) != ord('A') and ord(letra) != ord('E') and ord(letra) != ord('I') and ord(letra) != ord('O') and ord(letra) != ord('U'):  #para que no agrege vocales
                list_consonante.append(letra)

print(list_consonante)
