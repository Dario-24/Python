# Desempaquetamiento: Es una forma de crear variables nuevas. Por ejemplo, sumando los datos de una tupla, 
# lista o conjuntos.
datos_en_tupla = ("Darío", "Loza", 21)
datos_en_lista = ["Darío", "Loza", 21]
datos_en_set = {"Darío", "Loza", 21}
nombre, apellido, edad = datos_en_tupla #Esto nos permite, colocarle un valor a cada elemento de la tupla
print(edad) #Esto imprime 21
#El desempaquetado funciona solo si cantidad_de_variables == cantidad_de_datos

