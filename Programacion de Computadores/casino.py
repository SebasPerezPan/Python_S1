import random
def juego (a,b,c,d,e):
    tiro_inicial = random.randint(2,12)
    print(tiro_inicial)
    if tiro_inicial == (a or b or c):
        print("Perdiste!")
    elif tiro_inicial == ( d or e):
        print("Ganaste!")
    else: 
        print("Empieza fase de tiros:")
        fase_2(tiro_inicial,e)

def fase_2(x,y):
    intentos = 4
    tiro_final = random.randint(2,12)
    print(tiro_final)
    while tiro_final != x and intentos > 1:
        tiro_final = random.randint(2,12)
        intentos -= 1
        if tiro_final == y:
            intentos = 0
        print(tiro_final)
    if tiro_final == x:
        print("Ganaste")
    else:
        print("Perdiste!")

# Funcion para el juego. Paso Inicial -- Paso 2

juego (2,3,12,7,11)