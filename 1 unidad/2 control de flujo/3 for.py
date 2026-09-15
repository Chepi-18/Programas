# range(5) -> Comienza en 0, termina en 4 (uno antes del 5)
for i in range(5):
    print(f"Iteración número {i}")

for i in range(5, 11):
    print(f"Contando: {i}")
estudiantes = ["Ana", "Carlos", "Beatriz"]

# En lugar de hacer un for con un contador 'i' y usar estudiantes[i]:
for estudiante in estudiantes:
    print(f"Revisando tarea de {estudiante}")
