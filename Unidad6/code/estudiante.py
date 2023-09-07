class Estudiante:
    def __init__(self, nombre):
        # Atributo privado con un guion bajo al principio
        self._nombre = nombre

    # Método de acceso (Getter)
    def get_nombre(self):
        return self._nombre

    # Método de acceso (Setter)
    def set_nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre

# Crea una instancia de la clase Estudiante con nombre "Juan"
estudiante = Estudiante("Juan")

# Acceder al nombre utilizando el método de acceso get_nombre
print("Nombre del estudiante:", estudiante.get_nombre())

# Cambiar el nombre utilizando el método de acceso set_nombre
estudiante.set_nombre("María")
# Imprimir el nombre después del cambio
print("Nombre del estudiante después del cambio:", estudiante.get_nombre())