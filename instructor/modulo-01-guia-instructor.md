# Guía del Instructor — Módulo 1: Introducción a Python

## Objetivos de Aprendizaje

Al finalizar este módulo, el estudiante será capaz de:

1. Explicar qué es Python y sus principales usos
2. Instalar Python y configurar un entorno de desarrollo
3. Escribir y ejecutar programas básicos
4. Usar variables, tipos de datos y funciones de entrada/salida
5. Aplicar buenas prácticas de nomenclatura desde el primer día

## Duración Estimada

- **Teoría**: 2 horas
- **Práctica**: 3 horas
- **Desafíos**: 2 horas
- **Total**: 7 horas

## Estructura de la Sesión

### Sesión 1: Fundamentos (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-15 min | Presentación del curso y expectativas | index.qmd |
| 15-30 min | ¿Qué es Python? Historia y filosofía | 01-que-es-python.qmd |
| 30-60 min | Instalación y configuración | 02-instalacion.qmd |
| 60-90 min | Hola Mundo y print() | 03-hola-mundo.qmd |
| 90-120 min | Variables y tipos de datos | 04-variables.qmd + 05-tipos-basicos.qmd |

### Sesión 2: Práctica (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-30 min | Repaso y preguntas | Todas las lecciones |
| 30-60 min | Entrada y salida de datos | 06-input-output.qmd |
| 60-90 min | Laboratorio 1: Primer programa | laboratorios/01-primer-programa.qmd |
| 90-120 min | Laboratorio 2: Variables en acción | laboratorios/02-variables-en-accion.qmd |

### Sesión 3: Desafíos (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-30 min | Desafíos 1-3 (individuales) | desafios/01-03 |
| 30-60 min | Desafíos 4-5 (en parejas) | desafios/04-05 |
| 60-90 min | Desafíos 6-7 (en equipos) | desafios/06-07 |
| 90-120 min | Revisión grupal y retroalimentación | Todas las soluciones |

## Preguntas Frecuentes Anticipadas

### ¿Python es un lenguaje compilado o interpretado?

**Respuesta:** Interpretado. Python lee y ejecuta tu código línea por línea a través del intérprete. No genera un archivo ejecutable como C o Java.

### ¿Por qué se usa snake_case y no camelCase?

**Respuesta:** Es la convención oficial de Python (PEP 8). Seguir las convenciones del lenguaje hace que tu código sea legible para cualquier programador Python.

### ¿input() siempre devuelve texto?

**Respuesta:** Sí. Siempre. Incluso si el usuario escribe un número, input() lo devuelve como string. Debes convertirlo explícitamente con int() o float().

### ¿Cuál es la diferencia entre / y //?

**Respuesta:** `/` siempre devuelve un float (división exacta). `//` devuelve un int (división entera, descarta decimales).

## Puntos de Atención

1. **Verificar instalaciones**: Los primeros 15 minutos dedica a verificar que todos tienen Python funcionando.
2. **No asumir conocimiento**: No uses términos como "iterar", "instanciar" o "parámetro" sin explicarlos.
3. **Fomentar la experimentación**: Después de cada ejemplo, pide que modifiquen algo y vean qué pasa.
4. **Errores como aprendizaje**: Cuando un estudiante tenga un error, no le des la solución. Guía con preguntas: "¿Qué te dice el mensaje de error?"

## Evaluación del Módulo

### Criterios de Aprobación

| Criterio | Peso | Mínimo |
|----------|------|--------|
| Desafíos completados (70%+) | 40% | 5 de 7 |
| Laboratorios completados | 30% | 2 de 2 |
| Participación en clase | 15% | Activa |
| Quiz final (Desafío 7) | 15% | 60% |

### Rúbrica de Evaluación

| Nivel | Descripción |
|-------|-------------|
| **Excelente (90-100%)** | Completa todos los desafíos, código limpio, nombres descriptivos, sin errores |
| **Bueno (75-89%)** | Completa la mayoría de desafíos, código funcional con mejoras menores |
| **Satisfactorio (60-74%)** | Completa desafíos básicos, necesita ayuda en los avanzados |
| **Necesita apoyo (<60%)** | Dificultad con conceptos fundamentales, requiere refuerzo |

## Troubleshooting Técnico

### Python no se encuentra en PATH (Windows)

```
Error: 'python3' is not recognized as an internal or external command
```

**Solución:** Reinstalar Python marcando "Add Python to PATH" o agregar manualmente:
`C:\Users\TU_USUARIO\AppData\Local\Programs\Python\Python3XX\` al PATH.

### El intérprete no ejecuta código

```
>>> print("hola")
  File "<stdin>", line 1
    print("hola")
    ^
IndentationError: unexpected indent
```

**Solución:** El código en el intérprete interactivo NO debe tener indentación al inicio. Solo usa espacios dentro de bloques (if, for, etc.).

### pip no funciona en el entorno virtual

```
pip: command not found
```

**Solución:** Asegúrate de que el entorno virtual está activado:
```bash
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```