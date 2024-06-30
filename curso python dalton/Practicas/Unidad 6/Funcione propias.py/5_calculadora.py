#Ejercicio 5 Realizar un menú similar a una calculadora. Funciones:

#Suma(num1, num2)
#Resta(num1, num2)
#Division(num1, num2)
#Multiplicacion(num1, num2)
#Factorial(num)
#Salir

import math

def suma(n1,n2):
    sum = n1 + n2
    return sum

def resta(n1,n2):
    rest = n1 - n2
    return rest

def division(n1,n2):
    div = n1/n2
    return div

def multiplicacion(n1,n2):
    mult = n1*n2
    return mult

def factorial(n1):
    fact = math.factorial(n1)
    return fact

def es_primo(numero):
    contador = 0
    for i in range(1,numero+1):
        if numero % i == 0:
            contador +=1
    if contador == 2:
        return True
    else:
        return False
    


def mostrar_menu():
    print("""¿Qué operación desea realizar?
    Suma(1)
    Resta(2)
    División(3)
    Multiplicación(4)
    Factorial(5)
    Salir(0)""")

while True:
    mostrar_menu()
    opcion = int(input("Ingrese su opción: "))

    if opcion == 0: #Salir
        print("Saliendo del programa...")
        break
    
    elif opcion == 1: #Suma
        while True:
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            print("La suma es:", suma(a, b))
            continuar = input("¿Desea realizar otra suma? (s/n): ")
            if continuar.lower() != 's':
                break
            
    elif opcion == 2: #Resta
        while True:
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            print("El resultado de la resta es:", resta(a, b))
            continuar = input("¿Desea realizar otra resta? (s/n): ")
            if continuar.lower() != 's':
                break
            
    elif opcion == 3: #División
        while True:
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            print("El resultado de la división es:", division(a, b))
            continuar = input("¿Desea realizar otra división? (s/n): ")
            if continuar.lower() != 's':
                break
    
    elif opcion == 4: #Multiplicación
        while True:
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            print("El resultado de la multiplicación es:", multiplicacion(a, b))
            continuar = input("¿Desea realizar otra multiplicación? (s/n): ")
            if continuar.lower() != 's':
                break
            
    elif opcion == 5: #Factorial
        while True:
            a = int(input("Ingrese el número: "))
            print("El resultado del factorial es:", factorial(a))
            continuar = input("¿Desea realizar otra operación? (s/n): ")
            if continuar.lower() != 's':
                break

    elif opcion == 6: #Número primo
        while True:
            a = int(input("Ingrese el número: "))
            if es_primo(a):
                print(f"{a} es un número primo")
            else:
                print(f"{a} no es número primo")
            continuar = input("¿Desea realizar otra operación? (s/n): ")
            if continuar.lower() != 's':
                break
    
    

            