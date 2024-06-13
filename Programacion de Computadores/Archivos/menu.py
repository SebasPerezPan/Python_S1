import math
# ready = input("Estas listo para comenzar? Y/N")
#     while != "Y
menu = int(input("Selecciona una aplicacion. 1. Teorema de Pitagoras. 2. Lista de Precios. 3. Contador de dias. 4. Calculadora de Interes compuesto y simple.\n"))

if menu == 1: 
    print("Elegiste el teorema!")
    var_a = int(input("Introduce el valor del primer cateto: "))
    var_b = int(input("Introduce el valor del segundo cateto: "))
    resultado = float(math.sqrt(var_a**2 + var_b**2))
    print(f"La hipotenusa es {resultado} we!")
if menu == 2:
    print("Elegiste la lista de precios.")
    var_a = int(input("Precio del primer producto \n"))
    var_b = int(input("Anadido \n"))
    var_c = int(input("Anadido \n"))
    var_d = int(input("Anadido \n"))
    var_e = int(input("Anadido \n"))
    list = [var_a, var_b, var_c, var_d, var_e]
    list.sort()
    resultado = var_a + var_b + var_c + var_d + var_e
    resultado = resultado + resultado*0.19
    print(f"Lista de precios {list}")
    print(f"El total de la compra es de ${resultado}.")

if menu == 3: 
    print("Elegiste el contador de dias.")
    var_a = int(input("Cuantos anos?\n")) 
    var_b = int(input("Cuantos meses?\n"))
    var_c = int(input("Cuantas semanas? \n"))
    var_d = int(input("Cuantos dias? \n"))
    resultado = (var_a*365 + var_b*31 + var_c*7 + var_d)
    print(f"La cantidad de dias fue: {resultado}")
if menu == 4:
    print("Elegiste la calculadora de interes compuesto y simple.")