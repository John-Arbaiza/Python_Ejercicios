#argumento o parametro end
#Este se usa para agregar cualquier cadena de caracteres al final de la salida e impresion de pantalla
print("Mi nombre es", end=" ")
print("John Elvis")
print("*************************************************")

#Parametro sep
#Se usa para dar formato a la cadena de caracteres que se van a imprimir en pantalla
print("1","2","3","4","5",sep=",")

#Uso de end y sep juntos
print("Esto es","una prueba",sep=" ☻ ", end=" ")
print("de end","y sep usados","al mismo tiempo",sep=" ☺ ")
print("*************************************************")

#Ejercicio de practica de LAB
#Primera parte de la flecha
print("     *\n   *   *\n  *     *\n *       *\n***     ***\n",end="")
#Parte 2
print("  *     *\n  *     *\n  *******\n")

#Al multiplicar x2 los print su resultado se multiplicara
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)

print("****************************************")
#Cuestionario de la seccion
print("Mi\nnombre\nes\nBond.", end=" ")
print("James Bond.")
print()

#Lo siguientes es un error ya que el sep se usa para dar formato y en este caso no hay a que
#Cadena darle un formato
#print(sep="&", "fish", "chips")

#¿Cual de las siguientes dara erro?
print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
#print('"Greg's book."')