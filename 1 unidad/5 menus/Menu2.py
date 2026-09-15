def calculadora_basica():
    opcion = -1
    while opcion != 0:
        print("\n --- CALCULADORA BÁSICA --- ")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Salir")
        try:
            opcion = int(input("\nElige una operación: "))
            match opcion:
                case 1:
                    print("\n -- SUMA -- ")
                    a = float(input("Ingresa el primer número: "))
                    b = float(input("Ingresa el segundo número: "))
                    print(f"Resultado: {a} + {b} = {a + b}")
                case 2:
                    print("\n -- RESTA -- ")
                    a = float(input("Ingresa el primer numero: "))
                    b = float(input("Ingresa el segundo numero: "))
                    print(f"Resultado: {a} - {b} = {a - b}")
                case 3:
                    print("\n -- MULTIPLICACIÓN -- ")
                    a = float(input("Ingresa el primer numero: "))
                    b = float(input("Ingresa el segundo numero: "))
                    print(f"Resultado: {a} * {b} = {a * b}")
                case 4:
                    print("\n -- DIVISIÓN -- ")
                    a = float(input("Ingresa el dividendo: "))
                    b = float(input("Ingresa el divisor: "))
                    if b == 0:
                        print("Error matematico: No se puede dividir entre cero.")
                    else:
                        print(f"Resultado: {a} / {b} = {a / b}")
                case 0:
                    print("Saliendo de la calculadora ... ")
                case _:
                    print(
                        "Error: Opcion no valida. Por favor, elige un número del 0 al 4."
                    )

        except ValueError:
            # Este except atrapara el error si escriben letras en el menú o letras en los números
            print("Error de formato: Debes ingresar un valor numerico valido.")


calculadora_basica()
