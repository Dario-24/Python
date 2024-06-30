# Ahora, supongamos que además dependiendo del día de la semana se puede recibir un descuento adicional acumulable. 
# Es decir, si se recibió un descuento del 10 % según el item y la sede y la compra se realiza un lunes, el 
# descuento total será un 20 % . Escribir un programa en el que la persona pueda ingresar el día de la semana, 
# el item a comprar y la sede del local. Luego, informar el descuento total a recibir. Utilizar la siguiente tabla 
# de descuentos:

#	        Lunes	Miércoles	Jueves
#Descuento	10%  	   8%	      5%

dia = input("Ingrese el día de hoy(lunes, martes, miercoles, jueves, viernes): ").lower()
item = input("Ingrese el item que quiere comprar( remera, zapatilla, pantalon): ").lower()
sede = input("Ingrese la sede( Rosario, Funes, Roldan)").lower()


descuentos = {
    "zapatilla": {"rosario": 30, "funes": 40, "roldan": 25},
    "remera": {"rosario": 20, "funes": 30, "roldan": 15},
    "pantalon": {"rosario": 10, "funes": 5, "roldan": 20},
    "lunes": 10,
    "miercoles": 8,
    "jueves": 5
}


if item in descuentos and sede in descuentos[item]:
    descuento = descuentos[item][sede]
    print(f"El descuento para {item} en la sede de {sede.capitalize()} es del {descuento}%.")
else:
    print("No se encontró el artículo o la sede especificada.")
    
descuento_total = descuento + descuentos[dia]
    
if dia in descuentos:
    print(f"Ademas, por ser {dia} tenes un {descuentos[dia]}% de descuento.") 
    print(f"Descuento toal: {descuento_total}%")
else:
    print("Este producto tiene descuentos los días lunes, miercoles y jueves")