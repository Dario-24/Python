import random
dia_random = random.randint(1,31)
mes_random = random.randint(1,12)
año_random = random.randint(1,2024)

fecha = dia_random,mes_random,año_random

dia = dia_random
mes = mes_random
año = año_random

if mes == 1:
    if dia >= 1 and dia <= 19:
        print("Pertenece al signo Capricornio")
    elif dia >= 20 and dia <= 31:
        print("Pertenece al signo Acuario")
    else:
        print("La fecha es errónea")
        
elif mes == 2:
    if dia >= 1 and dia <= 18:
        print("Pertenece al signo Acuario")
    elif dia >= 19 and dia <= 29:
        print("Pertenece al signo Picis")
    else:
        print("La fecha es errónea")

elif mes == 3:
    if dia >= 1 and dia <= 20:
        print("Pertenece al signo Picis")
    elif dia >= 21 and dia <= 31:
        print("Pertenece al signo Aries")
    else:
        print("La fecha es errónea")        

elif mes == 4:
    if dia >= 1 and dia <= 19:
        print("Pertenece al signo Aries")
    elif dia >= 20 and dia <= 30:
        print("Pertenece al signo Tauro")
    else:
        print("La fecha es errónea")

elif mes == 5:
    if dia >= 1 and dia <= 20:
        print("Pertenece al signo Tauro")
    elif dia >= 21 and dia <= 31:
        print("Pertenece al signo Géminis")
    else:
        print("La fecha es errónea")

elif mes == 6:
    if dia >= 1 and dia <= 20:
        print("Pertenece al signo Géminis")
    elif dia >= 21 and dia <= 30:
        print("Pertenece al signo Cáncer")
    else:
        print("La fecha es errónea")
        
elif mes == 7:
    if dia >= 1 and dia <= 22:
        print("Pertenece al signo Cáncer")
    elif dia >= 23 and dia <= 30:
        print("Pertenece al signo Leo")
    else:
        print("La fecha es errónea")
        
elif mes == 8:
    if dia >= 1 and dia <= 22:
        print("Pertenece al signo Leo")
    elif dia >= 23 and dia <= 31:
        print("Pertenece al signo Virgo")
    else:
        print("La fecha es errónea")

elif mes == 9:
    if dia >= 1 and dia <= 22:
        print("Pertenece al signo Virgo")
    elif dia >= 23 and dia <= 30:
        print("Pertenece al signo Libra")
    else:
        print("La fecha es errónea")

elif mes == 10:
    if dia >= 1 and dia <= 22:
        print("Pertenece al signo Libra")
    elif dia >= 23 and dia <= 31:
        print("Pertenece al signo Escorpio")
    else:
        print("La fecha es errónea")
        
elif mes == 11:
    if dia >= 1 and dia <= 21:
        print("Pertenece al signo Escorpio")
    elif dia >= 22 and dia <= 30:
        print("Pertenece al signo Sagitario")
    else:
        print("La fecha es errónea")

elif mes == 12:
    if dia >= 1 and dia <= 21:
        print("Pertenece al signo Sagitario")
    elif dia >= 22 and dia <= 31:
        print("Pertenece al signo Capricornio")
    else:
        print("La fecha es errónea")

print(f"Fecha dada: {fecha}")