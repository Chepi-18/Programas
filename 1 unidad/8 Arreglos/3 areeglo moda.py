A = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9, 9, 9, 9]

Conteo = []

moda = 0
for i in range(len(A)):
    Conteo.append(A.count(A[i]))
    print(f"EL valor {A[i]} esta {Conteo[i]}")
contador = max(Conteo)
print(f"Valor con mas veces: {contador}")
posicion = Conteo.index(contador)
print(f"Posicion donde se encuantra el mas repetido: {posicion}")
print(f"La moda es: {A[posicion]}")
