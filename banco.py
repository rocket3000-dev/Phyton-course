#saldo inicial 700
#el usuario puede realizar las siguientes operaciones
#abonar dinero
#retirar dinero
#consultar dinero
#no permitir retirar dinero si el saldo es insuficiente

def abonar(abono, saldo_actual):
    return(abono + saldo_actual)

def retirar(monto, saldo_actual):
    return(saldo_actual - monto)

saldo=700
accion=""
while accion != "a":
    print("Que deseas hacer / abonar,retirar,consultar")
    accion=input()

    if accion == "abonar":
        print("Ingresa la cantidad que dejara")
        cantidad=int(input())
        saldo=abonar(cantidad,saldo)
        print(saldo)

    elif accion == "retirar":
        print("Ingres la cantidad que retirara")
        cantidad=int(input())
        if cantidad < saldo:
            saldo=retirar(cantidad,saldo)
            print(saldo)
        else:
            print("error")

    elif accion == "consultar":
        print(saldo)
