# Análisis MIT 6.0001 → Mejoras para el Curso ABACOM Python

> **Fecha**: 2026-04-13
> **Autor**: Diego Saavedra
> **Referencia**: MIT 6.0001 Introduction to Computer Science and Programming in Python (Fall 2016)
> **Objetivo**: Identificar qué podemos aprender de MIT 6.0001 para mejorar nuestro curso de Python Fundamentos

---

## 1. Comparación Lado a Lado

| Dimensión | MIT 6.0001 | ABACOM Python | Brecha |
|-----------|------------|---------------|--------|
| **Duración** | Medio semestre (12 semanas, ~24 horas clase) | 50 horas | ✅ ABACOM tiene MÁS tiempo |
| **Lectures** | 12 sesiones con slides + código descargable | 10 módulos con teoría + desafíos | ✅ Estructura similar |
| **Problemas** | 6 problem sets (PS0-PS5), sustanciales | 63 desafios + 3 proyectos + 10 labs | ⚠️ Desafíos ABACOM son ejercicios pequeños |
| **Evaluación** | 2 quizzes + 6 PS (30% + 10% finger exercises) | 10 quizzes + desafios + 3 proyectos | ✅ ABACOM evalúa más continuamente |
| **Pensamiento computacional** | **Explícito** desde el Lecture 1 | **Implícito** en desafíos | 🔴 **Falta explícito** |
| **Complejidad algorítmica** | Big-O en Lectures 10-11 | **No cubierto** | 🔴 **No existe** |
| **Testing y debugging** | Lecture 7 dedicado + assertions | Módulo 9 (unidad 9.4 + 9.6) | ⚠️ Muy tarde en el curso |
| **Recursión** | Lecture 6 explícito | Módulo 4 (unidad 4.6) ✅ | ✅ Cubierto |
| **OOP** | Lectures 8-9 | **No cubierto** (out of scope) | ⚪ Fuera del scope |
| **Proyectos** | Hangman, Caesar cipher, DNA simulation, RSS filter | Gestor tareas, Tienda, Analizador CSV | ⚠️ Menos engagement |
| **Código descargable** | Cada lecture tiene código para ejecutar | Desafíos tienen código inline | ⚠️ Falta "código base" para modificar |
| **Decomposición** | Enfatizada explícitamente en Lecture 4 | Implícita en funciones | ⚠️ Falta énfasis explícito |

---

## 2. Qué le falta a ABACOM (y por qué importa)

### 2.1 🔴 Pensamiento computacional explícito

**Qué tiene MIT**: El curso se llama "Introduction to Computer Science and Programming". Desde el Lecture 1, enseñan **qué es computación**, no solo sintaxis de Python. Los estudiantes aprenden a:
- Descomponer problemas en partes más pequeñas
- Reconocer patrones
- Diseñar algoritmos antes de escribir código
- Evaluar múltiples enfoques para un problema

**Qué tiene ABACOM**: Los desafíos enseñan resolución de problemas **implícitamente**, pero nunca hay una sección que diga "así es como piensas como programador".

**Por qué importa**: Un estudiante puede aprender sintaxis de Python sin aprender a **pensar como programador**. La sintaxis cambia; el pensamiento computacional es transferible a cualquier lenguaje.

**Qué cambiar**:
1. Agregar un **Módulo 0: Pensamiento Computacional** antes de tocar Python
2. Incluir ejercicios de **pseudocódigo** antes de implementar
3. Cada desafío debe tener una sección "¿Cómo lo pienso?" antes de "¿Cómo lo escribo?"
4. Enseñar el ciclo: **Entender → Planificar → Implementar → Verificar**

**Ejemplo concreto para agregar**:

