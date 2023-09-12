class Carro:

    def __init__(self, color, motor, creacion):
        self.color = color
        self.motor = motor
        self.creacion = creacion

    def acelerar(self):
        return f"Estoy acelerando con mi motor {self.motor} en mi carrito color {self.color}"

Corsa = Carro("Negro", 1.8, 2006)
print(Corsa.color)
print(Corsa.acelerar())

Toyota = Carro("Rojo", 2000, 2012)
print(Toyota.color)
print(Toyota.acelerar())

Kia = Carro("Cafe", 3000, 2019)
print(Kia.color)
print(Kia.acelerar())