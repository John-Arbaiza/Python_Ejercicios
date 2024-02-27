# --- Tuples---

#Definiendo las tuplas
tupla1 = tuple()
my_other_tuple = ()
tupla2 = (10,20)
my_tuple = (20,7,"John","Trafalgar")

print(my_tuple, "---> " , type(my_tuple))
print("-" *20)
#=========================================
#------ Accediendo a los elementos ------
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[-3])
print("-" *20)
#=========================================
#------Metodos o operaciones de las tuplas ------
#operacion count
print(my_tuple.count("Trafalgar"))
#operacion index
print(my_tuple.index("John"))

'''
Esto dara error ya que una tupla es inmutable osea no podemos cambiar los
valores establecidos.
my_tuple[1] = 1.80
print(my_tuple)

Las tuplas son útiles cuando se necesita tener un conjunto de valores que no cambiarán
'''

#lo que se muestra a continuacion si funcionara ya que sumara las tuplas
# y sera como creemos una nueva tupla
print(my_tuple + tupla2)

print("-" *20)
#=========================================
#------Convirtiendo una tupla en lista ------
my_tuple = list(my_tuple)
print(type(my_tuple))
print(my_tuple)
#Ahora de esta manera si puedo cambiar la estructura de la tupla
my_tuple[3] = "Ace"
my_tuple.insert(1,22)
#Convertimos la lista de nuevo a una tupla ya con la estructura cambiada
my_tuple = tuple(my_tuple)
print(type(my_tuple))
print(my_tuple)