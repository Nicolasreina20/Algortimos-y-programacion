lectura_anterior = int(input("Ingrese la lectura anterior del medidor (en Kwh): "))
lectura_actual = int(input("Ingrese la lectura actual del medidor (en Kwh): "))

consumo = lectura_actual - lectura_anterior

if consumo <= 100:
    costo_kwh = 4600
elif consumo <= 300:
    costo_kwh = 80000
elif consumo <= 500:
    costo_kwh = 100000
else:
    costo_kwh = 120000

monto_pagar = consumo * costo_kwh

print("Consumo total:", consumo ("Kwh"))
print("Monto a pagar:", monto_pagar ("COP"))
