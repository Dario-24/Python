# Ejercicio 3 Realizar una función que pida al usuario una frase y una letra a buscar en esa frase. 
# La función debe devolver la cantidad de veces que encontró la letra.

def buscarletra():
    palabra = input("Ingrese la palabra: ")
    letra = input("Ingrese la letra que quiere buscar: ")
    coincidencias= palabra.count(letra)
    print(f"La letra {letra} se encontró {coincidencias} veces")

buscarletra()