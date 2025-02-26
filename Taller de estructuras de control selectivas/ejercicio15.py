edad = float(input("Ingrese la edad en años: "))
sexo = input("Ingrese el sexo (M/F): ")
nivel_hemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))

if edad <= 0.083:  # 0 a 1 mes
    limite_inferior, limite_superior = 13, 26
elif edad <= 0.5:  # Más de 1 mes hasta 6 meses
    limite_inferior, limite_superior = 10, 18
elif edad <= 1:  # Más de 6 meses hasta 12 meses
    limite_inferior, limite_superior = 11, 15
elif edad <= 5:  # Más de 1 año hasta 5 años
    limite_inferior, limite_superior = 11.5, 15
elif edad <= 10:  # Más de 5 años hasta 10 años
    limite_inferior, limite_superior = 12.6, 15.5
elif edad <= 15:  # Más de 10 años hasta 15 años
    limite_inferior, limite_superior = 13, 15.5
else:
    if sexo == "F":  # Mujeres mayores de 15 años
        limite_inferior, limite_superior = 12, 16
    elif sexo == "M":  # Hombres mayores de 15 años
        limite_inferior, limite_superior = 14, 18
    else:
        print("Sexo no válido. Use 'M' para masculino o 'F' para femenino.")
        

if nivel_hemoglobina < limite_inferior:
    resultado = "Positivo para anemia"
else:
    resultado = "Negativo para anemia"

print("El resultado del diagnóstico es:",resultado)
