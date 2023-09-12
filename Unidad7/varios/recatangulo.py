class Rectangulo:
    
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

# Crear dos instancias de Rectangulo
rectangulo1 = Rectangulo(5, 10)
rectangulo2 = Rectangulo(3, 7)

# Calcular el área de cada rectángulo
area1 = rectangulo1.calcular_area()
area2 = rectangulo2.calcular_area()

# Mostrar el área de cada rectángulo
print(f"Área del Rectángulo 1: {area1}")
print(f"Área del Rectángulo 2: {area2}")