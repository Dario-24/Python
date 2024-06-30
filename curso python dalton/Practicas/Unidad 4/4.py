# Dada la siguiente secuencia de números:
numeros = [12 , 75 , 150 , 180 , 145 , 525 , 50]
# imprimir aquellos divisibles por 5 y menores a 150.

for numero in numeros:
    resto = (numero %5)
    if resto != 0:
        continue
    elif numero >150:
        continue
    else:
        print(numero)

# Segunda opción
for numero in numeros:
    if numero % 5 == 0 and numero < 150:
        print(numero)
