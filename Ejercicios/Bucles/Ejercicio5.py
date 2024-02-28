'''
Escribe un programa que use un bucle for para "contar de forma mississippi" hasta cinco.
Habiendo contado hasta cinco, el programa debería imprimir en la pantalla el mensaje final
"¡Listos o no, ahí voy!"

has uso del modulo time y su método sleep() para suspender la ejecución de cada función posterior
de print() dentro del bucle for durante un segundo, de modo que el mensaje enviado a la consola se
parezca a un conteo real.
'''

#Hacemos el import del modulo time
import time

#Definimos el bucle for para el conteo de los mississippi
for con in range(1,5+1):
    #Empleamos el metodo sleep para que el conteo parezca real
    time.sleep(1)
    #Imprimimos la cuenta de los mississippi
    print(f"{con} mississippi ")

#Imprimos el mensaje final
print("\n¡Listos o no, ahí voy!")