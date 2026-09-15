class Estudiante:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.materias_aprobadas = 0

    def aprobar_materia(self):
        self.materias_aprobadas += 1

    def mostrar_info(self):
        return f"El alumno {self.nombre} ha aprobado {self.materias_aprobadas} materias"


if __name__ == "__main__":
    alumno1 = Estudiante("Carlos", "25050045")
    alumno2 = Estudiante("Ana", "25050028")

alumno1.aprobar_materia()
alumno1.aprobar_materia()

print(alumno1.mostrar_info())
print(alumno2.mostrar_info())
