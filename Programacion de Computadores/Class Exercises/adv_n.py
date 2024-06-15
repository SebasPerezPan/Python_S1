print("Adivina el digito de 2 cifras.")

ja_a = int(input("Ingrese la primera cifra."))
ja_b = int(input("Ingrese la segunda cifra."))
fam = 0
punto = 0
if (ja_a or ja_b) > 9 or ja_a <= 0:
    print("Error. No puede continuar.")
else:
    print(f"El numero seleccionado es {ja_a}{ja_b}.")
    turnos = 5

    
    def intento(turnos, ja_a, ja_b,punto,fam):
        if turnos != 0:
            jb_a = int(input("Ingrese la primera cifra: \n"))
            jb_b = int(input("Ingrese la segunda cifra: \n"))
            if ja_a == jb_a and ja_b == jb_b:
                print(f"Ganaste! Era {ja_a}{ja_b}!")
            elif ja_a == jb_a or ja_b == jb_b:
                turnos -= 1
                fam += 1
                print(f"Fama!\nTe quedan {turnos} turnos, llevas {fam} famas y {punto} puntos!")
                intento(turnos, ja_a, ja_b,punto,fam)
            elif ja_a == jb_b or ja_b == jb_a:
                turnos -= 1
                punto += 1
                print(f"Punto!\nTe quedan {turnos} turnos, llevas {fam} famas y {punto} puntos!")
                intento(turnos, ja_a, ja_b,punto,fam)
            else:
                turnos -= 1
                print(f"Sigue intentando!")
                intento(turnos, ja_a, ja_b,punto,fam)
        else:
            print(f"Perdiste, era {ja_a}{ja_b}\nQuedaste con {fam} famas y {punto} puntos!")
    intento(turnos, ja_a, ja_b,punto,fam)

