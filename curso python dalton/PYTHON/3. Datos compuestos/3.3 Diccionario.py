# Creando un diccionario
# La estructura de un diccionario es: Clave : Valor y separamos con comas
#                                       key : value
diccionario = {
    "clave" : "valor",
    "nombre" : "Darío Loza",
    "estudia" : "TUIA",
    "Rosario Central" : True,
    "Altura" : 1.70
}

# A diferencia de las listas, para hacer una llamada,  introducimos la clave (primer elemento)
# Para llamar al elemento se realiza de la siguiente forma:
print(diccionario["nombre"]) #"Darío Loza"
print(diccionario["Altura"]) #1.70