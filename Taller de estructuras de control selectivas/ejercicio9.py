monto_compra = float(input("Ingrese el monto de la compra: "))
if monto_compra < 50000:
    descuento = 0
elif monto_compra <= 100000:
    descuento = 0.05
elif monto_compra <= 700000:
    descuento = 0.11
elif monto_compra <= 1500000:
    descuento = 0.18
else:
    descuento = 0.25

descuento_aplicado = monto_compra * descuento
monto_final = monto_compra - descuento_aplicado
print(f"Descuento: {descuento_aplicado}, Monto a pagar: {monto_final}")
