#SET: Nos sirve para crear conjuntos
#Los datos de ser (o conjuntos) no son modificables.
conjunto = set(["dato1", "dato2"])
print(conjunto)

#FROZENSET: Sirve para meter un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}
print(conjunto2)


#Teoría de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#ISSUBSET: Permite ver si un conjunto es subconjunto de otro.
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1 #Esto es lo mismo que usar issubset
print(resultado) #Esto imprime True, porque el conjunto2 es subconjunto de conjunto1

#ISSUPERSET: Permite ver si un conjunto es un superconjunto de otro 
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto1 >= conjunto2 #Esto es lo mismo que usar issuperset
print(resultado) #Esto imprime True, porque el conjunto1 es superconjunto de conjunto2

#ISDISJOINT: Para ver si dos conjuntos son completamente diferentes
#Va a ser True cuando no compartan ningún elemento
#Va a ser False cuando haya minimo un elemento que coincida
resultado = conjunto2.isdisjoint(conjunto1)


