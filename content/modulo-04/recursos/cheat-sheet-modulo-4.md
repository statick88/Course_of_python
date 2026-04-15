# Recursos de Apoyo — Módulo 4: Funciones

## Cheat Sheet: Definir Funciones

| Concepto | Sintaxis | Ejemplo |
|----------|----------|---------|
| Definir función | `def nombre():` | `def saludar():` |
| Con parámetro | `def nombre(param):` | `def saludar(nombre):` |
| Con valor por defecto | `def nombre(param=valor):` | `def saludar(nombre="Ana"):` |
| Docstring | `"""Descripción"""` | `"""Saluda al usuario."""` |
| Devolver valor | `return expresion` | `return nombre.upper()` |
| Placeholder | `pass` | `def procesar(): pass` |

## Cheat Sheet: Parámetros y Argumentos

| Tipo | Sintaxis | Qué recibe | Ejemplo de llamada |
|------|----------|------------|-------------------|
| Posicional | `nombre` | Un valor en orden | `saludar("Ana")` |
| Con defecto | `nombre="Hola"` | Valor o defecto | `saludar()` |
| Keyword | `nombre="Ana"` | Valor con nombre | `saludar(nombre="Ana")` |
| `*args` | `*args` | Tupla de valores | `sumar(1, 2, 3)` |
| `**kwargs` | `**kwargs` | Diccionario | `perfil(edad=25)` |

**Orden correcto de parámetros:**
```
def funcion(obligatorio, opcional="defecto", *args, **kwargs):
```

## Cheat Sheet: Return

| Patrón | Ejemplo | Resultado |
|--------|---------|-----------|
| Return simple | `return x * 2` | Devuelve el valor |
| Return temprano | `if error: return "error"` | Sale de la función |
| Múltiples valores | `return a, b, c` | Devuelve tupla `(a, b, c)` |
| Sin return | (nada) | Devuelve `None` |
| Return booleano | `return x > 0` | Devuelve `True` o `False` |

## Cheat Sheet: Scope de Variables

| Scope | Dónde se define | Palabra clave | Visibilidad |
|-------|-----------------|---------------|-------------|
| Local | Dentro de función | — | Solo esa función |
| Enclosing | Función padre | `nonlocal` | Funciones anidadas |
| Global | Fuera de funciones | `global` | Todo el módulo |
| Built-in | Python mismo | — | Todo |

**Regla LEGB:** Local → Enclosing → Global → Built-in

## Cheat Sheet: Funciones Lambda

| Uso | Sintaxis | Ejemplo |
|-----|----------|---------|
| Simple | `lambda x: expresion` | `lambda x: x * 2` |
| Con `sorted()` | `key=lambda x: ...` | `sorted(lista, key=lambda x: x[1])` |
| Con `filter()` | `filter(lambda x: ..., lista)` | `list(filter(lambda x: x > 0, nums))` |
| Con `map()` | `map(lambda x: ..., lista)` | `list(map(lambda x: x**2, nums))` |

## Cheat Sheet: Recursión

| Parte | Descripción | Ejemplo |
|-------|-------------|---------|
| Caso base | Cuándo parar | `if n <= 1: return 1` |
| Caso recursivo | Cómo reducir | `return n * factorial(n-1)` |
| Límite Python | Máximo de llamadas | `sys.getrecursionlimit()` → 1000 |

**Estructura obligatoria:**
```python
def recursiva(parametro):
    if caso_base:
        return resultado_simple
    return recursiva(parametro_reducido)
```

## Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| `NameError` | Variable fuera de scope | Verifica si es local o global |
| `UnboundLocalError` | Modificar global sin `global` | Usa `global nombre_var` |
| `RecursionError` | Sin caso base o muy profundo | Agrega caso base o usa iteración |
| Mutable como defecto | `def f(lista=[])` | Usa `def f(lista=None)` |
| `TypeError: NoneType` | `print()` en vez de `return` | Cambia `print()` por `return` |
| Código después de return | Instrucciones inalcanzables | Mueve el código antes del return |

## Zen de Python Aplicado a Funciones

| Principio | Aplicación |
|-----------|------------|
| Beautiful is better than ugly | Nombres descriptivos: `calcular_promedio` no `calc` |
| Explicit is better than implicit | `return` explícito, no `print()` oculto |
| Simple is better than complex | Lambda para simple, `def` para complejo |
| Readability counts | Docstrings, parámetros con nombre |
| There should be one obvious way | `def` para funciones nombradas, lambda para orden superior |
| Errors should never pass silently | Caso base en recursión, validación de parámetros |

## Atajos Útiles

| Acción | Código |
|--------|--------|
| Ver docstring | `print(funcion.__doc__)` |
| Ver nombre | `print(funcion.__name__)` |
| Ver parámetros | `import inspect; inspect.signature(funcion)` |
| Límite recursión | `import sys; sys.getrecursionlimit()` |
