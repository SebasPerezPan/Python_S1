import math

print("Calculadora de Casa")

##Se van a definir variables para cantidades de cada cosa, ya sea banhos o cuartos.
##Hice primero la opcion mas larga, la de los 3 cuartos y luego solo fue copiar y pegar lo hecho.
##Por lo general, hay al final de cada grupo  de codigo, una ultima linea que imprime valor en metros.
n_hab = int(input("Cuantas habitaciones va a tener la casa?"))
gar_dim = 0
dim_hab_a = 0 
dim_hab_c = 0
dim_hab_b = 0
if n_hab >= 3:
    n_hab = 3
    hab_aa = int(input("Cual es el valor de ancho del primer cuarto?")) 
    hab_al = int(input("Cual es el valor de largo del primer cuarto?"))
    if hab_aa >= 10:
        hab_aa = 10
    elif hab_aa <= 2:
        hab_aa = 2
    if hab_al > 10:
        hab_al = 10
    elif hab_al <= 2:
        hab_al = 2
    dim_hab_a = hab_aa * hab_al
    
    print(f"El area del cuarto es de {dim_hab_a} m")
    
    hab_ba = int(input("Cual es el valor de ancho del segundo cuarto?")) 
    hab_bl = int(input("Cual es el valor de largo del segundo cuarto?"))
    
    if hab_ba >= 10:
        hab_ba = 10
    elif hab_ba <= 2:
        hab_ba = 2
    if hab_bl > 10:
        hab_bl = 10
    elif hab_bl <= 2:
        hab_bl = 2
    dim_hab_b = hab_ba * hab_bl
    
    print(f"El area del cuarto es de {dim_hab_b} m")

    hab_ca = int(input("Cual es el valor de ancho del tercer cuarto?")) 
    hab_cl = int(input("Cual es el valor de largo del tercer cuarto?"))
    
    if hab_ca >= 10:
        hab_ca = 10
    elif hab_ca <= 2:
        hab_ca = 2
    if hab_cl > 10:
        hab_cl = 10
    elif hab_cl <= 2:
        hab_cl = 2
    dim_hab_c = hab_ca * hab_cl

    print(f"El area del cuarto es de {dim_hab_c} m")


elif n_hab == 2:
    hab_aa = int(input("Cual es el valor de ancho del primer cuarto?")) 
    hab_al = int(input("Cual es el valor de largo del primer cuarto?"))
    if hab_aa >= 10:
        hab_aa = 10
    elif hab_aa <= 2:
        hab_aa = 2
    if hab_al > 10:
        hab_al = 10
    elif hab_al <= 2:
        hab_al = 2
    dim_hab_a = hab_aa * hab_al
    
    print(f"El area del cuarto es de {dim_hab_a} m")
    
    hab_ba = int(input("Cual es el valor de ancho del segundo cuarto?")) 
    hab_bl = int(input("Cual es el valor de largo del segundo cuarto?"))
    
    if hab_ba >= 10:
        hab_ba = 10
    elif hab_ba <= 2:
        hab_ba = 2
    if hab_bl > 10:
        hab_bl = 10
    elif hab_bl <= 2:
        hab_bl = 2
    dim_hab_b = hab_ba * hab_bl
    
    print(f"El area del cuarto es de {dim_hab_b} m")

    
    
elif n_hab <= 1:
    hab_aa = int(input("Cual es el valor de ancho del primer cuarto?")) 
    hab_al = int(input("Cual es el valor de largo del primer cuarto?"))
    if hab_aa >= 10:
        hab_aa = 10
    elif hab_aa <= 2:
        hab_aa = 2
    if hab_al > 10:
        hab_al = 10
    elif hab_al <= 2:
        hab_al = 2
    dim_hab_a = hab_aa * hab_al    
    
    print(f"El area del cuarto es de {dim_hab_a} m")

    
    
dim_habs = int(dim_hab_c + dim_hab_a + dim_hab_b)

print(f"Entendido, el numero de habitaciones es: {n_hab} para un total de: {dim_habs} m.")
##Continuamos con los banhos. Si el usuario no elije una de las dos opciones alrededor del area social, se le asignara el banho regular. 
n_ban = int(input("Cuantos baños tendra la casa?"))
n_ban_prem = int(input("Cuantos de estos baños quieres que sean Premium?"))

ban_prem = 9
ban_reg = 5
n_ban_reg = 0

if n_ban_prem >= n_ban:
    print("El resultado del calculo sera inpreciso.")

if n_ban >= 3:
    n_ban =3 
elif n_ban <= 1:
    n_ban = 1

if n_ban_prem >= 3:
    n_ban_prem =3
elif n_ban_prem <= 1:
    n_ban_prem = 1

n_ban_reg = n_ban - n_ban_prem

dim_ban = ban_prem * n_ban_prem + (n_ban_reg * ban_reg)

print(f"El area del baños es de {dim_ban} m")

#Area social. Si el usuario no elije una de las dos opciones alrededor del area social, se le asignara el 
# area social regular. 

dim_social = 0

ar_social = int(input("Respecto al area social, prefieres? \n 1. Regular.\n2. Premium"))

if ar_social == 2:
    dim_social = 40
else:
    dim_social = 20
print(f"El tamaño del area social es de :{dim_social} m")
#Patio. 

dim_patio = 0
patio = int(input("La casa tiene patio? 1. Si. 2. No."))
if patio == 1:
    pat_a = int(input("Cual es el valor de ancho del patio?")) 
    pat_l = int(input("Cual es el valor de largo del patio?"))
    if pat_a >= 10:
        pat_a = 10
    elif pat_a <= 2:
        pat_a = 2
    if pat_l > 10:
        pat_l = 10
    elif pat_l <= 2:
        pat_l = 2
    dim_patio = pat_a * pat_l
    

elif patio == 2:
    dim_patio = 0

print(f"El tamaño del patio es de {dim_patio} m.")

garaje = int(input("La casa tiene garaje? 1. Si 2. No."))
gar_size = int(input("El garaje es: 1. Doble. 2. Sencillo."))

if garaje == 1:
    if gar_size == 1:
        dim_gar = 20
    elif gar_size == 2:
        dim_gar = 10
print(f"El tamaño del garaje es de {dim_gar} m.")

dim_a = dim_habs + dim_patio + dim_ban + dim_social

sub_dim_total = dim_a * 1.25

dim_total = sub_dim_total + dim_gar

dim_mx = 100

##dim_tot_c = dim_tot_b + gar_dim

if dim_mx >= sub_dim_total:
    val_tot = 8000000 * sub_dim_total
elif dim_mx <= sub_dim_total:
    val_tot = 9000000 * sub_dim_total

val_gar = dim_gar * 5000000

val = val_tot + val_gar

val_tc = 1000000000

if val >= val_tc:
    val = val * 0.95

print(f"El tamaño total en m es de: {dim_total}.")
print(f"El valor total de la casa sera de: $ {val:,.2f}.")

print("Punto 2")

x = int(input("Defina un valor para x"))
y = float(input("Defina un valor para y"))

##Dividi toda la fraccion en dos variables, zau y zad. Podia usar math, pero me parecio mas humano simplemente convertir las raices. ar_x sera x, ar_y sera y.

resultado =(pow ((math.sqrt(5*x) + math.sqrt((math.sqrt(pow(y,(x-1)))) / (y + (2 * x)))),3)
)  - ( (pow(x,6)) / ((pow(y,3)) * x) + 1) - 3 * ((math.sqrt(3)) + math.sqrt(math.sqrt(x-1)))

print(resultado)