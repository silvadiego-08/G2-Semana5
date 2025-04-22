distancia_recorrida = int(input("Ingrese la distancia recorrida en km: "))
litros_consumidos = int(input("Ingrese la cantidad de litros consumidos: "))

rendimiento = distancia_recorrida / litros_consumidos

precio_gasolina = 48.98

total_en_combustible = litros_consumidos * precio_gasolina

print(f"""Distancia recorrida: {distancia_recorrida} km
Litros consumidos: {litros_consumidos} L
Rendimiento: {rendimiento:.2f} km/L
Total en combustible: ${total_en_combustible:.2f}""")
