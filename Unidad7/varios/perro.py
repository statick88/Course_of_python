class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} está ladrando.")

perro1 = Perro("Max", "Labrador")
perro1.ladrar()