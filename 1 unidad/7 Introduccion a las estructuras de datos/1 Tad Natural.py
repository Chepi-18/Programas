class Natural:
    def sucesion(self, numero: int) -> int:
        return numero + 1

    def suma(self, numero1: int, numero2: int) -> int:
        return numero1 + numero2

    def producto(self, numero1: int, numero2: int) -> int:
        return numero1 * numero2

    def comparacion(self, numero1: int, numero2: int) -> bool:
        return numero1 == numero2


if __name__ == "__main__":
    print("Probando el tad natural")
    print("Valores: 0, 1, 2...")
    print("Operaciones: secesion, suma, producto y comparacion")
    obj = Natural()
    opcion = -1
    num1 = 0
    num2 = 0
    while opcion != 0:
        print("\n --- Operaciones --- ")
        print("1. secesionn")
        print("2. suma")
        print("3. producto")
        print("4. comparacion")
        print("0. Salir")
        try:
            opcion = int(input("\nElige una operación: "))
            match opcion:
                case 1:
                    print("\n -- secesionn -- ")
                    num1 = int(input("ingresa el numero a ver la susecion "))
                    resultado = obj.sucesion(num1)
                    print(f"El resultado es: {resultado}")
                case 2:
                    print("\n -- suma -- ")
                    num1 = int(input("ingresa el primer numero a sumar "))
                    num2 = int(input("ingresa el segundo numero a sumar "))
                    resultado = obj.suma(num1, num2)
                    print(f"El resultado es: {resultado}")
                case 3:
                    print("\n -- producto -- ")
                    num1 = int(input("ingresa el primer numero a multiplicar "))
                    num2 = int(input("ingresa el segundo numero a multiplicar "))
                    resultado = obj.producto(num1, num2)
                    print(f"El resultado es: {resultado}")
                case 4:
                    print("\n -- comparacion -- ")
                    num1 = int(input("ingresa el primer numero a comparar "))
                    num2 = int(input("ingresa el segundo numero a comparar "))
                    resultado = obj.comparacion(num1, num2)
                    if resultado == False:
                        print("Los numeros no son iguales")
                    else:
                        print("Los numeros son iguales")
                case 0:
                    print("Saliendo de las operaciones ... ")
                case _:
                    print(
                        "Error: Opcion no valida. Por favor, elige un número del 0 al 4."
                    )
        except ValueError:
            print("Error de formato: Debes ingresar un valor numerico valido.")
