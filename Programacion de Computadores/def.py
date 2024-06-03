def juego(nsecreto1, nsecreto2, turnos, punto, fama):
    jugadorB_1 = int(input("Escriba el 1 digito: "))
    jugadorB_2 = int(input("Escriba el 2 digito: "))
    
    if (turnos != 0):
        turnos -= 1
        if (jugadorB_1 == nsecreto1):
            fama +=1
            if(jugadorB_2 == nsecreto2):
                fama +=1 
            else:
                print("Ese no es el número")
                juego(nsecreto1, nsecreto2, turnos, fama, punto)
        elif (jugadorB_1 == nsecreto2):
            punto += 1
            if(jugadorB_2 == nsecreto1):
                punto+=1 
            elif (jugadorB_2 == nsecreto2):
                fama += 1 
            else: 
                print("Ese no es el número")
                juego(nsecreto1, nsecreto2, turnos, fama, punto)
        else:
            print("Ese no es el número")
            juego(nsecreto1, nsecreto2, turnos, fama, punto)
    else: 
        print("El juego terminó, el número era: ", nsecreto1, nsecreto2)
        
