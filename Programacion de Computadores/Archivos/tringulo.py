print("Triangulo")

a = int(input("Ingresar lado a"))
b = int(input("Ingresar lado b"))
c = int(input("Ingresar lado c"))

if a == b and b == c: 
    print("Es equilatero.")
    
elif a == b or b == c:
    print("Es isoceles.")
    
else: 
    print("Es escaleno.")
