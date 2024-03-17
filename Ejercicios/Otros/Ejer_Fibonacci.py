'''
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
'''

#Definimos dos variables y las inicializamos 
numero1 = 0
numero2 = 1

#Empleamos un for para que nos ayude con la sucesión
for su in range(50):
    print(numero1)

    #Hacemos la suma de las varibles
    fibo = numero1 + numero2
    numero1 = numero2
    numero2 = fibo


