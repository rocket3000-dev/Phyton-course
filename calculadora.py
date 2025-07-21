


def suma(num1,num2):
    return num1+num2 

def resta(num1,num2):
        return num1-num2

def multiplicacion(num1,num2):
        return num1*num2

def division(num1,num2):
        return num1/num2


def calculadora():
    operacion=""
    while operacion != "-1":
        print("Escribe que quieres hace +,-,*,/")
        operacion=input()

        if operacion == "+":
            resultado=suma(5,7)
            print(resultado)

        elif operacion == "-":
            
            resultado=resta(15,7)
            print(resultado)

        elif operacion == "*":
            
            resultado=multiplicacion(8,7)
            print(resultado)

        elif operacion == "/":

            resultado=division(15,3)
            print(resultado)







def llamar_a_una_funcion_dentro_de_otra():
    calculadora()

    
llamar_a_una_funcion_dentro_de_otra()     
