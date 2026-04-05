# Cheat Sheet — Módulo 3: Estructuras de Control

> Referencia rápida de todas las estructuras de control de Python.

---

## Decisiones: `if`, `elif`, `else`

```python
# Estructura básica
if condicion:
    # se ejecuta si condicion es True
    pass
elif otra_condicion:
    # se ejecuta si la anterior fue False y esta es True
    pass
else:
    # se ejecuta si todas las anteriores fueron False
    pass
```

### Operadores de comparación

| Operador | Significado | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Diferente de | `5 != 3` | `True` |
| `>` | Mayor que | `10 > 3` | `True` |
| `<` | Menor que | `3 < 10` | `True` |
| `>=` | Mayor o igual | `5 >= 5` | `True` |
| `<=` | Menor o igual | `3 <= 5` | `True` |

### Operadores lógicos

| Operador | Descripción | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `and` | Ambas deben ser True | `True and False` | `False` |
| `or` | Al menos una True | `True or False` | `True` |
| `not` | Invierte el valor | `not True` | `False` |

### Operador ternario

```python
resultado = "mayor" if edad >= 18 else "menor"
```

---

## Bucles: `for`

```python
# Iterar sobre una lista
for item in lista:
    print(item)

# Iterar con índice
for i, item in enumerate(lista):
    print(f"{i}: {item}")

# Iterar con índice desde 1
for i, item in enumerate(lista, start=1):
    print(f"{i}. {item}")

# Iterar un número de veces
for i in range(10):        # 0 a 9
for i in range(1, 11):     # 1 a 10
for i in range(0, 20, 5):  # 0, 5, 10, 15
for i in range(10, 0, -1): # 10, 9, 8, ..., 1
```

### Iterar diccionarios

```python
# Solo claves
for clave in diccionario:
    print(clave)

# Solo valores
for valor in diccionario.values():
    print(valor)

# Clave y valor
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")
```

---

## Bucles: `while`

```python
# Bucle con condición
while condicion:
    # se repite mientras condicion sea True
    pass

# Bucle infinito controlado
while True:
    # hacer algo
    if condicion_salida:
        break

# Validación de entrada
while not valido:
    entrada = input("Ingresa un valor: ")
    if es_valido(entrada):
        valido = True
```

---

## Control de flujo

| Instrucción | Qué hace |
|-------------|----------|
| `break` | Sale del bucle inmediatamente |
| `continue` | Salta al siguiente elemento |
| `else` (del bucle) | Se ejecuta si el bucle terminó sin `break` |

### `else` en bucles

```python
for item in lista:
    if item == buscado:
        print("Encontrado")
        break
else:
    # Se ejecuta SOLO si NO hubo break
    print("No encontrado")
```

---

## Comprensión de listas

```python
# Básica
cuadrados = [x**2 for x in range(10)]

# Con filtro
pares = [x for x in range(20) if x % 2 == 0]

# Con transformación
nombres = [nombre.capitalize() for nombre in lista]

# Con if/else (ternario)
tipo = ["par" if x % 2 == 0 else "impar" for x in range(10)]

# Diccionario
cuadrados_dict = {x: x**2 for x in range(10)}

# Conjunto
unicos = {x for x in lista}
```

---

## Patrones comunes

### Acumulador

```python
total = 0
for valor in valores:
    total = total + valor
```

### Contador

```python
contador = 0
for item in items:
    if cumple_condicion(item):
        contador = contador + 1
```

### Búsqueda

```python
encontrado = False
for item in lista:
    if item == buscado:
        encontrado = True
        break
```

### Guard clauses

```python
def procesar(datos):
    if not datos:
        return "Sin datos"
    if not datos.es_valido():
        return "Datos inválidos"
    # Camino feliz
    return procesar_datos(datos)
```

### Menú interactivo

```python
while True:
    print("1. Opción A")
    print("2. Opción B")
    print("3. Salir")
    
    opcion = input("Elige: ")
    
    if opcion == "1":
        hacer_a()
    elif opcion == "2":
        hacer_b()
    elif opcion == "3":
        break
    else:
        print("Opción no válida")
```

---

## Decisiones rápidas

| ¿Qué necesitas? | Usa... |
|-----------------|--------|
| Decidir entre opciones | `if/elif/else` |
| Recorrer una colección | `for` |
| Repetir N veces | `for` + `range()` |
| Repetir hasta condición | `while` |
| Salir del bucle | `break` |
| Saltar iteración | `continue` |
| Crear lista rápido | Comprensión |
| Validar entrada | `while` + `break` |
| Múltiples validaciones | Guard clauses |

---

## Principios del Zen aplicados

| Principio | Aplicación |
|-----------|-----------|
| **Beautiful is better than ugly** | Comprensiones elegantes |
| **Readability counts** | Guard clauses, nombres claros |
| **Simple is better than complex** | `for item in lista` > índices |
| **Flat is better than nested** | Validaciones tempranas |
| **Explicit is better than implicit** | Condiciones con nombres |
| **Errors should never pass silently** | Validar entrada del usuario |

---

*Referencia rápida del Módulo 3 — Curso de Python*
