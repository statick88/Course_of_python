class Triangulo:
    def __init__(self, base=2, altura=2):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

# Crear una instancia de Triángulo
triangulo1 = Triangulo(6,8)

# Calcular el área del triángulo
area_triangulo = triangulo1.calcular_area()

# Mostrar el área del triángulo
print(f"Área del Triángulo: {area_triangulo}")