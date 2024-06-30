# juego de adivinanza: Escribe un programa que elija un número aleatorio entre 1 y 10 y le pida al usuario que 
#adivine el número. Si el usuario adivina correctamente, el programa imprimirá "¡Ganaste!", de lo contrario,
#el programa imprimirá "Intenta de nuevo" y le dará otra oportunidad al usuario para adivinar.

import random
usuario = int(input("Ingrese un número del 1 al 10: "))
numero = random.randint(1,10)
if usuario == numero:
    print("¡Ganaste!")
else:
    print("Intenta de nuevo")

print(numero)