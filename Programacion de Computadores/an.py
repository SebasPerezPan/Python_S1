##a

print("26")

n_veces = int(input("Cantidad de veces."))
b = 10
r = 1
exp = 0
f = 0
for i in range (1, n_veces):
    
    a = b**i
    r = a + r
    f += r

f += 1
print(f)


## b

a = int(input("Numero."))
b = 0

for i in range (1,a):
    if a % i == 0:
        b += i
        print(i)

if a == b:
    print("Es perfecto.")
else:
    print("No es perfecto.")
