Algoritmo ejercicio_6_hombres
	//entradas
	Escribir "numero de mujeres:"
	Leer mujeres
	Escribir "numero de hombres:"
	Leer hombres
	//caja hombres
	total_estudiantes<-mujeres+hombres
	porMujeres<-(mujeres/total_estudiantes*100)
	porHombres<-(hombres/total_estudiantes*100)
	//salidas
	Escribir "porcentaje Hombres", porHombres, "%"
	Escribir "porcentaje Mujeres", porMujeres, "%"
FinAlgoritmo
