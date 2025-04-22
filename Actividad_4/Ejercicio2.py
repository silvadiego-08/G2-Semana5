import datetime as dt
fecha_ingreso =input("Fecha de ingreso YYYY-MM-DD: ")
fecha_ingreso = dt.datetime.strptime(fecha_ingreso, "%Y-%m-%d").date()
fecha_actual = dt.datetime.now()

dias = (fecha_actual - fecha_ingreso).days
print (fecha_actual)
print (fecha_ingreso)
print ("dias", dias)

if dias > 30:
    print("Cuenta inactiva")