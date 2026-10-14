# 📋 Cheat Sheet — Módulo 2: Tipos de Datos y Variables

> Referencia rápida de operadores, casting y métodos de strings en Python.

---

## 🔢 Operadores Aritméticos

| Operador | Nombre | Ejemplo | Resultado |
|----------|--------|---------|-----------|
| `+` | Suma | `10 + 3` | `13` |
| `-` | Resta | `10 - 3` | `7` |
| `*` | Multiplicación | `10 * 3` | `30` |
| `/` | División (float) | `10 / 3` | `3.333...` |
| `//` | División entera | `10 // 3` | `3` |
| `%` | Módulo (residuo) | `10 % 3` | `1` |
| `**` | Potencia | `2 ** 3` | `8` |

### Operadores de asignación compuesta

```python
x += 5   # x = x + 5
x -= 3   # x = x - 3
x *= 2   # x = x * 2
x /= 4   # x = x / 4
x //= 2  # x = x // 2
x %= 3   # x = x % 3
x **= 2  # x = x ** 2
```

### Precedencia de operadores

1. `()` — Paréntesis
2. `**` — Potencia
3. `*`, `/`, `//`, `%` — Multiplicación y división
4. `+`, `-` — Suma y resta

---

## ⚖️ Operadores de Comparación

| Operador | Significado | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Diferente de | `5 != 3` | `True` |
| `>` | Mayor que | `5 > 3` | `True` |
| `<` | Menor que | `5 < 3` | `False` |
| `>=` | Mayor o igual | `5 >= 5` | `True` |
| `<=` | Menor o igual | `5 <= 3` | `False` |

### Comparaciones encadenadas

```python
18 <= edad <= 65    # True si edad está entre 18 y 65
0 <= nota <= 10     # True si nota está entre 0 y 10
```

---

## 🧠 Operadores Lógicos

| Operador | Regla | Ejemplo | Resultado |
|----------|-------|---------|-----------|
| `and` | Ambos deben ser `True` | `True and True` | `True` |
| `or` | Al menos uno `True` | `True or False` | `True` |
| `not` | Invierte el valor | `not True` | `False` |

### Valores Falsy

```python
False, 0, 0.0, "", None, [], {}
```

### Valores Truthy

```python
True, 1, -5, 3.14, "hola", [1, 2], {"a": 1}
```

### Patrón de valor por defecto

```python
nombre = entrada or "Invitado"  # Si entrada es vacía, usa "Invitado"
```

---

## 🔄 Casting (Conversión de Tipos)

| Función | Convierte a | Ejemplo | Resultado |
|---------|-------------|---------|-----------|
| `int()` | Entero | `int("42")` | `42` |
| `float()` | Decimal | `float("3.14")` | `3.14` |
| `str()` | Texto | `str(42)` | `"42"` |
| `bool()` | Booleano | `bool("")` | `False` |
| `round()` | Redondeado | `round(3.7)` | `4` |
| `bin()` | Binario | `bin(42)` | `"0b101010"` |
| `hex()` | Hexadecimal | `hex(42)` | `"0x2a"` |
| `oct()` | Octal | `oct(42)` | `"0o52"` |
| `ord()` | Código Unicode | `ord("A")` | `65` |
| `chr()` | Carácter | `chr(65)` | `"A"` |

### Conversiones que fallan

```python
int("hola")     # ❌ ValueError
int("3.14")     # ❌ ValueError (primero float, luego int)
float("abc")    # ❌ ValueError
```

### Validación segura

```python
if texto.isdigit():
    numero = int(texto)
```

---

## 📝 Métodos de Strings

### Transformación

| Método | Qué hace | Ejemplo | Resultado |
|--------|----------|---------|-----------|
| `.upper()` | Mayúsculas | `"hola".upper()` | `"HOLA"` |
| `.lower()` | Minúsculas | `"HOLA".lower()` | `"hola"` |
| `.title()` | Título | `"hola mundo".title()` | `"Hola Mundo"` |
| `.capitalize()` | Primera mayúscula | `"hola mundo".capitalize()` | `"Hola mundo"` |
| `.swapcase()` | Invierte caso | `"Hola".swapcase()` | `"hOLA"` |

