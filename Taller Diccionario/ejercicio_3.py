usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
        "apellido": "Muguruza",
        "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
        "apellido": "Olaizola",
        "password": "123456"
    }
}

intentos = 0
MAX_INTENTOS = 3

while intentos < MAX_INTENTOS:
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario in usuarios and usuarios[usuario]["password"] == contraseña:
        print(f"Bienvenido, {usuarios[usuario]['nombre']} {usuarios[usuario]['apellido']}")
        break
    else:
        print("Usuario o contraseña incorrectos.\n")
        intentos += 1

if intentos == MAX_INTENTOS:
    print("Has superado el número máximo de intentos. Acceso denegado.")