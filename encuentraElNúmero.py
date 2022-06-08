# Este juego trata sobre encontrar el número

import random

intentos = 0

# Aquí nos saluda y pregunta nuestro nombre
print("Buenas tardes, ¿Cómo te llamas?")
jugador = input()
print("Bien, " + jugador + ", vamos a comenzar.")

# Aquí nos generá un número random, entre 1 y 20, y nos avisa entre que número esta pensando
numero = random.randint(1, 20)
print("Bueno, "+ jugador + ", estoy pensando en un número entre 1 y 20")

# Aquí nos pone un numero de intentos, en este caso 6, junto con la pregunta de intenta adivinarlo
while intentos < 6:
    print("Intenta adivinarlo.")
    estimacion = input()
    estimacion = int(estimacion)
# Aquí va sumando los intentos que hacemos
    intentos = intentos + 1
# Aquí nos avisa si el número que dimos, esta más bajo, alto, o si encontramos el número, para agilizar y añadir estrategia al juego
    if estimacion < numero:
        print("Uff, andas muy bajo.")
    
    if estimacion > numero:
        print("Te pasaste, andas muy alto.")

    if estimacion == numero:
        break
# Si logramos encontrar el número, nos dice que lo hicimos bien y nos da nuestro número de intentos
if estimacion == numero:
    intentos = str(intentos)
    print("¡Bien hecho " + jugador + "! ¡Has encontrado el número solo en " + intentos + " intentos!")
# Este mensaje es por si nos pasamos del número de intentos
else :
    print("Perdiste, agotaste tus 6 intentos")