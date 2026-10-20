class Recursivid:
    # 1, Factorial
    def factorial_iterativo(self, n: int) -> int:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    def factorial_recursivo(self, n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * self.factorial_recursivo(n - 1)


if __name__ == "__main__":
    obj = Recursivid()
    opcion = -1
    entrada = 0
    while opcion != 0:
        print("\n --- Factorial --- ")
        print("1. iterativo")
        print("2. recursivo")
        print("0. Salir")
        try:
            opcion = int(input("\nElige una operación: "))
            match opcion:
                case 1:
                    entrada = int(input("Ingrese el numero"))
                    print(f"{obj.factorial_iterativo(entrada)}")
                case 2:
                    entrada = int(input("Ingrese el numero"))
                    print(f"{obj.factorial_recursivo(entrada)}")
                case 0:
                    print("Saliendo de las operaciones ... ")
                case _:
                    print(
                        "Error: Opcion no valida. Por favor, elige un número del 0 al 4."
                    )
        except ValueError:
            print("Error de formato: Debes ingresar un valor numerico valido.")
