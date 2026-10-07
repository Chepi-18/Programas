arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valor = int(input("Ingrese un valor: "))
print(f"valores del arreglo: {arreglo}")
for i in range(len(arreglo)):
    print(
        f" el valor ingresado {valor}, se multiplicara por el valor del arreglo en la posicion {i}, dando como resultado: {arreglo[i]*valor}"
    )
