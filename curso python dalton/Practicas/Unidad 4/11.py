# Escriba un programa que dada una secuencia numérica compute la suma de los números pares. Utilice un 
# bucle while y la sentencia continue para saltear los casos donde el número no sea par.

# Resultados esperados:
valores = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
# suma -> 30

valores = [1 , 4 , 7 , 10]
# suma -> 14

suma = 0

for numeros in valores:
    if (numeros%2) != 0:
        continue
    elif (numeros%2) == 0:
      suma += numeros
    
print(suma)

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = 0
indice = 0

while indice < len(valores):
    if valores[indice] % 2 == 0:
        suma += valores[indice]
    indice += 1

print("suma ->", suma)