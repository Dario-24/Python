diccionario = {
    "nombre": "Darío",
    "apellido": "Loza",
    "años": 21
}

#Iterar el diccionario para que nos de solo las claves
for keys in diccionario:
    print(keys)
print("-----------------")

#Iterrar un diccionario para darnos las claves y valores
for keys in diccionario.items():
    print(keys) #Este bloque imprime las tuplas ("key", "value")
print("-----------------")
    
for datos in diccionario.items():
    key = datos[0]    #Datos[0] equivale al indice 0 de la tupla (key) que da diccionario.items()
    value = datos[1]  #Datos[1] equivale al indice 1 de la tupla (valor) que da diccionario.items()
    print(f"La clave es {key} y el valor es {value}")
print("-----------------")