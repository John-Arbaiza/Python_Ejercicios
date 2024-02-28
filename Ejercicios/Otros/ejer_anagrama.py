'''
  Escribe una función que reciba dos palabras (String) y retorne verdadero o falso según sean o no anagramas.
  - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
  - NO hace falta comprobar que ambas palabras existan.
  - Dos palabras exactamente iguales no son anagrama.
'''

#pedimos al usuario que ingrese dos palabras para comparar 
palabra1 = input("Ingrese una palabra:")
palabra2 = input("Ingrese otra palabra:")

#Definimos una funcion que nos ayude a verificar si son anagramas
def anagrama(palabra_1,palabra_2):
    palabra_1 = palabra_1.lower()
    palabra_2 = palabra_2.lower()
# Comparamos si las palabras son anagramas al ordenar sus letras
    return sorted(palabra_1)  == sorted(palabra_2)

# Llamamos a la función y mostramos el resultado
if anagrama(palabra_1= palabra1, palabra_2= palabra2):
    print("¡Son anagramas!")
else:
    print("No son anagramas.")


    



