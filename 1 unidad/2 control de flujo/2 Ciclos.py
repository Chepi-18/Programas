boletos_disponibles = int(input("Cuantos boletos tiene para vender? "))

while boletos_disponibles > 0:
    boletos_disponibles -= 1
    print(f"Vendiendo boleto. Quedan {boletos_disponibles}")


print("Boletos agotados.")
