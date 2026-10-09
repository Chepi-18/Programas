# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for f in range(len(matriz)):
#     for c in range(len(matriz[0])):
#         print(f"Posicion[{f}] [{c}] = {matriz[f][c]}")


def ejemplo_ingreso_manual():
    print(" === LLENADO DE MATRIZ 3x4 === ")
    matriz = []

    # 1. Llenado de la matriz
    for f in range(3):
        fila_temporal = []
        for c in range(4):
            # Pedimos el dato (sumamos 1 a f y c solo para que el usuario vea base 1)
            valor = int(input(f"Ingrese posicion [{f+1},{c+1}]: "))
            fila_temporal.append(valor)
        # Agregamos la fila completa a la matriz principal
        matriz.append(fila_temporal)

    # 2. Impresión de la matriz
    print("\n --- Resultado ---")
    for f in range(3):
        for c in range(4):
            # end="\t" tabula el texto para que parezca una cuadrícula
            print(f"{matriz[f][c]}\t", end="")
        print()


if __name__ == "__main__":
    ejemplo_ingreso_manual()
