# Calculadora Interactiva

# Presenta el menú de opciones al usuario
print("Calculadora Interactiva")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Solicita al usuario seleccionar una opción
opcion = int(input("Selecciona una opción: "))

# Solicita al usuario los números para realizar la operación
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Realiza la operación correspondiente según la opción 
# seleccionada
if opcion == 1:
    resultado = num1 + num2
    operacion = "suma"
elif opcion == 2:
    resultado = num1 - num2
    operacion = "resta"
elif opcion == 3:
    resultado = num1 * num2
    operacion = "multiplicación"
elif opcion == 4:
    if num2 != 0:
        resultado = num1 / num2
        operacion = "división"
    else:
        resultado = "Error: división por cero"
        operacion = "división"

# Muestra el resultado de la operación
if isinstance(resultado, float):
    print(f"El resultado de la {operacion} es: {resultado:.2f}")
else:
    print(resultado)