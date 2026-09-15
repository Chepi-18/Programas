# Multiples excepciones
lista_numeros = [10, 20, 30]


def procesar_datos(indice):
    try:

        # Podría fallar si el índice no existe o si dividimos por cero
        valor = lista_numeros[indice]
        calculo = 100 / valor
        print(f"El resultado es {calculo}")

    except IndexError:
        print("Error: El indice que buscas esta fuera de los limites del arreglo.")
    except ZeroDivisionError:
        print("Error: El valor en esa posicion es 0, no se puede dividir.")
    except Exception as e:
        # El bloque general de Exception siempre debe ir al final (como un default)
        print(f"Ocurrió un error inesperado: {e}")


print(f"Datos del arreglo{lista_numeros}")
indice = int(input("Tecle un indice para ver los datos de esa posicion"))
procesar_datos(indice)
