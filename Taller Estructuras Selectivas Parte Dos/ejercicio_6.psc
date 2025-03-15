Algoritmo ejercicio_6
    Escribir "Ingrese un año:" 
    Leer año
    Si (año %4 = 0 Y año % 100 <>0) O (año %400 = 0) Entonces
        Escribir "Es bisiesto"
    Sino
        Escribir "No es bisiesto"
    FinSi
FinAlgoritmo