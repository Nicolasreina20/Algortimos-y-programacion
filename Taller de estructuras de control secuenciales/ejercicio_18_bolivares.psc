Algoritmo ejercicio_18_bolivares
	
	Escribir "Ingrese el capital prestado (Bolívares): "
    Leer capital
    Escribir "Ingrese el total de intereses pagados : "
    Leer interes
    Escribir "Ingrese el tiempo en años (por ejemplo, 6): "
    Leer tiempo
    
    razonAnual = (interes * 100) / (capital * tiempo)
   
    Escribir "La tasa de interes anual es: ", razonAnual, " %"
FinAlgoritmo
