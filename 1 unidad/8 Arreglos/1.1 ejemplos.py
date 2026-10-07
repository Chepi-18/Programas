b = 0
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8]

for a in range(10):
    if c[a] % 2 == 0:
        b += c[a]

print(b)

numeros = [5, 2, 8, 7, 0, 3]
izq = 0
der = 5

while izq <= der:
    numeros[der] = numeros[izq]
    izq += 1
    der -= 1

print(numeros)
