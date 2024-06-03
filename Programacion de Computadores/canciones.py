
artistas = ["Carlos Vives", "Fonseca", "Guns n' Roses"]

nombre_cancion = ["La gota fria", "Nuestro secreto", "El arroyito", "Simples corazones", "Welcome to the jungle", "November Rain"]

id_artista_cancion = [0,0,1,1,2,2]

duracion_cancion = [241, 354, 278, 197, 534, 415]

mix = [0,1,3,5,4]

for i in range(len(mix)):
    print("La canción",nombre_cancion[mix[i]],"de",artistas[id_artista_cancion[mix[i]]],"y dura",duracion_cancion[mix[i]])

