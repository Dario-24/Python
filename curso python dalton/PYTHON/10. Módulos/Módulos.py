#Todos los archivos .py son módulos

#Podemos llamar a la librería de otro módulo y utilizar sus funciones o métodos
import modulo_saludar                     
saludo = modulo_saludar.Saludar("Darío")  
print (saludo)

#Podemos cambiarle el nombre al módulo para que sea más cómodo
import modulo_saludar as ms                      
saludo = ms.Saludar("ms")  
print (saludo)

#Podemos importar una función especifica
from modulo_saludar import Saludar_raro
saludo_raro = Saludar_raro("Hola soy German")
print(saludo_raro)

#Podemos cambiarle el nombre a la función extraída de otro módulo
from modulo_saludar import Saludar_raro as sr
saludo_raro = sr("SR")
print(saludo_raro)

#Llamar a una variable: Para llamar a una variable es lo mismo, por eso es mejor iniciar el nomnre de
#las funciones con mayusculas.
saludo2 = ms.saludar
print(saludo2)

#Para ver propiedades y métodos del namespace:
print(dir(ms))

#Para ver el nombre de un módulo:
print(ms.__name__)




