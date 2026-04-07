# Guía del Instructor — Módulo 9: Buenas Prácticas y Testing

## Objetivos de Aprendizaje

Al finalizar este módulo, el estudiante será capaz de:

1. Aplicar las reglas de PEP 8 para código limpio
2. Escribir nombres descriptivos para variables y funciones
3. Crear documentación con docstrings
4. Implementar manejo de errores con try/except
5. Escribir tests básicos con pytest
6. Realizar code review básico

## Duración Estimada

- **Teoría**: 2.5 horas
- **Práctica**: 3 horas
- **Desafíos**: 1.5 horas
- **Total**: 7 horas

## Estructura de la Sesión

### Sesión 1: PEP 8 y Nombres (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-30 min | Repaso Módulo 8 | Módulos |
| 30-75 min | PEP 8 y estilo | 01-pep8-estilo.qmd |
| 75-120 min | Nombres descriptivos | 02-nombres-descriptivos.qmd |

### Sesión 2: Errores y Funciones Puras (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-45 min | Funciones puras | 03-funciones-puras.qmd |
| 45-90 min | Manejo de errores | 04-manejo-errores.qmd |
| 90-120 min | Documentación | 05-documentacion.qmd |

### Sesión 3: Testing y Desafíos (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-45 min | Testing básico | 06-testing-basico.qmd |
| 45-120 min | Desafíos | desafios/01-07 |

## Preguntas Frecuentes Anticipadas

### ¿Qué es PEP 8?

**Respuesta:** Python Enhancement Proposal 8 - Guía de estilo de código. Define convenciones como snake_case, 4 espacios, líneas max 79 chars.

### ¿Por qué necesito docstrings?

**Respuesta:** El código se lee más veces de lo que se escribe. Los docstrings ayudan a otros (y a ti mismo) a entender qué hace cada función.

### ¿Cuándo usar try/except?

**Respuesta:** Para manejar errores esperados (archivo no existe, usuario ingresa texto en vez de número). NO para errores de programación.

### ¿Qué es un test unitario?

**Respuesta:** Código que verifica que una función behaves como se espera. Si el código cambia y el test falla, detectas el problema.

## Analogías para Enseñar

### PEP 8 como las reglas de tránsito
> "No es obligatorio, pero todos las seguimos para que sea seguro. Si cada conductor inventara sus propias reglas, habría caos."

### Docstrings como el manual de un carro
> "Sin manual, no sabes cómo usar el carro. Sin docstrings, no sabes cómo usar la función."

## Soluciones de Desafíos

### Desafío 2: Docstrings

```python
def calcular_area_circulo(radio: float) -> float:
    """Calcula el área de un círculo dado su radio.
    
    Args:
        radio: El radio del círculo (debe ser positivo).
    
    Returns:
        El área del círculo.
    
    Raises:
        ValueError: Si el radio es negativo o cero.
    
    Ejemplo:
        >>> calcular_area_circulo(5)
        78.53981633974483
    """
    if radio <= 0:
        raise ValueError("El radio debe ser positivo")
    import math
    return math.pi * radio ** 2
```

### Desafío 3: Validador Robusto

```python
def validar_usuario(nombre, edad, email):
    """Valida datos de usuario."""
    errores = []
    
    # Validar nombre
    if not nombre or len(nombre) < 2:
        errores.append("Nombre debe tener al menos 2 caracteres")
    if not nombre.isalpha():
        errores.append("Nombre solo puede tener letras")
    
    # Validar edad
    try:
        edad = int(edad)
        if edad < 0 or edad > 150:
            errores.append("Edad debe estar entre 0 y 150")
    except ValueError:
        errores.append("Edad debe ser un número")
    
    # Validar email
    if "@" not in email or "." not in email.split("@")[1]:
        errores.append("Email inválido")
    
    return errores if errores else "Válido"

# Uso
resultado = validar_usuario("Ana", "25", "ana@email.com")
print(resultado)
```

### Desafío 4: Test Calculadora

```python
# calculator.py
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

# test_calculator.py (debe estar en archivo separado)
import pytest
from calculator import suma, resta

def test_suma_positivos():
    assert suma(2, 3) == 5

def test_suma_negativos():
    assert suma(-1, -1) == -2

def test_resta():
    assert resta(10, 5) == 5

def test_resta_negativo():
    assert resta(5, 10) == -5
```

Para ejecutar: `pytest test_calculator.py -v`

### Desafío 7: Code Review Checklist

```markdown
# Code Review - Nombre del Archivo

## Legibilidad
- [ ] Nombres descriptivos (no x, y, temp)
- [ ] Variables en snake_case
- [ ] Funciones hacen una cosa

## Estilo PEP 8
- [ ] 4 espacios de indentación
- [ ] Líneas max 100 caracteres
- [ ] Espacios alrededor de operadores

## Documentación
- [ ] Docstrings en funciones públicas
- [ ] Comentarios solo donde sea necesario

## Errores
- [ ] try/except para errores esperados
- [ ] No manejo genérico de excepciones
```

## Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| Bare except | `except:` sin especificar excepción | Usar `except Exception:` mínimo |
| Silent fail | pass en except | Siempre registrar o manejar el error |
| Tests que no run | Nombres incorrectos | Funciones deben empezar con `test_` |

## Evaluación

| Criterio | Peso |
|----------|------|
| Desafíos completados | 40% |
| Código según PEP 8 | 25% |
| Documentación adecuada | 20% |
| Tests funcionales | 15% |