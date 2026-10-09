def calcular_fibonacci(n):
    if n <= 1:
        return n

    anterior, actual = 0, 1

    for _ in range(2, n + 1):
        anterior, actual = actual, anterior + actual

    return actual
