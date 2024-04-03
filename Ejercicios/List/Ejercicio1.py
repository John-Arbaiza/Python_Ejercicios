'''
Había una vez un sombrero. El sombrero no contenía conejos, sino una lista de cinco números: 1, 2, 3, 4, y 5.

Tu tarea es:

escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (Paso 1)
escribir una línea de código que elimine el último elemento de la lista (Paso 2)
escribir una línea de código que imprima la longitud de la lista existente (Paso 3).
¿Listo para este desafío?
'''

#Importamos el siguiente modulo para darle mas diversion al ejercicio
import time

#Definimos nuestra lista
hat_list = [1,2,3,4,5]

#Mostramos un mensaje al usuario
print("\t\tBIENVENIDOS")
print("Al increible mundo de las listas magicas\n")

print("Mi sombrero tiene los siguientes numeros ", hat_list)
print("Cambiemos magicamente el valor central")

#Pedimos al usuario que ingrese el numero que indica el paso 1
new_number = int(input("Por favor ingrese el nuevo numero a meter al sombrero:"))
print("Soplamos el sombrero y ahora tenemos" )
for i in range(2):
    time.sleep(1)
    print("|     |\nv     v")
#Reemplazamos el numero central definido por el nuevo numero ingresado por el usuario
hat_list[2] = new_number
print(hat_list)

#Ahora hacemos el paso 2
print("\nAhora con la magia de las listas eliminemos\nel ultimo numero de mi sombrero")
print("Se eliminara a la cuenta de")
del hat_list[4]
for i in range(3):
    time.sleep(1)
    print(i + 1)

print("\nVeamos ahora cuantos numeros me quedan en mi sombrero magico")
print("Me quedan .... ",len(hat_list), " numeros")