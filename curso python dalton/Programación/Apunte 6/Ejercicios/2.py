# Proponga una función que se llame C_a_F que tome una temperatura expresada en grados celsius y 
# devuelva esa misma temperatura expresada en grados fahrenheit.

celsius= int(input("Ingrese los grados Celsius: "))
def C_a_F(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit
print(f"{celsius} grados Celsius, son equivalentes a {C_a_F(celsius)} grados Fahrenheit")
    
    