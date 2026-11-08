from lista_enlazada import ListaEnlazada

if __name__ == "__main__":
    lista1 = ListaEnlazada()
    op = -1

    while op != 0:
        print("\n --- Operaciones sobre listas ligadas --- ")
        print("1: Crear Lista")
        print("2: Mostrar Lista")
        print("3: Promedio de la lista")
        print("4: Personal: vaciar listas")
        print("5: Insertar al Inicio")
        print("6: Insertar al Final")
        print("7: Insertar antes de nodo X")
        print("8: Insertar despues de nodo X")
        print("9: Eliminar primer nodo")
        print("10: Eliminar último nodo")
        print("11: Eliminar nodo con información X")
        print("12: Busqueda de elemento")
        print("13: eliminar nodo antes de nodo X")
        print("0: Salir")
        try:
            op = int(input("\nElige una opcion: "))

            match op:
                case 1:
                    lista1.crear_lista()
                case 2:
                    lista1.mostrar_lista()
                case 3:
                    lista1.promedio_lista()
                case 4:
                    lista1.personal_vaciar_lista()
                case 5:
                    dato = int(input("Dame un número para insertarlo al inicio: "))
                    lista1.inserta_inicio(dato)
                case 6:
                    dato = int(input("Dame un número para insertarlo al final: "))
                    lista1.inserta_final(dato)
                case 7:
                    referencia = int(input("Dame un número para tomar referencia: "))
                    dato = int(
                        input(
                            "Dame un número para insertarlo anterior a la referencia: "
                        )
                    )
                    lista1.inserta_antes_de(dato, referencia)
                case 8:
                    referencia = int(input("Dame un número para tomar referencia: "))
                    dato = int(
                        input(
                            "Dame un número para insertarlo despues de la referencia: "
                        )
                    )
                    lista1.inserta_despues_de(dato, referencia)
                case 9:
                    lista1.eliminar_inicio()
                case 10:
                    lista1.Eliminar_ultimo()
                case 11:
                    dato = int(input("Dame un número para eliminar: "))
                    lista1.Eliminar_nodo_x(dato)
                case 12:
                    dato = int(input("Dame un número para buscarlo en la lista: "))
                    lista1.Busqueda(dato)
                case 13:
                    referencia = int(
                        input(
                            "Dame un número que este en la lists para tomar referencia: "
                        )
                    )
                    lista1.eliminar_nodo_antes_de(referencia)
                case 14:
                    referencia = int(
                        input(
                            "Dame un número que este en la lists para tomar referencia: "
                        )
                    )
                    lista1.eliminar_nodo_despues_de(referencia)
                case 0:
                    print("Adios")
                case _:
                    print("Opción no válida")
        except ValueError:
            print("Por favor, ingresa un valor numerico.")
