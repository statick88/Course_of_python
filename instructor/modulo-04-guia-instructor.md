# Guía del Instructor — Módulo 4: Funciones

## Objetivos de Aprendizaje

Al finalizar este módulo, el estudiante será capaz de:

1. Definir funciones propias con def
2. Comprender parámetros y argumentos
3. Usar return para devolver valores
4. Entender scope de variables (local vs global)
5. Crear funciones lambda simples
6. Implementar recursión básica

## Duración Estimada

- **Teoría**: 2.5 horas
- **Práctica**: 3 horas
- **Desafíos**: 1.5 horas
- **Total**: 7 horas

## Estructura de la Sesión

### Sesión 1: Fundamentos de Funciones (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-30 min | Repaso estructuras de control | Módulo 3 |
| 30-75 min | Definir funciones | 01-definir-funciones.qmd |
| 75-120 min | Parámetros y argumentos | 02-parametros-argumentos.qmd |

### Sesión 2: Return y Scope (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-45 min | Return de valores | 03-return.qmd |
| 45-90 min | Scope de variables | 04-scope-variables.qmd |
| 90-120 min | Ejercicios prácticos | Desafíos 1-3 |

### Sesión 3: Avanzado (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-45 min | Funciones lambda | 05-funciones-lambda.qmd |
| 45-90 min | Recursión | 06-funciones-recursivas.qmd |
| 90-120 min | Desafíos completos | Desafíos 4-7 |

## Preguntas Frecuentes Anticipadas

### ¿Para qué sirven los parámetros?

**Respuesta:** Los parámetros hacen que las funciones sean reutilizables. La misma función puede procesar diferentes datos.

### ¿Qué es el return vs el print?

**Respuesta:** `return` devuelve un valor para usar en el código. `print` solo muestra texto en pantalla.

### ¿Cuándo usar una función lambda?

**Respuesta:** Para funciones pequeñas y simples que solo se usan una vez. Ej: `doble = lambda x: x*2`

### ¿Qué es la recursión?

**Respuesta:** Una función que se llama a sí misma. Necesita un caso base para evitar bucle infinito.

## Analogías para Enseñar

### Función como una receta
> "Una función es como una receta: tiene ingredientes (parámetros), instrucciones (código), y produce un plato (return)."

### Scope como el organisasiión de una oficina
> "Las variables locales son como documentos en un escritorio privado. Las globales son como documentos en un pasillo donde todos pueden verlos."

## Soluciones de Desafíos

### Desafío 5: Verificador de Primos

```python
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Pruebas
for num in range(1, 21):
    if es_primo(num):
        print(f"{num} es primo")
```

### Desafío 6: Serie Fibonacci

```python
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    serie = [0, 1]
    for i in range(2, n):
        serie.append(serie[-1] + serie[-2])
    return serie

print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Desafío 7: Calculadora con Funciones

```python
def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplica(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error"

operaciones = {
    "+": suma,
    "-": resta,
    "*": multiplica,
    "/": divide
}

a = float(input("Primer número: "))
op = input("Operación (+-*/): ")
b = float(input("Segundo número: "))

resultado = operaciones[op](a, b)
print(f"Resultado: {resultado}")
```

## Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| NameError: name 'x' is not defined | Variable no existe en el scope | Definirla o pasarla como parámetro |
| TypeError: unsupported operand | Return no devuelve nada (None) | Agregar return con valor |
| RecursionError | Caso base faltante | Siempre tener condición de parada |

## Evaluación

| Criterio | Peso |
|----------|------|
| Desafíos completados | 40% |
| Funciones con parámetros correctos | 25% |
| Uso apropiado de return | 20% |
| Código limpio y documentado | 15% |