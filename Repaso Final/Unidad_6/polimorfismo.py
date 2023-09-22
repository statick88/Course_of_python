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
    return animal.sonido()

# Crear instancias de las clases
perro = Perro()
gato = Gato()

# Llamar a la función con objetos de diferentes clases
ladrar = hacer_sonar(perro)  
maullar = hacer_sonar(gato)   

print(ladrar) # Salida: Guau
print(maullar) # Salida: Miau