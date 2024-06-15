lista_xd = []
for sum in range(2,100011):
    d = 2
    while sum % d != 0:
        d += 1 

    if d == sum:
        lista_xd.append(sum)

print(f"los numeros primos son: \n{lista_xd}")