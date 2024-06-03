import random

jug_1 = int(input("Ingrese un numero."))

acierto = 0
intentos = 5

def ganaste (jug_1,acierto):
    if acierto == 0:
        jug_2 = int(input("Adivina cual es el numero."))
        if jug_1 == jug_2:
            print("Ganaste!")
            acierto += 1
        elif jug_1 != jug_2:
            print("Incorrecto.")
            ganaste(jug_1,acierto)
    else:
        print("ganaste")

ganaste(jug_1,acierto)
jug_2 = 0

while jug_1 != jug_2 and intentos != 0:
        jug_2 = int(input("Adivina cual es el numero."))
        intentos -= 1
        print(f"Tienes {intentos} intentos.")

if jug_1 == jug_2:
    print("Ganaste!")
else:
    print("Perdiste!")
        
    
print("Blackjack!")

monto = int(input("Cual es el monto total que traes?"))

carta_c = random.randint(1,11)

import random

print("Blackjack!")

cartas_n = 0
cartas = random.randint(1,11)

jug_a = random.randint(1,21)
oportunidades = 2
while cartas_n != 2 and cartas <= 21:
    print(f"De momento, el total es {cartas}")
    carta_ad = int(input("Quieres una carta?\n 1. Si\n 2. No."))
    if carta_ad == 1:
        cartas_n += 1
        cartas = cartas + random.randint(1,11)
    else:
        cartas_n = 2


print(f"Sacaste {cartas} y la maquina {jug_a}")
if jug_a == 21 or cartas == 21:
    print("Puntaje maximo!")

if cartas > 21: 
    print("Perdiste!")
        
elif jug_a == cartas and cartas < 21:
    print("Empataste.")
elif jug_a > cartas:
    print("Perdiste!")
elif cartas > jug_a:
    print("Ganaste!")

print("m.c.m")

numero = int(input("Numero"))
puntaje = 0

while puntaje == 0 and numero != 1:
    a = int(input("Por que numero lo quieres dividir?"))
    b = numero % a
    if b != 0:
        puntaje = 1
        print(f"No puede ser dividido por {a}.")
    else: 
        numero = numero / a
    print(f"Tenemos entonces {numero}")    

if numero == 1:
    print("Es la expresion minima.")





##while monto > 0:
##    apuesta= int(input("Cuanto deseas apostar en la mano?"))
##    monto -= apuesta
##    cartas = random.randint(1,11) + random.randint(1,11)
##    jug_a == random.randint(1,21)
##    print(f"Sacaste un total de {cartas}")
##    carta_c = int("Quieres una tercera carta?\n 1. Si\n 2. No.")
##    if carta_c    
