diccionario = {
    "nombre": "Darío",
    "Apellido": "Loza",
    "Edad": 21,
    "Argentino": True
}

print(diccionario)

#KEYS: Devuelve las keys (tambien llamada claves). A la vez sirve para iterar.
claves = diccionario.keys()
print(claves) #devuelve nombre, apellido, edad y Argentino.

#GET: Sirve para devolver un valor, llamando a su clave
ver_valor = diccionario.get("Edad")
print(ver_valor) #devuelve 21

#CLEAR: Elimina todos los elementos del diccionario.
#diccionario.clear()

#POP: Elimina un elemento o varios del diccionario.
diccionario.pop("Apellido")
print(diccionario) #elimina la clave "Apellido"

#ITEMS: Devuelve un elemento dicc_items iterable
items = diccionario.items()
print(items)