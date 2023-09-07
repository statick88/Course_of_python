"""
Crea una clase Figura con un atributo “color” y un método 
“mostrar_color” para mostrar el color de la figura.
Crea una clase derivada Circulo que herede de “Figura” y 
agregue un atributo “radio” y un método “calcular_area” 
para calcular el área del círculo.
"""

class Figura:

    def __init__(self, color):
        self.color = color

    def mostrar_color(self):
        print(f"Su color es {self.color}")

class Circulo(Figura):

    radio = float(input("Por favor ingrese el radio: "))
    calculo = 3.14*(radio*radio)

    def calcular_area(self):
        print(f"El area es: {self.calculo}")

circulo1 = Circulo("negro")
circulo1.calcular_area()

