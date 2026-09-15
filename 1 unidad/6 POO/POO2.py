import datetime


class Persona:

    def __init__(self, nombre, fechaNacimiento):
        self.nombre = nombre
        self.fechaNacimiento = fechaNacimiento

    def calcularEdad(self):
        # obtenemos el año
        anio_actual = datetime.date.today().year
        # calculamos
        edad = anio_actual - self.fechaNacimiento
        return edad

    def mostrarInformacion(self):
        return f"Nombre: {self. nombre} y tu edad es {self.calcularEdad()}"


if __name__ == "__main__":
    alumno = Persona("Juan", 2005)
print(f"Tu informacion actual: {alumno.mostrarInformacion()}")