```
Módulo 0: Pensamiento Computacional (4 horas)
├── 0.1 ¿Qué es computación? De recetas a algoritmos
├── 0.2 Descomposición: dividir para conquistar
│       └── Desafío: Descomponer "preparar una cena" en pasos ejecutables
├── 0.3 Patrones y abstracción: reconocer lo que se repite
│       └── Desafío: Identificar patrones en secuencias numéricas
├── 0.4 Diseño de algoritmos: pseudocódigo antes que Python
│       └── Desafío: Escribir en español los pasos para ordenar una lista
└── 0.5 Evaluación de enfoques: ¿hay una mejor manera?
        └── Desafío: Resolver el mismo problema de 2 formas distintas
```

### 2.2 🔴 Complejidad algorítmica (Big-O)

**Qué tiene MIT**: Lectures 10-11 cubren "Understanding Program Efficiency" con notación Big-O. Los estudiantes aprenden que no basta con que funcione; debe funcionar **eficientemente**.

**Qué tiene ABACOM**: Ninguna mención de complejidad. Un estudiante podría escribir un algoritmo O(n²) sin saber que existe O(n).

**Por qué importa**: 
- Diferencia un "programador que hace funcionar código" de un "programador que escribe buen código"
- Esencial para entrevistas técnicas
- Ayuda a tomar decisiones de diseño informadas

**Qué cambiar**:
1. Agregar unidad al **Módulo 8** o crear **Módulo adicional**: "Eficiencia de programas"
2. Mantenerlo **conceptual** sin matemáticas avanzadas
3. Usar ejemplos concretos del curso

**Ejemplo concreto para agregar**:

```
Nueva unidad: 8.7 Eficiencia: ¿tu código escala?
├── ¿Por qué importa la eficiencia?
│   └── Ejemplo: buscar en lista de 10 vs 10,000,000 elementos
├── Notación Big-O: el lenguaje de la eficiencia
│   └── O(1) → O(log n) → O(n) → O(n²) → O(2ⁿ)
│   └── Analogía: buscar en diccionario (búsqueda binaria) vs leer página por página
├── Ejemplos del curso:
│   ├── Buscar elemento en lista: O(n) — lineal
│   ├── Búsqueda binaria: O(log n) — logarítmica
│   ├── Dos bucles anidados: O(n²) — cuadrática
│   └── Acceso por índice: O(1) — constante
└── Desafío: Comparar 2 soluciones al mismo problema
        └── Contar operaciones con timeit
```

**Código de ejemplo**:

```python
# Comparar eficiencia: búsqueda lineal vs binaria
import time

def busqueda_lineal(lista, objetivo):
    """O(n) — revisa cada elemento."""
    for i, elem in enumerate(lista):
        if elem == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    """O(log n) — requiere lista ordenada."""
    izq, der = 0, len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izq = medio + 1
        else:
            der = medio - 1
    return -1

# Demostrar la diferencia con una lista grande
grande = list(range(1_000_000))

inicio = time.perf_counter()
busqueda_lineal(grande, 999_999)
lineal_time = time.perf_counter() - inicio

inicio = time.perf_counter()
busqueda_binaria(grande, 999_999)
binaria_time = time.perf_counter() - inicio

print(f"Lineal:  {lineal_time:.6f}s")
print(f"Binaria: {binaria_time:.6f}s")
print(f"Binaria es {lineal_time/binaria_time:.0f}x más rápida")
```

### 2.3 🔴 Testing y debugging como skill core (no afterthought)

**Qué tiene MIT**: Lecture 7 dedicado a "Testing, Debugging, Exceptions, Assertions". Testing no es un tema avanzado; es una **habilidad fundamental** desde el inicio.

**Qué tiene ABACOM**: Testing está en el Módulo 9 (unidad 9.6), casi al final del curso. Los estudiantes pasan 8 módulos escribiendo código sin tests.

**Por qué importa**:
- Si los estudiantes aprenden a testear desde el Módulo 1, escriben **mejor código desde el inicio**
- Debugging sistemático vs "print() y rezar"
- Assertions como documentación ejecutable

