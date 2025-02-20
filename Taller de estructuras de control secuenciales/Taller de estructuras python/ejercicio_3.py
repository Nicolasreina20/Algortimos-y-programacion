#Entradas
Sueldo_base=int(input("ingrese sueldo base:"))
venta_1=int(input("ingrese venta 1:"))
venta_2=int(input("ingrese venta 2:"))
venta_3=int(input("ingrese venta 3:"))
#Caja negra
dinero_ventas= (venta_1 + venta_2 + venta_3) 
dinero_comision=(dinero_ventas*(0.10))
sueldo_total=(Sueldo_base + dinero_comision)
#Salida
print ("total comision es", dinero_comision)
print ("sueldo total", sueldo_total)