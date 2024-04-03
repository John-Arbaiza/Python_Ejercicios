#A continuación se le da una lista su tarea es buscar cual es el mayor
#elemento que se encuentra dentro de esta, para dicho ejercicio no puede
# emplear la función max que python proporciona.

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13,20]

#Definimos una variable que nos ayude a almacenar dicho elemento
elemto_mayor = my_list[0]

#Empleamos un for para recorrer la lista
for i in range(1,len(my_list)):
    # Comparamos con el valor actual almacenado
    if my_list[i] > elemto_mayor:
        #Almacenamos el elemento mayor encontrado
        elemto_mayor = my_list[i]

#Imprimimos el resultado
print(f"El elemento más grande en la lista es: {elemto_mayor}")

#Segunda forma en que puede resolverse 
elemto_mayor = my_list[0]

for i in my_list:
    if i > elemto_mayor:
        elemto_mayor = i
        
print(f"El elemento más grande en la lista es: {elemto_mayor}")



