'''
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
'''

#Definimos una funcion para verificar si el numero es primo
def num_Primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

#Definimos otra funcion que nos ayude a imprimir los numeros
def muestra():
    print("Números primos entre 1 y 100:")
    for num in range(1, 101):
        if num_Primo(num):
            print(num)

# Llama a la función para imprimir los números primos
muestra()