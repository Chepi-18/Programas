from pila import Pila


def esta_balanceada(expresion: str) -> bool:
    pila = Pila()
    pares = {")": "(", "]": "[", "}": "{"}

    for caracter in expresion:
        if caracter in "([{":
            pila.push(caracter)

        elif caracter in ")]}":
            if pila.is_empty():
                return False
            tope = pila.pop()
            if tope != pares[caracter]:
                return False

    return pila.is_empty()


if __name__ == "__main__":
    expresion = input("Ingresa una expresión matemática o de código: ")

    if esta_balanceada(expresion):
        print("La expresión está BALANCEADA correctamente.")
    else:
        print("Error de sintaxis: La expresión NO está balanceada.")
