random.seed(1234)
equipos = ["Junior", "Millonarios", "Santafé", "Nacional", "Medellín", "Bucaramanga", "Pasto" ,"Alianza", "Huila", "Tolima"]
num_equipos = 10;
num_partidos; #Calcular este número a partir del número de equipos
equipo_local = [0]*<Inserte la dimensión adecuada>
equipo_visita = [0]*<Inserte la dimensión adecuada>
goles_local = [0]*<Inserte la dimensión adecuada>
goles_visita = [0]*<Inserte la dimensión adecuada>
total_puntos = [0]*<Inserte la dimensión adecuada>
    
generar_partidos(equipo_local, equipo_visita, goles_local, goles_visita, num_equipos)
calcular_puntos(equipo_local, equipo_visita, goles_local, goles_visita, total_puntos, num_partidos)
campeon = calcular_campeon(total_puntos, num_equipos)
    
print_puntos_totales(equipos, total_puntos, num_equipos)
print("El ganador del campeonato es",equipos[campeon],"con",total_puntos[campeon],"puntos."
