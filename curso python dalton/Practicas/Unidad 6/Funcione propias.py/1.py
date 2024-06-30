# Ejercicio 1 Realizar una función que calcule la suma de dos números. En el algoritmo principal le pediremos 
#al usuario que ingrese por consola los dos números para pasárselos a la función. Después la función 
#calculará la suma y lo devolverá para imprimirlo en el algoritmo.

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

def suma():
    sum = n1 + n2
    print(sum)
suma()
