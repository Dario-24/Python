#Proponga una funcion que se llame s_a_hms que tome una duración expresada en segundos y devuelva esa 
# misma duración expresada en horas, minutos y segundos.

def s_a_hms(segundos_totales):
    horas = segundos_totales//3600
    segundos_restantes= segundos_totales % 3600
    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60
    return horas,minutos,segundos
    
print(s_a_hms(824374))
