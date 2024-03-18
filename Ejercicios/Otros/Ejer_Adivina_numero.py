#has un juego donde el usuario deba adivinar un numero haciendo uso de numeros aleatorio

#Importamos el modulo de los numeros aleatorios 
import random

#Mensaje de bienvenida 
print("="*30)
print("\t BIENVENIDO \n \t  AL JUEGO")
print("="*30)

#Definimos el numero aleatorio
numero_secreto = random.randint(1,10)
#Establecemos un numero determinado de intentos
intentos = 3

#Preguntamos al usuario si quiere jugar
jugar = input("\nDesea jugar ingrese\nS para si, N para no:")
print()

#Verificamos la respuesta atraves de un while
while jugar.upper() == "S":
    #Definimos una excepcion para controlar cualquier error 
    try:
        #Hacemos uso de un for para controlar las veces que se le pedira al usuario adivinar
        for intenta in range(intentos):
            numero = int(input("Ingrese el numero que considera correcto:"))
    
            #Verificamos dicho numero
            if numero > numero_secreto:
                print("\nEl numero ingresado es mayor al correcto")
                #Decrementamos el numero de intentos
                intentos-= 1
            elif numero < numero_secreto:
                print("\nEl numero ingresado es menor que el correcto")
                #Decrementamos el numero de intentos
                intentos-= 1
            elif numero == numero_secreto:
                print("\nFelicidades has ganado")
                break
            print(f"Te quedan {intentos} intentos\n")
        
        #Imprimimos el resultado  
        print()
        print("-"*36)
        print(f"El numero correcto era {numero_secreto}")
        print("-"*36)
        break
    except:
        print()
        print("-"*36)
        print("El dato ingresado es erroneo")
        print("-"*36,"\n")