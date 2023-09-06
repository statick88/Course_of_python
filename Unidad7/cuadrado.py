class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        area = self.lado ** 2
        return area

# Crear una instancia de Cuadrado
cuadrado1 = Cuadrado(4)

# Calcular y mostrar el área del cuadrado
area_cuadrado = cuadrado1.calcular_area()
print(f"Área del Cuadrado: {area_cuadrado}")