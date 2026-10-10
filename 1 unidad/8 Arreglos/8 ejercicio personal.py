import random

Jugador1 = []
Jugador2 = []
masCartas = ""
masCartas2 = ""
for i in range(2):
    carta1 = random.randint(1, 11)
    carta2 = random.randint(1, 11)
    Jugador1.append(carta1)
    Jugador2.append(carta2)
print(f"puntos iniciales del ugador 1: {Jugador1}")
print(f"puntos iniciales del ugador 2: {Jugador2}")

while masCartas != "n" and sum(Jugador1) < 21:
    while masCartas != "n":
        masCartas = input(
            f"Jugador 1 desea tomar otra carta? Tus puntos actuales son: {sum(Jugador1)}. s/n "
        )
        match masCartas:
            case "s":
                Jugador1.append(random.randint(1, 11))
                print(f"Sus puntos son: {sum(Jugador1)}")
            case "n":
                print("Ya no se sumara mas")
            case _:
                print("Valor no encontrado")

while masCartas2 != "n" and sum(Jugador2) < 21:
    while masCartas2 != "n":
        masCartas2 = input(
            f"Jugador 2 desea tomar otra carta? Tus puntos actuales son: {sum(Jugador2)}. s/n "
        )
        match masCartas2:
            case "s":
                Jugador2.append(random.randint(1, 11))
                print(f"Sus puntos son: {sum(Jugador2)}")
            case "n":
                print("Ya no se sumara mas")
            case _:
                print("Valor no encontrado")

puntos1 = sum(Jugador1)
puntos2 = sum(Jugador2)
print("Resultados")
print(f"El jugador 1 tuvo: {sum(Jugador1)} puntos")
print(f"El jugador 2 tuvo: {sum(Jugador2)} puntos")
if puntos1 > 21 and puntos2 > 21:
    print("Los dos perdieron por pasarse de 21 puntos")
elif puntos1 > 21:
    print("El jugador 2 gano")
elif puntos2 > 21:
    print("El jugador 1 gano")
elif puntos1 == puntos2:
    print("Es un empate")
elif puntos1 > puntos2:
    print(
        f"El jugador 1 ganó por tener {sum(Jugador1) - sum(Jugador2)} puntos mas que el jugador 2 sin pasarse de 21"
    )
else:
    print(
        f"El jugador 2 ganó por tener {sum(Jugador2) - sum(Jugador1)} puntos mas que el jugador 1 sin pasarse de 21"
    )
