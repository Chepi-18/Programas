import iterativo
import recursivo


def main():
    posicion = 6

    res_iterativo = iterativo.calcular_fibonacci(posicion)
    res_recursivo = recursivo.calcular_fibonacci(posicion)

    print(f"Resultado iterativo: {res_iterativo}")
    print(f"Resultado recursivo: {res_recursivo}")


if __name__ == "__main__":
    main()
