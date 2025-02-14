Algoritmo ejercicio_21_computadores
	
	escribir "Ingrese el precio de contado (P) del computador en COP: "
    Leer P
    Escribir "Ingrese el valor de la cuota (T) en COP: "
    Leer T
    

    totalCuotas <- 12 * T
    recargo <- totalCuotas - P
    porcentajeRecargo <- (recargo / P) * 100
    
   
    Escribir "Precio de contado: ", P, " COP"
    Escribir "Total a pagar en 12 cuotas: ", totalCuotas, " COP"
    Escribir "Recargo total: ", recargo, " COP"
    Escribir "Porcentaje de recargo: ", porcentajeRecargo, " %"
	
FinAlgoritmo
