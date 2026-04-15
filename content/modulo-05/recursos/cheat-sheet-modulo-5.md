# Cheat Sheet — Módulo 5: Listas y Tuplas

## 📋 Crear listas y tuplas

```python
# Listas (mutables)
vacia = []                          # Lista vacía
numeros = [1, 2, 3, 4, 5]          # Lista de enteros
mixta = ["Ana", 25, True]           # Tipos mixtos
desde_rango = list(range(5))        # [0, 1, 2, 3, 4]
desde_texto = list("Python")        # ['P', 'y', 't', 'h', 'o', 'n']

# Tuplas (inmutables)
coordenada = (10, 20)               # Tupla de 2 elementos
un_elemento = (42,)                 # ¡La coma es obligatoria!
desde_lista = tuple([1, 2, 3])      # (1, 2, 3)
sin_parentesis = 1, 2, 3            # También es tupla
```

## 🔍 Acceder a elementos

```python
lista = ["a", "b", "c", "d", "e"]

# Índices positivos
lista[0]     # "a" — primer elemento
lista[2]     # "c" — tercer elemento
lista[4]     # "e" — último elemento

# Índices negativos
lista[-1]    # "e" — último elemento
lista[-2]    # "d" — penúltimo elemento
lista[-5]    # "a" — primer elemento

# Slicing [inicio:fin:paso]
lista[1:4]   # ["b", "c", "d"] — del 1 al 3
lista[:3]    # ["a", "b", "c"] — desde el inicio
lista[2:]    # ["c", "d", "e"] — hasta el final
lista[::2]   # ["a", "c", "e"] — cada 2
lista[::-1]  # ["e", "d", "c", "b", "a"] — invertida
lista[:]     # Copia de toda la lista
```

## ➕ Agregar elementos

| Método | Qué hace | Ejemplo |
|--------|----------|---------|
| `append(x)` | Agrega al final | `lista.append("x")` |
| `insert(i, x)` | Inserta en posición `i` | `lista.insert(0, "x")` |
| `extend(iterable)` | Agrega varios | `lista.extend(["a", "b"])` |

## ➖ Eliminar elementos

| Método | Qué hace | Devuelve |
|--------|----------|----------|
| `remove(x)` | Elimina primera aparición de `x` | `None` |
| `pop(i)` | Elimina elemento en posición `i` | El elemento |
| `pop()` | Elimina el último | El elemento |
| `clear()` | Vacía la lista | `None` |
| `del lista[i]` | Elimina por índice | — |
| `del lista[i:j]` | Elimina por rango | — |

## 🔧 Transformar

| Método | Qué hace | Modifica original |
|--------|----------|:-----------------:|
| `sort()` | Ordena ascendente | ✅ Sí |
| `sort(reverse=True)` | Ordena descendente | ✅ Sí |
| `reverse()` | Invierte el orden | ✅ Sí |
| `sorted(lista)` | Devuelve nueva lista ordenada | ❌ No |
| `copy()` | Copia superficial | ❌ No |

## 🔎 Buscar

```python
lista = ["a", "b", "c", "a", "b"]

"b" in lista              # True — existe
"c" not in lista          # False — sí existe
lista.index("b")          # 1 — primera posición
lista.count("a")          # 2 — cuántas veces aparece
```

## 🔄 Iterar

```python
frutas = ["manzana", "banana", "cereza"]

# Solo valores
for fruta in frutas:
    print(fruta)

# Índice + valor
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")

# Índice + valor (desde 1)
for i, fruta in enumerate(frutas, start=1):
    print(f"{i}. {fruta}")

# Dos listas en paralelo
nombres = ["Ana", "Carlos"]
edades = [25, 30]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre}: {edad} años")
```

## 📝 List Comprehensions

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Transformar
cuadrados = [n ** 2 for n in numeros]           # [1, 4, 9, 16, ...]

# Filtrar
pares = [n for n in numeros if n % 2 == 0]      # [2, 4, 6, 8, 10]

# Transformar + Filtrar
dobles_pares = [n * 2 for n in numeros if n % 2 == 0]  # [4, 8, 12, 16, 20]

# Matriz 3x3 de ceros
matriz = [[0] * 3 for _ in range(3)]
```

## 📐 Listas anidadas (matrices)

```python
# Crear matriz 3x4
matriz = [[0] * 4 for _ in range(3)]

# Acceder
matriz[0][0]    # Fila 0, Columna 0
matriz[1][2]    # Fila 1, Columna 2
matriz[0]       # Fila 0 completa

# Recorrer
for fila in matriz:
    for celda in fila:
        print(celda, end=" ")
    print()

# Con posiciones
for i, fila in enumerate(matriz):
    for j, celda in enumerate(fila):
        print(f"[{i}][{j}] = {celda}")

# ⚠️ NUNCA hacer esto (referencias compartidas):
# matriz_mal = [[0] * 4] * 3
```

## 🎯 Tuplas: desempaquetado

```python
# Básico
coordenada = (10, 20)
x, y = coordenada          # x=10, y=20

# Intercambio
a, b = b, a                # Sin variable temporal

# Capturar resto
primero, *resto = [1, 2, 3, 4, 5]   # primero=1, resto=[2, 3, 4, 5]
*inicio, ultimo = [1, 2, 3, 4, 5]   # inicio=[1, 2, 3, 4], ultimo=5
primero, *medio, ultimo = [1, 2, 3, 4, 5]  # primero=1, medio=[2, 3, 4], ultimo=5
```

## ⚖️ Lista vs Tupla: ¿cuándo usar cada una?

| Criterio | Lista `[]` | Tupla `()` |
|----------|:----------:|:----------:|
| Datos que cambian | ✅ | ❌ |
| Agregar/quitar elementos | ✅ | ❌ |
| Datos fijos/constantes | ⚠️ | ✅ |
| Clave de diccionario | ❌ | ✅ |
| Heterogéneos (tipos mixtos) | ⚠️ | ✅ |
| Rendimiento | Normal | Más rápida |
| Protección contra cambios | ❌ | ✅ |

## ⚠️ Errores comunes

```python
# ❌ Índice fuera de rango
lista = [1, 2, 3]
# lista[3]  → IndexError

# ✅ Verificar antes
if len(lista) > 3:
    print(lista[3])

# ❌ Modificar mientras se itera
# for x in lista:
#     lista.remove(x)  → Comportamiento impredecible

# ✅ Crear nueva lista
lista = [x for x in lista if condicion]

# ❌ sort() devuelve None
# resultado = lista.sort()  → resultado es None

# ✅ sort() modifica en su lugar
lista.sort()
resultado = lista

# ❌ Matriz con referencias compartidas
# matriz = [[0]*3] * 3  → Todas las filas son la misma lista

# ✅ Matriz con listas independientes
matriz = [[0]*3 for _ in range(3)]
```

## 🧮 Funciones útiles con listas

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

len(numeros)      # 8 — cantidad de elementos
sum(numeros)      # 31 — suma total
max(numeros)      # 9 — valor máximo
min(numeros)      # 1 — valor mínimo
sorted(numeros)   # [1, 1, 2, 3, 4, 5, 6, 9] — nueva lista ordenada
reversed(numeros) # Iterador invertido
```
