list_number=[]
list_original=[]
k=0
number=0
contador=1
list_sort=[]

while number != -1:
    print("Ingrese un orden de numeros y escriba -1 para finalizar")
    number=int(input())

    if number != -1:
        list_number.append(number)
        list_original.append(number)
print("Cuanto quieres que se inviertan")   
k=int(input())     

for m in list_number:
    
    if contador > len(list_number) - k:
        list_sort.append(m)

    contador+=1

for n in range(0, k):
    list_number.pop()

print(list_number)

while len(list_sort) != 0:
    list_number.append(list_sort.pop()) 

print(list_original)    #lista original
print(list_number)      #lista invertida
