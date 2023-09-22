class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

coche1 = Coche("Toyota", "Corola")
coche1.mostrar_info()

coche2 = Coche("Ford", "Fiesta")
coche2.mostrar_info()