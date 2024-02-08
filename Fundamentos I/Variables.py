# --- Variables en python ---

#====== Numericas ======
#Enteros ---> int
numero = 20
print(numero, type(numero))

#flotantes ----> float
dinero = 2534.73
print("\nSu dinero disponible es: ", dinero)
print(type(dinero))
print()

#======= Strings =======
name = "Elvis"
lastname = "Arbaiza"
print(name, type(name))
print(lastname, type(name))

#Funciones 
print(len(name))
print()

#====== Booleanas ======
'''
variable de tipo booleano sólo puede tener
dos valores: True (cierto) y False (falso). 
'''
exampleBool = True
print(exampleBool, type(exampleBool))

#===== Variables en una sola linea =====
#Nota: No se debe abusar de esta sintaxis
#=======================================
nombre, apellido, user, age = "John", "Arbaiza", "Trafalgar", 20
print("\nHola me llamo ", nombre, apellido)
print("Mi usuario es ",user, " y tengo ",age, "años")

#Otras cosas
#Números octales y hexadecimales

#octal
'''
Si un número entero esta precedido por un código 0O
o 0o (cero-o), el número será tratado como un valor
octal.
'''
num = 0o123
print(f"\nEl número octal (0o123) en decimal es: {num}")

# hexadecimal
'''
Si un número entero esta precedido por  por el prefijo
0x o 0X (cero-x), el número será tratado como un valor
hexadecimal
'''
num2 = 0x123
print(f"\n(0x123) es un número hexadecimal con valor decimal de: {num2}")