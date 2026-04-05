# 📋 Cheat Sheet — Módulo 10: Proyecto Integrador

## Estructura profesional de un proyecto Python

```
mi_proyecto/
├── README.md              # Documentación del proyecto
├── main.py                # Punto de entrada (python main.py)
├── datos/                 # Archivos de datos (JSON, CSV)
│   └── datos.json
└── modulos/               # Código organizado
    ├── __init__.py        # Hace que sea un paquete
    ├── gestor.py          # Lógica de negocio
    └── utilidades.py      # Funciones auxiliares
```

## Patrones de código esenciales

### 1. Punto de entrada estándar

```python
def main():
    """Función principal del programa."""
    pass

if __name__ == "__main__":
    main()
```

### 2. Leer archivo JSON

```python
import json
import os

def cargar(archivo):
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []  # Default si no existe
```

### 3. Escribir archivo JSON

```python
def guardar(archivo, datos):
    os.makedirs(os.path.dirname(archivo), exist_ok=True)
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
```

### 4. Leer archivo CSV

```python
import csv

def leer_csv(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        return list(lector)
```

### 5. Validar entrada numérica

```python
def pedir_entero(mensaje, minimo=1, maximo=999):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"Debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Ingresa un número válido.")
```

### 6. Menú interactivo

```python
def main():
    while True:
        print("1. Opción A")
        print("2. Opción B")
        print("3. Salir")
        opcion = input("Elige: ").strip()

        if opcion == "1":
            hacer_a()
        elif opcion == "2":
            hacer_b()
        elif opcion == "3":
            print("¡Adiós!")
            break
```

### 7. Búsqueda en lista de diccionarios

```python
# Buscar por texto (insensible a mayúsculas)
def buscar(lista, campo, termino):
    termino = termino.lower()
    return [item for item in lista if termino in item[campo].lower()]

# Buscar por ID exacto
def obtener_por_id(lista, id_buscar):
    for item in lista:
        if item["id"] == id_buscar:
            return item
    return None
```

### 8. Estadísticas básicas

```python
def media(valores):
    return sum(valores) / len(valores) if valores else 0

def mediana(valores):
    if not valores:
        return 0
    ordenados = sorted(valores)
    n = len(ordenados)
    medio = n // 2
    if n % 2 == 0:
        return (ordenados[medio - 1] + ordenados[medio]) / 2
    return ordenados[medio]

def moda(valores):
    if not valores:
        return None
    frecuencias = {}
    for v in valores:
        frecuencias[v] = frecuencias.get(v, 0) + 1
    return max(frecuencias, key=frecuencias.get)
```

## Principios del Zen de Python aplicados

| Principio | Aplicación en proyectos |
|-----------|------------------------|
| Beautiful is better than ugly | Código indentado, nombres claros |
| Explicit is better than implicit | Docstrings, tipos claros |
| Simple is better than complex | Una función = una responsabilidad |
| Readability counts | snake_case, comentarios mínimos |
| Errors should never pass silently | try/except, validación de entrada |
| There should be one obvious way | Seguir convenciones de Python |

## Checklist antes de entregar

- [ ] El programa se ejecuta sin errores
- [ ] README explica qué hace y cómo usarlo
- [ ] Todas las funciones tienen docstrings
- [ ] Los nombres de variables son descriptivos
- [ ] No hay código comentado innecesario
- [ ] Se manejan errores de entrada del usuario
- [ ] Los datos persisten entre ejecuciones
- [ ] La estructura de carpetas es clara
- [ ] No hay datos hardcodeados (excepto ejemplos iniciales)
- [ ] El código sigue PEP 8 (snake_case, indentación)

## Errores frecuentes y soluciones

| Error | Causa | Solución |
|-------|-------|----------|
| `FileNotFoundError` | Archivo no existe | `os.path.exists()` antes de abrir |
| `json.decoder.JSONDecodeError` | Archivo JSON corrupto | Validar contenido o recrear |
| `ValueError` | `int("abc")` | `try/except ValueError` |
| `KeyError` | Clave no existe en dict | `dict.get("clave", default)` |
| `IndexError` | Índice fuera de rango | Verificar `len(lista)` antes |
| IDs duplicados | `len(lista) + 1` | `max(id for x in lista) + 1` |
| Stock negativo | No verificar antes de restar | `if stock >= cantidad` |
| Búsqueda falla | Case-sensitive | `.lower()` en ambos lados |

---

> **Simple is better than complex.** Guarda esta cheat sheet como referencia rápida.
