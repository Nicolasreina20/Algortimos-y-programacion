ventas_dept1=int(input("ingrese la ventas dept1:"))
ventas_dept2=int(input("ingrese las ventas dept2:"))
ventas_dept3=int(input("ingrese las ventas dept3:"))

sueldo_empleados=int(input("ingrese sueldo de empleados:"))
 

if ventas_dept1 > 0.33:
   pago_extradept1= ventas_dept1 * 0.20
if ventas_dept2 > 0.33:
   pago_extradept2= ventas_dept2 * 0.20
if ventas_dept3 > 0.33:
   pago_extradept3= ventas_dept3 * 0.20

print("el nuevo sueldo de los empleados dept1 es", pago_extradept1)
print("el nuevo sueldo de los empleados dept2 es", pago_extradept2)
print("el nuevo sueldo de los empleados dept3 es", pago_extradept3)