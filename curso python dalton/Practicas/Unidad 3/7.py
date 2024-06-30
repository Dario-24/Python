# Una marca de ropa tienen descuentos diferentes dependiendo de la sede del local:

# Item	            Rosario	       Funes	Roldan
# Zapatillas	        30%	         40%	25%
# Remeras	            20%	         30%	15%
# Pantalones	        10%	          5%	20%
# Dado un item y la sede del local, devolver el descuento que recibe.

descuentos = {
    "Zapatillas": {"Rosario": 30, "Funes": 40, "Roldan": 25},
    "Remeras": {"Rosario": 20, "Funes": 30, "Roldan": 15},
    "Pantalones": {"Rosario": 10, "Funes": 5, "Roldan": 20}
}

item = "Zapatillas"
sede = "Rosario"

if item in descuentos and sede in descuentos[item]:
    descuento = descuentos[item][sede]
    print(f"El descuento para {item} en la sede de {sede} es del {descuento}%.")
else:
    print("No se encontró el artículo o la sede especificada.")

# Ahora, supongamos que además dependiendo del día de la semana se puede recibir un descuento adicional acumulable. 
# Es decir, si se recibió un descuento del 10 % según el item y la sede y la compra se realiza un lunes, el 
# descuento total será un 20 % . Escribir un programa en el que la persona pueda ingresar el día de la semana, 
# el item a comprar y la sede del local. Luego, informar el descuento total a recibir. Utilizar la siguiente tabla 
# de descuentos:
