Distancia=int(input("ingrese total de distancia Km:"))

if Distancia <= 300 :
    total_pagar= Distancia * 50.000
elif Distancia <= 1000:   
      total_pagar= Distancia * 70.000 + (Distancia - 300) * 30.000
else: 
     total_pagar= 150.000 + (Distancia - 1000) * 9.000

print("el total a pagar es:", total_pagar)


