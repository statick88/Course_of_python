# Ejemplo de código en Python
# Puede incluir múltiples bloques de código si es necesario.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"{self.nombre} saluda"

class Perro(Animal):
    def ladrar(self):
        return f"{self.nombre} está ladrando"

# Crear una instancia de la clase Perro
perro1 = Perro("Buddy")

# Llamar a métodos de la clase base y derivada
saludar = perro1.saludar()
ladrar = perro1.ladrar()

print(saludar)
print(ladrar)