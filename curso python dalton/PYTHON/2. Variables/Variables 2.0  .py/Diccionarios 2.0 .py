#DICT(): sirve para crear un diccionario
#Con dict() podemos crear un diccionario vacío.
diccionario = dict(nombre = "Darío", apellido = "Loza")

#Las listas no pueden ser claves y usamos frozenset para meter conjuntos.
diccionario = {frozenset(["dalto","rancio"]):"jajas"}

#FROMKEYS: Funcion que nos permite crear diccionarios con todos los valores none.
#El primer dato es un iterable (algo que podemos iterar) y el segundo dato es a lo que vamos a igualar fromkeys
diccionario = dict.fromkeys(["nombre","apellido"]) #Imprimir esto nos daría None (predeterminado)
diccionario = dict.fromkeys(["nombre", "apellido"], "no sé") #Cambia el valor None a "no sé"
print (diccionario)