tema =                                       "CICLO WHILE"
# Un ciclo while es un ciclo indefinido donde se repite el calculo del cuerpo mientras
# una cierta condicion es verdadera.

# while <condición>: #<condicion> es una expresion booleana, si se cumple, sigue el ciclo.
#     <hacer algo> # <hacer algo> es una o más instrucciones

# El sentido de esta instrucción es el siguiente:
# 1. Evaluar la condición
# 2. Si es falsa, salir del ciclo.
# 3. Si es verdadera, ejecutar el cuerpo.
# 4. Volver al inicio del ciclo y evaluar la condicion

tema =                                     "CICLO INTERACTIVO"

# Definimos una variable HayMasDatos, que valdrá "Si" mientras haya más datos
                   #Esta variable luego de su primer ejecución, no influye en while ya que dentro de while
HayMasDatos = "Si" #se le da su propio valor a la variable. Solo sirve de arranque.
while HayMasDatos == "Si":
    x = float(input("Ingrese un número: "))
    if x > 0:
        print("Es positivo")
    elif x<0:
        print("Es negativo")
    else:
        print("Es igual a 0")
    HayMasDatos = input("Hay más numeros? ingrese Si o No: ")
# El esquema del ciclo interactivo es el siguiente:
# 1. HayMasDatos hace referencia a "Si"
# 2. Mientras HayMasDatos haca referencia a "Si"
#   a) Pedir datos
#   b) Realizar calculos
#   c) Preguntar al usuario si hay más datis. HayMasDatos hace referencia al valor asignado.

