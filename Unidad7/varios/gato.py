class Gato:
    def __init__(self, nombre):
        self.nombre = nombre

    def maullar(self):
        print(f"{self.nombre} está maullando.")

gato1 = Gato("Mittens")
gato2 = Gato("Whiskers")

gato1.maullar()
gato2.maullar()