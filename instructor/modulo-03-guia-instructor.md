# Guía del Instructor — Módulo 3: Estructuras de Control

## Objetivos de Aprendizaje

Al finalizar este módulo, el estudiante será capaz de:

1. Implementar decisiones condicionales con if/elif/else
2. Crear bucles deterministas con for
3. Crear bucles condicionales con while
4. Controlar el flujo de bucles con break, continue y else
5. Usar comprensión de listas para código conciso

## Duración Estimada

- **Teoría**: 2.5 horas
- **Práctica**: 3 horas
- **Desafíos**: 1.5 horas
- **Total**: 7 horas

## Estructura de la Sesión

### Sesión 1: Condicionales (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-30 min | Repaso Módulo 2 + warm-up | index.qmd |
| 30-75 min | Condicionales if/else | 01-if-else.qmd |
| 75-120 min | Condicionales anidados | 02-if-anidado.qmd |

### Sesión 2: Bucles for (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-30 min | Repaso condicionales | Lecciones anteriores |
| 30-75 min | Bucle for básico | 03-for-loop.qmd |
| 75-120 min | Range y enumerate | 03-for-loop.qmd |

### Sesión 3: Bucles while y control (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-45 min | Bucle while | 04-while-loop.qmd |
| 45-90 min | Break, continue, else | 05-break-continue.qmd |
| 90-120 min | Desafíos supervisados | desafios/ |

## Preguntas Frecuentes Anticipadas

### ¿Cuál es la diferencia entre for y while?

**Respuesta:** `for` itera sobre una secuencia conocida (lista, rango). `while` itera mientras una condición sea verdadera (número不确定de iteraciones).

### ¿Cuándo usar break vs continue?

**Respuesta:** `break` sale completamente del bucle. `continue` salta a la siguiente iteración.

### ¿Para qué sirve el else en un for?

**Respuesta:** El else de un for se ejecuta cuando NO se ejecutó el break. Es como "si terminaste sin interrupciones".

### ¿Qué es comprensión de listas?

**Respuesta:** Una forma concisa de crear listas: `[x*2 for x in range(5)]` = `[0, 2, 4, 6, 8]`

## Analogías para Enseñar

### If/Else como un semáforo
> "El código decide qué camino tomar según una condición, como un semáforo que indica verde o rojo."

### For como un empleado que recorrre una lista
> "Imagina que tienes una lista de tareas y un empleado las hace una por una. Eso es un for."

### While como esperar hasta que-suene-el-despertador
> "El código sigue ejecutándose 'mientras' no se cumpla una condición. Como esperar hasta que suene la alarma."

## Soluciones de Desafíos

### Desafío 3: FizzBuzz (Clásico)

```python
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

### Desafío 5: Piedra Papel Tijera

```python
import random

opciones = ["piedra", "papel", "tijera"]
usuario = input("piedra, papel o tijera: ").lower()
computadora = random.choice(opciones)

if usuario == computadora:
    print(f"Empate: ambos eligieron {usuario}")
elif (usuario == "piedra" and computadora == "tijera") or \
     (usuario == "papel" y computadora == "piedra") or \
     (usuario == "tijera" y computadora == "papel"):
    print(f"Ganaste: {usuario} vence a {computadora}")
else:
    print(f"Perdiste: {computadora} vence a {usuario}")
```

### Desafío 7: Cajero Automático (Completo)

```python
saldo = 1000
while True:
    print(f"\nSaldo actual: ${saldo}")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    opcion = input("Elige: ")
    
    if opcion == "1":
        print(f"Tu saldo es: ${saldo}")
    elif opcion == "2":
        monto = float(input("Monto a depositar: "))
        if monto > 0:
            saldo += monto
            print(f"Depositaste ${monto}")
    elif opcion == "3":
        monto = float(input("Monto a retirar: "))
        if monto > 0 and monto <= saldo:
            saldo -= monto
            print(f"Retiraste ${monto}")
        else:
            print("Monto inválido o insuficiente")
    elif opcion == "4":
        print("¡Gracias por usar el cajero!")
        break
    else:
        print("Opción inválida")
```

## Errores Comunes a Anticipar

| Error | Causa | Solución |
|-------|-------|----------|
| IndentationError | Código fuera del bloque | Verificar indentación (4 espacios) |
| Infinite loop | Condición de while nunca cambia | Agregar forma de salir del bucle |
| Else sin if | Sintaxis incorrecta | `else:` debe estar alineado con `for:` |

## Evaluación

| Criterio | Peso |
|----------|------|
| Desafíos completados | 40% |
| Funcionalidad del código | 30% |
| Uso correcto de estructuras | 20% |
| Legibilidad y comentarios | 10% |