a = int(input("Agregue el numero a descomponer."))

b = a

c = False

d = 2

divisores = [1]

while b != 1:
    if a / d == 1:
        c = True
        
    if b % d == 0:
        b = b / d
        divisores.append(d)
        d = 2
    else:
        d += 1


print(f"El numero {a} debe ser dividido por {divisores}")
if c == True:
    print(f"{a} es un numero primo.")
else:
    print(f"{a} no es un numero primo.")

  
  
s = int(input("Agregue el numero a descomponer."))

p = s

r = False

d = 2

divisoresb = [1]

while p != 1:
    if s / d == 1:
        c = True
        
    if p % d == 0:
        p = p / d
        divisoresb.append(d)
        d = 2
    else:
        d += 1


print(f"El numero {s} debe ser dividido por {divisoresb}")
if c == True:
    print(f"{s} es un numero primo.")
else:
    print(f"{s} no es un numero primo.")

mcm = set (divisoresb) | set (divisores)

print(mcm)
  
#primos. La logica es que f es el divisor. Mientras que f != n el programa corre, o hasta que descu


for n in range(2,101):
    
    c = True
    f = 2
    while n % f != 0:
        f += 1
    
    if c == False:
        print(f"{n} No es primo")
    elif c == True:
        print(f"{n} Es primo.")
        
  
  
  
  
  
  
    # a = 2
# s = a
# d = 2
# s = []

# while b != 1:
#     if a / d == 1:
#         c = True
        
#     if b % d == 0:
#         b = b / d
#         divisores.append(d)
#         d = 2

# s = range(1,100)
# num_rang = [s]
# prime = []

# for a in s
# while a < 10:
    
#     if b / d == 1:
#         s.append(a)
#         d = 2
#     elif b / d != 1:
#         a = a + 1
#     else:
#         d += 1

# print(s)
