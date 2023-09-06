class Estudiante:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

estudiante1 = Estudiante("Ana", 20)
print(estudiante1.nombre)
print(estudiante1.edad)

estudiante2 = Estudiante("Juan", 22)
print(estudiante2.nombre)
print(estudiante2.edad)