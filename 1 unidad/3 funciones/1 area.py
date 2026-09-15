def calcular_area_rectangulo(base: float, altura: float) -> float:
    # La variable 'area' se crea en el momento
    area = base * altura
    return area


# Llamada a la función
base = float(input("Introduce la base "))
altura = float(input("Introduce la altura "))

resultado = calcular_area_rectangulo(base, altura)
print(f"El área es: {resultado}")
