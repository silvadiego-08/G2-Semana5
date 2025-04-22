litros_mes = float(input("Ingrese la cantidad de litros consumidos en el mes: "))
cantidad_personas = int(input("Ingrese la cantidad de personas: "))

mensual_por_persona = litros_mes / cantidad_personas
consumo_diario = mensual_por_persona / 30

print(f"""Litros consumidos en el mes: {litros_mes:.2f} L
Cantidad de personas: {cantidad_personas} personas
Consumo mensual por persona: {mensual_por_persona:.2f} L
Consumo_diario por persona: {consumo_diario:.2f} L""")
