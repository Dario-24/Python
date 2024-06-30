primer_parte=                   "Declaración e invocación de funciones propias"
# Para definir nuestras propias funciones usamos DEF.

#def nombre_funcion (parametros):
#    código
#    return retorno

def di_hola():
    """ 
    La funcion di_hola es una funcion, que no recibe parámetros, y no devuelve
    ningún resultado.
    sirve para imprimir en la pantalla el mensaje Hola
    """
    print("Hola")

#Para ejecutar la función simplemente la llamamos
di_hola() #Imprime "Hola".

segunda_parte=               "Retorno y envío de valores"

#RETURN: Nos permite dos cosas:
# • Salir de la funcion y transferir la ejecución de vuelta a donde se realizó la llamada.
# • Devolver uno o varios resultados, fruto de la ejecución de la función.
# El código que va luego del return nunca se ejecuta , por eso solo lo llamamos una vez finalizado el código.

def noreturn():
    print("Esto entra")
    return
noreturn()
# Acá no me dejó escribir más código xd

#Por otro lado, return, nos permite devolver un resultado.
def di_hola_v2():
    """
    Esta funcion es como la anterior pero devuelve el "Hola" con return y no con un print.
    """
    return "Hola"
print(di_hola_v2())

def duplicar(x):
    """
    La funcion es una que multiplica un número x
    """
    return 2*x
print(duplicar(8))


###########################################################################################################

tercer_parte=                 "Argumentos, Parámetros, Valor y Referencia"

# Volviendo sobre la definicion de la funcion di_hola. Vamos a agregar un parametro de entrada en el 
#encabezado de la función di_hola. si pasamos como entrada un nombre, se imprimirá "Hola" seguido del nombre

def di_hola_v3(nombre):
    print("Hola",nombre)
    return
di_hola_v3("Mario")

z=                                     "Argumentos por nombre"
#supongamos que tenemos resta(n1,n2)
#si le pasamos n2=4 y n1= 10, nos dará como resultado 10-4=6. ejemplo:
def resta(n1,n2):
    rest = n1-n2
    print(rest)
resta(n2=4, n1=10)

z=                                     "Argumentos por posicion"
#Es la más basica.Si tenemos suma(n1,n2) y le pasamos 3, 6, ambos tomaran el mismo indice como parametro.

z=                                     "Argumentos por defecto"
# Tal vez queramos tener una funcion con un parametro opcional, que pueda ser usado o no dependiendo de 
#diferentes circunstancias. Paraello podemos asignar un valor por defecto.
def suma(a,b,c=0):   #C valdría 0 salvo que se indique lo contrario.
    return a+b+c
# Dado que c tiene un parametro por defecto, la función puede ser llamada solo con dos argumentos.
suma(1,4) # Esto sería igual a 1 + 4 + 0.
#Tambien podemos asignar un valor por defecto a todos los parametros
def suma_v2(a=3, b=5, c=0):
    return a+b+c
suma_v2() #Esto daría como resultado la suma de 3+5+0.

z=                                     "Paso por valor y referencia"
# Paso por valor:
x = 10                         #Iniciamos la x a 10 y se la pasamos a funcion_v1. Dentro de la funcion
def funcion_v1(entrada):       #hacemos que la variable valga 0. Dentro de la funcion se crea una copia
    entrada = 0                #local de x, ya que python trata a los int como pasados por valor,por lo
    funcion_v1(x)              #que la variable original no es modificada.
print(x)                    

# Paso por referencia: Si x es una lista, python lo trata como si estuviese pasada por referencia, lo que 
#hace que se modifique la variable original. La variable original x ha sido modificada.

x = [10, 20, 30]
def funcionv2_ (entrada):
    entrada.append(40)
funcionv2_(x)
print(x)

z=                                     "Uso de *args"
# Gracias a los *args en Python, podemos definir funciones cuyo número de argumentos es variable. Es decir,
#podemos definir funciones genéricas que no aceptan un número determinado de parámetros, sino que se
#“adaptan” al número de argumentos con los que son llamados.

def suma (* args ):             #El uso de args es totalmente arbitrario, pero si es necesario el simbolo *
    s = 0                       #Funciona como tupla
    for arg in args :
        s += arg
    return s

suma(1,2,13,2,4,6,8,4,3,2,24,5,63,3,2)

z=                                     "Uso de **kwargs"
#El nombre kwargs es arbitrario, pero hay que usar **.
#kwargs dunciona como diccionario y nos permite dar un nombre a cada argumento de entrada, pudiendo acceder
#a ellos dentro de la función a través de un diccionario.

def suma (** kwargs ):
    s = 0
    for clave , valor in kwargs . items ():
        print ( clave , "=", valor )
    s += valor
    return s
suma ( a =3 , b =10 , c =3)






   
              













