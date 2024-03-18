''' 
Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre un
mensaje cada vez que un número no sea mayor que el primero.
'''

print("="*14, "| BIENVENIDO |", "="*14)
#Preguntamos al usuario si desea participar
participa = input("Desea participar ingrese S para si o N para no:")

#Vefificamos la respuesta por medio de un while
while participa.upper() == "S":
    #Definimos una excepcion para controlar culaquier error que se presente 
    try:
        #Pedimos al usuario que indique la cantidad de numeros a ingresar
        cantidad_num = int(input("¿Cuátos valores va a introducir? --> "))
        #Validamos que el usuario no indique el ingreso de numeros negativos
        if cantidad_num < 0:
            #En caso de ingreso de un numero negativo mostramos el mensaje siguiente
            print("!IMPOSIBLE¡")
        else:
            #pedimos el numero
            num = int(input("Escriba un numero:"))
            #Hacemos uso de un ciclo for para pedir los numeros segun la cantidad indicada
            for cantidad in range(cantidad_num - 1):
                #Pedimos un segundo numero
                num2 = int(input(f"Escriba un numero mas grande que {num}:"))
                #Por medio de condicionales vamos verificando 
                if num2 == num:
                    print(f"El nuevo numero ingresado es igual a {num}")
                elif num >= num2:
                    print(f"{num2} no es mayor que {num}")
        print("="*7,"| Gracias por su Colaboración |","="*7)
        break
    except:
        print()
        print("-"*36)
        print("El dato ingresado no es correcto")
        print("-"*36,"\n")
print("Hasta pronto")