class Pila:
    class Nodo:
        def __init__(self, info: int):
            self.info = info
            self.sig = None

    def __init__(self):
        self.tope = None

    def push(self, dato: int) -> None:
        """Agrega un elemento en la cima de la pila (Push)."""
        nuevo = self.Nodo(dato)
        nuevo.sig = self.tope
        self.tope = nuevo

    def is_empty(self) -> bool:
        """Devuelve True si la pila está vacía, False en caso contrario."""
        return self.tope is None

    def pop(self) -> int | str:
        """Extrae y retorna el elemento de la cima (Pop)."""
        if self.is_empty():
            return "Error :Underflow"

        informacion = self.tope.info
        self.tope = self.tope.sig
        return informacion

    def imprimir(self) -> None:
        """Muestra los elementos desde la cima hasta el fondo."""
        if self.is_empty():
            print("[Pila Vacía]")
            return

        reco = self.tope
        while reco is not None:
            print(f"{reco.info} ")
            reco = reco.sig

    def promedio(self):
        """pues saca el promedio"""
        if self.is_empty():
            print("[Pila Vacía]")
            return

        contador = 0
        suma = 0
        q = self.tope
        while q is not None:
            contador += 1
            suma += q.info
            q = q.sig
        print(f"El promedio es: {suma/contador}")

    def tamaño(self):
        if self.is_empty():
            print("[Pila Vacía]")
            return
        contador = 0
        q = self.tope
        while q is not None:
            contador += 1
            q = q.sig
        print(f"El tamaño de la pila es de: {contador}")

    def busqueda(self, referencia):
        if self.is_empty():
            print("[Pila Vacía]")
            return
        q = self.tope
        bandera = True
        while q.info != referencia and bandera:
            if q.sig is not None:
                q = q.sig
            else:
                bandera = False

        if bandera is False:
            print("No se encontro coincidencia en la pila")
        else:
            print(f"El elemento {referencia} fue encontrado con exito en la pila")

    def tope_sin_eliminar(self):
        if self.is_empty():
            print("[Pila Vacía]")
            return
        print(f"el tope de la pila es: {self.tope.info}")

    def eliminar_pila(self):
        if self.is_empty():
            print("la pila ya esta vacia")
            return
        self.tope = None
        print("pila eliminada con exito")

    def Lectura_kamikase(self):
        if self.is_empty():
            print("[Pila Vacía]")
            return
        print("Los datos que estaban en la pila son: ")
        while self.tope is not None:
            print(self.tope.info)
            self.tope = self.tope.sig
        print("La lista quedo vacia")
