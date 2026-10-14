# Cheat Sheet — Módulo 6: Diccionarios y Sets

## Diccionarios

### Creación

```python
# Forma recomendada
persona = {"nombre": "Ana", "edad": 28}

# Alternativa con dict()
config = dict(host="localhost", puerto=8080)

# Vacío
datos = {}
```

### Acceso

```python
dic = {"nombre": "Ana", "edad": 28}

# Directo (error si no existe)
nombre = dic["nombre"]

# Seguro (None si no existe)
email = dic.get("email")

# Con valor por defecto
email = dic.get("email", "no@email.com")
```

### Modificación

```python
# Agregar o modificar
dic["edad"] = 29
dic["email"] = "ana@correo.com"

# Actualizar varios
dic.update({"ciudad": "Quito", "pais": "Ecuador"})

# Crear si no existe
dic.setdefault("rol", "usuario")
```

### Eliminación

```python
# Eliminar sin devolver
del dic["email"]

# Eliminar y devolver valor
valor = dic.pop("edad", None)

# Eliminar último par (clave, valor)
clave, valor = dic.popitem()
```

### Iteración

```python
# Solo claves
for clave in dic:
    print(clave)

# Solo valores
for valor in dic.values():
    print(valor)

# Clave y valor (más común)
for clave, valor in dic.items():
    print(f"{clave}: {valor}")
```

### Comprensión de diccionarios

```python
# Crear diccionario al vuelo
cuadrados = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Con filtro
pares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

### Verificar existencia

```python
if "nombre" in dic:
    print("Existe")

if "email" not in dic:
    print("No existe")
```

---

## Sets

### Creación

```python
# Con llaves
colores = {"rojo", "azul", "verde"}

# Desde lista (elimina duplicados)
numeros = set([1, 2, 3, 2, 1])  # {1, 2, 3}

# Vacío (¡OJO! {} es diccionario)
conjunto = set()
```

### Operaciones básicas

```python
s = {1, 2, 3}

# Agregar
s.add(4)

# Eliminar (error si no existe)
s.remove(2)

# Eliminar (seguro, sin error)
s.discard(99)
```

### Operaciones de conjuntos

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Unión: todos los elementos
a | b  # {1, 2, 3, 4, 5, 6}

# Intersección: elementos comunes
a & b  # {3, 4}

# Diferencia: en A pero no en B
a - b  # {1, 2}

# Diferencia simétrica: en uno u otro, no en ambos
a ^ b  # {1, 2, 5, 6}

# Subconjunto
{1, 2} <= a  # True

# Superconjunto
a >= {1, 2}  # True
```

### Métodos equivalentes

| Operador | Método |
|----------|--------|
| `\|` | `.union()` |
| `&` | `.intersection()` |
| `-` | `.difference()` |
| `^` | `.symmetric_difference()` |

---

## JSON

```python
import json

# Diccionario → JSON string
json_str = json.dumps(dic, indent=2)

# JSON string → Diccionario
dic = json.loads(json_str)

# Guardar en archivo
with open("datos.json", "w") as f:
    json.dump(dic, f, indent=2)

# Leer desde archivo
with open("datos.json", "r") as f:
    dic = json.load(f)
```

### Conversión de tipos

| Python | JSON |
|--------|------|
| `dict` | `object` |
| `list` | `array` |
| `str` | `string` |
| `int` / `float` | `number` |
| `True` | `true` |
| `False` | `false` |
| `None` | `null` |

---

## ¿Cuándo usar cada estructura?

| Necesitas... | Elige... |
|--------------|----------|
| Orden y posición | Lista `[]` |
| Búsqueda por nombre | Diccionario `{}` |
| Sin duplicados | Set `{}` |
| Búsqueda rápida | Set `{}` |
| Datos con atributos | Diccionario `{}` |
| Operaciones de conjunto | Set `{}` |

---

## Errores comunes

```python
# ❌ Clave inexistente con []
valor = dic["clave_inexistente"]  # KeyError

# ✅ Usar .get() con valor por defecto
valor = dic.get("clave_inexistente", "default")

# ❌ {} crea diccionario, no set
conjunto = {}  # dict, no set!

# ✅ set() para set vacío
conjunto = set()

# ❌ Modificar diccionario mientras iteras
for k in dic:
    del dic[k]  # RuntimeError

# ✅ Iterar sobre copia de claves
for k in list(dic.keys()):
    del dic[k]
```

---

*Referencia rápida del Módulo 6 — Curso de Python Fundamentos*
