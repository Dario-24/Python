#Escribir un programa que almacene la cadena de caracteres 'pepito' en una variable, pregunte al usuario 
# por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada 
# en la variable sin tener en cuenta mayúsculas y minúsculas.

variable = "pepito"
contraseña = input("Ingrese la contraseña: ")
if contraseña.lower() == variable:
    print("correcta")
else:
    print("incorrecta")