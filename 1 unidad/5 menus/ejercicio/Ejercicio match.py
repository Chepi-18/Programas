def Cajero():
    saldo = 0
    opc = -1
    while opc != 0:
        print("\n --- CAJERO Automatico --- ")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("0. Salir")
        try:
            opc = int(input("\nElige una opcion: "))
            match opc:
                case 1:
                    print(f"Su saldo es de {saldo} pesos")
                case 2:
                    try:
                        deposito = float(input("Cuanto dinero desea depositar? "))
                        if deposito < 0:
                            print("No puedes depositar una cantidad negativa")
                        elif deposito == 0:
                            print("No puedes ingresar 0 pesos")
                        else:
                            saldo = deposito + saldo
                            print(
                                f"Se an depositado {deposito} pesos, su saldo total actual es de {saldo}"
                            )
                    except TypeError:
                        print(
                            "El tipo de dato es incompatible: Debes ingresar un valor numerico valido."
                        )
                case 3:
                    try:
                        retiro = float(
                            input(
                                f"Cuanto dinero desea retirar?, actualmente tienes {saldo} pesos en tu cuenta "
                            )
                        )
                        if retiro > saldo:
                            print("No puedes retirar el dinero que no tienes")
                        elif retiro <= 0:
                            print("No puedes retirar una cantidad negativa o igual a 0")
                        else:
                            saldo = saldo - retiro
                            print(
                                f"Se an retirado {retiro} pesos de su cuenta exitosamente. Su saldo actual es de {saldo} "
                            )
                    except TypeError:
                        print(
                            "El tipo de dato es incompatible: Debes ingresar un valor numerico valido."
                        )
                case 0:
                    print("Saliendo de la calculadora ... ")
                case _:
                    print(
                        "Error: Opcion no valida. Por favor, elige un número del 0 al 4."
                    )
        except ValueError:
            print("Error de formato: Debes ingresar un valor numerico valido.")


Cajero()
