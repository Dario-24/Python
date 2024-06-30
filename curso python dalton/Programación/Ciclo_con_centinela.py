# Para evitar preguntarle al usuario si desea seguir, podemos usar el método de centinela: un valor
# distinguido que; si se lee, le indica al programa que el usuario desea salir del ciclo.

# En este caso podemos suponer que si ingresa el carácter ’*’ es una indicación de que desea terminar.

# El equema es el siguiente:
# 1. Pedir datos.
# 2. Mientras el dato pedido no coincida con el centinela:
# a) Realizar cálculos
# b) Pedir datos

x = input("Ingrese un número (* para terminar): ")
while x != "*":
    x = float(x)
    if x > 0:
        print("Es positivo")
    elif x < 0:
        print("Es negativo")
    elif x == 0:
        print("Es igual a 0")
    else:
        print("Error")
    x = input("Ingrese un número (* para terminar): ")
    
breakk =                                  "TRUE Y BREAK"
# Para evitar problemas inecesarios, podemos tomar un while como True para que su ciclo se repita 
# indefinidamente, para lo que necesitaremos también un break
# Break nos permite salir de adentro de un ciclo (Tanto sea for como while en medio de su ejecución.)
# El diseño es el siguiente:
# 1. Repetir indefinidamente 

# while <condición>:
#     <hacer_algo_1>
#     if <condif>:
#         break
#     <hacer_algo_2>

while True:
    x = input("Ingrese un número (* para terminar): ")
    if x == "*":
        break
    x = float(x) #Convertimos la cadena a número
    if x > 0:
        print("Es positivo")
    elif x < 0:
        print("Es negativo")
    else:
        print("Es iguala 0")

Continue =                                       "CONTINUE"
#  Continue se salta todo el código restante en la iteración actual y vuelve al principio en el caso de que aún
# queden iteraciones por completar
#  La diferencia entre el break y continue es que el continue no rompe el bucle, si no que pasa a la siguiente
# iteración saltando el código pendiente

while True:
    x = input("Ingrese un número (* para terminar): ")
    if x == "*":
        break
    x = float(x) #Convertimos la cadena a número
    if x > 0:
        print("Es positivo")
    elif x == 0:
        continue 
    else:
        print("Es negativo")

Pass =                                           "PASS"
#  La ejecución de pass no produce efecto alguno más que evitar un error de sintaxis. Usualmente se utiliza
# para reservar un espacio dentro del código para lineas que todavía no han sido escritas.
while True:
    x = input("Ingrese un número (* para terminar): ")
    if x == "*":
        break
    x = float(x) 
    if x > 0:
        print("Es positivo")
    elif x == 0:
        pass
    else:
        print("Es negativo")    
    