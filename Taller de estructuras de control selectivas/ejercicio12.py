cantidad = int(input("Ingrese la cantidad en COP: "))

billetes_monedas = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]
resultado = []

for valor in billetes_monedas:
    if cantidad >= valor:
        cantidad_billetes = cantidad // valor
        cantidad %= valor
        for _ in range(cantidad_billetes):
            resultado.append(valor)

print("Desglose en billetes y monedas: ", ", ".join(map(str, resultado)))