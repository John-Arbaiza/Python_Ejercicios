#Ejercicio para encontrar el numero mayor

#Definimos una variable y la inicializamos en 0
n_mayor = 0

#Pedimos al usuario que ingrese un numero
numero = int(input("Ingrese un numero o escriba -1 para detener el programa: "))

#Definimos un ciclo o bucle while para comparar la respuesta del usuario
while numero != -1:
    #Verificamos el numero mayor a traves de un if
    if(numero > n_mayor):
        n_mayor = numero
    #Pedimos el ingreso del siguiente numero
    numero = int(input("Ingrese un numero o escriba -1 para detener el programa: "))

#Imprimos el resultado
print("El numero mayor es: ", n_mayor)