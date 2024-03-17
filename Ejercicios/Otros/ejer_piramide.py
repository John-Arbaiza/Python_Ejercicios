'''
Un niño y su padre, un programador de computadoras, juegan con bloques de madera. Están construyendo una pirámide.
Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide es plana.
La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.
Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la
pirámide que se puede construir utilizando estos bloques.
'''

#Primero pedimos al usuario que ingrese la cantidad de bloques
bloques = int(input("Ingrese la cantidad de bloques que dispone para la piramide:"))

#Definimos dos variables 
altura = 0
bloques_empleados = 0 

#Hacemos uso de un while para que nos ayude con la altura 
while bloques_empleados + altura + 1 <= bloques:
    altura += 1
    bloques_empleados += altura

#Imprimimos el resultado 
print(f"Al usar {bloques} bloques la altura de la piramide es: {altura}")