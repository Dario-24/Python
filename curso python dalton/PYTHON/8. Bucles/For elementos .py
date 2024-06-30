#Un elemento iterable en Python es cualquier objeto que se puede recorrer o iterar mediante un bucle. 
#Esto significa que puedes recorrer sus elementos uno a uno. Los elementos iterables pueden ser, por ejemplo, 
#listas, tuplas, diccionarios, conjuntos e incluso strings. Para recorrer un elemento iterable, 
#puedes utilizar un bucle for o funciones que acepten iterables como argumentos
#Ejemplo:

animales = ["perro","gato","loro","cocodrilo","pez"]
for animal in animales:
    print(animal)
    
# ROL DE ANIMAL: cuando se ejecute el código, animal va a ser igual al primer elemento (perro), cuando termina de
# dar la vuelta al bloque va a revisar si hay mas elementos en la lista, si los hay, se va a volver a ejecutar,
# pero ahora animal va a ser igual al siguiente elemento (gato) y volverá a ejecutar el bloque. Termina de 
# ejecutarse y consulta si hay otro elemento en la lista animales, el cual sería loro el siguiente, y se ejecutaría
# animal = loro, lo mismo sucede posteriormente con cocodrilo, pasando a ser animal = cocodrilo y ejecutando el 
# bloque de código, que en este caso ejecuta un print para todos los casos

#Otro ejemplo:
numeros = [27,35,76,29,92]
for numero in numeros:
    numero_doble = numero * 2
    print(numero_doble) # Esto nos dará cada uno de los numeros, multiplicados por 2.

# ZIP(): Sirve para iterar dos o más listas al mismo tiempo
# Ambas listas tienen que tener la misma cantidad de elementos, en caso contrario, el bucle termina con el indice 
# mayor compartido

for numero, animal in zip(numeros,animales):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")
    
#RANGE(): Itera numeros desde el inicio al final de los parametros.
for num in range(5,10):
    print(num)
    
#ENUMERATE(): Sirve para recorrer una lista con su indice.
for num in enumerate(numeros):
    print(num) # Esto nos muestra una tupla de (indice, valor)
    indice = num[0] # El 0 y 1 hace referencia al indice de la tupla que se crea, siendo 0 el indice y 1 el valor.
    valor = num[1]
    print(f"El indice es {indice} y su valor es {valor}")
    
#FOR/ELSE
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, el valor actual es: {numero}")
else:
    print("El bucle ha finalizado")
    
#Todo lo anterior funciona tanto para tuplas como para listas y conjuntos.