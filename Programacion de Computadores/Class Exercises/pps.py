import random

a = int(input("Seleccione una opcion. \n 1. Papel. \n 2. Piedra. \n 3. Tijera"))

b = random.randint(1,3)


if b == 1:
    c = "Papel"
elif b == 2:
    c = "Piedra"
else: 
    c = "Tijera"

print(f"La maquina saco {c}")
    

if a == b:
    print("Empate.")
elif a == 1 and b == 2 or a == 2 and b == 3 or a == 3 and b==1:
    print("Ganaste") 
elif a <= 0 or a > 3:
    print("Codigo Invalido.")
else:
    print("Perdiste")
