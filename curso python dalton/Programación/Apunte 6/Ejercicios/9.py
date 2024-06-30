# Proponga un función factorial que tome un entero positivo o cero y calcule su factorial. El factorial de un
#número n se obtiene la siguiente multiplicación: 1 x 2 x ... x n.

def factorial(numero):
    multiplicacion = 1
    for i in range(2,numero+1):
        multiplicacion *= i
    print(f"El factorial de {numero} es {multiplicacion}")
    
factorial(8)
        
