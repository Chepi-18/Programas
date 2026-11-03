import os
import time
from tqdm import tqdm


def contar_elementos_totales(ruta_directorio: str) -> int:
    total = 0
    try:
        for root, dirs, files in os.walk(ruta_directorio):
            total += len(dirs) + len(files)
    except PermissionError:
        pass
    return total


def listar_archivos_recursivamente(
    ruta_directorio: str, barra_progreso: tqdm, nivel: int = 0, retardo: float = 0.02
):
    try:
        indentacion = "   " * nivel
        nombre_carpeta = os.path.basename(os.path.normpath(ruta_directorio))

        tqdm.write(f"{indentacion}📁 Carpeta: {nombre_carpeta}")

        elementos = os.listdir(ruta_directorio)

        # 1. Imprimir archivos y actualizar la barra
        for elemento in elementos:
            ruta_completa = os.path.join(ruta_directorio, elemento)
            if os.path.isfile(ruta_completa):
                tqdm.write(f"{indentacion}   📄 {elemento}")
                barra_progreso.update(1)
                time.sleep(retardo)  # Pausa artificial para visualizar la barra

        # 2. Llamada recursiva para subcarpetas
        for elemento in elementos:
            ruta_completa = os.path.join(ruta_directorio, elemento)
            if os.path.isdir(ruta_completa):
                barra_progreso.update(1)
                time.sleep(retardo)
                listar_archivos_recursivamente(
                    ruta_completa, barra_progreso, nivel + 1, retardo
                )

    except PermissionError:
        tqdm.write(
            f"{indentacion}   ⚠️ No se pudo acceder: {ruta_directorio} (Permiso denegado)"
        )


def main():
    ruta_inicial = r"C:\Users\delga\Downloads"
    print(f"Calculando elementos en: {ruta_inicial}...")

    if os.path.exists(ruta_inicial):
        total_elementos = contar_elementos_totales(ruta_inicial)
        print(f"Total de elementos encontrados: {total_elementos}\n")

        if total_elementos == 0:
            print("La carpeta está vacía o no contiene archivos accesibles.")
            return

        # Ajusta retardo a 0.02 para pausar la animación, o a 0 para velocidad real
        retardo_visual = 0.02

        with tqdm(
            total=total_elementos, desc="Escaneando directorio", unit="elem"
        ) as barra_progreso:
            listar_archivos_recursivamente(
                ruta_inicial, barra_progreso, nivel=0, retardo=retardo_visual
            )
    else:
        print("La ruta especificada no existe.")


if __name__ == "__main__":
    main()
