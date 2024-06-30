#Ejercicio 2 Escribir una función que calcule la longitud de una cadena.
#Nota: no utilizar la función len.

def longitudCadena():
    cadena = input("Ingrese una cadena: ")
    ordenado = sorted(cadena)
    cantidad = 0
    for i in ordenado:
        cantidad +=1
    print(f"La cadena ({cadena}) cuenta con {cantidad} elementos")
longitudCadena()

def longitud_cadena(cadena):
    longitud = 0
    for caracter in cadena:
        longitud += 1
    return longitud

# Ejemplo de uso
cadena_ejemplo = "Hola, mundo!"
print("La longitud de la cadena es:", longitud_cadena(cadena_ejemplo))
