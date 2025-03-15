#solicita al usuario ingresar materias 
#despues de solicitar todas las materias dile al usuario las calificaciones
#despues de aver capturado las materias y calificaciones por separado el usuario podra consultar (hasta que coloque -1) su calificacion colocando la materia
#lista de materia = matematicas , español , ingles
#lista de calificaciones = 8 , 9 , 5

materias=""
calificacion=0
asignatura=""
list_materia=[]
list_calificacion=[]
contador=-1
uno=1
contador2=-1

while materias != "ñ":
    print("Ingrese una materia (asignatura) o escriba ñ para finalizar")
    materias=input()

    if materias != "ñ":
        list_materia.append(materias)
        contador_materia=len(list_materia)

while calificacion != "-1":
    print("ingrese su calificacion")
    calificacion=input()

    if calificacion != "-1":
        list_calificacion.append(calificacion)

while asignatura != "ñ":
    print("Que calificacion quieres saber (ingrese la materia) o ingrese ñ para acabar")
    asignatura=input()

    for m in list_materia:
        contador+=uno
        contador2+=uno

        if asignatura == m:
            print(m,",",list_calificacion[contador])
            uno-=1

        elif contador2 == contador_materia:
            print("materia no encontrada")

    uno=1
    contador2=0
    contador=-1