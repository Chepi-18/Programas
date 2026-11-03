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

    def calcular_fibonacci(self, n: int) -> int:
        if n <= 1:
            return n
        anterior, actual = 1, 1
        while n > 2:
            nuevo = anterior + actual
            anterior = actual
            actual = nuevo
            n -= 1
        return nuevo

    def calcular_fibonacci_Re(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.calcular_fibonacci_Re(n - 1) + self.calcular_fibonacci_Re(n - 2)

    def repetir(self):
        self.repetir()

    def imprimir(self, n: int) -> int:
        print(f"{n}")
        self.imprimir(n - 1)

    def imprimir_descendente(self, x: int):
        if x == 0:
            print(x, end=" ")
        self.imprimir_descendente(x - 1)

    def imprimir_Hasta(self, n: int):
        if n > 0:
            self.imprimir_Hasta(n - 1)
            print(n, end=" ")

    def invertir_cadena(self, cadena: str) -> str:
        if len(cadena) <= 1:
            return cadena
        else:
            return self.invertir_cadena(cadena[1:]) + cadena[0]

    def ecuacion_recurrente(self, n: int) -> int:
        if n == 0:
            return 1
        else:
            return self.ecuacion_recurrente(n - 1) + (2**n)


if __name__ == "__main__":
    obj = Recursivid()
    opcion = -1
    entrada = 0
    while opcion != 0:
        print("\n --- Factorial --- ")
        print("1. iterativo factorial")
        print("2. recursivo factorial")
        print("3. recursivo fibonacci")
        print("4. recursivo fibonacci")
        print("5. repetir")
        print("6. imprimir")
        print("7. imprimir desendente")
        print("8. imprimir hasta")
        print("9. invertir cadena")
        print("10. ecuacion recurrente")
        print("0. Salir")
        try:
            opcion = int(input("\nElige una operación: "))
            match opcion:
                case 1:
                    entrada = int(input("Ingrese el numero: "))
                    print(f"{obj.factorial_iterativo(entrada)}")
                case 2:
                    entrada = int(input("Ingrese el numero: "))
                    print(f"{obj.factorial_recursivo(entrada)}")
                case 3:
                    entrada = int(input("Ingrese el numero: "))
                    print(f"{obj.calcular_fibonacci(entrada)}")
                case 4:
                    entrada = int(input("Ingrese el numero: "))
                    print(f"{obj.calcular_fibonacci_Re(entrada)}")
                case 5:
                    obj.repetir()
                case 6:
                    entrada = int(input("Ingrese el numero: "))
                    print(f"{obj.imprimir(entrada)}")
                case 7:
                    entrada = int(input("Ingrese el numero: "))
                    obj.imprimir_descendente(entrada)
                case 8:
                    entrada = int(input("Ingrese el numero: "))
                    obj.imprimir_Hasta(entrada)
                case 9:
                    entrada = input("Ingrese la cadena: ")
                    print(f"{obj.invertir_cadena(entrada)}")
                case 10:
                    entrada = int(input("Ingrese el numero: "))
                    print(f"{obj.ecuacion_recurrente(entrada)}")
                case 0:
                    print("Saliendo de las operaciones ... ")
                case _:
                    print(
                        "Error: Opcion no valida. Por favor, elige un número del 0 al 4."
                    )
        except ValueError:
            print("Error de formato: Debes ingresar un valor numerico valido.")
