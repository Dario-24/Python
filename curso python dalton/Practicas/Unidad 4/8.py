# Resuelva los siguientes ejercicios:

# a. Calcular el cuadrado de los primeros 10 números enteros positivos.

# b. Calcular la suma de los números enteros entre 0 y 100 inclusive.

# c. Calcular la suma de los números pares menores a 100. ¿Cuántos números pares hay menores a 100?

# d. Calcular la suma de los números impares menores a 100. ¿Cuántos números impares hay menores a 100?

# A)

for numero in range(1,11):
    cuadrado = numero**2
    print(cuadrado)
    
# B)

enteros = 0
for numero in range(1,101):
    enteros += numero
print(F"La suma total es {enteros}")

# C)

suma = 0
cantidad = 0
for i in range(2,101,2):
    suma += i
    cantidad += 1
print (f"La totalidad de la suma de numeros pares es: {suma}")
print (f"Hay un total de {cantidad} numeros pares menores a 100")

# D)

suma = 0
cantidad = 0
for i in range(1,101,2):
    suma += i
cantidad = len(range(1,101,2))
print (f"La totalidad de la suma de numeros impares es: {suma}")
print (f"Hay un total de {cantidad} numeros impares menores a 100")