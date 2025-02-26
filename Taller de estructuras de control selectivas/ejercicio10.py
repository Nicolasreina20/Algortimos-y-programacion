categoria= int(input("Ingrese la categoría del trabajador (1-5): "))
sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador: "))

aumentos = {
        1: 0.10,
        2: 0.15,
        3: 0.20,
        4: 0.40,
        5: 0.60
    }
   
if categoria in aumentos:
        aumento = sueldo_bruto * aumentos[categoria]
        nuevo_sueldo = sueldo_bruto + aumento
  
    

print("Categoría del trabajador:", categoria)
print("Nuevo sueldo bruto:", nuevo_sueldo )

