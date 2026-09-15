from celular import Celular  # Traemos la clase del otro archivo

# Ejecución principal con menú interactivo


def main():

    print("POO de un Celular")
    marca = input("Introduce la marca de tu celular ")
    modelo = input("Introduce el modelo ")
    obj = Celular(marca, modelo)
    opcion = -1  # Inicializamos la variable de control
    while opcion != 0:
        print("\nOpciones:")
        print("1. Agregar saldo")
        print("2. Mostrar saldo")
        print("3. Mostrar Informacion de tu celular")
        print("0. Salir")
        try:
            opcion = int(input("\nElige una opción: "))
            # Reemplazamos el switch de C# por el match-case de Python 3.10+
            match opcion:
                case 1:
                    print("Ingresa el saldo a agregar:")
                    saldo = int(input())
                    obj.agregarSaldo(saldo)
                    print("Saldo agregado con éxito")
                case 2:
                    print(f"Tu saldo actual es {obj.obtenerSaldo()}")
                case 3:
                    print(obj.mostrarInfo())
                case 0:
                    print("¡Adios !!! ")
                case _:  # Equivalente a default
                    print("Opción no válida")
        except ValueError:
            print("Error: Por favor ingresa un numero entero valido.")


if __name__ == "__main__":
    main()
