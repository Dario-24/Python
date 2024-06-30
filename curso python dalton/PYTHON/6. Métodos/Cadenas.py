cadena1 = "Hola,Maquina,Como,Estas"
cadena2 = "Bienvenido maquinola"

# Un método es una función aplicada a  un objeto
# La estructura de los metodos es la siguiente:

#            Dato.Método()


# UPPER: convierte todo a mayusculas
mayusc = cadena1.upper()

#LOWER: convierte todo a minusculas
minusc = cadena1.lower()

#CAPITALIZE: primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1

cadena11 = "Hola,Maquina,Como,Estas"
busqueda_find = cadena11.find("q") #7

#INDEX: buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepciòn
busqueda_index = cadena1.index("H")

#ISNUMERIC: si es numerico, devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()

#ISALPHA: si es alfanumèrico (letras y números, descartando el espacio que es un caracter especial) 
#devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

#COUNT: contamos coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("la ma")

#LEN : función donde contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#STARWITCH: verificamos si una cadena empieza con otra cadena dada, si es asì devuelve True
empieza_con = cadena1.startswith("H")

#ENDSWITH: verificamos si una cadena termina con otra cadena dada, si es asì devuelve True
termina_con = cadena1.endswith("H")

#REPLACE: si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2
remplazar = "Hola como andas?"
cadena_nueva = remplazar.replace("andas","estas")

#separar cadenas con la cadena que le pasemos
separar = "Hola,como,andas?"
cadena_separada = separar.split(",")

print(cadena_separada)