**Qué cambiar**:
1. Mover testing a **Módulo 2** (después de variables y tipos)
2. Introducir `assert` como herramienta de aprendizaje, no como concepto avanzado
3. Cada desafío desde Módulo 2+ incluye tests que el estudiante debe pasar
4. Agregar sección de **debugging sistemático** (no solo "revisa tu código")

**Plan de integración temprana**:

```
Módulo 2 (modificado): Tipos de Datos + Testing Temprano
├── 2.7 Testing con assert: tu red de seguridad
│   ├── ¿Por qué assert? Verificar tus suposiciones
│   ├── assert condición, "mensaje de error"
│   └── Desafío: Escribir asserts para validar funciones del módulo

Módulo 3 (modificado): Estructuras de Control + Debugging
├── 3.7 Debugging sistemático
│   ├── Leer tracebacks (no entrar en pánico)
│   ├── Print debugging vs debugger real
│   ├── Estrategia: aislar, reproducir, fijar, verificar
│   └── Desafío: Arreglar 3 bugs intencionales en código dado

Módulo 9 (refinado): Buenas Prácticas (sin testing básico, más avanzado)
├── 9.4 Manejo de errores: try/except avanzado
├── 9.5 Documentación
├── 9.6 Testing con pytest (ahora es nivel avanzado, no intro)
├── 9.7 Tests parametrizados y fixtures
└── 9.8 Tests de integración
```

### 2.4 ⚠️ Proyectos con más engagement

**Qué tiene MIT**:
- **PS2: Hangman** — juego interactivo, feedback inmediato, los estudiantes VEN el resultado
- **PS3/PS4: Caesar cipher + word game** — criptografía real, aplicar matemáticas
- **PS5: RSS feed filter / DNA mutation simulation** — proyecto sustancial con datos reales

**Qué tiene ABACOM**:
- Gestor de tareas (CLI) — funcional pero no emocionante
- Tienda de productos — CRUD básico
- Analizador de CSV — útil pero genérico

**Por qué importa**: Los proyectos de MIT generan **"wow, construí algo real"**. Los de ABACOM generan "ok, completé el ejercicio".

**Qué cambiar**: Mantener los proyectos actuales pero **agregar alternativas** inspiradas en MIT:

**Proyecto A: Juego Hangman (inspirado en PS2 de MIT)**

```
Proyecto: El Ahorcado en Python
Objetivo: Construir un juego interactivo que el estudiante pueda jugar con amigos

Conceptos que integra:
├── Strings y manipulación de texto
├── Listas y selección aleatoria (random)
├── Bucles while y control de flujo
├── Funciones y descomposición
├── Input/output del usuario
└── Manejo de estados del juego

Entregables:
├── hangman.py — juego principal
├── words.txt — lista de palabras (archivo externo)
└── README.md — cómo jugar

Desafíos progresivos:
1. Versión básica: palabra fija, 6 intentos
2. Palabra aleatoria desde archivo
3. Mostrar letras usadas
4. Dibujar el ahorcado en ASCII art
5. Sistema de puntuación (letras únicas = más puntos)
6. Modo 2 jugadores: uno escribe, otro adivina
```

**Proyecto B: Cifrado César + Criptoanálisis (inspirado en PS3/PS4 de MIT)**

```
Proyecto: Criptografía Básica con Python
Objetivo: Implementar cifrado César y romperlo con análisis de frecuencia

Conceptos que integra:
├── Strings, ord(), chr()
├── Aritmética modular
├── Diccionarios (frecuencia de letras)
├── Archivos de texto
├── Funciones puras
└── Testing (cifrar → descifrar = original)

Entregables:
├── caesar.py — cifrar/descifrar
├── breaker.py — criptoanálisis por frecuencia
├── mensaje_secreto.txt — texto para cifrar
└── tests.py — tests que verifican todo

Desafíos progresivos:
1. Cifrar un string con desplazamiento fijo
2. Descifrar (misma función con desplazamiento negativo)
3. Leer mensaje desde archivo
4. Probar TODOS los desplazamientos (fuerza bruta)
5. Detectar automáticamente el correcto (análisis de frecuencia)
6. Cifrado Vigenère (clave en vez de número)
```

