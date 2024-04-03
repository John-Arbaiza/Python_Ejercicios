# list 2
#------------------------------------------------------------------------------------------------
#Rabanada de listas 
#Una rebanada es un elemento de la sintaxis de Python que permite hacer una copia nueva
#de una lista, o partes de una lista. (copia el contenido de la lista, no el nombre de la lista)
#------------------------------------------------------------------------------------------------
#Ejemplos
#---------------------------------------------
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)
print("="*25)
#---------------------------------------------
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
print("="*25)
#---------------------------------------------
# Rebanadas – índices negativos
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)
print("="*25)
#--------------------------------------------
#La instrucción del descrita anteriormente puede
#eliminar más de un elemento de la lista a la vez,
#también puede eliminar rebanadas:
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)
print("="*25)
#--------------------------------------------
#También es posible eliminar todos los elementos a la vez:
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)
print("="*25)
#------------------------------------------------------------------------------------------------
#operadores in y not in
#Python ofrece estos dos operadores muy poderosos, capaces de revisar la lista para verificar si 
#un valor específico está almacenado dentro de la lista o no.
#------------------------------------------------------------------------------------------------
#Definimos una lista
my_list = [0, 3, 12, 8, 2]

# in (verifica si un elemento dado (el argumento izquierdo) está actualmente almacenado en algún
# lugar dentro de la lista (el argumento derecho) - el operador devuelve True en este caso.)
print(5 in my_list)
print(12 in my_list)
# not in (comprueba si un elemento dado (el argumento izquierdo) está ausente en una lista - el
#  operador devuelve True en este caso.)
print(5 not in my_list)
print(12 not in my_list)
print("="*25)
#--------------------------------------------

