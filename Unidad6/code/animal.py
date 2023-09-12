class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        pass

class Perro(Animal):

    def saludar(self):
        print(f"{self.nombre} saluda soy un perro")
    
    def ladrar(self):
        print(f"{self.nombre} está ladrando")


class Gato(Animal):

    def saludar(self):
        print(f"{self.nombre} saluda soy un gato")

    def maullar(self):
        print(f"{self.nombre} está maullando")

# Crear una instancia de la clase Perro
perro1 = Perro("Buddy")

# Llamar a métodos de la clase base y derivada
perro1.saludar()
perro1.ladrar()

gato1 = Gato("Garfield")

gato1.saludar()
gato1.maullar()