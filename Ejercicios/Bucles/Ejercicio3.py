'''
Un mago ha elegido un número secreto. Lo ha escondido en una variable llamada secret_number.Quiere que todos los que ejecutan
su programa jueguen el juego Adivina el número secreto,y adivina qué número ha elegido para ellos. ¡Quiénes no adivinen el número 
quedarán atrapados en un bucle sin fin para siempre! Desafortunadamente, él no sabe cómo completar el código.

Tu tarea es ayudar al mago a completar el código de tal manera que el código:
- pedirá al usuario que ingrese un número entero;
- utilizará un bucle while;
-comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago.Si el número elegido por el usuario
es diferente al número secreto del mago, el usuario debería ver el mensaje "¡Ja, ja! ¡Estás atrapado en mi bucle!" y se le solicitará
que ingrese un número nuevamente. Si el número ingresado por el usuario coincide con el número escogido por el mago, el número debe imprimirse
en la pantalla, y el mago debe decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora."
¡El mago está contando contigo! No lo decepciones.
'''

#Hacemos que el numero dado por el mago sea aleatorio para esto importamos la siguiente libreria
import random
#generamos el numero secreto
secret_number = random.randint(1,10)
print(secret_number)
print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

#Pedimos el numero
number = int(input("Ingresa tu respuesta muggle!"))

#Evaluamos el numero ingresado atraves de un while
while number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    number = int(input("Intenta de nuevo muggle!"))

print("¡Bien hecho, muggle!")

