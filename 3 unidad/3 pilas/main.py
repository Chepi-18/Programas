from pila import Pila

if __name__ == "__main__":
    lista1 = Pila()
    opcion = -1

    while opcion != 0:
        print("\n --- Operaciones --- ")
        print("1. Agregar elemento")
        print("2. Verificar si esta vacia")
        print("3. Eliminar elemento")
        print("4. Mostrar Lista")
        print("5. Promendio")
        print("0. Salir")
        try:
            opcion = int(input("\nElige una operación: "))
            match opcion:
                case 1:
                    dato = int(input("Dame un número para insertarlo al inicio: "))
                    lista1.push(dato)
                case 2:
                    lista1.is_empty()
                case 3:
                    lista1.pop()
                case 4:
                    lista1.imprimir()
                case 0:
                    print("Saliendo de las operaciones ... ")
                case _:
                    print(
                        "Error: Opcion no valida. Por favor, elige un número del 0 al 4."
                    )
        except ValueError:
            print("Error de formato: Debes ingresar un valor numerico valido.")
