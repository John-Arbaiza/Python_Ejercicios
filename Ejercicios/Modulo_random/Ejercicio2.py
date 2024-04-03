'''
Se ha realizado un muestreo con los precios del barril de petróleo durante el último mes (de 30 días), suponga
que dichos valores son enteros y que han fluctuado entre $ 130 y $ 150 (en forma aleatoria).


Una vez elaborada la muestra, se desea determinar:

a) El promedio del precio del petróleo
b) ¿Cuál fue el día en el que estuvo más barato el barril de petróleo?
c) ¿Cuántos días el petróleo tuvo precios superiores al promedio?
'''

#Importamos el modulo a emplear
import random

#Definimos una lista para almacenar los precios del petroleo
precios = list()

#Variables a emplear
suma = 0
dias = 30
promedio = 0

print("="*30)
print("\t BIENVENIDO")
print("Precios de la gasolina en los\n\tultimos 30 dias")
print("="*30)

#generamos losprecios de los ultimos 30 dias
for i in range(30):
    #Definimos una variable para almacenar los precios de tipo aleatorio
    pre = random.uniform(130,150)
    #Imprimos los precios
    print(f"Precio del día {i + 1} es de {round(pre,2)} ")
    #Agregamos los precios a la lista
    precios.append(pre)

print("="*30)
#Ahora hacemos el calaculo del promedio del petroleo
#Para esto hacemos uso de una comprensión de lista
suma = sum([elementos for elementos in precios])
promedio = suma / dias
print(f"Promedio del precio del petróleo")
print(round(promedio,2))

print("="*30)

#Verificando el dia que estuvo mas bajo el precio del petroleo

#Primero determinamos el precio mas bajo
precio_bajo = min(precios)
#Buscamos el indice al que pertenece dicho precio
dia_bajo = precios.index(precio_bajo) + 1
print(f"Dia con el precio mas bajo: \n{dia_bajo}")
print(f"Precio de ese dia: \n{round(precio_bajo, 2)}")

print("="*30)

#Verificamos los dias en que el precio fue mayor al promedio
#Para esto hacemos uso de la comprension de lista
dias_mayor = [i + 1 for i, precio in enumerate(precios) if precio > promedio]
can_dias = len(dias_mayor)
print(f"Cantidad de dias con precio\nMayor al promedio: {can_dias}")
print(f"Dias en que fue mayor al promedio:\n{dias_mayor}")















    


