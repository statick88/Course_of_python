# Definición de la clase base "Figura" con un constructor que toma el atributo "color".
class Figura:
    def __init__(self, color):
        self.color = color

    # Método en la clase base para mostrar el color de la figura.
    def mostrar_color(self):
        print(f"Color: {self.color}")

# Definición de la clase derivada "Circulo" que hereda de "Figura" y agrega un atributo "radio".
class Circulo(Figura):
    def __init__(self, color, radio):
        # Llamamos al constructor de la clase base "Figura" utilizando "super()".
        super().__init__(color)
        self.radio = radio

    # Método en la clase derivada para calcular el área del círculo.
    def calcular_area(self):
        area = 3.14 * self.radio ** 2
        return area

# Creación de una instancia de la clase "Circulo" llamada "circulo1" con color "Rojo" y radio 5.
circulo1 = Circulo("Rojo", 5)

# Llamada al método "mostrar_color" de la clase base para mostrar el color del círculo.
circulo1.mostrar_color()

# Llamada al método "calcular_area" de la clase derivada para calcular el área del círculo.
area = circulo1.calcular_area()

# Imprimir el resultado del cálculo del área.
print(f"Área del círculo: {area}")