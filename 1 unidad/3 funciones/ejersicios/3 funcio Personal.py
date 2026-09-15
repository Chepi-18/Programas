def Suma(num1: float, num2: float):
    print(f"La suma de los 2 numeros es: {num1 + num2}")


def Resta(num1: float, num2: float):
    print(f"La resta de los 2 numeros es: {num1 - num2}")


def Multiplicacion(num1: float, num2: float):
    print(f"El resultado es: {num1 * num2}")


def Divicion(num1: float, num2: float):
    if num2 == 0:
        print("No puedes dividir entre 0")
    else:
        print(f"El resultado es: {num1 / num2}")


def Exponente(num1: float, num2: float):
    print(f"el resultado es: {num1 ** num2}")


num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese otro numero: "))
print("Que desea hacer con ellos?")
opcion = 0
while opcion != 7:
    print("1 sumar")
    print("2 resar")
    print("3 multiplicar")
    print("4 dividir")
    print("5 elevar un numero a una potencia")
    print("6 Ingresar nuevos numeros")
    print("7 Salir")
    opcion = int(input("Opcion: "))
    match opcion:
        case 1:
            Suma(num1, num2)
        case 2:
            Resta(num1, num2)
        case 3:
            Multiplicacion(num1, num2)
        case 4:
            Divicion(num1, num2)
        case 5:
            Exponente(num1, num2)
        case 6:
            num1 = float(input("Ingrese un numero: "))
            num2 = float(input("Ingrese otro numero: "))
            print(f"Los numeros ingresados son: {num1} y {num2}")
        case 7:
            print("Gracias por usar la calculadora")
        case _:
            print("Opcion no encontrada")
