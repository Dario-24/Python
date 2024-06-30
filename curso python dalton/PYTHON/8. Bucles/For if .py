frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]

#Saltear un elemento.
for fruta in frutas:
    if fruta == "granada":
        continue #continue hace que si se cumple la condición, que se saltee.
    print(F"Me voy a comer una {fruta}")
print("------------")

#Evitar que el bucle continúe
for fruta in frutas:
    print(F"Me voy a comer una {fruta}")
    if fruta == "pera":
        break #Esto da por finalizado el bucle
else: #Este else hace que si no se encuentra un break, al terminar el bucle, imprime "Terminado"
    print("Terminado")
    
    
    
    
    

    




