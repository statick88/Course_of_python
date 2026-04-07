# Guía del Instructor — Módulo 6: Diccionarios y Sets

## Objetivos de Aprendizaje

Al finalizar este módulo, el estudiante será capaz de:

1. Crear y manipular diccionarios (crear, acceder, modificar, eliminar)
2. Iterar sobre diccionarios (keys, values, items)
3. Comprender sets y sus operaciones (unión, intersección, diferencia)
4. Usar diccionarios anidados para estructuras de datos complejas
5. Aplicar diccionarios en casos reales (agendas, inventarios, encuestas)

## Duración Estimada

- **Teoría**: 2 horas
- **Práctica**: 3 horas
- **Desafíos**: 2 horas
- **Total**: 7 horas

## Estructura de la Sesión

### Sesión 1: Fundamentos de Diccionarios (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-30 min | Repaso Módulo 5 | Listas y tuplas |
| 30-75 min | Crear y acceder | 01-crear-diccionarios.qmd, 02-acceder-modificar.qmd |
| 75-120 min | Iterar diccionarios | 03-iterar-diccionarios.qmd |

### Sesión 2: Sets y Avanzado (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-45 min | Sets y operaciones | 04-sets.qmd |
| 45-90 min | Diccionarios anidados | 05-diccionarios-anidados.qmd |
| 90-120 min | Desafíos iniciales | Desafíos 1-3 |

### Sesión 3: Desafíos Avanzados (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-60 min | Desafíos 4-5 | desafios/04-05 |
| 60-120 min | Desafíos 6-7 | desafios/06-07 |

## Preguntas Frecuentes Anticipadas

### ¿Cuál es la diferencia entre diccionarios y listas?

**Respuesta:** Listas usan índices numéricos (0, 1, 2...). Diccionarios usan claves personalizadas (strings, números).

### ¿Pueden las claves del diccionario ser cualquier tipo?

**Respuesta:** Las claves deben ser hashables (inmutables): strings, números, tuplas. NO listas ni diccionarios.

### ¿Cómo verifico si una clave existe en un diccionario?

**Respuesta:** Dos formas:
```python
# Forma 1: in
if "nombre" in diccionario:
    print(diccionario["nombre"])

# Forma 2: get (más segura)
print(diccionario.get("nombre", "valor por defecto"))
```

### ¿Qué es un set en Python?

**Respuesta:** Es como una lista pero sin duplicados y sin orden. Útil para eliminar duplicados o hacer operaciones de conjuntos.

## Analogías para Enseñar

### Diccionario como una guía telefónica
> "El nombre es la clave (índice), el número de teléfono es el valor. Buscas por nombre, obtienes el teléfono."

### Set como unclub único
> "Solo puedes entrar una vez. No importa el orden de llegada, solo importan los miembros únicos."

## Soluciones de Desafíos

### Desafío 1: Agenda de Contactos

```python
agenda = {}

def agregar_contacto(nombre, telefono, email=None):
    agenda[nombre] = {
        "telefono": telefono,
        "email": email
    }

def buscar_contacto(nombre):
    return agenda.get(nombre, "No encontrado")

def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        return True
    return False
```

### Desafío 5: Sistema de Votaciones

```python
votos = {}

def registrar_voto(candidato):
    if candidato in votos:
        votos[candidato] += 1
    else:
        votos[candidato] = 1

def mostrar_resultados():
    for candidato, cantidad in sorted(votos.items(), key=lambda x: x[1], reverse=True):
        print(f"{candidato}: {cantidad} votos")

# Prueba
registrar_voto("Ana")
registrar_voto("Ana")
registrar_voto("Juan")
mostrar_resultados()
```

### Desafío 6: Base de Datos de Estudiantes

```python
estudiantes = {
    "001": {"nombre": "Ana", "curso": "Python", "notas": [8, 9, 7]},
    "002": {"nombre": "Juan", "curso": "Python", "notas": [6, 7, 8]},
}

def promedio_estudiante(codigo):
    if codigo in estudiantes:
        notas = estudiantes[codigo]["notas"]
        return sum(notas) / len(notas)
    return None

def estudiantes_aprobados():
    return [cod for cod, data in estudiantes.items() 
            if sum(data["notas"]) / len(data["notas"]) >= 7]
```

## Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| KeyError | Clave no existe | Usar `.get()` con valor por defecto |
| Unhashable type: list | Usar lista como clave | Usar tupla o string como clave |
| Modificar dict mientras iteras | Error de comportamiento | Iterar sobre `.keys()` o `.items()` |

## Evaluación

| Criterio | Peso |
|----------|------|
| Desafíos completados | 40% |
| Uso correcto de diccionarios | 25% |
| Lógica de programación | 20% |
| Código limpio y documentado | 15% |