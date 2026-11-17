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
        print("6. Tamaño")
        print("7. Busqueda de un elemento")
        print("8. Obtener Tope sin eliminar")
        print("9. Limpiar lista")
        print("10. Ver lista kamikase")
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
                case 5:
                    lista1.promedio()
                case 6:
                    lista1.tamaño()
                case 7:
                    referencia = int(input("Dame un número para buscarlo: "))
                    lista1.busqueda(referencia)
                case 8:
                    lista1.tope_sin_eliminar()
                case 9:
                    lista1.eliminar_pila()
                case 10:
                    lista1.Lectura_kamikase()
                case 0:
                    print("Saliendo de las operaciones ... ")
                case _:
                    print(
                        "Error: Opcion no valida. Por favor, elige un número del 0 al 10."
                    )
        except ValueError:
            print("Error de formato: Debes ingresar un valor numerico valido.")
