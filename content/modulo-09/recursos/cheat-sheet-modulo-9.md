# Recursos de Apoyo — Módulo 9

## Cheat Sheet: PEP 8

| Regla | Ejemplo correcto | Ejemplo incorrecto |
|-------|------------------|-------------------|
| Indentación | 4 espacios | Tabs o 2 espacios |
| Líneas en blanco entre funciones | `def a():\n\n\ndef b():` | `def a():\ndef b():` |
| Espacios en operadores | `x = 5 + 3` | `x=5+3` |
| Imports | `import os` + `import sys` | `import os, sys` |
| Líneas máx. | 79 caracteres | Líneas infinitas |
| snake_case | `calcular_promedio()` | `calcularPromedio()` |
| PascalCase (clases) | `class UsuarioActivo:` | `class usuario_activo:` |
| MAYÚSCULAS (constantes) | `MAX_INTENTOS = 3` | `max_intentos = 3` |

## Cheat Sheet: Nombres Descriptivos

| Tipo | Patrón | Ejemplo |
|------|--------|---------|
| Booleanos | `es_`, `tiene_`, `esta_` | `es_valido`, `tiene_permiso` |
| Funciones que devuelven | `obtener_`, `calcular_`, `encontrar_` | `obtener_usuario()` |
| Funciones que verifican | `validar_`, `verificar_`, `es_` | `validar_email()` |
| Funciones que crean | `crear_`, `generar_`, `construir_` | `crear_reporte()` |
| Funciones que transforman | `procesar_`, `convertir_`, `formatear_` | `convertir_temperatura()` |

## Cheat Sheet: Funciones Puras

| Característica | Función Pura | Función Impura |
|----------------|--------------|----------------|
| Misma entrada → misma salida | ✅ Siempre | ❌ A veces |
| Modifica estado externo | ❌ Nunca | ✅ A veces |
| Depende de variables globales | ❌ Nunca | ✅ A veces |
| Fácil de testear | ✅ Sin configuración | ❌ Requiere setup |
| Ejemplo | `def sumar(a, b): return a + b` | `print("hola")` |

## Cheat Sheet: Manejo de Errores

| Patrón | Cuándo usarlo | Ejemplo |
|--------|---------------|---------|
| `try/except` | Código que puede fallar | `try: int(texto) except ValueError:` |
| `except Específico` | Sabes qué error esperar | `except FileNotFoundError:` |
| `else` | Código si NO hay error | `else: print("Éxito")` |
| `finally` | Limpieza siempre | `finally: archivo.close()` |
| `raise` | Lanzar error propio | `raise ValueError("mensaje")` |
| `pytest.raises` | Testear que hay error | `with pytest.raises(ValueError):` |

## Cheat Sheet: Docstrings (Formato Google)

```python
def funcion(param1, param2):
    """Resumen corto de una línea.
    
    Descripción más detallada si es necesaria.
    
    Args:
        param1: Descripción del primer parámetro.
        param2: Descripción del segundo parámetro.
    
    Returns:
        Descripción del valor de retorno.
    
    Raises:
        ValueError: Cuándo y por qué se lanza.
    
    Examples:
        >>> funcion(1, 2)
        3
    """
```

## Cheat Sheet: Type Hints

| Tipo | Sintaxis | Ejemplo |
|------|----------|---------|
| Entero | `int` | `def func(x: int):` |
| Decimal | `float` | `def func(x: float) -> float:` |
| Texto | `str` | `def func(nombre: str):` |
| Booleano | `bool` | `def func(activo: bool):` |
| Lista | `List[tipo]` | `def func(items: List[int]):` |
| Diccionario | `Dict[clave, valor]` | `def func(d: Dict[str, int]):` |
| Opcional | `Optional[tipo]` | `def func(x: Optional[str]):` |
| Tupla | `Tuple[tipo, ...]` | `def func() -> Tuple[str, int]:` |

## Cheat Sheet: Testing con pytest

| Patrón | Sintaxis | Para qué sirve |
|--------|----------|----------------|
| Assert básico | `assert resultado == esperado` | Verificar igualdad |
| Assert con mensaje | `assert x > 0, "Debe ser positivo"` | Mensaje personalizado |
| Verificar error | `with pytest.raises(ValueError):` | Testear que hay error |
| Parametrizado | `@pytest.mark.parametrize("x,y", [(1,2), (3,4)])` | Múltiples casos |
| Ejecutar tests | `pytest -v` | Ver detalles de cada test |
| Ejecutar un archivo | `pytest test_archivo.py` | Tests específicos |

## Zen de Python (completo)

Ejecuta `import this` en Python para ver los 20 principios. Los más relevantes para este módulo:

1. **Beautiful is better than ugly** — Código limpio y bien formateado
2. **Explicit is better than implicit** — Sé claro, no asumas nada
3. **Simple is better than complex** — La solución simple es la mejor
4. **Complex is better than complicated** — Si es complejo, que sea organizado
5. **Readability counts** — Escribe para humanos, no para máquinas
6. **Errors should never pass silently** — Maneja los errores, no los ignores
7. **There should be one obvious way to do it** — Sigue las convenciones

## Herramientas Recomendadas

| Herramienta | Para qué sirve | Comando |
|-------------|----------------|---------|
| `ruff` | Linter ultrarrápido | `ruff check archivo.py` |
| `ruff --fix` | Corregir automáticamente | `ruff check --fix archivo.py` |
| `pytest` | Framework de testing | `pytest -v` |
| `pytest --cov` | Cobertura de tests | `pytest --cov=mi_modulo` |
| `python -m doctest` | Tests en docstrings | `python -m doctest archivo.py` |

## Errores Comunes y Soluciones

| Error | Causa | Solución |
|-------|-------|----------|
| Nombres genéricos | `x`, `data`, `tmp` | Usar nombres descriptivos |
| Funciones impuras | Dependen de globales | Pasar todo como parámetro |
| Sin docstrings | "El código se explica solo" | Documentar el porqué, no el qué |
| Sin tests | "Funciona en mi máquina" | Escribir tests antes de cambiar |
| Capturar Exception | `except: pass` | Capturar excepciones específicas |
| Recursos abiertos | `open()` sin `with` | Usar `with open() as f:` |
