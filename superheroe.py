class Hombre_araña:
    def __init__(self,joven,inteligente,fuerte,nivel_vida):
        self. joven = joven
        self. inteligente = inteligente
        self. fuerte = fuerte
        self. nivel_vida = nivel_vida

    def golpear(self):
        print("pega")

    def columpearse(self):
        print("columpear")

    def telaraña(self):
        print("lanza telarañas")

    def recibir_daño(self):
        self.nivel_vida-=1

#####################################################

opcion=0

edad = 22
inteligencia = "156 IQ"
fuerza = 678
nv = 100

heroe=Hombre_araña(edad,inteligencia,fuerza,nv)

while opcion != -1:
    print("que opcion desea ver / 1 = quien es / 2 = accion 1 / 3 = accion 2 / 4 = accion 3 / 5 = recibir daño / 6 = mostrar via")
    opcion=int(input())

    if opcion == 1:
        print("El superheroe es spiderman su edad es ", heroe.joven , "tiene un IQ de",heroe.inteligente,"con fuerza de",heroe.fuerte)

    elif opcion == 2:
        heroe.golpear()

    elif opcion == 3:   
        heroe.columpearse()

    elif opcion == 4:
        heroe.telaraña()  

    elif opcion == 5:   
        heroe.recibir_daño()
        print("Recibio daño spider man")

    elif opcion == 6:
        print("nivel de vida es",heroe.nivel_vida)