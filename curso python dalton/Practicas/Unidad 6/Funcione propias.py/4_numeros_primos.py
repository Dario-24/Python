# Ejercicio 4 Un número es primo si solo si sus únicos divisores son 1 y el mismo número.
#a. Escriba una función que determine si un numero es primo o no.
#b. Escriba otra función que reciba un número n e imprima todos los números primos menores que n.

def es_primo(numero):
    contador = 0
    for i in range(1,numero+1):
        if numero % i == 0:
            contador +=1
    if contador == 2:
        print(f"{numero} es un número primo")

def primos_menores(n):
    for i in range(1,n):
        if es_primo(i):
            print(i)
            
es_primo(29)
es_primo(28)

primos_menores(28)