**Proyecto C: Simulador de Mutación de ADN (inspirado en PS5 de MIT)**

```
Proyecto: Simulador de Mutación Genética
Objetivo: Simular mutaciones en secuencias de ADN y analizar resultados

Conceptos que integra:
├── Strings como secuencias biológicas
├── Probabilidad y random
├── Funciones de transformación
├── Estadísticas básicas
├── Archivos JSON para guardar resultados
└── Visualización de datos (texto/tablas)

Entregables:
├── dna.py — simulador de mutaciones
├── secuencias.json — secuencias iniciales
├── analisis.py — estadísticas de mutaciones
└── reporte.md — resultados de la simulación

Desafíos progresivos:
1. Representar ADN como string (A, T, C, G)
2. Mutación puntual: cambiar un carácter aleatorio
3. Mutación por inserción: agregar un carácter
4. Mutación por deleción: remover un carácter
5. Simular N generaciones y guardar resultados
6. Comparar secuencias originales vs mutadas
7. Visualizar la "distancia genética" entre secuencias
```

### 2.5 ⚠️ Código descargable por "lectura"

**Qué tiene MIT**: Cada lecture tiene archivos `.py` descargables que los estudiantes **ejecutan y modifican**. No son ejercicios; son **puntos de partida**.

**Qué tiene ABACOM**: Cada desafío tiene código inline en el `.qmd`. El estudiante copia y pega.

**Por qué importa**: Tener archivos `.py` separados enseña estructura de proyectos reales, no solo snippets.

**Qué cambiar**:
1. Cada módulo debe tener un directorio `codigo/` con archivos `.py` ejecutables
2. Archivos deben ser **puntos de partida** con ejercicios para completar
3. Incluir archivos con **bugs intencionales** para debugging practice

**Estructura propuesta**:

```
content/modulo-03/
├── 01-if-else.qmd
├── 02-if-anidado.qmd
├── ...
└── codigo/
    ├── ejemplos_01_condicionales.py    # Código de la lección 1
    ├── ejemplos_02_bucles.py           # Código de la lección 2
    ├── para_completar_03.py            # Ejercicio con funciones vacías
    └── debug_me_04.py                  # Código con 3 bugs intencionales
```

### 2.6 ⚠️ Decomposición y abstracción explícitas

**Qué tiene MIT**: Lecture 4 es "Decomposition, Abstraction, Functions". No es solo "cómo definir funciones"; es **por qué descomponer problemas**.

**Qué tiene ABACOM**: Módulo 4 enseña funciones (sintaxis), pero no enfatiza el **por qué de la descomposición**.

**Qué cambiar**:
1. Renombrar Módulo 4: "Funciones: Decomposición y Abstracción"
2. Agregar unidad sobre **estrategias de descomposición**:
   - Descomposición por responsabilidad (cada función hace UNA cosa)
   - Descomposición por nivel de abstracción (alto nivel → bajo nivel)
   - Descomposición por reutilización (DRY principle)
3. Ejercicio: Refactorizar un script de 100 líneas en 5 funciones de 20 líneas

---

## 3. Mapeo de Temas MIT → Módulos ABACOM

