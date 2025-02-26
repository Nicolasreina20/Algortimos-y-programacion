fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm): ")
dia, mes= [int(x) for x in fecha_nacimiento.split("/")]

signos = [
    ("Capricornio", (22, 12), (20, 1)),
    ("Acuario", (21, 1), (19, 2)),
    ("Piscis", (20, 2), (19, 3)),
    ("Aries", (21, 3), (20, 4)),
    ("Tauro", (21, 4), (21, 5)),
    ("Géminis", (22, 5), (21, 6)),
    ("Cáncer", (22, 6), (22, 7)),
    ("Leo", (23, 7), (23, 8)),
    ("Virgo", (24, 8), (22, 9)),
    ("Libra", (23, 9), (22, 10)),
    ("Escorpión", (23, 10), (21, 11)),
    ("Sagitario", (22, 11), (21, 12))
]

signo_zodiaco = ""
for signo, (dia_inicio, mes_inicio), (dia_fin, mes_fin) in signos:
    if (mes == mes_inicio and dia >= dia_inicio) or (mes == mes_fin and dia <= dia_fin):
        signo_zodiaco = signo


print(f"Su signo zodiacal es: {signo_zodiaco}")

