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
