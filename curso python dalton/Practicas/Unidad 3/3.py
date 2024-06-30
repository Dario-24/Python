#Desarrollar un programa que permita verificar la seguridad de una contraseña ingresada por el usuario. 
#El programa debe realizar las siguientes comprobaciones:

# a. Longitud superior a 8 caracteres e inferior a 16.
# b. Contiene al menos un caracter especial
# caracteres_especiales ='!@#$%^&*_.?'
# c. Contiene al menos un número
# El programa debe informar al usuario si la contraseña cumple con estos requisitos de seguridad o no.

contraseña_ejemplo = "D@riox88"
contraseña = input ("Cree una nueva contraseña: ")
caracter_especial = '!@#$%^&*_.?'
numeros = "1234556789"
if len(contraseña) < 8:
    print("La contraseña es demasiado corta")
elif len(contraseña) >= 16:
    print("La contraseña es demasiado larga")
else:
    contiene_caracter = any(caracter in caracter_especial for caracter in contraseña)
    contiene_numero = any(caracter.isdigit() for caracter in contraseña)
    if contiene_caracter and contiene_numero:
        print("Contraseña creada")
    else:
        print("No cumple los requisitos")
        
