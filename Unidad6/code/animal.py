class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"{self.nombre} saluda")

class Perro(Animal):
    
    def ladrar(self):
        print(f"{self.nombre} está ladrando")

# Crear una instancia de la clase Perro
perro1 = Perro("Buddy")

# Llamar a métodos de la clase base y derivada
perro1.saludar()
perro1.ladrar()