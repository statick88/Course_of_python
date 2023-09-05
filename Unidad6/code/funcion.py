def saludar(nombre="Diego"):
    return "Hola bienvenido, " + nombre

mensaje = saludar()
print(mensaje)

mensaje = saludar("Maria")
print(mensaje)

def suma(num1, num2):
    return num1 + num2

respuesta = suma(1, 4)
print(respuesta) #5

def calcular_cuadrado(numero):
    """Esta función espera como parámetro un valor entero"""
    respuesta = numero**2
    return f"el cuadrado del numero es {respuesta}" 

mensaje3 = calcular_cuadrado(4)
print(mensaje3)