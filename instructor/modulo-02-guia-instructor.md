# Guía del Instructor — Módulo 2: Tipos de Datos y Variables

## Objetivos de Aprendizaje

Al finalizar este módulo, el estudiante será capaz de:

1. Comprender y usar operadores aritméticos (+, -, *, /, //, %, **)
2. Realizar comparaciones con operadores de comparación
3. Combinar condiciones con operadores lógicos (and, or, not)
4. Convertir entre tipos de datos (casting)
5. Manipular strings con métodos avanzados

## Duración Estimada

- **Teoría**: 2 horas
- **Práctica**: 3 horas
- **Desafíos**: 2 horas
- **Total**: 7 horas

## Estructura de la Sesión

### Sesión 1: Operadores Básicos (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-30 min | Repaso Módulo 1 + preguntas | index.qmd |
| 30-60 min | Operadores aritméticos | 01-operadores-aritmeticos.qmd |
| 60-90 min | Operadores de comparación | 02-operadores-comparacion.qmd |
| 90-120 min | Operadores lógicos | 03-operadores-logicos.qmd |

### Sesión 2: Casting y Strings (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-30 min | Repaso de operadores | Todas las lecciones |
| 30-60 min | Casting avanzado | 04-casting-avanzado.qmd |
| 60-90 min | Strings avanzados | 05-strings-avanzado.qmd |
| 90-120 min | Laboratorio práctico | Labs correspondientes |

### Sesión 3: Desafíos (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-45 min | Desafíos 1-3 (individuales) | desafios/01-03 |
| 45-90 min | Desafíos 4-5 (en parejas) | desafios/04-05 |
| 90-120 min | Desafíos 6-7 (avanzados) | desafios/06-07 |

## Preguntas Frecuentes Anticipadas

### ¿Cuál es la diferencia entre == y =?

**Respuesta:** `=` es asignación (guarda un valor en una variable). `==` es comparación (verifica si dos valores son iguales).

### ¿Por qué 10 / 3 da 3.3333 y no 3?

**Respuesta:** En Python 3, `/` siempre devuelve un float (división exacta). Usa `//` para división entera.

### ¿Para qué sirve el operador %?

**Respuesta:** El módulo (%) devuelve el residuo de una división. Útil para verificar si un número es par/impar: `n % 2 == 0`.

### ¿Cuál es la diferencia entre "Hola" y 'Hola'?

**Respuesta:** No hay diferencia. Python acepta comillas simples o dobles indistintamente.

## Puntos de Atención

1. **Precedencia de operadores**: Enseñar el orden (PEMDAS) con ejemplos prácticos
2. **Casting implícito**: Explicar cuándo Python convierte tipos automáticamente
3. **Strings inmutables**: Aclarar que los métodos devuelven nuevos strings, no modifican el original
4. **Errores comunes**: TypeError por mezclar tipos incompatible

## Evaluación del Módulo

| Criterio | Peso | Mínimo |
|----------|------|--------|
| Desafíos completados (70%+) | 40% | 5 de 7 |
| Labs completados | 30% | 100% |
| Participación | 15% | Activa |
| Quiz del módulo | 15% | 60% |

## Soluciones de Desafíos

### Desafío 1: Calculadora de Propinas

```python
print("=== CALCULADORA DE PROPINAS ===")
total_cuenta = float(input("Total de la cuenta: "))
porcentaje = float(input("Porcentaje de propina (10, 15, 20): "))
personas = int(input("Número de personas: "))

monto_propina = round(total_cuenta * (porcentaje / 100), 2)
total_con_propina = round(total_cuenta + monto_propina, 2)
por_persona = round(total_con_propina / personas, 2)

print(f"Propina ({porcentaje}%): ${monto_propina:.2f}")
print(f"Total con propina: ${total_con_propina:.2f}")
print(f"Cada persona paga: ${por_persona:.2f}")
```

### Desafío 4: Generador de DNI

```python
import random

def generar_dni():
    numero = random.randint(10000000, 99999999)
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    letra = letras[numero % 23]
    return f"{numero}{letra}"

dni = generar_dni()
print(f"DNI generado: {dni}")
```

### Desafío 5: Cifrado César

```python
def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            nueva_letra = chr((ord(letra) - base + desplazamiento) % 26 + base)
            resultado += nueva_letra
        else:
            resultado += letra
    return resultado

mensaje = input("Mensaje a cifrar: ")
desplazamiento = int(input("Desplazamiento (1-25): "))
print(f"Mensaje cifrado: {cifrar_cesar(mensaje, desplazamiento)}")
```

## Troubleshooting Técnico

### TypeError: can't multiply sequence by non-int of type 'str'

**Causa:** Estás intentando multiplicar un string por algo que no es un entero.
**Solución:** Convierte a int/float antes: `int(input("número: ")) * 5`

### ValueError: could not convert string to float

**Causa:** El usuario escribió texto donde se esperaba un número.
**Solución:** Usa try/except para validar la entrada.