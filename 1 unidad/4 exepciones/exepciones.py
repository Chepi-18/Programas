try:
    # Código que podría fallar
    edad = int(input("Ingresa tu edad en números: "))
    print(f"Tienes {edad} años.")
except ValueError:
    # Se ejecuta solo si el usuario teclea texto en lugar de un número
    print("Error: Debes ingresar un numero entero válido.")
# Capturar mensaje de error original
try:

    resultado = 10 / 0
except ZeroDivisionError as u:
    print(f"Ocurrió un error matemático: {u}")
