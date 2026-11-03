class NodoItem:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None  # En Python, None equivale a nullptr


class Inventario:
    def __init__(self):
        self.cabeza = None

    # Inserción al inicio (O(1))
    def agregar_item(self, nuevo_nombre):
        nuevo_nodo = NodoItem(nuevo_nombre)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    # Recorrido secuencial (O(n))
    def mostrar_items(self):
        actual = self.cabeza
        elementos = []
        while actual is not None:
            elementos.append(actual.nombre)
            actual = actual.siguiente
        print(" -> ".join(elementos) + " -> None")

    # Eliminación (Desvinculación)
    def consumir_item(self, objetivo):
        actual = self.cabeza
        anterior = None

        while actual is not None and actual.nombre != objetivo:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            return  # El ítem no existe en la secuencia

        if anterior is None:
            self.cabeza = actual.siguiente  # Se elimina la cabeza
        else:
            anterior.siguiente = actual.siguiente  # Se puentea el nodo intermedio
