# --- Sets ---

#Definiendo los sets
my_set = set()
my_other_set = {}
print(type(my_set))
print(type(my_other_set)) #inicialmente es un diccionario

my_other_set = {"John","Arbaiza",20}
print(type(my_other_set)) #Ya es un set
print(len(my_other_set))
#-----------------------------------------

#Operaciones de los sets
my_other_set.add("Elvis")
#Un set no es una estructura ordenada 
print(my_other_set)
# Un set no admite repeditos
my_other_set.add("Elvis")
print(my_other_set)

#-----------------------------------------

#Sintaxis para comprobar que un elemento existe dentro de un set
print("\n","John" in my_other_set)
print("Juan" in my_other_set)

#-----------------------------------------

#clear elimina los elementos del set
my_other_set.clear()
print("\n",my_other_set)
print(len(my_other_set))

#-----------------------------------------

# remove 
#Para probar el remove en los set agregamos un elemento a este
my_other_set.add("Pedro")
print("\n",my_other_set)
#Empleamos el metodo remove
my_other_set.remove("Pedro")
print(my_other_set)

#-----------------------------------------

#Transformando un set en una lista 
my_new_set = {"Ali","Juan", "Maria","Luis"}
print("\n", type(my_new_set))
my_list = list(my_new_set)
print(type(my_list))
print(my_list) 
print(my_list[0]) #Los elementos cada vez que se ejecute cambiaran de orden 
# Este tipo de transformaciones no es lo mas recomendado ya que el orden de la
# Lista cambia cada vez que se ejecuta.

#-----------------------------------------

#Uniendo sets
my_other_set = {"C#", "JAVA", "Python"}
my_set_unido = my_new_set.union(my_other_set)
print()
print(my_set_unido.union(my_set_unido).union({"Kotlin","Rust","C++"}))

#-----------------------------------------
# Haciendo uso de difference Devuelve la diferencia
# de dos o más conjuntos como un nuevo conjunto.
print()
print(my_set_unido.difference(my_new_set))