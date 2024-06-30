#Un alumno es profesor
#Un alumno es asistente
#A)Pedir el nombre y la edad de los compañeros de clase y ordenar los datos de menor a mayor
#B)El mayor es el profesor y el menor es el ayudante. Quien es quien?

compañeros = []
asistencia = int(input("Cuantos alumnos asistieron hoy?: "))
for i in range(asistencia):
    nombre = input("Inserte nombre del alumno: ")
    edad = int(input("Inserte la edad del alumno: "))
    alumno = (nombre, edad)
    compañeros.append(alumno)
print(compañeros)
orden = compañeros.sort(reverse=True)
mayor = orden[0]
menor = orden[-1]

    