#-*-coding: utf-8-*-
"""Este Juego Adivina un numero Aleatorio"""
import random
INTENTOS = 0
ERROR = 0
ALEATORIO = random.randint(1, 51)
NOMBRE = raw_input("Ingrese su nombre")
print ""
print "¡Hola!" + NOMBRE +"Bienvenido al Juego Adivina el Número"
print "INSTRUCCIONES:"
print " "
print """En Este Juego debes adivinar un número del 1 al 50,
tendrás únicamente 8 intentos para encontrar el número"""
print ""

while INTENTOS < 8:
    INTENTOS = INTENTOS + 1
    print "Elige un número"
    NUMERO = raw_input()
    try:
        NUMERO = int(NUMERO)
        ERROR = 1
    except ValueError:
        print "solo puedes ingresar números"
        ERROR = 0
        INTENTOS = INTENTOS + 1
    if NUMERO > 50 or NUMERO < 1:
        print "Ingreso Incorrecto\n"
    if ERROR == 1:
        if NUMERO < ALEATORIO:
            print "Tu número es mas bajo\nIntentalo de nuevo"
        if NUMERO > ALEATORIO:
            print "Tu número es mas alto\nIntentalo de nuevo"
        if NUMERO == ALEATORIO:
            break

if NUMERO == ALEATORIO:
    print "Correcto. Usted gana."
if NUMERO != ALEATORIO:
    print "Juego terminado, juega de nuevo."