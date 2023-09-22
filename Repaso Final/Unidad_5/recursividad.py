# Función recursiva para calcular el factorial
def factorial(n):
    # Caso base
    if n == 1:
        return 1
    # Llamada recursiva
    else:
        return n * factorial(n - 1)

resultado = factorial(5)
print("El factorial de 5 es:", resultado)