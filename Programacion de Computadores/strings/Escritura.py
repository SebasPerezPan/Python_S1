with open("data.csv", "r") as reader:
    #print(reader.read())#Read the whole file.
     print(reader.read()) #Reads one line. the first x characters of a line.
    

reader.close()

with open("prueba.txt", "w") as writer:
    for i in range (25):
        writer.write("Hola "+str(i)+"\n")
writer.close()


personas = []
notas = []
count = 0
with open ("data.csv", "r") as reader:
    for line in reader: 
        if count > 0:
            data = line.split(",")
            personas.append([data[0], data[1], data[2], str(data[6])])
            notas.append([float(data[3]), float(data[4]), float(data[5])])
        count += 1
reader.close()

prom_a = 0.0
prom_b = 0.0
prom_c = 0.0


for i in range(len(personas)):
    prom_a += (notas[i][0])
    prom_b += (notas[i][1])
    prom_c += (notas[i][2])

prom_a = prom_a / len(notas)
prom_b = prom_b / len(notas)
prom_c = prom_c / len(notas)

Male = 0
Fem = 0

for i in range(len(personas)):
    if "M" in personas[i][3]:
        Male += 1
    else:
        Fem += 1
if Male > Fem: 
    gender = "Hombres."
else: 
    gender = "Mujeres."

with open("Final.txt", "w") as writer:
    writer.write(f"El promedio de la primera nota es: {prom_a}\nEl promedio de la segunda nota es: {prom_b}\nEl promedio de la tercera nota es {prom_c}\nLa mayoria de participantes son: {gender}")
writer.close()
