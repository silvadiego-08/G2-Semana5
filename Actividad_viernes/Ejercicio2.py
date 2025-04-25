sueldo = float(input("Introduce el sueldo: "))
bono = 0
if sueldo >3000:
    bono = sueldo * 0.10
elif sueldo > 1500 and sueldo <= 3000:
    bono = sueldo * 0.05
else:
    bono = 0

print(f"El sueldo es: {sueldo:.2f}")
print(f"El bono es: {bono:.2f}")
print ((f"Salario total es {sueldo + bono:.2f}"))