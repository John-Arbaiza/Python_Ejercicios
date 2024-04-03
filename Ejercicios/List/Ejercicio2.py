#Ordenamiento Burbuja

#Definimos una lista con elemetos desordenados
my_list = [1,9,8,10,2,16,3]
#Definimos una variable para poder entrar al bucle while que definiremos mas adelante
swapped = True #La iniciazalizamos en True

#Imprimimos la lista desordenada
print(my_list)
print("="*24)

#Definimos un bucle while
while swapped:
    #En caso de no haber un intercambio cambiamos el valor de sawpped
    swapped = False
    #Definimos un for que nos ayude con las comparaciones
    for i in range(len(my_list) - 1):
        #Comparamos los elemetos adyacentes con la yuda de un if
        if my_list[i] > my_list[i + 1]:
            #Indicamos que ocurrio un intercambio
            swapped = True
            # Si terminamos aquí, tenemos que intercambiar elementos.
            my_list[i], my_list[i + 1] =  my_list[i + 1], my_list[i]

#Imprimimos el resultado
print(my_list)
