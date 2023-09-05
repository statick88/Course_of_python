"""
Crea una función recursiva llamada potencia que calcule la potencia de un número base elevado a un exponente.
Utiliza la función para calcular 2^3 y muestra el resultado en la consola.
"""
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

resultado = potencia(2, 3)
print("El resultado de 2^3 es:", resultado)
