# pila = []

# # Operaciones Push (Agregar al tope)
# pila.append("Página 1")
# pila.append("Página 2")
# pila.append("Página 3")

# # Operación Pop (Extraer del tope - LIFO)
# ultimo_visitado = pila.pop()
# print(f"Elemento extraído: {ultimo_visitado}")  # Salida: Página 3

# # Consultar el tope sin extraer (Peek)
# print(f"Elemento en el tope: {pila[-1]}")        # Salida: Página 2
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class PilaDinamica:
    def __init__(self):
        self.tope = None

    def push(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo

    def pop(self):
        if self.tope is None:
            return None
        valor = self.tope.dato
        self.tope = self.tope.siguiente
        return valor

    def peek(self):
        if self.tope is None:
            return None
        return self.tope.dato

# Inicialización de la pila dinámica
pila = PilaDinamica()
# Operaciones Push (Agregar al tope)
pila.push("Página 1")
pila.push("Página 2")
pila.push("Página 3")
# Operación Pop (Extraer del tope - LIFO)
ultimo_visitado = pila.pop()
print(f"Elemento extraído: {ultimo_visitado}")  # Salida: Página 3
# Consultar el tope sin extraer (Peek)
print(f"Elemento en el tope: {pila.peek()}")     # Salida: Página 2