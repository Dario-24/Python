# Imprimir el valor factorial del número 5 usando un bucle. El valor factorial (símbolo: !) se obtiene de 
# multiplicar todos los números enteros desde el número elegido hasta 1. Resultado esperado: 120

factorial = 1

for numero in range(5, 0, -1):
    factorial *= numero

print(factorial)
