class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

coche1 = Coche("Toyota", "Camry")
coche2 = Coche("Honda", "Civic")
coche3 = Coche("Ford", "Fiesta")
# coche4 = Coche()

print(coche1.marca, coche1.modelo)
print(coche2.marca, coche2.modelo)
print(coche3.marca, coche3.modelo)
# print(coche4.marca, coche4.modelo)