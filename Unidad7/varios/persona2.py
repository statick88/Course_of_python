class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear una instancia de Persona
persona1 = Persona("Ana", 30)

# Llamar al método saludar para mostrar un saludo personalizado
persona1.saludar()

persona2 = Persona("Diego", 35)
persona2.saludar()