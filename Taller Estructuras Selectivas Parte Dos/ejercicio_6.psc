Algoritmo ejercicio_6
    Escribir "Ingrese un a�o:" 
    Leer a�o
    Si (a�o %4 = 0 Y a�o % 100 <>0) O (a�o %400 = 0) Entonces
        Escribir "Es bisiesto"
    Sino
        Escribir "No es bisiesto"
    FinSi
FinAlgoritmo