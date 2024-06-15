count = 0
lista_compras = []

with open("compras.csv" , "r") as reader:
    for line in reader:
        if count >= 1:
            data = line.split(",")
            lista_compras.append([int(data[0]),int(data[1]),int(data[2])])
        count += 1
reader.close()

count = 0
lista_personas = []  
    
## Para sentirme mas comodo, voy a asignar valores para Hombre y Mujer. 

## Mujer = 1 Hombre = 2

with open("personas.csv" , "r") as reader:
    for line in reader:
        if count >= 1:
            data = line.split(",")
            if data[2] == "M\n":
                data[2] = 2
            else:
                data[2] = 1
            lista_personas.append([int(data[0]),(data[1]),(data[2])])
        count += 1
reader.close()

count = 0
lista_productos = []

with open("productos.csv" , "r") as reader:
    for line in reader:
        if count >= 1:
            data = line.split(",")
            lista_productos.append([int(data[0]),(data[1]),int(data[2])])
        count += 1
reader.close()

lista_compras_cliente = []

#Tips: Revisa todo lo que te piden en las funciones. Analizalas, posiblemente, en una arreglo muy extenso puedas guardar todo y facilitarte la vida. 

    
#Por cliente necesitamos Nombre, Cosa, cantidad, valor.

#Haz una ruta explicando como vas a sacar cada cosa.

#Lista Compras. [0] = Lista_personas[0] , Lista_personas[1] ; [1] = Lista_productos[0] , Lista_productos[1] ; [2] = Lista_productos[2] * lista_compras[2]



#Recuerda entender el indice y los elementos dentro del programa.

1 - 30
0 - 29
for i in range(29):
    
    id_persona = lista_compras[i][0] - 1
    id_producto = lista_compras[i][1] -1

    nombre = lista_personas[id_persona][1]
    producto = lista_productos[id_producto][1]

    valor = lista_productos[id_producto][2]
    unidades = lista_compras[i][2]
    valor_total = valor * (unidades)
    genero = lista_personas[id_persona][2]

    lista_compras_cliente.append([nombre , producto , valor, unidades, valor_total, genero])

for i in range (29):
    print(f"Nombre del Cliente: {lista_compras_cliente[i][0]}\nProducto Comprado: {lista_compras_cliente[i][1]}\nValor Unidad: ${lista_compras_cliente[i][2]:.2f}\nUnidades: {lista_compras_cliente[i][3]}\nValor total: ${lista_compras_cliente[i][4]:.2f}\n")

## Total de Compras por genero. Necesitamos la lista principal, y la lista que hicimos.



def versus(lista_compras_cliente):
    
    cantidad_hombres = 0
    cantidad_mujeres = 0

    cantidades_hombres = 0
    cantidades_mujeres = 0

    valor_hombres = 0
    valor_mujeres = 0

    for i in range (29):
        if lista_compras_cliente[i][5] == 1:
                cantidad_mujeres += 1
                cantidades_mujeres += lista_compras_cliente[i][3]
                valor_mujeres += lista_compras_cliente[i][4]
        else:
                cantidad_hombres += 1
                cantidades_hombres += lista_compras_cliente[i][3]
                valor_hombres += lista_compras_cliente[i][4]
    print(f"Cantidad de hombres que compraron: {cantidad_hombres}\nCantidad de mujeres que compraron: {cantidad_mujeres}\n\nUnidades totales compradas por hombres: {cantidades_hombres}\nUnidades totales compradas por mujeres: {cantidades_mujeres}\n\nValor total gastado por hombres: ${valor_hombres}\nValor total gastado por mujeres: ${valor_mujeres}\n")
    if cantidad_hombres>cantidad_mujeres:
        print("Los hombres compraron mas.")
    else:
        print("Las mujeres compraron mas.")

def max_cliente(lista_compras_cliente):
    max_valor = 0
    cliente = "Sebas"
    for i in range(29):
        if lista_compras_cliente[i][4] > max_valor:
            max_valor = lista_compras_cliente[i][4]
            cliente = lista_compras_cliente[i][0]
    print(f"\n{cliente} fue quien mas gasto, con un total de: ${max_valor}")

def max_producto(lista_compras_cliente):
    max_producto = 0
    articulo = "Sebas"
    for i in range(29):
        if lista_compras_cliente[i][3] > max_producto:
            max_producto = lista_compras_cliente[i][3]
            articulo = lista_compras_cliente[i][1]
    print(f"\n{articulo} fue el producto mas comprado\nUnidades: {max_producto}")

def max_valor(lista_compras_cliente):
    max_valor = 0
    for i in range(29):
        if lista_compras_cliente[i][4] > max_valor:
            max_valor = lista_compras_cliente[i][4]
            valor_nombre = lista_compras_cliente[i][1]
    print(f"\n{valor_nombre} fue el producto que mas recaudo.\nRecaudo total: ${max_valor}")

## Crearemos un arreglo bidimensional super tranqui. 
name = "Sebas"
apellidos = []
cantidad_ = 0
cantidad_apellidos =[]
for i in range (29):
    cantidad_ = 0
    for j in range(len(lista_compras_cliente[i][0])):
        name = lista_compras_cliente[i][0] 
        if name[j] == " ":
            cantidad_ = lista_compras_cliente[i][3]
            apellidos.append(name[j+1])
            cantidad_apellidos.append([cantidad_])

def compras_inicial(apellidos):
    updated_apellidos = []
    updated_valores = []
    lista_final = []
    print(cantidad_apellidos)
    for i in range (29):
        valor_apellidos = 0
        if apellidos[i][0] not in updated_apellidos:
            for j in range(29):
                if j != i:
                    if apellidos[i][0] == apellidos[j][0]:
                        valor_apellidos += cantidad_apellidos[i][0]
            updated_apellidos.append(apellidos[i][0])
            updated_valores.append(valor_apellidos)
            lista_final.append([apellidos[i][0],valor_apellidos])
    print(lista_final)
compras_inicial(apellidos)

versus(lista_compras_cliente)
max_cliente(lista_compras_cliente)
max_producto(lista_compras_cliente)
max_valor(lista_compras_cliente)
