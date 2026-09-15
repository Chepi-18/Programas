def ejecutar_comando(comando):
    match comando:
        case "iniciar":
            print("El sistema está arrancando ... ")

        case "pausar":
            print("Sistema en pausa.")

        case "detener":
            print("Apagando el sistema ... ")

        case _:
            # El guion bajo (_) es el comodín. Funciona como el 'default'.
            # Atrapa cualquier cosa que no coincida con los casos de arriba
            print("Error: Comando no reconocido.")


# Probamos la función
ejecutar_comando("iniciar")
ejecutar_comando("saltar")
