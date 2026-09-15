# alcance de variables
impuesto = 0.16 # Variable Global

def calcular_precio_final(precio_base: float) -> float:
# 'precio_base' es local.
# Puede LEER la variable global 'impuesto' sin problema.
    return precio_base + (precio_base * impuesto)

resultadoPrecio = calcular_precio_final(500)
print(f"El precio modificado es {resultadoPrecio}")