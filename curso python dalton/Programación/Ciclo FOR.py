# Ciclos definidos FOR.
# for <variable> in <secuencia de valores>

#Por ejemplo:
suma = 0
for i in [1, 2, 3, 4, 5]:
    nota = int(input("Ingrese una nota: "))
    suma = suma + nota
print("El promedio es", suma/5)

#RANGE(): Sirve para generar una secuencia de enteros en un ciclo definido
# range(inicio, fin, salto)
#Solo es obligatorio el fin, si no se establece un inicio, este será 0.


# Ejemplo de uso FOR y RANGE:
cant = int(input("Cuantos numeros desea ingresar: "))
for i in range(cant): # range(cant) da como final el numero que ingrese el usuario. 5 = [range(0,5,1)]=[0,1,2,3,4]
    x = float(input("Ingrese un numero: "))
    if x > 0:
        print("Es numero positivo")
    elif x < 0:
        print("Es negativo")
    else:
        print("Es igual a 0")
