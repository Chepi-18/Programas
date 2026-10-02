A = [2, 5, 8, 100, 1, 2, 100, 5, 5, 5]
for i in range(len(A)):
    print(f"la posicion {i}, tiene el valor {A[i]}")
suma = 0
for i in A:
    print(f"{i} ", end="")
    suma += i
print(f"Suma = {suma}")
print(f"El promedio es: {suma / len(A)}")

moda = None
maxRep = 0
for i in range(len(A)):
    RepAct = 0
    for j in range(len(A)):
        if A[i] == A[j]:
            RepAct += 1
    if RepAct > maxRep:
        maxRep = RepAct
        moda = A[i]
print(f"La moda es: {moda}")
