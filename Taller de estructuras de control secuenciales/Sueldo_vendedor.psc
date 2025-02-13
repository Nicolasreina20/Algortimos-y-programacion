Algoritmo Sueldo_vendedor
	
	//entradas
	Escribir "sueldo base:"
	Leer sueldo_base
	Escribir "venta 1:"
	Leer venta1
	Escribir "venta 2:"
	Leer venta2
	Escribir "venta 3:"
	Leer venta3
	//caja negra
	
	dinero_ventas=(venta1+venta2+venta3)
	
	dinero_comision=(dinero_ventas*(0.10))
	
	
	sueldo_total=(sueldo_base+dinero_comision)
	
	//salida
	Escribir "total de comisiones es:", dinero_comision
	Escribir "sueldo total:", sueldo_total
FinAlgoritmo
