import random
import  sys

if __name__ == '__main__':
    n = int(random.randint(1,2))
    
for number in range (n):
    print(n)

list = list(range(1,101))
print(list)
#En python el sizeof es Getsizeof. 
a = sys.getsizeof(list)
print(a)

prime = []

for number in list:
    if number == 2 or number == 3 or number == 5:
        print(f'El numero {number} es primo')
        prime.append(number)
    elif number == 1 or number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
        print(f'El numero {number} no es primo')
    else:
        print(f"El numero {number} es primo")
        prime.append(number)

print(prime)