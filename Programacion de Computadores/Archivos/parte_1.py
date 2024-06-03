# Punto y Fama.

# Jugador A: Palabra. 
# Jugador B: Adivina.

# Resultado de Intento. Recordar Intento en una lista.

import random
print("Punto y Fama.")
value_write = []

def word_record():
    with open("punto_fama.txt", "w") as writer:
        count = 0   
        while count < 3:
            value_ = input(f"Choose {3 - count} numbers:")
            count += 1
            value_write.append(value_)
        writer.write(str(value_write))
    writer.close()

def game():
    with open("punto_fama.txt", "r") as reader:
        options =[]

        for line in reader:
            campos = line.split(",")
            opt_a = campos[0]
            opt_b = campos[1]
            opt_c = campos[2]
            options.append([opt_a,opt_b,opt_c])
    reader.close()
    return options

word_record()
options = game()
tries = 0
print(options)
answer = str(options[0][random.randint(0,2)])
print(answer)
while tries < 10:
    choose = input("Choose a number:")
    if choose[0] == answer[0] or choose[1] == answer[1]:
        print("Fama!")
    elif choose[0] == answer[0] and choose[1] == answer[1]:
        print("You win!")
        tries = 11
    elif choose[1] == answer[0] and choose[0] == answer[1]:
        print("Punto!")
    else:
        print(choose[0])
        print("Try again.")
    tries += 1