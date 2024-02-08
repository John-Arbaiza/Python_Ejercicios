# --- Lists ---

''' 
La lista es un tipo de colección ordenada. Sería equivalente a lo que en
otros lenguajes se conoce por arrays, o vectores.

Las listas pueden contener cualquier tipo de dato: números, cadenas,
booleanos, … y también listas.
'''

#Definiendo listas
my_list = list()
mi_otra_lista = [1,2,3,4,5,6]
lista2 = [34, 1.77, "Juan", "Flores"]

#Mostrando los resultados
#-------- Longitud de la lista----------
print(len(my_list))
print(len(mi_otra_lista))
#-------- Contenido de la lista --------
print("-" *20)
print(mi_otra_lista)
print(lista2)
#=========================================
#------ Accediendo a los elementos ------
print("-" *20)
print(lista2[0])
print(lista2[1])
print(lista2[-1])
print(lista2[-4])

#=========================================
#------ Desempaquetando la lista ------
print("-" *20)
edad, altura , nombre, apellido = lista2
print("Mi nombre es", nombre,apellido, "Tengo", edad, "años y mido", altura, sep=" ")

#=========================================
#Concatenando listas 

list_example = [1,2,3,4]
list_example2 = ["uno","dos","tres","cuatro"]

print(list_example + list_example2)