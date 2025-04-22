cantidad_inicial = int(input("Ingrese la cantidad de inventario inicial: "))
productos_recibidos = int(input("Ingrese la cantidad de productos recibidos: "))
productos_vendidos = int(input("Ingrese la cantidad de productos vendidos: "))

inventario_actual = (productos_recibidos + cantidad_inicial) - productos_vendidos

print(f"Cantidad inicial: {cantidad_inicial}")
print(f"Productos recibidos: {productos_recibidos}")
print(f"Productos vendidos: {productos_vendidos}")
print(f"Inventario actual: {inventario_actual}")
