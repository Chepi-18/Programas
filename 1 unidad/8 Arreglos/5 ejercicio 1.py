Ntiempos = int(input("Ingrese la cantidad de tiempos de respuesta a analizar: "))
A = [0] * Ntiempos
print(f"Introduce {Ntiempos} valores:")
for i in range(Ntiempos):
    A[i] = int(input())
Conteo = []
moda = 0
for i in range(len(A)):
    Conteo.append(A.count(A[i]))
contador = max(Conteo)
posicion = Conteo.index(contador)


print(f"El tiempo de respuesta mas rapido fue de {max(A)} milisegundos")
print(f"El tiempo de respuesta mas lento fue de {min(A)} milisegundos")
print(f"El tiempo de respuesta promedio fue de {sum(A)/len(A)} milisegundos")
print(f"El tiempo de respuesta mas repetido fue de {A[posicion]} milisegundos")
