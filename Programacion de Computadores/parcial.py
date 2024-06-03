import math

print("Calculadora de Casa")

n_hab = int(input("Cuantas habitaciones va a tener la casa?"))
gar_dim = 0
dim_hab_a = 0 
dim_hab_c = 0
dim_hab_b = 0
if n_hab >= 3:
    n_hab = 3
    n_hab_aa = int(input("Cual es el valor de ancho del primer cuarto?")) 
    n_hab_al = int(input("Cual es el valor de largo del primer cuarto?"))
    if n_hab_aa >= 10:
        n_hab_aa = 10
    elif n_hab_aa <= 2:
        n_hab_aa = 2
    if n_hab_al > 10:
        n_hab_al = 10
    elif n_hab_al <= 2:
        n_hab_al = 2
    dim_hab_a = n_hab_aa * n_hab_al
    
    print(f"El area del cuarto es de {dim_hab_a} m")
    
    n_hab_ba = int(input("Cual es el valor de ancho del segundo cuarto?")) 
    n_hab_bl = int(input("Cual es el valor de largo del segundo cuarto?"))
    
    if n_hab_ba >= 10:
        n_hab_ba = 10
    elif n_hab_ba <= 2:
        n_hab_ba = 2
    if n_hab_bl > 10:
        n_hab_bl = 10
    elif n_hab_bl <= 2:
        n_hab_bl = 2
    dim_hab_b = n_hab_ba * n_hab_bl
    
    print(f"El area del cuarto es de {dim_hab_b} m")

    n_hab_ca = int(input("Cual es el valor de ancho del tercer cuarto?")) 
    n_hab_cl = int(input("Cual es el valor de largo del tercer cuarto?"))
    
    if n_hab_ca >= 10:
        n_hab_ca = 10
    elif n_hab_ca <= 2:
        n_hab_ca = 2
    if n_hab_cl > 10:
        n_hab_cl = 10
    elif n_hab_cl <= 2:
        n_hab_cl = 2
    dim_hab_c = n_hab_ca * n_hab_cl

    print(f"El area del cuarto es de {dim_hab_c} m")


elif n_hab == 2:
    n_hab_aa = int(input("Cual es el valor de ancho del primer cuarto?")) 
    n_hab_al = int(input("Cual es el valor de largo del primer cuarto?"))
    if n_hab_aa >= 10:
        n_hab_aa = 10
    elif n_hab_aa <= 2:
        n_hab_aa = 2
    if n_hab_al > 10:
        n_hab_al = 10
    elif n_hab_al <= 2:
        n_hab_al = 2
    dim_hab_a = n_hab_aa * n_hab_al
    
    print(f"El area del cuarto es de {dim_hab_a} m")
    
    n_hab_ba = int(input("Cual es el valor de ancho del segundo cuarto?")) 
    n_hab_bl = int(input("Cual es el valor de largo del segundo cuarto?"))
    
    if n_hab_ba >= 10:
        n_hab_ba = 10
    elif n_hab_ba <= 2:
        n_hab_ba = 2
    if n_hab_bl > 10:
        n_hab_bl = 10
    elif n_hab_bl <= 2:
        n_hab_bl = 2
    dim_hab_b = n_hab_ba * n_hab_bl
    
    print(f"El area del cuarto es de {dim_hab_b} m")

    
    
elif n_hab <= 1:
    n_hab_aa = int(input("Cual es el valor de ancho del primer cuarto?")) 
    n_hab_al = int(input("Cual es el valor de largo del primer cuarto?"))
    if n_hab_aa >= 10:
        n_hab_aa = 10
    elif n_hab_aa <= 2:
        n_hab_aa = 2
    if n_hab_al > 10:
        n_hab_al = 10
    elif n_hab_al <= 2:
        n_hab_al = 2
    dim_hab_a = n_hab_aa * n_hab_al    
    
    print(f"El area del cuarto es de {dim_hab_a} m")

    
    
dim_habs = int(dim_hab_c + dim_hab_a + dim_hab_b)

print(f"Entendido, el numero de habitaciones es: {n_hab} para un total de: {dim_habs} m.")

n_ban = int(input("Cuantos banñs tendra la casa?"))
ban_typ = int(input("Que categoria tienen? 1. Premium. 2. Regulares"))
dim_ban = 0
if n_ban >= 3:
    n_ban = 3
elif n_ban <= 1:
    n_ban = 1

if ban_typ == 1:
    dim_ban = n_ban * 9
if ban_typ == 2:
    dim_ban = n_ban * 5

print(f"El area del cuarto es de {dim_ban} m")
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
        gar_dim = 20
    elif gar_size == 2:
        gar_dim = 10
print(f"El tamaño del garaje es de {gar_dim} m.")

dim_tot_a = dim_habs + dim_patio + dim_ban
dim_tot_b = dim_tot_a * 1.25
dim_tot_c = dim_tot_b + gar_dim
dim_ma = 100
dim_tot_b_g = dim_tot_b 
if dim_ma >= dim_tot_b_g:
    val_tot = 8000000 * dim_tot_b
elif dim_ma <= dim_tot_b_g:
    val_tot = 9000000 * dim_tot_b
val_gar = gar_dim * 5000000
val_tot_a = val_tot + val_gar
val_tc = 1000000000
if val_tot_a >= val_tc:
    val = val_tot_a * 0.95
val = val_tot_a
print(f"El tamaño total en m es de: {dim_tot_c}.")
print(f"El valor total de la casa sera de: $ {val:,.2f}.")

print("Punto 2")

ar_x = float(input("Defina un valor para x"))
ar_y = float(input("Defina un valor para y"))
##Dividi toda la fraccion en dos variables, zau y zad. Podia usar math, pero me parecio mas humano simplemente convertir las raices.
zau = ((5*ar_x + ((((ar_y)**ar_x-1)**1/2)/(ar_y+2*ar_x)))**1/2)**3
zad =(((ar_x**2)**3)/(((ar_y)**3)*(ar_x+1))) - 3 * ((3)**1/2+(ar_x-1)**1/4)
z = zau - zad
print(z)


a = math.sqrt((8),(3))
print(a)