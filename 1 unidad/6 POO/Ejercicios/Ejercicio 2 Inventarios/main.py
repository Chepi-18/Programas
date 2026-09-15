from producto import Producto


def main():

    Nombre = input("Introduce la Nombre del producto ")
    Precio = float(input("Introduce el Precio del producto "))
    Stock = int(input("Intoduce el stock del producto "))
    obj = Producto(Nombre, Precio, Stock)
    opcion = -1  # Inicializamos la variable de control
    while opcion != 0:
        print("\nOpciones:")
        print("1. Vender")
        print("2. Mostrar informacion del producto")
        print("3. Actualizar precio del producto")
        print("4. Surtir stock del producto")
        print("0. Salir")
        try:
            opcion = int(input("\nElige una opción: "))
            match opcion:
                case 1:
                    cantidad = int(input("Ingresa la cantidad del producto a vender: "))
                    print(obj.vender(cantidad))
                case 2:
                    print(obj.mostrarInfo())
                case 3:
                    print(f"El precio actual del producto es de {obj.precio}")
                    try:
                        nuevoPrecio = float(input("cual sera el nuevo precio? "))
                        print(obj.actualizarPrecio(nuevoPrecio))
                    except TypeError:
                        return "El tipo de dato es incompatible: Debes ingresar un valor numerico valido."

                case 4:
                    try:
                        stockNuevo = int(input("cualnto stock nuevo agregas? "))
                        print(obj.surtit(stockNuevo))
                    except TypeError:
                        return "El tipo de dato es incompatible: Debes ingresar un valor numerico valido."
                case 0:
                    print("¡Adios !!! ")
                case _:
                    print("Opción no válida")
        except ValueError:
            print("Error: Por favor ingresa un numero entero valido.")


if __name__ == "__main__":
    main()
