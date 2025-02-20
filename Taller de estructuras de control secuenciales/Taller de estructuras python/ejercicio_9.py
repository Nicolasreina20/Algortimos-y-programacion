#Entradas
Horas=int(input("ingrese horas trabajadas:"))
Precio=int(input("ingrese precio de hora:"))
#Caja negra
Salario= (Horas * Precio )
Descuento=(Salario * 0.20)
Sueldo_total=(Salario - Descuento)
#Salida
print ("Salario base es", Salario)
print ("Descuento por impuestos", Descuento)
print ("El salario neto es", Sueldo_total)