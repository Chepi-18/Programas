def calcular_salario_neto(bruto: float, impuestos: float) -> float:
    return bruto - (bruto * impuestos / 100)


Bruto = float(input("Ingresa tu sueldo bruto: "))
Inpuestos = float(input("Ingresa tu Inpuestos: "))
print(calcular_salario_neto(Bruto, Inpuestos))
