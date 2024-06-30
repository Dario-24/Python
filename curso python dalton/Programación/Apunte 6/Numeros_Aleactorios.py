z=                                      "Números aleatorios"
# El módulo random proporciona funciones que generan números pseudoaleatorios (a los que simplemente
#llamaremos “aleatorios” de ahora en adelante). La función random devuelve un número flotante aleatorio
#entre 0.0 y 1.0 (incluyendo 0.0, pero no 1.0 ). Cada vez que se llama a random, se obtiene el número
#siguiente de una larga serie.

# Nota: Para poder invocar las funciones definidas en un módulo debemos indicar al intérprete dónde 
#se encuentran definidas, importando el módulo: import modulo

#RANDOM: Devuelve un número flotante aleatorio entre 0.0 y 1.0 (incluyendo 0.0, pero no 1.0 )
import random
for i in range (10):
    x = random . random ()
    print ( x )
    
# RANDIT():  toma los parámetros inferior y superior, y devuelve un entero entre inferior y superior 
#(incluyendo ambos extremos).
aleactorio_int= random . randint (5 , 74)
print(aleactorio_int)

#CHOICE()Para elegir un elemento de una secuencia aleatoriamente, se puede usar @italicchoice:
t = [1 , 2 , 3]
random . choice ( t )

