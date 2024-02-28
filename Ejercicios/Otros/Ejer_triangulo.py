'''
Escriba un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de
más abajo, de altura el número introducido.

*
**
***
****
*****

'''

#Pedimos al usuario que ingrese el numero
altura = int(input("Ingrese la altura que desea que tenga el rectangulo: "))

#Hacemos uso de un ciclo for para dibujar el rectangulo
for i in range(altura+1):
    print("*" *i)
