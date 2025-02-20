#Entradas
Metros=int(input("ingrese cantidad de metros"))
#Caja negra
Pulgadas_totales=(Metros * 39.27)
pies=(Pulgadas_totales/12)
Pulgadas=(Pulgadas_totales-(pies*12))
#Salida
print ("la cantidad equivale a", pies, "pies y", Pulgadas,"Pulgadas")