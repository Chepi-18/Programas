from tqdm import tqdm
import time
import random


def maxComun_divisor(numero_1, numero_2):
    if numero_2 == 0:
        return numero_1
    return maxComun_divisor(numero_2, numero_1 % numero_2)


def minComun_multiplo(numero_1, numero_2):
    if numero_1 == 0 or numero_2 == 0:
        return 0
    # el abs se usa para sacar el valor absoluto
    return abs(numero_1 * numero_2) // maxComun_divisor(numero_1, numero_2)


def mostrar_animacion_de_calculo():
    print()
    for _ in tqdm(range(100), desc="Calculando", unit="%"):
        time.sleep(0.005)


# --- Menú principal ---
if __name__ == "__main__":
    opcion_seleccionada = -1
    numero_1 = 0
    numero_2 = 0

    while opcion_seleccionada != 0:
        print("\n --- Operaciones --- ")
        print("1. Calcular MCD (Máximo Común Divisor)")
        print("2. Calcular MCM (Mínimo Común Múltiplo)")
        print("3. Calcular MCD y MCM al mismo tiempo")
        print("4. Ejecutar prueba automática con 500 pares aleatorios")
        print("0. Salir")

        try:
            opcion_seleccionada = int(input("\nElige una operación: "))

            match opcion_seleccionada:
                case 1:
                    numero_1 = int(input("Ingresa el primer número: "))
                    numero_2 = int(input("Ingresa el segundo número: "))
                    mostrar_animacion_de_calculo()
                    resultado_mcd = maxComun_divisor(numero_1, numero_2)
                    print(
                        f"\nResultado: El MCD({numero_1}, {numero_2}) es: {resultado_mcd}"
                    )

                case 2:
                    numero_1 = int(input("Ingresa el primer número: "))
                    numero_2 = int(input("Ingresa el segundo número: "))
                    mostrar_animacion_de_calculo()
                    resultado_mcm = minComun_multiplo(numero_1, numero_2)
                    print(
                        f"\nResultado: El MCM({numero_1}, {numero_2}) es: {resultado_mcm}"
                    )

                case 3:
                    numero_1 = int(input("Ingresa el primer número: "))
                    numero_2 = int(input("Ingresa el segundo número: "))
                    mostrar_animacion_de_calculo()
                    resultado_mcd = maxComun_divisor(numero_1, numero_2)
                    resultado_mcm = minComun_multiplo(numero_1, numero_2)
                    print(f"\nResultados:")
                    print(f"- MCD({numero_1}, {numero_2}) = {resultado_mcd}")
                    print(f"- MCM({numero_1}, {numero_2}) = {resultado_mcm}")

                case 4:
                    lista_de_pares = [
                        (random.randint(100, 5000), random.randint(100, 5000))
                        for _ in range(500)
                    ]
                    lista_de_resultados = []

                    print()
                    for num_a, num_b in tqdm(
                        lista_de_pares,
                        desc="Procesando 500 pares de prueba",
                        unit="par",
                    ):
                        res_mcd = maxComun_divisor(num_a, num_b)
                        res_mcm = minComun_multiplo(num_a, num_b)
                        lista_de_resultados.append((num_a, num_b, res_mcd, res_mcm))
                        time.sleep(0.012)

                    print(
                        f"\nProcesados {len(lista_de_resultados)} pares exitosamente."
                    )
                    ejemplo_a, ejemplo_b, ejemplo_mcd, ejemplo_mcm = (
                        lista_de_resultados[0]
                    )
                    print(
                        f"Muestra del primer par -> MCD({ejemplo_a}, {ejemplo_b}) = {ejemplo_mcd} | MCM({ejemplo_a}, {ejemplo_b}) = {ejemplo_mcm}"
                    )

                case 0:
                    print("Saliendo de las operaciones ... ")

                case _:
                    print(
                        "Error: Opción no válida. Por favor, elige un número del 0 al 4."
                    )

        except ValueError:
            print("Error de formato: Debes ingresar un valor numérico válido.")
