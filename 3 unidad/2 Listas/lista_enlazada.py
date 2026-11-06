from nodo import Nodo


class ListaEnlazada:
    def __init__(self):
        self.p = None

    def crear_lista(self):
        print("\n --- CREACION DE LISTAS LIGADAS ---")
        dato = int(input("Introduce el primer elemento a la lista: "))
        self.p = Nodo(dato)
        t = self.p

        res = int(input("¿Desea ingresar más nodos a la lista? (1: Si, 0: No): "))
        while res == 1:
            nuevo_dato = int(input("Escribe el elemento: "))
            q = Nodo(nuevo_dato)
            t.liga = q  # El anterior apunta al nuevo
            t = q  # 't' avanza al nuevo final
            res = int(input("¿Desea ingresar más nodos a la lista? (1: Si, 0: No): "))

    def mostrar_lista(self):
        print("\n --- Elementos de la lista --- ")
        q = self.p
        if q is None:
            print("La lista está vacía.")
            return
        # Repetir mientras Q <> NILL
        while q is not None:
            print(f"[{q.info}] -> ", end="")
            q = q.liga  # Q = Q.LIGA
        print("NILL")

    def promedio_lista(self):
        print("\n --- Promedio de la lista --- ")
        q = self.p
        if q is None:
            print("La lista está vacía.")
            return
        suma = 0
        contador = 0
        while q is not None:
            suma += q.info
            contador += 1
            q = q.liga
        promedio = suma / contador if contador > 0 else 0
        print(f"El promedio de los elementos de la lista es: {promedio}")

    def inserta_inicio(self, dato: int):
        q = Nodo(dato)  # CREAR (Q) y asignar INFORMACION
        q.liga = self.p  # Q.LIGA = P
        self.p = q  # P= Q
        print(f"Elemento {dato} insertado al inicio.")

    def inserta_final(self, dato: int):
        if self.p is None:
            self.inserta_inicio(dato)
            return

        t = self.p
        # Recorrido hasta el penúltimo (T.LIGA <> NILL)
        while t.liga is not None:
            t = t.liga

        q = Nodo(dato)
        t.liga = q  # Enlaza el último nodo al nuevo
        print(f"Elemento {dato} insertado al final.")
