dividiendo=int(input())
divisor=int(input())

cociente=0
residuo= dividiendo
if divisor==0 :

    while dividiendo >=divisor:
        dividiendo= divisor - dividiendo 
        cociente= cociente + 1
        residuo= cociente
        print("Cociente:",cociente)
        print("Residuo:",divisor)