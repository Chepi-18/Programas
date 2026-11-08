from nodo import Nodo
from graphviz import Digraph


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

    def inserta_antes_de(self, dato, ref):
        q = self.p
        t = None
        band = True

        if q is None:
            return  # Validación de seguridad

        while q is not None and q.info != ref and band:
            if q.liga is not None:
                t = q
                q = q.liga
            else:
                band = False

        if band:
            # Creación del nuevo nodo
            x = Nodo(dato)
            if self.p == q:
                x.liga = self.p
                self.p = x
                print(f"\nElemento {dato} insertado antes del primer nodo ({ref}).")
            # Insercion en el medio o final
            else:
                t.liga = x
                x.liga = q
                print(f"\nElemento {dato} insertado antes de {ref}.")

    def inserta_despues_de(self, dato, ref):
        q = self.p  # 'self.p' representa el nodo inicial 'p'
        band = True

        # Validación básica por si la lista está vacía
        if q is None:
            return

        # Adaptacion del bucle do-while original a un while convencional en Python
        while q is not None and q.info != ref and band:
            if q.liga is not None:
                q = q.liga
            else:
                band = False

        # Si se encontro el nodo de referencia (BAND sigue siendo true)
        if band:
            # Creación del nuevo nodo (equivalente a nodo T = new nodo(); T.INFO = DATO;)
            t = Nodo(dato)

            # Inserción del nuevo nodo 't' después del nodo 'q'
            t.liga = q.liga
            q.liga = t

            # Impresion del resultado (equivalente a Console.WriteLine)
            print(f"\nElemento {dato} insertado despues de {ref}.")

    def eliminar_inicio(self):
        if self.p is None:
            print("No hay nodos para eliminar.")
            return

        q = self.p
        # Se verifica si la lista tiene más de un nodo
        if q.liga is not None:
            self.p = q.liga  # Se redefine el puntero al inicio
            print(f"Elemento {q.info} eliminado (quedan más nodos).")
        else:
            self.p = None  # P = NILL
            print(f"Elemento {q.info} eliminado (la lista quedó vacía).")

    def Eliminar_ultimo(self):
        if self.p is None:
            print("No hay nodos para eliminar.")
            return

        if self.p.liga is None:
            self.p = None
            print("La lista quedo vacia")
        else:
            q = self.p
            t = None
            while q.liga is not None:
                t = q
                q = q.liga
            t.liga = None
            print(f"Elemento {q.info} (último nodo) eliminado.")

    def Eliminar_nodo_x(self, dato):
        if self.p is None:
            print("La lista está vacía.")
            return

        q = self.p
        Band = True
        t = None
        while q.info != dato and Band:
            if q.liga is not None:
                t = q
                q = q.liga
            else:
                Band = False

        if Band is False:
            print(f"El elemento {dato} no fue encontrado en la lista. ")
        else:
            if self.p is q:
                self.p = q.liga
                print(f"Elemento {dato} eliminado con exito. ")
            else:
                t.liga = q.liga
                print(f"Elemento {dato} eliminado con exito. ")

    def Busqueda(self, dato):
        if self.p is None:
            print("La lista está vacía.")
            return

        q = self.p
        Band = True

        while q.info != dato and Band:
            if q.liga is not None:
                q = q.liga
            else:
                Band = False

        if Band is False:
            print(f"El elemento {dato} no se encuenta en la lista. ")
        else:
            print(f"El elemento {dato} fue encontrado en la lista. ")

    def personal_vaciar_lista(self):
        if self.p is None:
            print("La lista ya está vacía.")
            return

        self.p = None
        print("La lista ha sido vaciada por completo.")

    def eliminar_nodo_antes_de(self, referencia):
        if self.p is None:
            print("La lista está vacía.")
            return

        q = self.p
        t = None
        band = True

        if q is None:
            return  # Validación de seguridad

        while q is not None and q.info != referencia and band:
            if q.liga is not None:
                t = q
                q = q.liga
            else:
                band = False

        if band:

            if self.p == q:
                print(f"No existe ningun nodo antes del primero ")
            elif self.p == t:
                self.p = q
                print(f"El elemento antes de {referencia} eliminado con exito. ")
            else:
                q = self.p
                anterior = None
                while q != t:
                    if q.liga is not None:
                        anterior = q
                        q = q.liga
                anterior.liga = q.liga
                print(f"El elemento antes de {referencia} fue eliminado con exito. ")
        else:
            print(f"El elemento {referencia} no esta en la lista")

    def eliminar_nodo_despues_de(self, referencia):
        if self.p is None:
            print("La lista está vacía.")
            return

        q = self.p
        band = True

        if q is None:
            return  # Validación de seguridad

        while q is not None and q.info != referencia:
            q = q.liga
        if q is None:
            band = False

        if band:
            if q.liga == None:
                print(f"No existe ningun nodo despues del ultimo ")
            else:
                t = q.liga
                q.liga = t.liga
                print(f"El elemento despues de {referencia} fue eliminado con exito. ")
        else:
            print(f"El elemento {referencia} no esta en la lista")
