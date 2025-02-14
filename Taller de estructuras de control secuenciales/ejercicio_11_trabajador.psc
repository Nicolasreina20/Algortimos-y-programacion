Algoritmo ejercicio_11_trabajador
	Escribir "ingrese nombre de trabajador:"
	Leer nombre
	Escribir "ingrese numero de horas normales trabajadas:"
	Leer horasnormales
	Escribir "Ingrese el pago por hora normal: "
	Leer pagohora
	Escribir "Ingrese el numero de horas extras trabajadas: "
	Leer horasextras
	Escribir "Ingrese el numero de hijos del trabajador: "
	Leer numerohijos
	
	
	// Sueldo base solo horas normales
	sueldoBase <- horasnormales * pagohora
	
	//Pago por horas extras 
	pagohorasextras <- horasextras * pagohora * 1.25
	
	// Deducciones
	deduccionPagoForzoso <- sueldoBase * 0.05
	deduccionPoliticaHabitacional <- sueldoBase * 0.02
	deduccionCajaAhorro <- sueldoBase * 0.07
	totalDeducciones <- deduccionPagoForzoso + deduccionPoliticaHabitacional + deduccionCajaAhorro
	
	//  Asignaciones fijas y por hijo
	totalAsignaciones <- 250000 + (173000 * numeroHijos) + 180000
	
	// Cálculo del sueldo neto
	sueldoNeto <- (sueldoBase + pagoHorasExtras) - totalDeducciones + totalAsignaciones
	
	// SALIDAS
	Escribir "---------- RESULTADOS ----------"
	Escribir "Trabajador: ", nombre
	Escribir "Asignaciones totales: ", totalAsignaciones, " COP"
	Escribir "Deducciones totales: ", totalDeducciones, " COP"
	Escribir "Sueldo neto a recibir: ", sueldoNeto, " COP"
FinAlgoritmo

