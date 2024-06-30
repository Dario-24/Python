# (IF)    -Si se cumple una condicion (True):
#    Se va a ejecutar este codigo
# (Else) -De lo contrario(anterior condición False):
#    Se ejecutará este codigo

edad = 21

if edad >= 18:
    print("Es mayor de edad")
    
else:
    ("Es menor de edad")
 
###########################################################################################################
###########################################################################################################
# Uso de ELIF   
# Podemos agregar elif para sumar mas condiciones en un mismo bloque

edad = 15

if edad < 18:
    print("Es menor de edad")
    
elif 18 <= edad < 30:
    print("Es adulto joven")
    
elif 30 <= edad < 70:
    print("es adulto mayor")

else:
    print("Es una persona anciana")
    
###########################################################################################################
###########################################################################################################

# Uso de if anidados

edad = 4

if edad < 18:
    if edad <= 3:
        print("Es un bebé")
    elif 3< edad <12:
        print("Es un niño")   
    else:
        print("Es un adolescente")
        
         
elif 18 <= edad < 30:
    print("Es adulto joven")
    
elif 30 <= edad < 70:
    print("es adulto mayor")

else:
    print("Es una persona anciana")
