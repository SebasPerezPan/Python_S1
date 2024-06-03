cadena = input("Ingrese una palabra.")
resultado = []
for i in range(len(cadena)):
    resultado.append((cadena[len(cadena)- 1 - i]))
    print((resultado[i]), end="" )

## Contador de caracteres 
print("\n")

frase = input("Ingrese una palabra")
frase_ = frase.lower()

def contador(letra , conjunto_str):
    contador = 0
    for i in range (len(conjunto_str)):
        if letra in conjunto_str[i]:
            contador += 1
    print(f"la letra {letra} esta:{contador}")
frase__ = []
fras = []
for i in range (len(frase_)):
    if frase_[i] not in frase__: 
        contador(frase_[i],frase_)
        fras.append(frase_[i])
    frase__.append((frase_[i]))

 # Online Python compiler (interpreter) to run Python online.

for i in range(len(fras)):
    print(fras[i], end="")
