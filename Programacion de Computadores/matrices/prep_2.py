import random



def generacion():
    numero_vuelos = int(input("Cuantos vuelos seran generados?"))
    if numero_vuelos < 1:
        generacion ()
    else:
        return numero_vuelos

numero_vuelos = generacion()
cant_pasajeros = []
distancia =[]
def base_vuelos(numero_vuelos):
    for i in range(numero_vuelos):
        cant_pasajeros.append(random.randint(50,100))
        distancia.append(random.randint(500,5000))
base_vuelos(numero_vuelos)

print("\nInformacion de Vuelos:\n")
for i in range(len(cant_pasajeros)):
    print(f"Pasajeros: {cant_pasajeros[i]}\nDistancia: {distancia[i]}\n\n")

codigos = []

def pasajeros_(numero_vuelos,cant_pasajeros):
    for i in range(numero_vuelos):
        for j in range(cant_pasajeros[i]):
            codigos.append(random.randint(100,999))
pasajeros_(numero_vuelos,cant_pasajeros)

status = []
#Los Status van a ser numericos. 1 = VIP, 2 = Diamante 0 = Sin Status.
def status_(codigos):
    
    for i in range(len(codigos)):
        if codigos[i] & 12 == 0:
            status.append(2)
        elif codigos[i] & 7 == 0:
            status.append(1)
        else:
            status.append(0)

status_(codigos)

millas = []

def calc_millas(distancia,cant_pasajeros,millas):
    base = 0
    for i in range(len(distancia)):
        for j in range(base,(base + cant_pasajeros[i])):
            if status[j] == 2:
                millas.append(distancia[i]/20)
            elif status[j] == 1:
                millas.append(distancia[i]/60)
            else:
                millas.append(distancia[i]/100)
            base += 1

calc_millas(distancia,cant_pasajeros,millas)

with open("vuelos.txt","w") as writer:
    base_2 = 0
    for i in range(numero_vuelos):
        writer.write(f"Vuelo {i+1}:\nDistancia: {distancia[i]} km\n")
        for w in range(base_2,(base_2 + cant_pasajeros[i])):
            writer.write(f"Cliente: {codigos[w]} Status: {status[w]} Millas: {millas[w]} \n")
            base_2 += 1
writer.close()