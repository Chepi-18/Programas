filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))
suma_Matriz = 0
matriz = []

for f in range(filas):
    fila_temporal = []
    for c in range(columnas):
        valor = int(input(f"Ingrese posicion [{f+1},{c+1}]: "))
        fila_temporal.append(valor)
    matriz.append(fila_temporal)
    suma_Matriz += sum(fila_temporal)

print("\n --- la matriz tiene los siguientes datos ---")
for f in range(filas):
    for c in range(columnas):
        print(f"{matriz[f][c]}\t", end="")
    print()

print(f"El promedio de la matriz da como resultado: {(suma_Matriz/(filas+columnas))}")
