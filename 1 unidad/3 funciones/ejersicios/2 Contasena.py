def valida_password(password: str) -> bool:
    if password == "1234":
        print("Bienvenido.")
        return True
    else:
        print("Contraseña no valida.")
        print("Intente de nuevo..")
        return False


contra = str(input("ingrese su contraseña: "))
while valida_password(contra) != True:
    contra = str(input("ingrese su contraseña: "))
