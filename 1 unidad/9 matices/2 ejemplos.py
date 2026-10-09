import random


class MatrizDinamica:
    def __init__(self, filas: int, columnas: int):
        self.filas = filas
        self.columnas = columnas
        self.matriz = []

    def llenar_matriz(self):
        """Llena la matriz con números aleatorios entre 0 y 9"""
        for f in range(self.filas):
            fila_temporal = []
            for c in range(self.columnas):
                # random.randint incluye ambos limites (0 y 9)
                numero = random.randint(0, 9)
                fila_temporal.append(numero)
            self.matriz.append(fila_temporal)

    def mostrar_matriz(self):
        """Imprime la matriz en formato de cuadrícula"""
        for f in range(self.filas):
            for c in range(self.columnas):
                print(f"{self.matriz[f][c]} ", end="")
            print()


def ejecutar_ejemplo_aleatorio():
    print("=== MATRIZ ALEATORIA ===")
    f = int(input("Escriba un numero de filas: "))
    c = int(input("Escriba un numero de columnas: "))

    # Instanciamos el objeto
    mi_matriz = MatrizDinamica(f, c)
    mi_matriz.llenar_matriz()

    print("\nMatriz Generada:")
    mi_matriz.mostrar_matriz()


if __name__ == "__main__":
    ejecutar_ejemplo_aleatorio()
