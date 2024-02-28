#Haga un programa cuya tarea es escribir algunas de las primeras potencias de dos

#Definimos una variable
potencia = 1

#Por medio de un for calculamos y escribimos los resultados 
for e in range(16):
    # (e) se utiliza como una variable de control para el bucle e indica el valor actual del exponente
    print(f"2 a la potencia de {e} es  : {potencia}")
    potencia*= 2