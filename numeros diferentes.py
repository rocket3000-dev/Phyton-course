#muestra en una lista los numeros que se repitan solo dos veces
#1,3,2,5,4,1,3 ---> 1,3

number=""
list_number=[]
list_duplicate=[]
contador_dup=0
contador_new=0

while number != "-1":
    print("Ingrese un numero o escriba -1 para finalizar")
    number=input()
    
    if number != "-1":
        list_number.append(number)

for num_main in list_number:

    for num_sec in list_number:

        if num_main == num_sec: 
            contador_dup+=1  

    if contador_dup == 2:
        #num_main = 1
        for num_new in list_duplicate:
            if num_main == num_new:
                contador_new+=1

        if contador_new == 0:
            list_duplicate.append(num_main)

    contador_new = 0
    contador_dup = 0

print(list_duplicate)