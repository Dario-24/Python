# Escriba un programa que dada una secuencia de números y un valor de umbral vaya sumando los números de la 
# secuencia hasta que la suma alcance el umbral. Utilice break para terminar la ejecución del bucle cuando 
# la suma alcance el umbral.

# Resultados esperados:

#############################################################################################################
EJERCICIO =               "A"
umbral = 21
valores = [3 , 5 , 4 , 4 , 5 , 5 , 3 , 5 , 2 , 7]
# suma -> 21

suma = 0
for numeros in valores:
    suma += numeros
    if suma >= 21:
        break
print (suma)

##############################################################################################################
EJERCICIO =               "B"
umbral = 34
valores = [3 , 5 , 4 , 4 , 5 , 5 , 3 , 5 , 2 , 7]
# suma -> 34
suma2 = 0
for numeros in valores:
    suma2 += numeros
    if suma2 >= 34:
        break
print(suma2)

##############################################################################################################
EJERCICIO =               "C"
umbral = 100
valores = [3 , 5 , 4 , 4 , 5 , 5 , 3 , 5 , 2 , 7]
# suma -> 43
suma3 = 0
for numeros in valores:
    suma3 += numeros
    if suma3 >= 100:
        break
print(suma3)