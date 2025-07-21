
#una funcion comienza con def
#despues es el nombre de la funcion
#despues ()
#al final {}
def saludar() :{
    print("hola")
}

#saludar()
#entre los parentesis podemos recibir parametros

def sumar(num1, num2) :{
    print(num1+num2)
}

#sumar(2, 3)

def division(num1, num2) :  
    return num1 / num2 

resultados=division(88,3)

#print(resultado)

#ejercicios :v

def multiplicar(num1,num2):
    print(num1*num2)

multiplicar(8,7)


def edad():{
    print("Iker es bien noob")
}
edad()


def resta(num1,num2):
    return num1-num2

resultado=resta(35,17)

print(resultado)



def porcentaje(num1,num2):
    return num1%num2

resultado=porcentaje(78,17)

print(resultado)


def matriz(fila,columna):
    flag_fila= fila >= 0 and fila <=2
    flag_columna=columna >=0 and columna <=2
    return flag_fila and flag_columna    


def matriz2(fila,columna):
    return fila >= 0 and fila <=2 and columna >= 0 and columna <=2

resultado=matriz(0,5)

print(resultado)

