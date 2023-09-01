"""
Desarrolla un programa que simule una lista de compras. 
Permite al usuario agregar elementos a la lista y 
luego imprimir la lista completa.
"""
compras1 = input("Por favor ingrese el primer producto ")
compras2 = input("Por favor ingrese el segundo producto ")
compras3 = input("Por favor ingrese el tercero producto ")

# compras = [compras1, compras2, compras3]

compras = []
compras.append(compras1)
compras.append(compras2)
compras.append(compras3)
print("La lista de compras es: ", compras)

compras_copy = compras.copy()
print(compras_copy)

compras_clear = compras.clear()
print(compras_clear)

compras.insert()


