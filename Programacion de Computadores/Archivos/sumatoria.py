import random

def hoy(y,x,j,m):
    suma = 0
    numeros = []
    pares = 0
    impares = 0
    size = 0
    for i in range(y,x):
        i = random.randint(j,m)
        numeros.append(i)
        suma += i
        size += 1
        if i % 2 != 0:
            impares += i
        else:
            pares += i
    promedio = suma / x
    print(numeros,promedio)
    print(f"El total es: {suma}\nLa suma de pares es: {pares}\nLa suma de impares {impares}.")
    return numeros
    

lista = hoy(1,30,1,10)

def num_mnx(x,h):
    if h == 1:
        num = 1000
        for i in range(29):
            if x[i] < num:
                num = x[i]
    else:
        num = 0
        for i in range(29):
            if x[i] > num:
                num = x[i]
    return num
print(num_mnx(lista,1))

def pos_mnx(x,h):
    if h == 1:
        num = 1000
        for i in range(29):
            if x[i] < num:
                num = x[i]
                pos = i
    else:
        num = 0
        for i in range(29):
            if x[i] > num:
                num = x[i]
                pos = i
    return pos + 1
print(pos_mnx(lista,0))

def find(x,y,n):
    for i in range(n):
        if x[i] == n:
            y = 1
            return y
print(find(lista,3,9))

##Poner nombres que signifiquen algo.
    
