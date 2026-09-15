materias = int(input("Cuantas materias cursaste? "))
suma = 0
for i in range(materias):
    materia = int(input(f"Ingresa la calificacion de la materia {i+1} "))
    suma += materia
Promedio = suma / materias
if Promedio >= 85:
    print(f"Su promedio es: {Promedio}, eres apto para una beca")
else:
    print(f"Su promedio es: {Promedio}, no eres apto para una beca")
