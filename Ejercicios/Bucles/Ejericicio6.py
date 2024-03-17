#Definimos la palabra secreta 
palabra_secreta = "chupacabra"

#pedimos al usuario que ingrese la palabra
palabra = input("ingrese una palabra: ")

#Verificamos la palabra para ver si entramos al bule
while palabra != palabra_secreta:
    #Pedimos la palabra nuevamente
    palabra = input("ingrese una palabra: ")
    #verificamos nuevamente la pabra
    if palabra.lower == palabra_secreta:
        #si la palabra es igual a la establecida pasamos al break
        break

print("Has dejado el bucle con éxito.")