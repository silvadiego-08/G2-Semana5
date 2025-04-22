Capital_inicial = int(input("Ingrese el capital inicial: "))
tasa_interes_anual = float(input("Ingrese la tasa de interes anual en porcentaje: "))
años = int(input("Ingrese el numero de años: "))

tasa_interes_anual_decimal = tasa_interes_anual / 100
monto_final = (1+tasa_interes_anual_decimal) ** años * Capital_inicial

interes_ganado = monto_final - Capital_inicial
print(f"""Capital inicial: {Capital_inicial}
tasa interes anual: {tasa_interes_anual}
Años: {años}""")