| MIT Lecture | Tema MIT | ABACOM Módulo | Estado | Acción |
|-------------|----------|---------------|--------|--------|
| **Lecture 1** | Introduction to computation, Python | Módulo 1 | ⚠️ Parcial | Agregar "qué es computación" (no solo Python) |
| **Lecture 2** | Branching, iteration | Módulo 3 | ✅ Cubierto | Agregar más ejemplos de iteración |
| **Lecture 3** | String manipulation, loops | Módulo 2 + 3 | ✅ Cubierto | Unificar mejor |
| **Lecture 4** | Decomposition, abstraction, functions | Módulo 4 | ⚠️ Parcial | Agregar sección de descomposición explícita |
| **Lecture 5** | Tuples, lists, mutability, aliasing | Módulo 5 | ✅ Cubierto | Agregar ejercicios de aliasing |
| **Lecture 6** | Recursion, dictionaries | Módulo 4 + 6 | ✅ Cubierto | Mover recursión a su propia unidad |
| **Lecture 7** | Testing, debugging, exceptions | Módulo 9 | 🔴 Tarde | **Mover testing a Módulo 2, debugging a Módulo 3** |
| **Lecture 8** | Complexity, O notation | **No existe** | 🔴 No cubierto | **Crear nueva unidad o módulo** |
| **Lecture 9** | Binary search, bubble sort, merge sort | **No existe** | 🔴 No cubierto | Agregar como ejemplo de complejidad |
| **Lecture 10** | Classes and OOP | Fuera de scope | ⚪ OK | Fuera del alcance del curso |
| **Lecture 11** | Generators | Fuera de scope | ⚪ OK | Fuera del alcance del curso |
| **Lecture 12** | Searching, sorting | **No existe** | 🔴 No cubierto | Integrar con complejidad algorítmica |

---

## 4. Recomendaciones Pedagógicas Prioritarias

### Prioridad 1: Agregar Pensamiento Computacional (Módulo 0)

**Qué**: Crear un módulo introductorio de 4 horas antes de tocar Python.

**Contenido**:

```
Módulo 0: Pensamiento Computacional
===================================

0.1 ¿Qué es computación?
    - Computación ≠ programación
    - De problemas reales a soluciones computacionales
    - Analogía: receta de cocina → algoritmo

0.2 Descomposición: el arte de dividir problemas
    - Técnica: identificar entradas, proceso, salidas
    - Ejercicio: "planificar una fiesta" descompuesto en funciones
    - Patrón: dividir hasta que cada parte sea manejable

0.3 Patrones: reconocer lo que se repite
    - Secuencias numéricas: reconocer la regla
    - Patrones en texto: palíndromos, repeticiones
    - Abstracción: de lo específico a lo general

0.4 Algoritmos: pasos precisos para resolver problemas
    - Pseudocódigo: escribir en español antes de Python
    - Ejercicio: algoritmo para ordenar cartas
    - Criterios: ¿funciona? ¿termina? ¿es eficiente?

0.5 Evaluación de enfoques
    - Mismo problema, múltiples soluciones
    - Ejercicio: encontrar el máximo de 3 formas distintas
    - Introducir la idea de "mejor" solución

0.6 Del problema al programa
    - Ciclo completo: problema → pseudocódigo → Python → test
    - Ejercicio integrador: resolver un problema completo
```

**Por qué primero**: Los estudiantes llegan queriendo "aprender Python" pero necesitan "aprender a pensar como programador". Sin esto, los desafios son ejercicios de sintaxis, no de resolución de problemas.

### Prioridad 2: Mover Testing y Debugging Temprano

**Qué**: Reestructurar la secuencia de módulos.

**Nuevo orden**:

```
Módulo 1: Introducción a Python (sin cambios)
Módulo 2: Tipos de Datos + Testing temprano (agregar assert)
Módulo 3: Estructuras de Control + Debugging (agregar debugging sistemático)
Módulo 4: Funciones: Decomposición y Abstracción (renombrar + agregar)
Módulo 5: Listas y Tuplas (sin cambios mayores)
Módulo 6: Diccionarios y Sets (sin cambios mayores)
Módulo 7: Manejo de Archivos (sin cambios)
Módulo 8: Módulos, Paquetes y Eficiencia (agregar Big-O)
Módulo 9: Buenas Prácticas (refinar, testing avanzado)
Módulo 10: Proyecto Integrador (con nuevas opciones)
```

### Prioridad 3: Agregar Eficiencia y Complejidad

**Qué**: Unidad en Módulo 8 sobre complejidad algorítmica.

