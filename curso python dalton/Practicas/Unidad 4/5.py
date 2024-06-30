# Imprimir los primeros 10 valores de la secuencia de Fibonacci. La secuencia de Fibonacci es una serie de 
# números en la cual los dos primeros números son 0 y 1, y el siguiente número se corresponde a la suma de 
# los dos números anteriores. Resultado esperado: 0 1 1 2 3 5 8 13 21 34

fib = [0,1]
for i in range(2,10):
    fib += [fib[-1] + fib[-2]]
    print(*fib)