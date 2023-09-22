# Ejemplo de código en Python
# Puede incluir múltiples bloques de código si es necesario.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Me llamo {self.nombre} y tengo {self.edad} años."

# Crear una instancia de Persona
persona1 = Persona("Carlos", 28)

# Llamar al método para presentarse
presentarse = persona1.presentarse()
print(presentarse)