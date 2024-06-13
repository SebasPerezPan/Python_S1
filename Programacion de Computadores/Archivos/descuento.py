a = int(input("Cantidad de productos.\n"))
b = float(input("Valor de unidad del producto:\n"))
c = float(a*b)
iva = 1.19
if a >= 48:
    c = (c * 0.9) * iva
elif 30 < a <= 47 and a >= 1:
    c = (c * 0.97) * iva
elif a < 1:
    print("La transaccion carece de datos suficientes.")
else:
    c = c * iva

print(f"El valor final por la compra de {a} articulos a ${b} es de $ {c:,.2f} iva incluido.") 
