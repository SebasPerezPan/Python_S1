import random

print("Partido.")
equipos = ["Junior", "Millonarios", "Santafé", "Nacional", "Medellín", "Bucaramanga", "Pasto" ,"Alianza", "Huila", "Tolima"]

numero_de_equipos = 10
goles_local = []
goles_visita = []
equipo_local = []
equipo_visita = []
total_puntos = []
numero_partidos = 0
for i in range(numero_de_equipos):
    for j in range(numero_de_equipos):
        if i != j:
            equipo_local.append(i)
            equipo_visita.append(j)
            goles_local.append(random.randint(0, 5))
            goles_visita.append(random.randint(0, 5))
            numero_partidos += 1

# for i in range(len(equipo_local)):
#     print(f"{equipo_local[i]} vs {equipo_visita[i]}")
#     print(f"Resultado: {goles_local[i]} - {goles_visita[i]}\n")

for i in range(numero_de_equipos):
    total_puntos.append(0)

for i in range(numero_partidos):
    if goles_local[i] > goles_visita[i]:
        total_puntos[equipo_local[i]] = total_puntos [equipo_local[i]] + 3

    elif goles_local[i] < goles_visita[i]:
        total_puntos[equipo_visita[i]] = total_puntos [equipo_visita[i]] + 3

    else: 
        total_puntos[equipo_local[i]] = total_puntos[equipo_local[i]] + 1
        total_puntos[equipo_visita[i]] = total_puntos[equipo_visita[i]] + 1

ganador = 0
puntos = 0
for i in range(numero_de_equipos):
    if total_puntos[i] > puntos:
        ganador = equipos[i]
        puntos = total_puntos[i]
for i in range(len(equipos)):
    print(f"{equipos[i]}: {total_puntos[i]}")


print(f"El ganador del torneo es {ganador} con {puntos} puntos.")