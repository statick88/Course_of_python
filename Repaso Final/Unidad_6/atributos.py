class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

producto1 = Producto("Teléfono", 500)
print(f"Producto: {producto1.nombre}, Precio: {producto1.precio}")