#Programa para hallar el maximo comun multiplo entre 2 numeros. 
a = int(input("Agregue el primer numero."))
b = int(input("Agregue el segundo numero."))
c = False
mcm = 2
while c != True:
    if mcm % a == 0 and mcm % b == 0:
        c = True
    else:
        mcm = mcm + 1


print(f"El mcm es : {mcm}")

#primos. La logica es que f es el divisor. Mientras que f != n el programa corre, o hasta que descu

n = int(input("Ingrese el numero que desea saber si es primo."))
f = 2
while n % f != 0:
    f +=1

if n == f:
    print(" primo.")
else:
    print("no Primo.")