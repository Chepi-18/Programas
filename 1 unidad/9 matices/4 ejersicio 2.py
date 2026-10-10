import random

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))
matriz = []
contador_0 = 0

for f in range(filas):
    fila_temporal = []
    for c in range(columnas):
        numero = random.randint(0, 5)
        fila_temporal.append(numero)
    matriz.append(fila_temporal)

print("\n --- la matriz tiene los siguientes datos ---")
for f in range(filas):
    for c in range(columnas):
        print(f"{matriz[f][c]}\t", end="")
    print()

for f in range(filas):
    for c in range(columnas):
        if matriz[f][c] == 0:
            contador_0 += 1
if contador_0 >= 1:
    print(f"ALERTA: se detectaron {contador_0} nodo(s) fuera de linea (valor 0)")
else:
    print("Sin nodos fuera de linea")
