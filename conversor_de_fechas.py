#01-06-2025 -> uno de Junio del dos mil veinticinco 
list_date_final=[]
index=0
print("Ingrese una fecha (como ejemplo 01-05)")
fecha=input()
dia = fecha[0] + fecha[1]
mes = fecha[3] + fecha[4]

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
#hubo algun cambio