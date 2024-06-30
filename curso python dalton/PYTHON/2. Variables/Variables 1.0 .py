# Una variable  es un objeto de memoria cuyo valor puede cambiar durante el desarrollo del algoritmo o ejecución del 
# programa. La declaración implica darle un lugar en memoria, un nombre y un tipo de dato asociado.
# La declaración se hace con el signo =. ejemplos:

x = 10
y = 5
c = x + y
# La variable se puede redefinir y no cambia lo sucedido anteriormente. 
#El alcance (o el bloque de código) donde puede ser utilizada una variable definida se llama scope
campeon = "Francia"
print(campeon) #Esto imprimirá "Francia"
campeon = "Argentina" #El valor de la variable campeon ya no imprimirá más "Francia", sino, "Argentina"
perro = "mili"
delincuencia = "mucha"

#Para Eliminar una variable, usamos el comando DEL:
del delincuencia
print (delincuencia) #Este print dará error ya que eliminamos la delincuencia.