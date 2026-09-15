try:

    archivo = open("Datos.txt", "r")
    # Intentamos leer el archivo ...
    print(archivo.read())

except FileNotFoundError:
    print("Error: El archivo no existe en la carpeta.")

else:
    # Esto corre solo si el archivo se abrió correctamente
    print("Lectura exitosa, procesando datos ... ")

finally:
    # Esto corre pase lo que pase (haya existido el archivo o no, falle o no)
    print("Terminó el bloque de ejecución.")
    archivo.close()
