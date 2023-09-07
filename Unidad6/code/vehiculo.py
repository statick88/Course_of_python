class Vehículo:
    def arrancar(self):
        print("El vehículo arranca")

class Coche(Vehículo):
    def arrancar(self):
        print("El coche arranca")

class Motocicleta(Vehículo):
    def arrancar(self):
        print("La motocicleta arranca")

coche = Coche()
motocicleta = Motocicleta()

coche.arrancar()
motocicleta.arrancar()