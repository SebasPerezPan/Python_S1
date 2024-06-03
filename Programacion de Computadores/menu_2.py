menu = int(input("Selecciona un programa a ejecutar: 1. Par o impar. 2. Calculadora de descuentos. 3. IMC 4. Temperatura."))

if (menu == 1):
  print("Calculadora de numeros impares")
  num = int(input("Ingrese un numero."))
  if (num%2 == 0):
    print(f"El numero {num} es par")
  elif (num%2 != 0):
    print(f"El numero {num} es impar")
if (menu == 2):
  print("Calculadora de descuentos.")
  precio = int(input("Cual es el valor del producto?"))
  limit = 100
  if (precio >= limit): 
    precio_final = precio * 0.9
  elif (precio < limit):
    precio_final = precio
  print(f"el precio final del producto es de $ {precio_final}")

print("Traductor de Temperatura")
temp = int(input("Ingrese valor de la temperatura"))
measure = input("ingrese C para grados Celsius, o F para grados Farenheit.")

#if (measure != c or measure != C):
