print("Calculadora de presupuests investigativos!")

investqu = int(input("Cuántos investigadores van a hacer parte de tu investigación?"))
investho = int(input("Cuánto va a ser el pago estandar por horas de los investigadores?"))
investhwk = int(input("Cuantas horas semanales trabajaran los investigadores?"))
investmo = int(input("Por cuantos meses se extendera el contrato?"))
invest_total = int(investqu*investhwk*(investmo*4)*investho)
print(f"El costo total de los investigadores es de $ {invest_total:,.2f}. ")

assistqu = int(input("Cuántos asistentes van a hacer parte de tu investigación?"))
assistho = int(input("Cuánto va a ser el pago estandar por horas de los asistentes?"))
assistwk = int(input("Cuantas horas semanales trabajaran los asistentes?"))
assistmo = int(input("Por cuantos meses se extendera el contrato?"))
assist_total = int(assistqu*assistho*assistwk*(assistmo*4))
print(f"El costo total de los asistentes es de $ {assist_total:,.2f}. ")

tripq = int(input("Cuantos viajes son requeridos para la investigacion?"))
tripp = int(input("Cuantas personas del equipo tienen que viajar?"))
triph = int(input("Cual es el valor por tiquete?"))
tripd = int(input("Cual es el valor por dia de alojamiento?"))
trip_qahosp = int(input("Cuantos dias planean alojarse en el viaje?"))
trip_total = int((tripp*triph)+(trip_qahosp*tripd)+(tripp*tripd*trip_qahosp))
print(f"El valor gastado en viajes es de $ {trip_total:,.2f}. ")



equipo = int(input("Cual es el valor total de los equipos que van a ser usados en la investigacion?"))
subtotal = trip_total + equipo + assist_total + invest_total
admin = (invest_total +equipo + trip_total)*0.30
subtotala = subtotal + admin
subtotalb = subtotala + subtotala*0.19
print(f"El subtotal de la investigacion es ${subtotal:,.2f}, los costos administrativos seran de ${admin:,.2f}, para un total de ${subtotala:,.2f}, y teniendo en cuenta el iva un total ${subtotalb:,.2f}")
