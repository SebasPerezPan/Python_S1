import random

def generar_vuelos(pv, dv, n):
    for i in range(n):
        pv[i] = random.randint(50,100)
        dv[i] = random.randint(500,5000)

def calcular_factor_bono(cp):
    if cp % 12 == 0:
        factor = 20
    elif cp % 7 == 0:
        factor = 60
    else:
        factor = 100
    return factor


def calcular_millas(pv, dv, mt, n):
    for i in range(n):
        for j in range(pv[i]):
            codpasajero = random.randint(100,999)
            mt[codpasajero-100] += calcular_millas(codpasajero, dv[i])

millas_totales = [0]*900

nv = int(input("Escriba el número de vuelos"))

pasajeros_vuelo = [0]*nv
distancia_vuelo = [0]*nv

generar_vuelos(pasajeros_vuelo, distancia_vuelo,nv)

calcular_millas(pasajeros_vuelo, distancia_vuelo, millas_totales, nv)

for i in range(900):
    if millas_totales[i] > 0:
        print("El pasajero",i,"tiene",millas_totales[i],"millas")



