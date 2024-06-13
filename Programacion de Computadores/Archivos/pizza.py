print("Construye tu masa para pizza")

a = int(input("Para empezar, necesitamos elegir la harina. \n Selecciona una opcion: \n 1. Harina de Trigo. \n 2. Harina de Avena"))

if a == 1:
    print("Genial! La harina de trigo es perfecta para la pizza")
elif a == 2:
    print("Que extraña decision. Usualmente se usan harinas de trigo... Pero continuemos!")
else:
    print("Entonces nada, esta bien...")

b = int(input("Lo que sigue es el metodo de levado, necesitamos elegir entonces el ingrediente. \n Selecciona una opcion: \n 1. Levadura seca. \n 2. Polvo para hornear."))

if b == 1 and a == 1:
    print("Genial, por ahora, vamos siguiendo el proceso correcto!")
elif b == 2 and a == 1:
    print("No es la mejor de las opciones... pero tal vez no teniamos sufiente levadura, continuemos!")
elif b == 1 and  a == 2:
    print("Genial, es la opcion perfecta!")
elif b == 2 and a == 2:
    print("La receta era masa para pizza, no pastel...")
else:
    print("Entonces nada, está bien...")
    
c = int(input("Lo que sigue es esperar a que leve. ¿Cuanto quieres esperar? \n Selecciona una opcion: \n 1. Media hora. \n 2. 6 horas."))

if c >= 3 and c == a and c == b or c <= 0 and c == a and c == b:
    print("Parece que nos faltó una variable.")
elif c == 1 and c == b and b == a:
    print("La masa quedó perfecta!")
elif c == 2 and c == b and b == a:
    print("La masa no quedo muy bien para la pizza... Por otro lado, con un par de huevos podriamos hacer pastel! ")
elif a == 1 and b == a and c == 2:
    print("No levó demasiado, pero si suficiente, genial!")
elif a == b and c == 1:
    print("Fue el tiempo de levado suficiente, pero lastimosamente la mezcla no fue la ideal. :c ")
elif b == 2 and b == c and a == 1:
    print("La masa no levó bien, la pizza puede quedar un poco dura, pero al menos no usaste harina de trigo.")
elif b == c and a == 2:
    print("Bueno, no fue la harina ideal, pero levó, la masa se ve decente, yo creo que va a quedar una buena pizza.")
elif a == 1 and a == c and b == 2:
    print("No levó tan bien por el polvo para hornear, pero bueno, va a ser comestible. ")
elif a == c and b == 1:
    print("Alcanzo a levar un poco, no creo que sea apta para pizza, pero podrias intentar algun pan, busca en gugol. ")
