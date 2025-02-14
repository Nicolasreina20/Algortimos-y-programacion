Algoritmo ejercicio_19_agricultor
	
	
    Escribir "Ingrese la cantidad total de naranjas : "
    Leer totaldenaranjas
    Escribir "Ingrese el costo (Bs.) por docena: "
    Leer docena
    Escribir "Ingrese el ingreso total tras la venta: "
    Leer venta
    
    costoCompra <- ( totaldenaranjas / 12) * docena
    ganancia <- venta - costoCompra
    porcentajeGanancia <- (ganancia / costoCompra) * 100
    

    Escribir "El costo de compra fue: ", costoCompra, " Bs."
    Escribir "La ganancia obtenida fue: ", ganancia, " Bs."
    Escribir "El porcentaje de ganancia es: ", porcentajeGanancia, "%"
	
FinAlgoritmo
