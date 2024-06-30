#Ejercicio 3 Realizar una función que tome como parámetros 3 números, se fije cual es el número más 
# grande (N) y el más chico (M) y devuelva la potencia de Nᴹ. Utilizar solo funciones built in.

import random
import math
n1 = random.randint(1,10)
n2 = random.randint(1,10)
n3 = random.randint(1,10)

N = max(n1,n2,n3)
M = min(n1,n2,n3)
print (f"n1={n1}, n2={n2}, n3={n3}")
print(f"n = {N}")
print(f"m = {M}")
print(math.pow(N,M))

