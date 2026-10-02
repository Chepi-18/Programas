datos = [10, 20, 30]
print(datos)
print(f" Longitud del arreglo: {len(datos)}")
print(f" Valor mínimo del arreglo: {min(datos)}")
print(f" Valor máximo del arreglo: {max(datos)}")
print(f" Suma de los valores del arreglo: {sum(datos)}")

nombres = ["Juan", "Maria"]
# agregar un elemento al final del arreglo
nombres.append("Jesus")
print(nombres)

# agregar un elemento en una posición específica
nombres.insert(1, "Panfilo")
print(nombres)

# eliminar un elemento del arreglo por la posición
extraido = nombres.pop(1)
print(extraido)
print(nombres)

# eliminar un elemento del arreglo por el nombre del elemento
nombres.remove("Jesus")
print(nombres)

valores = [4, 2, 1, 7]
# ordenar de mayor a menor
valores.sort(reverse=True)
print(valores)

# ordenar de menor a mayor
valores.sort()
print(valores)

# muestra la posición de un elemento en el arreglo
colores = ["rojo", "verde", "azul", "verde"]
posicion = colores.index("verde")
print(posicion)

# cuenta cuantas veces aparece un elemento en el arreglo
votos = ["a", "b", "b", "c", "d"]
total_b = votos.count("b")
print(total_b)
