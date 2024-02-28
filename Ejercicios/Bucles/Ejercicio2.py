'''
Hacer un programa que lea una secuencia de números y cuente cuántos números
son pares y cuántos son impares.
El programa termina cuando se ingresa un cero.
'''

#Mensaje de bienvenida
print("=" *28)
print("\tBIENVENIDO")
print("=" *28)

#Definimos dos variables 
pares = 0
impares = 0

#definimos dos listas para alamacenar los numeros pares e impares
#Esto es un extra al ejercicio
num_impares = []
num_pares = []

#Pedimos al usuario que ingrese los numeros
numero = int(input("Ingrese el número que desea verificar o ingrese 0 para salir: "))

#Definimos un ciclo while para que nos ayude 
while numero != 0:
    if(numero % 2 == 1):
        #icrementamos el contador de impares
        impares += 1
        num_impares.append(numero)
    else:
        #incrementamos el contador de pares
        pares += 1
        num_pares.append(numero)
    #Preguntamos nuevamente si desea ingresar otro numero para verificar
    numero = int(input("Ingrese el número que desea verificar o ingrese 0 para salir: "))

#Imprimimos la cantida de pares e impares que salio de la secuencia
print(f"Cantidad de numeros pares: {pares}")
print(f"Cantidad de numeros impares: {impares}")
print("\nNumeros pares",num_pares, sep=" \n")
print("Numeros impares", num_impares, sep=" \n")
    


