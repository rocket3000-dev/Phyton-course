word=""
list_big=[]
contado=0
while word != "stop":
    print("Ingrese una palabra o escriba stop para finalizar")
    word=input()#casa

    leng = 0
    for letra in word:#casa
        leng+=1
        if leng > 5:
            list_big.append(word)

print(list_big)