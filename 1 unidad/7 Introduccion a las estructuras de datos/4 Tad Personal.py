class Reales:
    def SumaImagina(self, num1: complex, num2: complex) -> complex:
        return num1 + num2

    def SumaComun(self, num1: float, num2: float) -> float:
        return num1 + num2

    def DivicionNormal(self, num1: float, num2: float) -> float:
        return num1 / num2

    def MultiplicaciomImagina(self, num1: complex, num2: complex) -> complex:
        return num1 * num2


if __name__ == "__main__":
    obj = Reales()
    opcion = -1
    num1 = 0
    num2 = 0
    while opcion != 0:
        print("\n --- Operaciones --- ")
        print("1. Hacer una suma con numeros imaginarios")
        print("2. Hacer una suma comun")
        print("3. Hacer una divicion comun")
        print("4. Hacer una Multiplicacion con numeros imaginarios")
        print("0. Salir")
        try:
            opcion = int(input("\nElige una operación: "))
            match opcion:
                case 1:
                    num1 = complex(input("ingresa el primer numero imaginario: "))
                    num2 = complex(input("ingresa el segundo numero imaginario: "))
                    print(f"el resultado es: {obj.SumaImagina(num1, num2)}")
                case 2:
                    num1 = float(input("ingresa el primer numero flotante: "))
                    num2 = float(input("ingresa el segundo numero flotante: "))
                    print(f"el resultado es: {obj.SumaComun(num1, num2)}")
                case 3:
                    num1 = float(input("ingresa el primer numero flotante: "))
                    num2 = float(input("ingresa el segundo numero flotante: "))
                    if num2 == 0:
                        print("Error: No se puede dividir entre cero.")
                    else:
                        print(f"el resultado es: {obj.DivicionNormal(num1, num2)}")
                case 4:
                    num1 = complex(input("ingresa el primer numero imaginario: "))
                    num2 = complex(input("ingresa el segundo numero imaginario: "))
                    print(
                        f"La multiplicacion da: {obj.MultiplicaciomImagina(num1, num2)}"
                    )
                case 0:
                    print("Saliendo de las operaciones ... ")
                case _:
                    print(
                        "Error: Opcion no valida. Por favor, elige un número del 0 al 4."
                    )
        except ValueError:
            print("Error de formato: Debes ingresar un valor numerico valido.")
