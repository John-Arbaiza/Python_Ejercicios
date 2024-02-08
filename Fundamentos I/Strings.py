# --- Strings ---

#Definimos un string
my_string = " Esto es un string"
#Imprimiendo la variable con el string
print(my_string)
print(len(my_string))

print("----------------------------------")
#---------------------------------------------------------------------
#Formateo de un string
#Definimos las variables a emplear
name, lastname, age = "Elvis", "Arbaiza", 20
#Forma 1: se usa ({}) cuando se quiere que tal cual se imprima el obejto
print("Mi nombre es {} {} y mi edad es {} ".format(name, lastname,age))
#Forma 2: se usa (%s,%d) cuando ya estamos trabajando con el numero formateado
print("Mi nombre es %s %s y mi edad es %d " %(name,lastname,age))
#Inferencia de datos
print(f"Mi nombre es {name} {lastname} y mi edad es {age}")

print("----------------------------------")
#---------------------------------------------------------------------
#Desempaquetado de caracteres
lenguaje = "python"
a, b, c ,d, e, f = lenguaje
print(a)
print(b)
print()
#---------------------------------------------------------------------
#Division
divide = lenguaje[1:4]
print(divide)
divide = lenguaje[2:]
print(divide)
divide = lenguaje[-3]
print(divide)
print()
#---------------------------------------------------------------------
#Funciones
print(lenguaje.capitalize()) #Pone en mayuscula el primer caracter
print(lenguaje.upper()) #Pone en mayuscula toda la cadena
print(lenguaje.count("p")) #Cuenta los caracteres que hay segun el que se le indique
#Se encarga de verificar si es un número
print(lenguaje.isnumeric())
print("1".isnumeric())
print("PYTHON".lower()) #Para pasar la cadena a minusculas
print(lenguaje.startswith("py"))
