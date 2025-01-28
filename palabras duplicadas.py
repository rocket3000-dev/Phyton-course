#solicita una lista de palabras hasta que el usuario escriba stop
#perro , gato , conejo , perro , lombriz
#gato , conejo , lombriz 

"""list_animal=[]
word=""
list_final=[]
contador=0
list_duplicidi=[]

while word != "stop":
    print("Ingrese una palabra o escriba stop para finalizar")
    word=input()

    for palabra in list_animal:
        if word == palabra:
            contador+=1

    if contador != 0 and word != "stop":
        list_duplicidi.append(word)

    if contador == 0 and word != "stop":
            list_animal.append(word)

print(list_animal)"""

list_no_duplicates=[]
list_duplicates =[]
contador_no_duplicated=0
contador_duplicates=0
word=""
while word != "stop":
    print("ingrese una palabra o escriba stop para finalizar")
    word = input() #perro

    if word != "stop":
        #contar cuantas veces aparece la palabra word en la lista no duplicados
        for palabra in list_no_duplicates:#perro, gato
            if palabra == word:
                contador_no_duplicated+=1
        
        for palabra in list_duplicates:
            if palabra == word:
                contador_duplicates+=1

        if contador_duplicates  == 0 and contador_no_duplicated == 0:
            list_no_duplicates.append(word)
        
        if(contador_no_duplicated != 0):
            list_no_duplicates.remove(word)
            list_duplicates.append(word)
        
        contador_duplicates = 0
        contador_no_duplicated = 0

print(list_no_duplicates)
print(list_duplicates)