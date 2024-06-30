# Proponga una función que se llame hms_a_s que tome una duración expresada en horas, minutos y segundos,
# y devuelva esa misma duración expresada en segundos.

#21
#2
#17

FORMA_1 =                                                                                                ""
def hms_a_s():
    horas = int(input("Ingrese horas: "))
    minutos = int(input("Ingrese minutos: "))
    segundos = int(input("Ingrese segundos: "))
    seg_totales = horas*3600 + minutos * 60 + segundos
    return seg_totales
print(hms_a_s())

FORMA_2 =                                                                                                ""
def hms_a_s2(horas,minutos,segundos):
    seg_totales = horas*3600 + minutos * 60 + segundos
    return seg_totales
print(hms_a_s2(21,2,17)) #Le pasamos los valores acá