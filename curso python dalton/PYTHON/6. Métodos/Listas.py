lista = ["hola", "Darío", 21, "1.70", "Argentino"]

# LEN: Sirve para contar la cantidad de elementos.
len_l = len(lista)

#APPEND: Sirve para agregar un elemento a la lista.
lista.append("10/05/2003")

#INSERT: Agrega elementos a la lista en un indice determinado.
lista.insert(4,"es")

#EXTEND: Sirve para agregar varios elementos a la lista.
lista.extend(["extend","extend2"])

#POP: Elimina un elemento de la lista por su indice
lista.pop(8) #elimina "extend2" ubicado en indice 8
lista.pop(-1) #elimina el ultimo elemento de la lista

#REMOVE: Remueve un elemento de la lista por su valor
lista.remove("es")

#CLEAR: Elimina todos los elementos de la lista
lista.clear()

#SORT: Ordena la lista de forma ascendente (False, True, Números). Da error si hay cadenas.
lista.sort()
#SORT(REVERSE=TRUE): Ordena la lista en forma descendente.
lista.sort(reverse=True)

#REVERSE: Invierte el orden de la lista(acepta cadenas)
lista.reverse()
print(lista)


