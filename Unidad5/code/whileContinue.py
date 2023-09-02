contador = int(input("Por favor ingrese un número menor a 5: "))

while contador < 5:
    contador += 1
    if contador == 2:
        continue
    print("Contador:", contador)