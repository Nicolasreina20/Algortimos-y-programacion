
A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
C = float(input("Ingrese el valor de C: "))

discriminante = B**2 - 4*A*C

if discriminante > 0:
    X1 = (-B + (discriminante)) / (2*A)
    X2 = (-B - (discriminante)) / (2*A)
    print("Las soluciones son X1 =",  X1)
    print("Las soluciones son X2 =",  X2)
elif discriminante == 0:
    X = -B / (2*A)
    print("La única solución es X =", X)
else:
    print("No tiene solución en los números reales.")