# Una mañana ponés un billete en la vereda al lado del Monumento a la Bandera. A partir de ahí, cada día 
# vas y duplicás la cantidad de billetes, apilándolos prolijamente. ¿Cuánto tiempo pasa antes de que la 
# pila de billetes sea más alta que la del Monumento? Considere los siguientes valores para comenzar a 
# resolver el problema:
billete_milimetros = 0.11
milimetro_en_metros = 0.001
billete_grosor = 0.11 * 0.001  # grosor de un billete en metros
altura_monumento = 70 # altura en metros
billetes_n = 1
dia = 1
altura_billetes = billete_grosor
# Utilice un bucle while para resolver el problema.
while altura_monumento >= altura_billetes:
    dia += 1
    billetes_n *= 2
    altura_billetes = billetes_n * billete_grosor
print(f"Se tardó un total de {dia} días")
print(altura_billetes)
