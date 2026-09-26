class Compara:
    def menorIgual(self, num1: int, num2: int) -> bool:
        return num1 <= num2

    def menor(self, num1: int, num2: int) -> bool:
        return num1 < num2

    def mayor(self, num1: int, num2: int) -> bool:
        return num1 > num2

    def mayorIgual(self, num1: int, num2: int) -> bool:
        return num1 >= num2


if __name__ == "__main__":
    obj = Compara()
    opcion = -1
    num1 = 0
    num2 = 0
    while opcion != 0:
        print("\n --- Operaciones --- ")
        print("1. Verificar si el primer numero es menor o igual que el segundo")
        print("2. Verificar si el primer numero es menor que el segundo")
        print("3. Verificar si el primer numero es mayor que el segundo")
        print("4. Verificar si el primer numero es mayor o igual que el segundo")
        print("0. Salir")
        try:
            opcion = int(input("\nElige una operación: "))
            match opcion:
                case 1:
                    num1 = int(input("ingresa el primer numero entero "))
                    num2 = int(input("ingresa el segundo numero entero "))
                    print(f"el resultado es: {obj.menorIgual(num1, num2)}")
                case 2:
                    num1 = int(input("ingresa el primer numero entero "))
                    num2 = int(input("ingresa el segundo numero entero "))
                    print(f"el resultado es: {obj.menor(num1, num2)}")
                case 3:
                    num1 = int(input("ingresa el primer numero entero "))
                    num2 = int(input("ingresa el segundo numero entero "))
                    print(f"el resultado es: {obj.mayor(num1, num2)}")
                case 4:
                    num1 = int(input("ingresa el primer numero entero "))
                    num2 = int(input("ingresa el segundo numero entero "))
                    print(f"el resultado es: {obj.mayorIgual(num1, num2)}")
                case 0:
                    print("Saliendo de las operaciones ... ")
                case _:
                    print(
                        "Error: Opcion no valida. Por favor, elige un número del 0 al 4."
                    )
        except ValueError:
            print("Error de formato: Debes ingresar un valor numerico valido.")
