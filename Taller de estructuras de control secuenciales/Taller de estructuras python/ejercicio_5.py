#Entradas
parcial_1=int(input("ingrese la primera calificacion parcial"))
parcial_2=int(input("ingrese la segunda calificacion parcial"))
parcial_3=int(input("ingrese la tercera calificacion parcial"))
examen_final =int(input("ingrese la calificacion del examen final"))
trabajo_final=int(input("ingrese calificacion del trabajo final"))
#Caja negra
promedio_parciales= (parcial_1 + parcial_2 + parcial_3 )/3
calificacion_final=(promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final* 0.15)

#Salida
print ("la calificacion final es", calificacion_final)

