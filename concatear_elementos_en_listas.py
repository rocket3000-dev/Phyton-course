text=""
list_text=[]
final=""

while text != "-1":
    print("Ingrese una palabra o escriba -1 para finalizar")
    text=input()

    if text != "-1":
        list_text.append(text)

print(list_text)
index=len(list_text)

for m in list_text:

    final = m
    index+=1

print(final)