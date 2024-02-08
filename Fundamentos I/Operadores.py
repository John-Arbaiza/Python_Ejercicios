# --- Operadores en python ---

#Operador suma
print(3 + 4)
#Resta
print(3 - 4)
#Multiplicacion
print(3 * 4)
'''---------------------| NOTA: |-----------------------------
  Este operador cuando es aplicado a una cadena y a un número
  se convierte en un operador de replicación:
  ------------------------------------------------------------
  Ejemplo:
'''
print()
print("        *         "*2)
print("       * *        "*2)
print("      *   *       "*2)
print("     *     *      "*2)
print("    *       *     "*2)
print("   *         *    "*2)
print("  *           *   "*2)
print(" *             *  "*2)
print("******     ****** "*2)
print("     *     *      "*2)
print("     *     *      "*2)
print("     *     *      "*2)
print("     *     *      "*2)
print("     *     *      "*2)
print("     *     *      "*2)
print("     *******      "*2)
print("="*40, "\n")
#=============================================
#Modulo
print(10 % 3)
#Division
print(10 / 2)
#Division entera
print(10 // 2)
#Elevando a un exponente
print(3 ** 2)

#Concatenación
print("\nHola que tal "+ "Desde Python")

#Operadores comparativos
print()
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(4 == 5)
print( 5!= 6)

#Uso de estos operadores empleando cadenas
print()
print("Hola" > "Python")
print("Hola" < "Python")
print("A" >= "B") #Cuenta el orden alfabetico
print(len("abcde") >= len("abcd"))#Cuenta los caracteres

#Operadores logicos
print()
print(4 > 5 and 6 < 7)
print(3<6 or 6>4)
print(not(3 > 4))