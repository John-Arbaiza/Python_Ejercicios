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
#Metodo append (Sirve para agregar elementos a la lista)
new_list.append("Negro")
print(new_list)
#------------------------------------------------------------------------------------------
#Metodo insert (sirve para insertar un elemento de lista en un índice específico)
new_list.insert(1,"dos")
print(new_list)
#------------------------------------------------------------------------------------------
#metodo remove (elimina el elemento especificado)
new_list.remove("dos")
new_list.remove(3)
print(new_list)
#------------------------------------------------------------------------------------------
#metodo pop (elimina el índice especificado)
print(new_list.pop())
print(new_list)
print(new_list.pop(2))
print(new_list)
#------------------------------------------------------------------------------------------
#metodo clear (vacía la lista)
new_list.clear()
print(new_list)
#------------------------------------------------------------------------------------------
#metodo copy (Sirve para copiar)
list_copy1 = [1,2,3,4]
list_copy2 = [0,9,8]
list_copy2 = list_copy1.copy()
print(list_copy2)
#------------------------------------------------------------------------------------------
#Metodo reverse (invierte el orden de clasificación de los elementos.)
list_copy2.reverse()
print(list_copy2)
#------------------------------------------------------------------------------------------
#metodo sort (ordena la lista de forma ascendente de forma predeterminada.)
lista3 = [9,10,1,2,34,90]
print(lista3)
lista3.sort()
print(lista3)
#------------------------------------------------------------------------------------------
#Metodo count (devuelve el número de elementos con el valor especificado.)
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)
#------------------------------------------------------------------------------------------
#Metodo extend (agrega los elementos de la lista especificados (o cualquier iterable) al final de la lista actual.)
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
#------------------------------------------------------------------------------------------
# instrucción del (en este se tiene que apuntar al elemento que quieres eliminar)
numbers = [1,2,3,4,5,6,7,8]
print("\n","="*20,"\nLista sin cambios")
print(f"La lista tiene {len(numbers)} elemetos los cuales son:\n {numbers}")
del numbers[1]
print("Lista con cambios")
print(f"La lista tiene {len(numbers)} elemetos los cuales son:\n {numbers}")