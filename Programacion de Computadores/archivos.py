#Utilidades va revisar si la cedula excede los requisitos.
def utilidades(identificacion,cadena):
    if identificacion[0] == "1":
        if len(identificacion) > 6 and len(identificacion) < 9 or len(identificacion) < 11 and len(identificacion) > 9 :
            if identificacion not in cadena:
                cadena.append(identificacion)
                formato_votaciones()
            else:
                print("La cedula ingresada ya fue registrada.")
                return False
        else:
            print(f"{identificacion} Extension invalida.")
            return False
    else: 
        print("Cedula no valida. No empieza en 1.")
        return False

def formato_votaciones():
    eleccion = int(input(f"Vota!\n1: Si. \n2: No. \n3: Voto en Blanco.\n"))
    if eleccion < 1 or eleccion > 3:
        print("Opcion Invalida.")
        formato_votaciones()
    else:
        facultad = int(input("A que facultad perteneces? \n1. Escuela de Administracion. \n2. Escuela de Medicina y Ciencias de la Salud. \n3. Escuela de Ciencias Humanas. \n4. Facultad de Economia. \n5. Facultad de Jurisprudencia. \n6. Facultad de Estudios Internacionales, Politicos y Urbanos. \n7. Facultad de Ciencias Naturales. \n8. Facultad de Creación. \n9. Escuela de Ingenieria, Ciencia y Tecnología."))
        if facultad < 10 and facultad > 0:
            voto = (f"{eleccion},{facultad}\n")    
            return writer. write(voto)
        else: 
            print("Voto Anulado.")
        
with open("datos.csv", "w") as writer:
    check = 1
    #Para llevar de mas datos el documento, se preguntara por confirmacion cada 5 votos.
    conteo = 0
    registro = []
    while check == 1:
        cedula = str(input("Ingresa tu cedula."))
        utilidades(cedula,registro) 
        conteo += 1
        if conteo == 5:    
            check = int(input(f"Deseas continuar? Presiona 1 si deseas continuar."))
    
writer.close()
voto = []
count = 0

with open("datos.csv", "r") as reader:
    for line in reader: 
        if count >= 0: 
            data = line.split(",")
            voto.append([int(data[0]), int(data[1])])
        count += 1
reader.close()

Facultades_si = []
Facultades_no = []
print(voto[0])



votos_si = 0
votos_no = 0
votos_blanco = 0

ADMIN = 0
CIENSALUD = 0
HUMANAS = 0
ECON= 0
JURIS = 0
EIPU = 0
NATURALES = 0
FACREA = 0

EICT = 0
for i in range (len(voto)):
    if voto[i][1] == 1:
        ADMIN += 1
    if voto[i][1] == 2:
        CIENSALUD += 1

    if voto[i][1] == 3:
        HUMANAS += 1
    if voto[i][1] == 4:
        ECON += 1

    if voto[i][1] == 5:
        JURIS += 1

    if voto[i][1] == 6:
        EIPU += 1

    if voto[i][1] == 7:
        NATURALES += 1

    if voto[i][1] == 8:
        FACREA += 1

    else:
        EICT += 1
        
for i in range (len(voto)):
        
    if voto[i][0] == 1:
        votos_si += 1
    elif voto[i][0] == 2:
        votos_no += 1
    else:
        votos_blanco += 1

print(votos_si,votos_no, votos_blanco)
