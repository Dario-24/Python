# Cree una función que se llame menu_v2 similar al que ya implementó, pero que además de la opciones
#muestre el id de la persona logueada en el sistema. El id deberá ser un parámetro de entrada de la función.
#Deberá mostrar, por ejemplo, para un id = 30567342 el siguiente menú:
#Menú (id 30567342):
# 1. Ingresar de datos
# 2. Modificar de datos
# 3. Listar datos
# 4. Salir

def menu_v2(id):
    print(f"Menú (id {id}):")
    print("1. Ingresar datos")
    print("2. Modificar datos")
    print("3. Lista datos")
    print("4. Salir")
menu_v2(92347892)