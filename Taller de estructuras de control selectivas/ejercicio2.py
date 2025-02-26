sueldo_trabajador=int(input("ingrese sueldo (COP):"))

if  sueldo_trabajador < 900000:
    aumento = sueldo_trabajador* 0.15
else: 
    aumento= sueldo_trabajador* 0.12

nuevo_sueldo= sueldo_trabajador + aumento

print("el nuevo sueldo del trabajador es(COP)", nuevo_sueldo)