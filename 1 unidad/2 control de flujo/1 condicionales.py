calificacion = int(input("Introduce tu calificacion: "))
if calificacion == 100:
    print("calificacion perfecta!")
elif calificacion >= 80 and calificacion <= 90:
    print("Buen promedio")
elif calificacion >= 70:
    print("Aprobado")
else:
    print("Reprobado")
