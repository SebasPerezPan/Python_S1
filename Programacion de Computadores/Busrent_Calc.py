print("Bienvenido a la Calculadora de ganancia de Transmillar!")

bus_driver = int(100000)
bus_kilometer = int(500)
diesel = int(10000)
diesel_kilometer = int(10)

distance = int(input("Cuantos kilometros se recorrieron en el viaje?\n"))
print("Respecto al horario normal, donde el valor del ticket es el regular.\n")
reg_ord = int(input("Cuantos boletos ordinarios fueron vendidos?"))
reg_old = int(input("Cuantos boletos para la tercera edad fueron vendidos?"))
reg_std = int(input("Cuantos boletos para estudiantes fueron vendidos?"))
reg_pub = int(input("Cuantos boletos para la fuerza publica fueron vendidos?"))

reg_price_old = 2000 
reg_price_std = 2100  
reg_price_ord = 3000
reg_price_pub= 1500

reg_total = reg_old*reg_price_old + reg_std*reg_price_std + reg_ord*reg_price_ord + reg_pub*reg_price_pub
reg_qa = reg_old + reg_std + reg_ord + reg_pub
print(f"Total de boletos vendidos: {reg_qa}./n Valor recaudado: {reg_total}")
print("\nRespecto al horario valle, donde el valor del ticket disminuye 30%.\n")
 
vall_ord = int(input("Cuantos boletos ordinarios fueron vendidos?"))
vall_old = int(input("Cuantos boletos para la tercera fueron vendidos?"))
vall_std = int(input("Cuantos boletos para estudiantes fueron vendidos?"))
vall_pub = int(input("Cuantos boletos para fuerza publica fueron vendidos?"))

vall_price_old = reg_price_old * 0.70
vall_price_std = reg_price_std *0.70  
vall_price_ord = reg_price_ord *0.70
vall_price_pub= reg_price_pub *0.70

vall_total = (vall_old*vall_price_old + vall_std*vall_price_std + vall_ord*vall_price_ord + vall_pub*vall_price_pub)
vall_qa = vall_old + vall_std + vall_ord + vall_pub

print("Respecto al horario pico, donde el valor del ticket aumenta 15%.\n")

rush_ord = int(input("Cuantos boletos ordinarios fueron vendidos?"))
rush_old = int(input("Cuantos boletos para la tercera fueron vendidos?"))
rush_std = int(input("Cuantos boletos para estudiantes fueron vendidos?"))
rush_pub = int(input("Cuantos boletos para fuerza publica fueron vendidos?"))

rush_price_old = reg_price_old * 1.15
rush_price_std = reg_price_std * 1.15 
rush_price_ord = reg_price_ord * 1.15
rush_price_pub= reg_price_pub * 1.15

rush_total = rush_old*rush_price_old + rush_std*rush_price_std + rush_ord*rush_price_ord + rush_pub*rush_price_pub
rush_qa = rush_old + rush_std + rush_ord + rush_pub

tickets = reg_qa + rush_qa + vall_qa
earning = rush_total + vall_total + reg_total
trip_cost = (distance*bus_kilometer + bus_driver) + (distance*diesel*diesel_kilometer)

totalearn = earning - trip_cost
totalearn_per = (totalearn/earning)*100
print(f"El viaje tuvo una duracion de {distance} km, y un costo total de ${trip_cost}.\n El total de boletos vendidos fue de {tickets}, de lo siguiente tenemos que en horas regulares fueron vendidos {reg_qa}, en hora valle {vall_qa} y en hora pico {rush_qa}. Lo recaudado en ticketeria fue de ${earning}, dejandonos una ganancia de {totalearn}. El porcentaje ganado fue de {totalearn_per} %")