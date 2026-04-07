# Guía del Instructor — Módulo 7: Manejo de Archivos

## Objetivos de Aprendizaje

Al finalizar este módulo, el estudiante será capaz de:

1. Abrir, leer y escribir archivos de texto
2. Usar el contexto `with` para manejo seguro de archivos
3. Procesar archivos CSV (lectura y escritura)
4. Trabajar con archivos JSON
5. Utilizar pathlib para operaciones con rutas

## Duración Estimada

- **Teoría**: 2 horas
- **Práctica**: 3 horas
- **Desafíos**: 2 horas
- **Total**: 7 horas

## Estructura de la Sesión

### Sesión 1: Archivos de Texto (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-30 min | Repaso Módulo 6 | Diccionarios |
| 30-75 min | Abrir/cerrar, leer archivos | 01-abrir-cerrar-archivos.qmd, 02-leer-archivos.qmd |
| 75-120 min | Escribir archivos | 03-escribir-archivos.qmd |

### Sesión 2: CSV y JSON (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-45 min | Procesar CSV | 04-manejo-csv.qmd |
| 45-90 min |JSON (guardar/cargar) | 05-manejo-json.qmd |
| 90-120 min | Pathlib | 06-pathlib.qmd |

### Sesión 3: Desafíos (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-60 min | Desafíos 1-4 | desafios/01-04 |
| 60-120 min | Desafíos 5-7 | desafios/05-07 |

## Preguntas Frecuentes Anticipadas

### ¿Por qué usar `with`?

**Respuesta:** El `with` cierra automáticamente el archivo, incluso si hay errores. Es más seguro y limpio.

```python
# ✅ Correcto - with se encarga de cerrar
with open("archivo.txt") as f:
    contenido = f.read()

# ❌ Peligrose - debes cerrar manualmente
f = open("archivo.txt")
contenido = f.read()
f.close()  # Si hay error antes, el archivo queda abierto
```

### ¿Cuál es la diferencia entre read(), readline() y readlines()?

**Respuesta:** 
- `read()`: Todo el contenido como string
- `readline()`: Una línea a la vez
- `readlines()`: Todas las líneas como lista

### ¿Cómo manejo archivos que no existen?

**Respuesta:** Verificar antes o usar try/except:

```python
import os
if os.path.exists("archivo.txt"):
    with open("archivo.txt") as f:
        ...

# o
try:
    with open("archivo.txt") as f:
        ...
except FileNotFoundError:
    print("El archivo no existe")
```

### ¿Para qué sirve el módulo csv?

**Respuesta:** Para procesar archivos CSV correctamente, manejando el parsing automáticamente.

```python
import csv
with open("datos.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # Cada fila como lista
```

## Analogías para Enseñar

### with como un candado automático
> "with es como un candado que se cierra solo cuando sales del edificio, aunque salgas por emergencia."

### Archivos como una biblioteca
> "Abrir es como entrar a la biblioteca. Leer es hojear libros. Escribir es escribir notas. Cerrar es salir. Si te olvidas de cerrar, la biblioteca se queda abierta para otros."

## Soluciones de Desafíos

### Desafío 3: Log Analyzer

```python
def analizar_log(archivo_log):
    errores = 0
    warnings = 0
    info = 0
    
    with open(archivo_log) as f:
        for linea in f:
            if "ERROR" in linea:
                errores += 1
            elif "WARNING" in linea:
                warnings += 1
            elif "INFO" in linea:
                info += 1
    
    return {"errores": errores, "warnings": warnings, "info": info}

resultado = analizar_log("servidor.log")
print(f"Errores: {resultado['errores']}")
```

### Desafío 4: CSV a Diccionario

```python
import csv

def csv_a_diccionario(archivo_csv, clave_columna):
    resultado = {}
    with open(archivo_csv) as f:
        reader = csv.DictReader(f)
        for fila in reader:
            clave = fila[clave_columna]
            resultado[clave] = fila
    return resultado

usuarios = csv_a_diccionario("usuarios.csv", "id")
print(usuarios["001"]["nombre"])
```

### Desafío 5: Configurador JSON

```python
import json

def guardar_config(config, archivo="config.json"):
    with open(archivo, "w") as f:
        json.dump(config, f, indent=4)

def cargar_config(archivo="config.json"):
    try:
        with open(archivo) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Uso
config = {"tema": "oscuro", "idioma": "es", "notificaciones": True}
guardar_config(config)
print(cargar_config())
```

## Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| FileNotFoundError | Ruta incorrecta | Verificar ruta con os.path.exists() |
| PermissionError | Sin permisos | Verificar permisos de escritura |
| UnicodeEncodeError | Caracteres especiales | Usar encoding="utf-8" |

## Evaluación

| Criterio | Peso |
|----------|------|
| Desafíos completados | 40% |
| Uso correcto de with | 25% |
| Manejo de errores | 20% |
| Código organizado | 15% |