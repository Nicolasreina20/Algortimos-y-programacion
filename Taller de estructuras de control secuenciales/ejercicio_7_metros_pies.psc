Algoritmo ejercicio_7_metros_pies
	Escribir "Cantidad en metros: "
	Leer Metros
	PulgadasTotales<- Metros * 39.27
	Pies<-  (PulgadasTotales / 12)
	Pulgadas<-PulgadasTotales-(Pies * 12)
	
	Escribir "La cantidad equivale a: " , Pies, " Pies y ", Pulgadas , " pulgadas "
	
FinAlgoritmo
