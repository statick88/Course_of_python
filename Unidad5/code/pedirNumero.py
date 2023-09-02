"""
Crea un programa que solicite al usuario un número y determine si es positivo, 
negativo o cero.
"""
numero = int(input("Por favor ingrese un número: "))

if numero > 0:
    # print(f"El número {numero} es positivo")
    print("El número " + str(numero) + " es positivo")
elif numero < 0:
    print(f"El número {numero} es negativo")
else:
    print(f"El número {numero} es 0")