**Alcance mínimo**:
- O(1), O(n), O(n²) — los 3 que importan para principiantes
- Ejemplos concretos del curso
- Comparación con `timeit`
- No matemáticas formales (sin límites, sin demostraciones)

**Alcance ideal** (si hay tiempo):
- Búsqueda binaria vs lineal
- Bubble sort como ejemplo de O(n²)
- Merge sort como ejemplo de O(n log n) — conceptual, no implementar

### Prioridad 4: Proyectos con Más Engagement

**Qué**: Ofrecer 6 opciones de proyecto en vez de 3, incluyendo los inspirados en MIT.

**Nuevas opciones**:

| Proyecto | Inspiración | Dificultad | Engagement |
|----------|-------------|------------|------------|
| Gestor de Tareas | ABACOM original | ⭐⭐ | ⭐⭐ |
| Tienda de Productos | ABACOM original | ⭐⭐⭐ | ⭐⭐ |
| Analizador CSV | ABACOM original | ⭐⭐⭐ | ⭐⭐⭐ |
| **El Ahorcado** | MIT PS2 | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Criptografía César** | MIT PS3/PS4 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Simulador ADN** | MIT PS5 | ⭐⭐⭐ | ⭐⭐⭐⭐ |

---

## 5. Apéndice de Pensamiento Computacional (Propuesta Completa)

Si no se puede agregar como Módulo 0, al menos incluir como **apéndice obligatorio**:

### Apéndice: Kit de Herramientas del Pensador Computacional

```
Apéndice D: Pensamiento Computacional
=====================================

D.1 El ciclo del programador
    Entender → Planificar → Implementar → Verificar → Refactorizar

D.2 Técnicas de descomposición
    - Por responsabilidad: cada función hace UNA cosa
    - Por nivel: alto nivel (qué) → bajo nivel (cómo)
    - Por reutilización: no repetir código (DRY)

D.3 Estrategias de debugging
    - Leer el traceback (no entrar en pánico)
    - Aislar el problema (¿dónde falla?)
    - Reproducir consistentemente (¿siempre falla igual?)
    - Hipótesis → prueba → conclusión
    - Print debugging vs debugger profesional

D.4 Cómo pensar antes de programar
    - Paso 1: ¿Cuál es la entrada? ¿Cuál es la salida?
    - Paso 2: ¿Puedo resolverlo a mano? ¿Cómo?
    - Paso 3: ¿Mis pasos a mano son un algoritmo?
    - Paso 4: ¿Hay una forma más simple?
    - Paso 5: ¿Mi solución cubre los casos borde?

D.5 Heurísticas de resolución de problemas
    - Fuerza bruta primero, optimización después
    - Dividir y conquistar
    - Trabajar hacia atrás (desde la solución)
    - Simplificar el problema (resolver una versión más fácil)
    - Analogías (¿este problema se parece a otro que ya resolví?)

D.6 Ejercicios de pensamiento computacional
    - 10 problemas SIN Python: solo pseudocódigo
    - 5 problemas con múltiples soluciones
    - 3 problemas "imposibles" que requieren un insight
```

---

## 6. Plan de Implementación por Fases

### Fase 1: Quick Wins (1-2 semanas)

| Tarea | Esfuerzo | Impacto |
|-------|----------|---------|
| Agregar `assert` al Módulo 2 | Bajo | Alto |
| Agregar debugging al Módulo 3 | Bajo | Alto |
| Renombrar Módulo 4 (Decomposición) | Bajo | Medio |
| Agregar sección "¿Cómo lo pienso?" a 10 desafios | Medio | Alto |

### Fase 2: Contenido Nuevo (2-4 semanas)

| Tarea | Esfuerzo | Impacto |
|-------|----------|---------|
| Crear Módulo 0: Pensamiento Computacional | Alto | **Muy Alto** |
| Agregar unidad Big-O al Módulo 8 | Medio | Alto |
| Crear proyecto Hangman | Medio | Alto |
| Crear proyecto Criptografía | Medio | Alto |
| Crear proyecto Simulador ADN | Medio | Medio-Alto |

