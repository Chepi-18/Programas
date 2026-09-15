class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.saldo = 0

    def agregarSaldo(self, saldoNuevo):
        self.saldo += saldoNuevo

    def obtenerSaldo(self):
        return self.saldo

    def mostrarInfo(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, saldo: {self.saldo}"