### Limpieza

| Método | Qué hace | Ejemplo | Resultado |
|--------|----------|---------|-----------|
| `.strip()` | Quita espacios | `" hola ".strip()` | `"hola"` |
| `.lstrip()` | Quita izquierda | `"  hola".lstrip()` | `"hola"` |
| `.rstrip()` | Quita derecha | `"hola  ".rstrip()` | `"hola"` |

### Búsqueda

| Método | Qué hace | Ejemplo | Resultado |
|--------|----------|---------|-----------|
| `.find()` | Índice primera | `"hola".find("o")` | `1` |
| `.rfind()` | Índice última | `"hola".rfind("o")` | `1` |
| `.count()` | Cuenta | `"hola".count("o")` | `1` |
| `.index()` | Índice (error si no) | `"hola".index("o")` | `1` |

### Verificación

| Método | Qué hace | Ejemplo | Resultado |
|--------|----------|---------|-----------|
| `.startswith()` | Inicia con | `"hola".startswith("h")` | `True` |
| `.endswith()` | Termina con | `"hola".endswith("a")` | `True` |
| `.isdigit()` | Solo dígitos | `"123".isdigit()` | `True` |
| `.isalpha()` | Solo letras | `"abc".isalpha()` | `True` |
| `.isalnum()` | Letras/números | `"abc123".isalnum()` | `True` |
| `.isspace()` | Solo espacios | `"  ".isspace()` | `True` |
| `.islower()` | Todo minúsculas | `"hola".islower()` | `True` |
| `.isupper()` | Todo mayúsculas | `"HOLA".isupper()` | `True` |
| `.istitle()` | Formato título | `"Hola".istitle()` | `True` |

### División y unión

```python
"a,b,c".split(",")        # ["a", "b", "c"]
"hola mundo".split()      # ["hola", "mundo"]
"-".join(["a", "b"])      # "a-b"
"\n".join(["a", "b"])     # "a\nb"
```

### Reemplazo

```python
"hola mundo".replace("mundo", "Python")  # "hola Python"
```

---

## 🎨 f-strings Avanzados

```python
nombre = "Ana"
saldo = 1234.5678
nota = 8.5

# Alineación
f"|{nombre:<10}|"   # "|Ana       |" (izquierda)
f"|{nombre:>10}|"   # "|       Ana|" (derecha)
f"|{nombre:^10}|"   # "|   Ana    |" (centrado)

# Números
f"${saldo:.2f}"     # "$1234.57" (2 decimales)
f"{nota:.1f}/10"    # "8.5/10" (1 decimal)
f"{0.85:.1%}"       # "85.0%" (porcentaje)
f"{8000000:,}"      # "8,000,000" (separador miles)

# Expresiones
f"El doble es {edad * 2}"
f"¿Mayor? {edad >= 18}"
```

---

## 🧩 Indexación y Slicing

```python
texto = "Python"

texto[0]      # "P" (primer carácter)
texto[-1]     # "n" (último carácter)
texto[0:3]    # "Pyt" (índices 0, 1, 2)
texto[2:]     # "thon" (desde índice 2)
texto[:3]     # "Pyt" (hasta índice 2)
texto[::-1]   # "nohtyP" (invertido)
```

---

## ⚡ Tips Rápidos

| Situación | Solución |
|-----------|----------|
| Dividir cosas enteras | Usa `//` |
| Saber si es par | `numero % 2 == 0` |
| Comparar floats | `math.isclose(a, b)` |
| Valor por defecto | `valor or "default"` |
| Normalizar texto | `texto.strip().lower()` |
| Validar número | `texto.isdigit()` |
| Invertir string | `texto[::-1]` |
| Contar palabras | `len(texto.split())` |
| Palabra más larga | `max(palabras, key=len)` |

---

> **Zen de Python:** *Readability counts.* — El código se lee más veces de las que se escribe.
