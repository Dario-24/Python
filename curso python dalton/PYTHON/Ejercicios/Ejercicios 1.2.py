#una persona promedio habla dos palabras por segundo
#A) Pedirle al usuario que diga cualquier texto real y:
#   -Calcular cuanto tardaría en decir esa frase
#   -Cuantas palabras dijo
#B) Si se tarda más de un minuto decirle "Para flaco tampoco te pedi un testamento"
#C) Dalto habla un 30% más rápido. Cuanto tardaría el en decirlo?

frase = input("Ingrese la frase o palabra: ")
palabras = frase.split(" ")
cantidad_de_palabras = len(palabras)

print(f"Usted dijo {cantidad_de_palabras} palabras, lo que tardaría {0.5*cantidad_de_palabras} segundos")

if cantidad_de_palabras > 2*60:
    print("Para flaco tampoco te pedi un testamento")

print(f"Dalto tardaría {round(((0.5*cantidad_de_palabras)/1.3),1)} segundos en decirlo")

