class CuentaBancaria:
    def __init__(self, saldo):
        # Atributo privado con un guion bajo al principio
        self._saldo = saldo

    # Método de acceso (Getter)
    def obtener_saldo(self):
        return self._saldo

    # Método de acceso (Setter)
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad

    # Método de acceso (Setter)
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad

# Crear una instancia de la clase CuentaBancaria
cuenta = CuentaBancaria(1000)

# Acceder al saldo utilizando el método de acceso
print("Saldo inicial:", cuenta.obtener_saldo())

# Realizar un depósito
cuenta.depositar(500)
print("Saldo después del depósito:", cuenta.obtener_saldo())

# Realizar un retiro
cuenta.retirar(200)
print("Saldo después del retiro:", cuenta.obtener_saldo())