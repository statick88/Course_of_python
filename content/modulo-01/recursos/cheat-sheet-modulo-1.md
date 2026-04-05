# Recursos de Apoyo — Módulo 1

## Cheat Sheet: Funciones Básicas

| Función | Qué hace | Ejemplo |
|---------|----------|---------|
| `print()` | Muestra en pantalla | `print("Hola")` |
| `input()` | Lee texto del usuario | `nombre = input("Nombre: ")` |
| `int()` | Convierte a entero | `int("42")` → `42` |
| `float()` | Convierte a decimal | `float("3.14")` → `3.14` |
| `str()` | Convierte a texto | `str(42)` → `"42"` |
| `type()` | Devuelve el tipo | `type(42)` → `<class 'int'>` |
| `len()` | Longitud de texto | `len("hola")` → `4` |

## Cheat Sheet: Operadores

| Operador | Qué hace | Ejemplo | Resultado |
|----------|----------|---------|-----------|
| `+` | Suma / concatena | `5 + 3` | `8` |
| `-` | Resta | `10 - 4` | `6` |
| `*` | Multiplica / repite | `3 * 4` | `12` |
| `/` | Divide (siempre float) | `10 / 3` | `3.33...` |
| `//` | División entera | `10 // 3` | `3` |
| `%` | Residuo | `10 % 3` | `1` |
| `**` | Potencia | `2 ** 3` | `8` |
| `==` | Igualdad | `5 == 5` | `True` |
| `!=` | Diferente | `5 != 3` | `True` |
| `>` | Mayor que | `5 > 3` | `True` |
| `<` | Menor que | `5 < 3` | `False` |
| `>=` | Mayor o igual | `5 >= 5` | `True` |
| `<=` | Menor o igual | `5 <= 3` | `False` |

## Cheat Sheet: Tipos de Datos

| Tipo | Nombre | Ejemplo | Mutable |
|------|--------|---------|---------|
| Entero | `int` | `42`, `-7`, `0` | No |
| Decimal | `float` | `3.14`, `-0.5`, `1e10` | No |
| Texto | `str` | `"hola"`, `'mundo'` | No |
| Booleano | `bool` | `True`, `False` | No |

## Zen de Python (resumen para principiantes)

Los principios que guían TODO el código en este curso:

1. **Beautiful is better than ugly** — Código limpio y legible
2. **Explicit is better than implicit** — Sé claro, no asumas
3. **Simple is better than complex** — La solución simple es la mejor
4. **Readability counts** — Escribe para humanos, no para máquinas
5. **Errors should never pass silently** — Maneja los errores, no los ignores
6. **There should be one obvious way to do it** — Sigue las convenciones

## Atajos de Terminal

| Comando | Qué hace |
|---------|----------|
| `python3 archivo.py` | Ejecuta un script Python |
| `python3` | Abre el intérprete interactivo |
| `python3 -m venv venv` | Crea un entorno virtual |
| `source venv/bin/activate` | Activa el entorno virtual (macOS/Linux) |
| `pip install paquete` | Instala un paquete |
| `pip list` | Lista paquetes instalados |
| `cd directorio` | Cambia de directorio |
| `ls` | Lista archivos |
| `mkdir nombre` | Crea un directorio |

## Errores Comunes y Soluciones

| Error | Causa | Solución |
|-------|-------|----------|
| `NameError` | Variable no definida | Verifica que la variable existe |
| `TypeError` | Tipo incorrecto | Convierte con `int()`, `str()`, etc. |
| `SyntaxError` | Error de escritura | Revisa paréntesis, comillas, dos puntos |
| `ValueError` | Valor inválido | Verifica que el dato tiene el formato correcto |
| `IndentationError` | Mala indentación | Usa 4 espacios, no mezcles tabs y espacios |