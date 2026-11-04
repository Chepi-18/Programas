import os


def listar_archivos_recursivamente(ruta_directorio: str, nivel: int = 0):
    try:
        # 1 preparar la identacion visual
        indentacion = "-" * (nivel * 3)
        # os.path.basename se usa para extraer el ultimo elemento de la ruta y os.path.normpath limpia la ruta
        nombre_carpeta = os.path.basename(os.path.normpath(ruta_directorio))
        print(f"{indentacion}📁 carpeta: {nombre_carpeta}")
        # Genera una lista con los nombres de todo lo que está directamente dentro de la carpeta
        elementos = os.listdir(ruta_directorio)

        # 2 imprimir los archivos primero
        for elemento in elementos:
            #                   os.path.join le agrega la \ entre la ruta de directorio y el elemento
            ruta_completa = os.path.join(ruta_directorio, elemento)
            # vebuelve true si en la ruta el archivo si existe y no es una carpeta
            if os.path.isfile(ruta_completa):
                print(f"{indentacion}📄 {elemento}")

        # 3 llamada recursiva para las sub carpetas
        for elemento in elementos:
            ruta_completa = os.path.join(ruta_directorio, elemento)
            # *       os.path.isdir es casi lo mismo solo que para carpetas
            if os.path.isdir(ruta_completa):
                listar_archivos_recursivamente(ruta_completa, nivel + 1)

    except PermissionError:
        print(
            f" !!! No se pudo acceder a la carpeta: {ruta_directorio} (Permiso denegado)"
        )


def main():
    ruta_inicial = r"C:\Users\delga\Downloads\tercer semestre\Cultura empresarial"
    print(f"Iniciando la búsqueda en: {ruta_inicial}\n")
    if os.path.exists(ruta_inicial):
        listar_archivos_recursivamente(ruta_inicial, 0)
    else:
        print("La ruta no existe.")


if __name__ == "__main__":
    main()
