# Guía del Instructor — Módulo 5: Listas y Tuplas

## Objetivos de Aprendizaje

Al finalizar este módulo, el estudiante será capaz de:

1. Crear y manipular listas (crear, agregar, eliminar, ordenar)
2. Acceder a elementos mediante índices y slicing
3. Recorrer listas con diferentes métodos
4. Comprender las diferencias entre listas y tuplas
5. Usar listas anidadas para estructuras de datos complejas

## Duración Estimada

- **Teoría**: 2 horas
- **Práctica**: 3 horas
- **Desafíos**: 2 horas
- **Total**: 7 horas

## Estructura de la Sesión

### Sesión 1: Fundamentos de Listas (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-30 min | Repaso Módulo 4 | Funciones |
| 30-75 min | Crear listas, índices | 01-crear-listas.qmd, 02-indexar-slicing.qmd |
| 75-120 min | Métodos de listas | 03-metodos-listas.qmd |

### Sesión 2: Recorrido y TUPLAS (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-45 min | Iterar listas | 04-iterar-listas.qmd |
| 45-90 min | Tuplas (inmutabilidad) | 05-tuplas.qmd |
| 90-120 min | Listas anidadas | 06-listas-anidadas.qmd |

### Sesión 3: Desafíos (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-60 min | Desafíos 1-4 (progresivos) | desafios/01-04 |
| 60-120 min | Desafíos 5-7 (avanzados) | desafios/05-07 |

## Preguntas Frecuentes Anticipadas

### ¿Las listas pueden tener tipos mixtos?

**Respuesta:** Sí, una lista puede contener integers, strings, floats, etc. Pero no es buena práctica.

### ¿Cuál es la diferencia entre append() y extend()?

**Respuesta:** `append()` agrega un elemento (puede ser lista). `extend()` agrega cada elemento de otra lista.

```python
lista = [1, 2]
lista.append([3, 4])   # [1, 2, [3, 4]]
lista.extend([3, 4])   # [1, 2, 3, 4]
```

### ¿Las tuplas tienen métodos como las listas?

**Respuesta:** Las tuplas tienen solo `count()` e `index()`. Son inmutables, no puedes agregar/eliminar elementos.

### ¿Para qué sirve enumerate()?

**Respuesta:** Para obtener índice y valor al mismo tiempo:
```python
for i, nombre in enumerate(nombres):
    print(f"{i+1}. {nombre}")
```

## Analogías para Enseñar

### Lista como un tren
> "Cada wagon es un elemento. Puedes agregar wagons (append), quitar wagons (pop), o reordenar el tren. Cada wagon tiene su número (índice)."

### Tupla como un contrato
> "Una vez firmado, no se puede cambiar. Es inmutable. Pero puedes leerlo (acceder a elementos)."

## Soluciones de Desafíos

### Desafío 4: Estadísticas de Lista

```python
def estadisticas(numeros):
    return {
        "media": sum(numeros) / len(numeros),
        "max": max(numeros),
        "min": min(numeros),
        "ordenada": sorted(numeros)
    }

datos = [5, 10, 3, 8, 12]
resultado = estadisticas(datos)
print(f"Media: {resultado['media']}")  # 7.6
print(f"Máx: {resultado['max']}")       # 12
```

### Desafío 6: Operaciones con Matrices

```python
def suma_matrices(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] 
            for i in range(len(a))]

# o con bucles tradicionales
def suma_matrices(a, b):
    resultado = []
    for i in range(len(a)):
        fila = []
        for j in range(len(a[0])):
            fila.append(a[i][j] + b[i][j])
        resultado.append(fila)
    return resultado
```

### Desafío 7: Gestor de Inventario

```python
inventario = [
    {"nombre": "Laptop", "cantidad": 5, "precio": 999.99},
    {"nombre": "Mouse", "cantidad": 20, "precio": 19.99},
]

def buscar_producto(nombre):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None

def actualizar_stock(nombre, cantidad):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            producto["cantidad"] += cantidad
            return True
    return False
```

## Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| IndexError | Índice negativo o mayor a len-1 | Verificar `len(lista)` antes de acceder |
| List assignment | Intentar modificar string inmutable | Usar listas para datos mutables |
| Mutating while iterating | Modificar lista mientras iteras | Iterar sobre copia: `for x in lista[:]` |

## Evaluación

| Criterio | Peso |
|----------|------|
| Desafíos completados | 40% |
| Uso correcto de métodos | 25% |
| Manejo de casos borde | 20% |
| Código limpio | 15% |