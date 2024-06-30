def suma(a, b):
    return a + b

def mostrar_menu():
    print("""¿Qué operación desea realizar?
    Suma(1)
    Resta(2)
    División(3)
    Multiplicación(4)
    Factorial(5)
    Volver al Menú Principal(0)""")

while True:
    mostrar_menu()
    opcion = int(input("Ingrese su opción: "))

    if opcion == 0:
        print("Saliendo del programa...")
        break
    elif opcion == 1:
        while True:
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            print("La suma es:", suma(a, b))
            continuar = input("¿Desea realizar otra suma? (s/n): ")
            if continuar.lower() != 's':
                break
    elif opcion == 2:
        # Lógica para la opción Resta
        pass  # Placeholder para la lógica de la resta
    elif opcion == 3:
        # Lógica para la opción División
        pass  # Placeholder para la lógica de la división
    elif opcion == 4:
        # Lógica para la opción Multiplicación
        pass  # Placeholder para la lógica de la multiplicación
    elif opcion == 5:
        # Lógica para la opción Factorial
        pass  # Placeholder para la lógica del factorial
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
