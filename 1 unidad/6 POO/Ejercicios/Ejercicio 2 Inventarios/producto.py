class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return f"El producto {self.nombre} se vendió correctamente, ganaste {self.precio * cantidad} pesos. Stock restante: {self.stock}."
        else:
            return "No cuenta con suficiente stock para realizar la venta."

    def mostrarInfo(self):
        print(f"Nombre del producto: {self.nombre} ")
        print(f"Precio del producto: {self.precio} ")
        print(f"Stock del producto: {self.stock} ")

    def actualizarPrecio(self, nuevoPrecio):
        if nuevoPrecio < 0:
            return f"No puedes cambiar el precio a una cantidad negativa. Se conserva el precio anterior de {self.precio}"
        elif nuevoPrecio == 0:
            return f"No somos caridad, no podemos regalar el producto. Se conserva el precio anterior de {self.precio}"
        else:
            self.precio = nuevoPrecio
            return f"Precio nuevo registrado correctamente. el precio actual del producto es de {self.precio}"

    def surtit(self, stockNuevo):
        if stockNuevo < 0:
            return f"No puedes agregar stock negativo. Se conserva el stock anterior de {self.stock}"
        elif stockNuevo == 0:
            return f"Si no quieres ingresar nuevo stock entonces se conserva el stock anterior de {self.stock}"
        else:
            self.stock += stockNuevo
            return f"stock nuevo registrado correctamente. el stock actual del producto es de {self.stock}"
