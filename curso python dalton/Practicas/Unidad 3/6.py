# Dada la nota de un parcial se quiere saber en que condición está el alumno.

# Si la nota no está entre 0 y 10: 'nota inválida'.
# Si la nota es mayor o igual a 0 y menor a 6: 'desaprobado'.
# Si la nota es mayor igual a 6 se debe mostrar en pantalla un mensaje que diga 'aprobado'.

nota = int(input("Inserte nota: "))
if 0 <= nota <6:
    print("Desaprobado")
elif 6 <= nota <= 10:
    print("Aprobado")
else:
    print("nota invalida")
