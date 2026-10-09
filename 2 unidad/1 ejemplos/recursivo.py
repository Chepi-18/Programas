def calcular_fibonacci(n):
    if n <= 1:
        return n

    return calcular_fibonacci(n - 1) + calcular_fibonacci(n - 2)
