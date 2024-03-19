''' 
Realizar un programa que simule un dado de 6 caras (6 números) sea lanzado 3 veces y
al final muestre la sumatoria de cada uno de los lanzamientos
'''

#Importamos el modulo random
import random

#Definimos las  variables a emplear en nuetro ejercicio
resultados = []
sumatoria = 0

#Definimos un ciclo for para hacer la sumatoria
for i in range(3):
    Dado = random.randint(1,6)
    resultados.append(Dado)
    sumatoria += Dado
    print(f"lanzamiento {i+1} el numero obtenido es {Dado} ")

print(f"La sumatoria de {resultados} es igual a {sumatoria}")
