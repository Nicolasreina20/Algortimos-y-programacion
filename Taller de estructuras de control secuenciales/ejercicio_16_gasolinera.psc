Algoritmo ejercicio_16_gasolinera
	// Dato 
    precioLitro = 50000
    
    Escribir "Ingrese la cantidad de galones surtidos: "
    Leer galones
    
    litros <- galones * 3.785
    
    totalAPagar <- litros * precioLitro
    
    Escribir "Litros surtidos: ", litros
    Escribir "Total a pagar (COP): ", totalAPagar
	
FinAlgoritmo