### Fase 3: Estructura (2-3 semanas)

| Tarea | Esfuerzo | Impacto |
|-------|----------|---------|
| Crear directorios `codigo/` por módulo | Medio | Medio |
| Generar archivos `.py` descargables | Medio | Medio |
| Crear archivos con bugs intencionales | Bajo | Alto |
| Refinar Módulo 9 (testing avanzado) | Bajo | Medio |

### Fase 4: Integración (1 semana)

| Tarea | Esfuerzo | Impacto |
|-------|----------|---------|
| Actualizar _quarto.yml con nuevo contenido | Bajo | Requerido |
| Actualizar spec.md y tasks.md | Bajo | Requerido |
| Actualizar guías de instructor | Medio | Alto |
| Actualizar rúbrica de proyectos | Bajo | Medio |

---

## 7. Métricas de Éxito

Después de implementar las mejoras:

| Métrica | Antes | Después (objetivo) |
|---------|-------|-------------------|
| Estudiantes que pueden explicar Big-O | 0% | 70%+ |
| Estudiantes que escriben tests sin que se los pidan | 5% | 50%+ |
| Estudiantes que descomponen problemas antes de programar | 10% | 60%+ |
| Proyectos que los estudiantes mencionan como "los mejores" | 0/3 | 3+/6 |
| Estudiantes que leen tracebacks sin pánico | 20% | 70%+ |

---

## 8. Lo que NO debemos copiar de MIT

MIT 6.0001 es excelente pero tiene características que **no** debemos copiar:

1. **Finger exercises obligatorios**: Son ejercicios pequeños del libro. Nuestros desafios ya cubren esto mejor (son más interactivos y contextualizados).

2. **Quizzes cerrados con papel**: Nuestros quizzes interactivos en Quarto son superiores.

3. **Sistema de late days**: Complejo de implementar y no necesario para un curso autocontenido.

4. **Recitations separadas**: Nuestro formato de labs integrados es más eficiente.

5. **OOP profundo**: Fuera del scope de nuestro curso de fundamentos.

6. **Generators**: Demasiado avanzado para principiantes absolutos.

---

## 9. Resumen Ejecutivo

### Lo que MIT 6.0001 hace mejor:
1. **Enseña a pensar**, no solo a programar
2. **Testing como skill fundamental**, no como tema avanzado
3. **Complejidad algorítmica** desde el inicio
4. **Proyectos con engagement real** (juegos, criptografía, ciencia)
5. **Código descargable** como punto de partida, no como snippet

### Lo que ABACOM hace mejor:
1. **Más tiempo** (50h vs 24h) — podemos ser más exhaustivos
2. **Desafíos más numerosos** (63 vs ~20 finger exercises)
3. **Labs integrados** (10 labs vs recitations separadas)
4. **Código limpio** desde el inicio (PEP8, nombres descriptivos)
5. **Formato interactivo** con Quarto (mejor que slides de MIT)

### Las 4 acciones prioritarias:
1. **Crear Módulo 0**: Pensamiento computacional (lo que más falta)
2. **Mover testing al Módulo 2**: No esperar hasta el Módulo 9
3. **Agregar Big-O al Módulo 8**: Eficiencia como concepto, no como matemáticas
4. **Agregar 3 proyectos MIT-inspired**: Hangman, Criptografía, Simulador ADN

### Estimación total: 6-10 semanas de trabajo

---

## Referencias

- MIT 6.0001 OCW: https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
- Textbook: Guttag, John. "Introduction to Computation and Programming Using Python" (2nd ed., MIT Press, 2016)
- ABACOM Python Spec: `/Users/statick/dev/apps/abacom/course_of_python/spec.md`
- ABACOM Python Tasks: `/Users/statick/dev/apps/abacom/course_of_python/tasks.md`
