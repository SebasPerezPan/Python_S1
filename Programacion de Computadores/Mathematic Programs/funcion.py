
def prime(i):
    d = 2
    while i % d != 0:
                d += 1
    if d == i:
        print(f"{i} es primo.") 

def rango (n,k):
    for i in range(n,k):
        prime(i)

rango(2,1230)