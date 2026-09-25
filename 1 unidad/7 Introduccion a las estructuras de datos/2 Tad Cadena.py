class Cadena:

    def concatenar(self, cadena1: str, cadena2: str) -> str:
        return cadena1 + cadena2

    def longitud(self, cadena: str) -> int:
        return len(cadena)

    def es_vacia(self, cadena: str) -> bool:
        return cadena == ""

    def son_iguales(self, cadena1: str, cadena2: str) -> bool:
        return cadena1 == cadena2


if __name__ == "__main__":
    obj = Cadena()
    opcion = -1
    cad1 = ""
    cad2 = ""
    cad = ""
    while opcion != 0:
        print("\n --- Operaciones --- ")
        print("1. concatenar")
        print("2. longitud")
        print("3. Ver si esta vacia")
        print("4. comparacion")
        print("0. Salir")
        try:
            opcion = int(input("\nElige una operación: "))
            match opcion:
                case 1:
                    print("\n -- concatenar -- ")
                    cad1 = input("Ingrese la primera cadena: ")
                    cad2 = input("Ingrese la segundo cadena: ")
                    print(
                        f"La concatenacion da como resultado: {obj.concatenar(cad1, cad2)}"
                    )
                case 2:
                    print("\n -- longitud -- ")
                    cad = input("Ingrese la cadena de texto: ")
                    print(f"La longitud de la cadena da: {obj.longitud(cad)}")
                case 3:
                    print("\n -- Ver si esta vacia -- ")
                    if obj.es_vacia() == False:
                        print("La cadena esta vacia")
                    else:
                        print("La cadena no esta vacia")
                case 4:
                    print("\n -- comparacion -- ")
                    cad1 = input("Ingrese la primera cadena: ")
                    cad2 = input("Ingrese la segundo cadena: ")
                    if obj.son_iguales == False:
                        print("Las 2 cadenas no son iguales")
                    else:
                        print("Las 2 cadenas son iguales")
                case 0:
                    print("Saliendo de las operaciones ... ")
                case _:
                    print(
                        "Error: Opcion no valida. Por favor, elige un número del 0 al 4."
                    )
        except ValueError:
            print("Error de formato: Debes ingresar un valor numerico valido.")
