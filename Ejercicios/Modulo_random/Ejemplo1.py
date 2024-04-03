''' 
Modulo random
El módulo random proporciona funciones para generar números pseudoaleatorios
'''

#A continuación se presentan las principales funciones que podemos encontrar
# al importar este modulo para nuestros proyectos.

#Importamos el modulo
import random

#Funcion randint: devuelve un entero aleatorio en el rango de [a,b]
#Veamos un ejemplo orientado al inicio de un juego

print("Ejemplo randint(a, b)")

#Almacenamos los numeros aleatorios en las siguientes variables
inicio = random.randint(0,1)
vidas = random.randint(1,5)

#Verificamos que jugador iniciara la partida 
if inicio == 0:
    print("\nJugador 1 comienza")
    #Verificamos el numero de vidas generadas
    if vidas <= 2:
        #Mostramos el mensaje siguiente en caso de ser una cantidad baja
        print("\nLA SUERTE NO ESTA DE TU LADO")
        print(f"Tus vidas disponibles son {vidas}")
    else:
        print("\nLA SUERTE TE SONRIE")
        print(f"Tus vidas disponibles son {vidas}")

else:
    print("\njugador 2 comienza")
    if vidas <= 2:
        print("\nLA SUERTE NO ESTA DE TU LADO")
        print(f"Tus vidas disponibles son {vidas}")
    else:
        print("\nLA SUERTE TE SONRIE")
        print(f"Tus vidas disponibles son {vidas}")

#---------------------------------------------------------------------------
print("\n============================================================")
print("Ejemplo randrange(a, b, salto)")

#randrange(a, b, salto):genera números enteros aleatorios comprendidos entre a y b
# separados entre sí con un salto

#Veamos un ejemplo de su uso al generar 20 valores pares aleatorios entre 0 y 100

#Definimos una lista para almacenar los numeros pares
list_pares = list()

for i in range(20):
    #Definimos la variables a emplear
    pares = random.randrange(0,100,2)
    #almacenamos los valores generados en nuestra lista
    list_pares.append(pares)

print(list_pares)

print("\n============================================================")
print("Ejemplo random()")

#La función random() devuelve un float comprendido entre [0.0 y 1.0)
for i in range(6):
    print(round(random.random(),3))