import random
import copy


class BatallaMatrices:
    def __init__(self, tamano):
        self.tamano = tamano

        self.mat1 = []
        self.mat2 = []

        for i in range(self.tamano):
            fila1 = []
            fila2 = []
            for j in range(self.tamano):
                fila1.append(random.randint(1, 9))
                fila2.append(random.randint(1, 9))
            self.mat1.append(fila1)
            self.mat2.append(fila2)

        self.orig_mat1 = copy.deepcopy(self.mat1)
        self.orig_mat2 = copy.deepcopy(self.mat2)

        self.pts1 = 0
        self.pts2 = 0
        self.turno = 1

    def mostrar_matriz(self, matriz, jugador):
        print(f"Matriz jugador {jugador}:")
        for i in range(self.tamano):
            texto_pantalla = ""
            for j in range(self.tamano):
                if matriz[i][j] == 0:
                    texto_pantalla = texto_pantalla + "[ 0 ] "
                else:
                    texto_pantalla = texto_pantalla + f"[{i+1},{j+1}] "
            print(texto_pantalla)
        print()

    def mostrar_matriz_original(self, matriz, jugador):
        print(f"Matriz original jugador {jugador}:")
        for i in range(self.tamano):
            texto_pantalla = ""
            for j in range(self.tamano):
                valor = matriz[i][j]
                texto_pantalla = texto_pantalla + f"[{valor}] "
            print(texto_pantalla)
        print()

    def quedan_vivos(self, matriz):
        for i in range(self.tamano):
            for j in range(self.tamano):
                if matriz[i][j] > 0:
                    return True
        return False

    def pedir_coordenada(self, matriz):
        while True:
            try:
                f = int(input(f"  Fila (1-{self.tamano}): ")) - 1
                c = int(input(f"  Columna (1-{self.tamano}): ")) - 1

                dentro_rango_f = f >= 0 and f < self.tamano
                dentro_rango_c = c >= 0 and c < self.tamano

                if not dentro_rango_f:
                    print("  ¡Fila fuera de rango! Intenta de nuevo.\n")
                    continue
                if not dentro_rango_c:
                    print("  ¡Columna fuera de rango! Intenta de nuevo.\n")
                    continue

                if matriz[f][c] == 0:
                    print("  ¡Esa posición ya es 0, ya la destruiste, elige otra.\n")
                    continue

                lista_coords = [f, c]
                return lista_coords

            except ValueError:
                print("  ¡Por favor ingresa un número válido!\n")

    def iniciar(self):
        print("\n=== Pelea de matrices ===")

        while self.quedan_vivos(self.mat1) and self.quedan_vivos(self.mat2):
            self.mostrar_matriz(self.mat1, 1)
            self.mostrar_matriz(self.mat2, 2)

            print(f">> Turno del jugador {self.turno} <<")

            if self.turno == 1:
                print("=> Elige tu posición para atacar (Matriz 1):")
                coords_ataque = self.pedir_coordenada(self.mat1)
                f_mia = coords_ataque[0]
                c_mia = coords_ataque[1]

                print("=> Elige la posición enemiga a destruir (Matriz 2):")
                coords_defensa = self.pedir_coordenada(self.mat2)
                f_ene = coords_defensa[0]
                c_ene = coords_defensa[1]

                val_mio = self.mat1[f_mia][c_mia]
                val_ene = self.mat2[f_ene][c_ene]
            else:
                print("=> Elige tu posición para atacar (Matriz 2):")
                coords_ataque = self.pedir_coordenada(self.mat2)
                f_mia = coords_ataque[0]
                c_mia = coords_ataque[1]

                print("=> Elige la posición enemiga a destruir (Matriz 1):")
                coords_defensa = self.pedir_coordenada(self.mat1)
                f_ene = coords_defensa[0]
                c_ene = coords_defensa[1]

                val_mio = self.mat2[f_mia][c_mia]
                val_ene = self.mat1[f_ene][c_ene]

            print("\n--- Resultado de la batalla ---")

            if val_mio > val_ene:
                print(f"¡Gana el jugador {self.turno}!")
                if self.turno == 1:
                    self.pts1 = self.pts1 + 1
                    self.mat2[f_ene][c_ene] = 0
                else:
                    self.pts2 = self.pts2 + 1
                    self.mat1[f_ene][c_ene] = 0

            elif val_ene > val_mio:
                enemigo = 2
                if self.turno == 2:
                    enemigo = 1
                print(
                    f"¡La defensa del jugador {enemigo} era más fuerte y gana el punto!"
                )

                if self.turno == 1:
                    self.pts2 = self.pts2 + 1
                    self.mat1[f_mia][c_mia] = 0
                else:
                    self.pts1 = self.pts1 + 1
                    self.mat2[f_mia][c_mia] = 0

            else:
                print("¡Empate! Ninguno gana punto y ambas posiciones se vuelven 0.")
                if self.turno == 1:
                    self.mat1[f_mia][c_mia] = 0
                    self.mat2[f_ene][c_ene] = 0
                else:
                    self.mat2[f_mia][c_mia] = 0
                    self.mat1[f_ene][c_ene] = 0

            print("-------------------------------\n")

            if self.turno == 1:
                self.turno = 2
            else:
                self.turno = 1

        self.mostrar_resultados()

    def mostrar_resultados(self):
        print("=== Fin del juego ===")
        self.mostrar_matriz(self.mat1, 1)
        self.mostrar_matriz(self.mat2, 2)

        print("Puntuación final:")
        print(f"Jugador 1: {self.pts1} puntos")
        print(f"Jugador 2: {self.pts2} puntos")

        if (
            self.quedan_vivos(self.mat1) == False
            and self.quedan_vivos(self.mat2) == True
        ):
            print(
                "\n¡El jugador 2 ha destruido todas las posiciones del jugador 1 y gana!"
            )
        elif (
            self.quedan_vivos(self.mat2) == False
            and self.quedan_vivos(self.mat1) == True
        ):
            print(
                "\n¡El jugador 1 ha destruido todas las posiciones del jugador 2 y gana!"
            )
        else:
            if self.pts1 > self.pts2:
                print("\nEl jugador 1 gana por tener más puntos")
            elif self.pts2 > self.pts1:
                print("\nEl jugador 2 gana por tener más puntos")
            else:
                print("\n¡Es un empate total!")

        print("\n--- Matrices originales ---")
        self.mostrar_matriz_original(self.orig_mat1, 1)
        self.mostrar_matriz_original(self.orig_mat2, 2)


if __name__ == "__main__":
    print("¡Pelea de matrices!")
    tamano_elegido = int(input("¿De qué tamaño quieres el tablero?: "))
    juego = BatallaMatrices(tamano_elegido)
    juego.iniciar()
