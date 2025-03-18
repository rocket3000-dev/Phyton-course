#solicita al usuario una longitud 

#cada vez que el usuario escriba b retrocedera un espacio 

#cada vez que coloque f se movera un espacio hacia delante

#ejemplo : longitud=10
#🚗__________   [" 🚗 "]  <------ correct
#el usuario ingresa f
#_🚗_________
#cuando el carrito llegue a la meta se debe imprimir cunatos movimientos le tomo en llegar

contador=-1
carro=0
lista_casilla=[" 🚗 "]

print("ingrese un numero para la longitud de la pista")
longitud=int(input())

for carrera in range(int(longitud)):    #ya tenemos guardado la distancia que recorrera el coche
    lista_casilla.append("_")

print(lista_casilla)
print("para que tu coche avance 1 casilla ingrese f ")
print("y para que tu coche retroceda 1 casilla ingrese b ")

while carro < int(longitud):
    print(lista_casilla)
    print("f = +1 casilla / b = -1 casilla / llegua al final de la carrera") 
    casilla=input()

    if casilla == "f":  #por si quiere que el coche avance
        carro+=1
        lista_casilla.insert(0,"_")
        lista_casilla.pop()

    elif casilla == "b":    #por si quiere que el coche retroceda

        if carro >= 1: 
            carro-=1
            lista_casilla.pop(0)
            lista_casilla.append("_")

        else: 
            print("tu coche no puede retroceder mas")   #por si el coche esta en el punto de inicio 
            contador-=1

    contador+=1

print(lista_casilla)


print("tu coche 🚗 logro terminar la carrera")
print("la cantidad de intentos que le tomo fue de",contador)
