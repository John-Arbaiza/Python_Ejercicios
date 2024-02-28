#Definimos las variables y pedimos los datos 
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
num3 = int(input("Ingrese un numero: "))

#Forma 1
#Definimos una funcion para verificar los numeros
def numMayor(n1,n2,n3):

   #de manera temporal asumimos que n1 es el mayor
    numero_mayor = n1 

    if n2 > numero_mayor:
        numero_mayor = n2

    if n3 > numero_mayor:
        numero_mayor = n3

    return numero_mayor

#Llamando a la funcion
mayor = numMayor(n1=num1, n2=num2, n3=num3)
print("El numero mayor es:", mayor)

#======================================================
#Forma 2 de hacerlo
nMayor = max(num1, num2, num3)
print("\nSegunda forma")
print("El numero mayor es:", mayor)



    