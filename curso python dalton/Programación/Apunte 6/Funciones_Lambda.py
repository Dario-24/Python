z=                                       "Funciones lambda"
# Las funciones lambda o anónimas son un tipo de funciones en Python que típicamente se definen en una
#línea y cuyo código a ejecutar suele ser pequeño.

# Lo que sería una función que suma dos números como la siguiente:
def suma (a , b ):
    return a + b

# Se podría expresar en forma de una función lambda de la siguiente manera:
lambda a , b : a + b

# Una función lambda no tiene un nombre, y por lo tanto salvo que sea asignada
#a una variable, no puede ser invocada

funcion_lambda = lambda a , b : a + b

# Se la llama como a cualquier otra función propia
print(funcion_lambda(7,4))



