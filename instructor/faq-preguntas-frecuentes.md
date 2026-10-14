# FAQ: Preguntas Frecuentes del Curso Python Fundamentos

## Instalación y Entorno

### ¿Qué versión de Python necesito?
**Python 3.8 o superior**. Recomendamos 3.10+ para las últimas características.

### ¿Puedo usar una versión anterior de Python?
No se recomienda. Algunas características del curso (como match/case en 3.10) no funcionan en versiones anteriores.

### ¿Necesito instalar algo más además de Python?
Sí, te recomendamos VS Code como editor. Es gratuito y tiene excelente soporte para Python.

### ¿Qué es un entorno virtual y por qué necesito uno?
Un entorno virtual aísla las dependencias de tu proyecto. Evita conflictos entre diferentes proyectos y versiones de paquetes.

### ¿Cómo sé que Python está instalado correctamente?
Ejecuta `python3 --version` en terminal. Deberías ver algo como `Python 3.12.1`.

---

## Errores Comunes

### SyntaxError: invalid syntax
Tu código tiene un error de sintaxis. Revisa:
- Paréntesis, corchetes y llaves balanceados
- Dos puntos `:` al final de if, for, while, def
- Comillas abiertas sin cerrar

### NameError: name 'x' is not defined
Estás usando una variable que no has definido. Verifica:
- Que la variable esté escrita exactamente igual
- Que se haya ejecutado la línea donde se define

### IndentationError: unexpected indent
Python usa indentación para definir bloques. No indentes al inicio de líneas sueltas. Usa 4 espacios, no tabs.

### TypeError: unsupported operand type(s)
Estás operando con tipos incompatibles. Ej: `"texto" + 5` da error. Convierte tipos: `int("5") + 5`

### ValueError: invalid literal for int()
Estás intentando convertir texto que no es un número. Usa `int(input())` correctamente o valida con try/except.

### IndexError: list index out of range
Estás accediendo a una posición que no existe en la lista. recuerda que los índices empiezan en 0.

---

## Conceptos de Python

### ¿Cuál es la diferencia entre = y ==?
- `=` (asignación) guarda un valor en una variable
- `==` (comparación) verifica si dos valores son iguales

### ¿Qué significa None?
None es el valor "nada" o "vacío" en Python. No es lo mismo que 0, False o "".

### ¿Por qué mi lista cambió sin que yo la modificara?
En Python, las listas se pasan por referencia. Si haces `lista2 = lista1` y modificas lista2, lista1 también cambia. Usa `lista2 = lista1.copy()` para crear una copia.

### ¿Strings son mutables?
No, los strings son inmutables. Los métodos como `.upper()` devuelven un nuevo string, no modifican el original.

### ¿Qué es una función pura?
Una función pura:
1. Dados los mismos argumentos, siempre devuelve el mismo resultado
2. No modifica variables outside de su scope
3. No tiene efectos secundarios (no modifica archivos, no imprime, etc.)

---

## Bucles y Condicionales

### ¿Cuál es la diferencia entre for y while?
- **for**: Itera sobre una secuencia conocida (lista, rango)
- **while**: Itera mientras una condición sea verdadera

### ¿Cuándo usar break vs continue?
- **break**: Sale completamente del bucle
- **continue**: Salta a la siguiente iteración

### ¿Para qué sirve el else en un for?
Se ejecuta si el bucle termina normalmente (sin break). Es útil para búsquedas: "si recorres todo y no lo encuentras..."

---

## Funciones

### ¿Qué es un parámetro vs un argumento?
- **Parámetro**: Variable en la definición de la función
- **Argumento**: Valor que pasas al llamar la función

### ¿Puede una función devolver varios valores?
Sí, Python devuelve una tupla: `return a, b` es equivalente a `return (a, b)`

### ¿Qué es *args y **kwargs?
- `*args`: número variable de argumentos posicionales
- `**kwargs`: número variable de argumentos con nombre

```python
def func(*args, **kwargs):
    print(args)   # tuple de argumentos
    print(kwargs) # dict de argumentos con nombre
```

---

## Archivos y Módulos

### ¿Cómo leo un archivo sin cerrarlo manualmente?
Usa el contexto `with`:
```python
with open("archivo.txt") as f:
    contenido = f.read()
# El archivo se cierra automáticamente
```

### ¿Qué es __name__ == "__main__"?
Cuando ejecutas un archivo directamente, su `__name__` es `"__main__"`. Cuando se importa, es el nombre del módulo. Úsalo para código que solo quieres ejecutar directamente.

### ¿Cómo importo solo una función de un módulo?
```python
from math import sqrt, pi
```

---

## Testing y Debugging

### ¿Cómo depuro mi código?
- **Print debugging**: Agrega print() para ver valores
- **VS Code Debugger**: Usa el depurador integrado (F5)
- **pdb**: Depurador interactivo `import pdb; pdb.set_trace()`

### ¿Cómo escribo un test básico?
```python
def test_suma():
    assert suma(2, 3) == 5
    
def suma(a, b):
    return a + b
```

### ¿Qué es pytest?
Pytest es un framework de testing. Ejecuta `pytest` en tu proyecto y descubrirá funciones que empiezan con `test_`.

---

## Buenos hábitos

### ¿Debo seguir PEP 8?
Sí. Usa:
- snake_case para variables y funciones
- SCREAMING_SNAKE_CASE para constantes
- Nombres descriptivos (no x, y, temp)

### ¿Cuándo usar docstrings?
Siempre. Explica qué hace la función, parámetros y retorno.

```python
def suma(a, b):
    """Suma dos números.
    
    Args:
        a: Primer número
        b: Segundo número
    
    Returns:
        La suma de a + b
    """
    return a + b
```

### ¿Cómo organizo mi código?
- Funciones pequeñas y con una responsabilidad
- Máximo 20-30 líneas por función
- Código que leerás más veces de lo que escribirás

---

## Preguntas de los Estudiantes (Reales)

### "Me da miedo romper algo"
**No te preocupes, no puedes romper tu computadora con código Python. Y siempre puedes empezar de nuevo."

### "No sé por dónde empezar"
**Copia el ejemplo del material, ejecútalo, luego cámbialo un poco. La práctica es clave."

### "Mi código no funciona y no entiendo el error"
**Lee el mensaje de error completo. Python te dice exactamente qué línea y qué problema tiene."

### "Esto es muy difícil para mí"
**Es normal al principio. Cada programador pasó por esto. Sigue practicando, cada día será más fácil."