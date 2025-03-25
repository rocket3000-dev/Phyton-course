
number=""
list_number=[]

while number != "-1":
    print("ingrese un numero o escriba -1 para acabar")
    number=input()

    if number != "-1":
        list_number.append(number)

index_externo=len(list_number)

for elemento in list_number: 
    print(f"indice: {index_externo}, valor:{list_number[index_externo]}")

    index_externo-=1
    