# --- Lists ---

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
#==========================================
#------ Metodos para las listas ------
print("-"*20)
new_list = [1,2,3,"Rojo","verde"]
print(new_list)
#Metodo append
new_list.append("Negro")
print(new_list)
#Metodo insert
new_list.insert(1,"dos")
print(new_list)
#metodo remove
new_list.remove("dos")
new_list.remove(3)
print(new_list)
#metodo pop
print(new_list.pop())
print(new_list)
print(new_list.pop(2))
print(new_list)
#metodo clear
new_list.clear()
print(new_list)
#metodo copy
list_copy1 = [1,2,3,4]
list_copy2 = [0,9,8]
list_copy2 = list_copy1.copy()
print(list_copy2)
#Metodo reverse
list_copy2.reverse()
print(list_copy2)
#metodo sort
lista3 = [9,10,1,2,34,90]
print(lista3)
lista3.sort()
print(lista3)