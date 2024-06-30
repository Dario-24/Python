# Escriba un programa que solicite un número entero al usuario y compute la suma de todos los números 
# naturales menores a él. Este programa debe ser interactivo. Es decir, el programa solicita un numero 
# al usuario, devuelve la suma, y solicita un nuevo número. Esto continúa así hasta que el usuario 
# ingresa "salir", determinando que el programa debe terminar. Utilice un bucle while para resolver este 
# problema. Tenga en cuenta la sentencia break para determinar la interrupción del bucle. Ejemplos:

# Ingrese un número o 'salir' para terminar : 10
# La suma es 45
# Ingrese un número o 'salir' para terminar : 50
# La suma es 1225
# Ingrese un número o 'salir' para terminar : salir

salida = "salir"
numero = input(f"Ingrese un numero o {salida} para terminar: ")
while True:
    if numero == salida:
        break
    numero = int(numero)
    suma_numero = sum(range(1,numero))
    print(suma_numero)
    numero = input(f"Ingrese un numero o {salida} para terminar: ")
        
    
    