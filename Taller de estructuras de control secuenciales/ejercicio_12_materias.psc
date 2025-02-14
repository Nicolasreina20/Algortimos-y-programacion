Algoritmo ejercicio_12_materias
	Escribir "Ingrese la nota del examen de Matematicas: "
    Leer examMate
    Escribir "Ingrese las tres notas de tareas de Matematicas: "
    Leer t1Mate
    Leer t2Mate
    Leer t3Mate
    
    promTareasMate <- (t1Mate + t2Mate + t3Mate) / 3
    finalMate <- examMate * 0.90 + promTareasMate * 0.10
    
    // FÍSICA
    Escribir "Ingrese la nota del examen de Fisica: "
    Leer examFisi
    Escribir "Ingrese las dos notas de tareas de Fisica: "
    Leer t1Fisi
    Leer t2Fisi
    
    promTareasFisi <- (t1Fisi + t2Fisi) / 2
    finalFisi <- examFisi * 0.80 + promTareasFisi * 0.20
    
    // QUÍMICA
    Escribir "Ingrese la nota del examen de Quimica: "
    Leer examQuimi
    Escribir "Ingrese las tres notas de tareas de Quimica: "
    Leer t1Quimi
    Leer t2Quimi
    Leer t3Quimi
    
    promTareasQuimi <- (t1Quimi + t2Quimi + t3Quimi) / 3
    finalQuimi <- examQuimi * 0.85 + promTareasQuimi * 0.15
    
    // PROMEDIO GENERAL
    promedioGeneral <- (finalMate + finalFisi + finalQuimi) / 3
    
    // SALIDAS
    Escribir "---------- RESULTADOS ----------"
    Escribir "Promedio final en Matematicas: ", finalMate
    Escribir "Promedio final en Fisica: ", finalFisi
    Escribir "Promedio final en Quimica: ", finalQuimi
    Escribir "Promedio general de las tres materias: ", promedioGeneral
	
FinAlgoritmo
