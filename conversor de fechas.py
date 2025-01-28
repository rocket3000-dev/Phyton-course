#01-06-2025 -> uno de Junio del dos mil veinticinco 
list_date_final=[]
index=0
print("Ingrese una fecha (como ejemplo 01-05)")
fecha=input()
dia = fecha[0] + fecha[1]
mes = fecha[3] + fecha[4]#02

if dia == "01":
    list_date_final.append("uno")
elif dia == "02":
    list_date_final.append("dos")
elif dia == "03":
    list_date_final.append("tres")
elif dia == "04":
    list_date_final.append("cuatro")
elif dia == "05":
    list_date_final.append("cinco")
elif dia == "06":
    list_date_final.append("seis")
elif dia == "07":
    list_date_final.append("siete")
elif dia == "08":
    list_date_final.append("ocho")
elif dia == "09":
    list_date_final.append("nueve")
elif dia == "10":
    list_date_final.append("diez")
elif dia == "11":
    list_date_final.append("once")
elif dia == "12":
    list_date_final.append("doce")
elif dia == "13":
    list_date_final.append("trece")
elif dia == "14":
    list_date_final.append("catorce")
elif dia == "15":
    list_date_final.append("quince")
elif dia == "16":
    list_date_final.append("diesiceis")
elif dia == "17":
    list_date_final.append("diesisiete")
elif dia == "18":
    list_date_final.append("diesiocho")
elif dia == "19":
    list_date_final.append("diecinueve")
elif dia == "20":
    list_date_final.append("veinte")
elif dia == "21":
    list_date_final.append("vientiuno")
elif dia == "22":
    list_date_final.append("veintidos")
elif dia == "23":
    list_date_final.append("veintitres")
elif dia == "24":
    list_date_final.append("veinticuatro")
elif dia == "25":
    list_date_final.append("veinticinco")
elif dia == "26":
    list_date_final.append("vientisies")
elif dia == "27":
    list_date_final.append("veintisiete")
elif dia == "28":
    list_date_final.append("veintiocho")
elif dia == "29":
    list_date_final.append("veintinueve")
elif dia == "30":
    list_date_final.append("treinta")
elif dia == "31":
    list_date_final.append("treintayuno")

list_date_final.append(" de ")

if mes == "01":
    list_date_final.append("Enero")
elif mes == "02":
    list_date_final.append("Febrero")
elif mes == "03":
    list_date_final.append("Marzo")
elif mes == "04":
    list_date_final.append("Abril")
elif mes == "05":
    list_date_final.append("Mayo")
elif mes == "06":
    list_date_final.append("Junio")
elif mes == "07":
    list_date_final.append("Julio")
elif mes == "08":
    list_date_final.append("Agosto")
elif mes == "09":
    list_date_final.append("Septiembre")
elif mes == "10":
    list_date_final.append("Octubre")
elif mes == "11":
    list_date_final.append("Noviembre")
elif mes == "12":
    list_date_final.append("Diciembre")

list_date_final.append(" del dos mil veinticinco")   
print(list_date_final)

"""    if date[0] == "0":
        if date[1] == "1":
            day="primero"
            list_date_final.append(day)
        elif date[1] == "2":
            day="dos"
            list_date_final.append(day)
        elif date[1] == "3":
            day="tres"
            list_date_final.append(day)
        elif date[1] == "4":
            day="cuatro"
            list_date_final.append(day)
        elif date[1] == "5":
            day="cinco"
            list_date_final.append(day)
        elif date[1] == "6":
            day="seis"
            list_date_final.append(day)
        elif date[1] == "7":
            day="siete"
            list_date_final.append(day)
        elif date[1] == "8":
            day="ocho"
            list_date_final.append(day)
        elif date[1] == "9":
            day="nueve"
        list_date_final.append(day)

    elif date[0] == "1":
        if date[1] == "0":
            day="diez"
            list_date_final.append(day)
        elif date[1] == "1":
            day="once"
            list_date_final.append(day)
        elif date[1] == "2":
            day="doce"
            list_date_final.append(day)
        elif date[1] == "3":
            day="trece"
            list_date_final.append(day)
        elif date[1] == "4":
            day="catorce"
            list_date_final.append(day)
        elif date[1] == "5":
            day="quince"
            list_date_final.append(day)
        elif date[1] == "6":
            day="dieciseis"
            list_date_final.append(day)
        elif date[1] == "7":
            day="diecisiete"
            list_date_final.append(day)
        elif date[1] == "8":
            day="dieciocho"
            list_date_final.append(day)
        elif date[1] == "9":
            day="diecinueve"
        list_date_final.append(day)

    elif date[0] == "2":
        if date[1] == "0":
            day="veinte"
            list_date_final.append(day)
        elif date[1] == "1":
            day="veintiuno"
            list_date_final.append(day)
        elif date[1] == "2":
            day="veintidos"
            list_date_final.append(day)
        elif date[1] == "3":
            day="veintitres"
            list_date_final.append(day)
        elif date[1] == "4":
            day="veinticuatro"
            list_date_final.append(day)
        elif date[1] == "5":
            day="veinticinco"
            list_date_final.append(day)
        elif date[1] == "6":
            day="veintiseis"
            list_date_final.append(day)
        elif date[1] == "7":
            day="veintisiete"
            list_date_final.append(day)
        elif date[1] == "8":
            day="veintiocho"
            list_date_final.append(day)
        elif date[1] == "9":
            day="veintinueve"
        list_date_final.append(day)

    elif date[0] == "3":
        if date[1] == "0":
            day="treinta"
            list_date_final.append(day)
        elif date[1] == "1":
            day="treintayuno"
            list_date_final.append(day)

for month in fecha:
    if month[3] == "0":
        if month[4] == "1":
            mes="Enero"
            list_date_final.append(mes)
        elif month[4] == "2":
            mes="Febrero"
            list_date_final.append(mes)
        elif month[4] == "3":
            mes="Marzo"
            list_date_final.append(mes)
        elif month[4] == "4":
            mes="Abril"
            list_date_final.append(mes)
        elif month[4] == "5":
            mes="Mayo"
            list_date_final.append(mes)
        elif month[4] == "6":
            mes="Junio"
            list_date_final.append(mes)
        elif month[4] == "7":
            mes="Julio"
            list_date_final.append(mes)
        elif month[4] == "8":
            mes="Agosto"
            list_date_final.append(mes)
        elif month[4] == "9":
            mes="Septiembre"
            list_date_final.append(mes)

    elif month[3] == "1":
        if month[4] == "0":
            mes="Octubre"
            list_date_final.append(mes)
        elif month[4] == "1":
            mes="Noviembre"
            list_date_final.append(mes)
        elif month[4] == "2":
            mes="Diciembre"
            list_date_final.append(mes)

print(list_date_final,"del dos mil veinticinco")"""
