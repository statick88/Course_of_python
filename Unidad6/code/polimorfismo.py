class Animal:
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "Guau"

class Gato(Animal):
    def sonido(self):
        return "Miau"

def hacer_sonar(animal):
    print(animal.sonido())

# Crear instancias de las clases
perro = Perro()
gato = Gato()

# Llamar a la función con objetos de diferentes clases
hacer_sonar(perro)  # Salida: Guau
hacer_sonar(gato)   # Salida: Miau