correo = input("Ingrese su correo.")
def first_ver(correo):
    count_a = 0
    count_b = 0
    verification = True

    for i in range(len(correo)):
        if correo[i] == "@":
            count_a += 1
        if correo[i] == " ":
            verification == False
            print("Correo invalido. Hay espacios.")

        if correo[i] == ("_" or "-"):
            count_b += 1
    
    if count_a > 1:
        verification = False
    if count_b < 1:
        verification = False
    
    return verification
    
print(first_ver(correo))
    
    
    
