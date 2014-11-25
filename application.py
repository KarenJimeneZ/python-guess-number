#-*-coding: utf-8-*-
import random

intentos = 0
error=0
x = random.randint (1, 51)
nombre = raw_input("Ingrese su nombre")
print ""
print "¡Hola!" + nombre +" Bienvenido al Juego Adivina el Número" 


print "INSTRUCCIONES:"
print ""
print "En Este Juego debes adivinar un número del 1 al 50, tendrás únicamente 8 intentos para encontrar el número"
print ""
while intentos < 8:
    intentos = intentos + 1
    print "Elige un número"
    numero = raw_input()


    try: 
        numero = int(numero)
        error=1
        
    except:

        print "solo puedes ingresar números"
        error=0

       
 
        intentos = intentos + 1 
    
    if numero >50 or numero <1:
            print "Ingreso Incorrecto"
    
    if error ==1 or error>1:
        if numero < x:
            print "Tu número es mas bajo"
        if numero > x:
            print "Tu número es mas alto"
        if numero == x:
            break

if numero == x:
    print "¡FELICIDADES! ¡ADIVINASTE, HAZ GANADO!"
        
if numero != x:
    print "¡LO SIENTO, EL JUEGO HA TERMINADO!"
