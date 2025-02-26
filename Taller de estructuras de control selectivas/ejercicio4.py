monto_total=int(input("ingrese monto total (COP):"))

if monto_total > 5000000:
   inversion= monto_total * 0.55
   prestamo= monto_total * 0.33
   Credito= monto_total * 0.15
else:
   inversion= monto_total * 0.70
   prestamo= 0
   Credito= monto_total * 0.30
interes_fabricante=Credito * 0.20

print("Cantidad a invertir de los fondos de empresa",inversion )
print("cantidad a pagar a credito",Credito )
print("Monto a pagar por interes", interes_fabricante)
if prestamo > 0:
   print("Cantidad prestada", prestamo)

