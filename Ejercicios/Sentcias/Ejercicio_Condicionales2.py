#Pedimos al usuario que ingrese el year
year = int(input("Ingrese el año que desea evaluar: "))

#Verificamos el año ingresado
if (year < 1582):
    print("No esta dentro del período del calendario Gregoriano")
else:
    if(year % 4 != 0):
        print("Año Común")
    elif(year % 100 !=0):
        print("Año Bisiesto")
    elif(year % 400 !=0):
        print("Año Común")
    else:
        print("Año Bisiesto")




