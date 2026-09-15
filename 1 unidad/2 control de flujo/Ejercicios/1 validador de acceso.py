contrasena = "PelaPapas"
intentos = 2
while intentos >= 0:
    intento = input("Ingrese la contraseña: ")
    if intento == contrasena:
        print(
            f"La contraseña es correcta, te quedaron {intentos} intentos sin usar. Biembenido"
        )
        intentos = -1
    else:
        print(f"Contraseña incorrecta, te quedan {intentos} intentos")
        intentos -= 1
