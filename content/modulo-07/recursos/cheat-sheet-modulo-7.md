# Cheat Sheet — Módulo 7: Manejo de Archivos

> Referencia rápida para trabajar con archivos en Python.

---

## 📂 Abrir y cerrar archivos

```python
# ✅ Forma recomendada: contexto with
with open("archivo.txt", "r") as f:
    contenido = f.read()
# El archivo se cierra automáticamente

# Modos de apertura
"r"   # Lectura (default)
"w"   # Escritura (sobreescribe)
"a"   # Append (agrega al final)
"x"   # Creación exclusiva (error si existe)
"rb"  # Lectura binaria
"wb"  # Escritura binaria
```

## 📖 Leer archivos

```python
# Todo el contenido
texto = f.read()

# Línea por línea (recomendado)
for linea in f:
    print(linea.strip())

# Una línea a la vez
linea = f.readline()

# Lista de líneas
lineas = f.readlines()
```

## ✏️ Escribir archivos

```python
# Escribir una cadena
f.write("Hola mundo\n")

# Escribir múltiples líneas
f.writelines(["línea 1\n", "línea 2\n"])

# pathlib: escribir y leer directamente
from pathlib import Path
Path("archivo.txt").write_text("contenido")
texto = Path("archivo.txt").read_text()
```

## 📊 Archivos CSV

```python
import csv

# Leer como listas
with open("datos.csv", "r") as f:
    for fila in csv.reader(f):
        print(fila)

# Leer como diccionarios (recomendado)
with open("datos.csv", "r") as f:
    for fila in csv.DictReader(f):
        print(fila["nombre"])

# Escribir desde listas
with open("datos.csv", "w", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nombre", "edad"])
    escritor.writerow(["Ana", 28])

# Escribir desde diccionarios
with open("datos.csv", "w", newline="") as f:
    escritor = csv.DictWriter(f, fieldnames=["nombre", "edad"])
    escritor.writeheader()
    escritor.writerow({"nombre": "Ana", "edad": 28})
```

## 📦 Archivos JSON

```python
import json

# Python → JSON (string)
json_texto = json.dumps(datos, indent=4)

# Python → archivo
with open("datos.json", "w") as f:
    json.dump(datos, f, indent=4)

# JSON (string) → Python
datos = json.loads(json_texto)

# archivo → Python
with open("datos.json", "r") as f:
    datos = json.load(f)

# Manejar errores
try:
    datos = json.load(f)
except json.JSONDecodeError as e:
    print(f"JSON inválido: {e}")
```

## 🛠️ pathlib — Rutas modernas

```python
from pathlib import Path

# Crear ruta
ruta = Path("directorio") / "subdir" / "archivo.txt"

# Propiedades
ruta.name      # "archivo.txt"
ruta.stem      # "archivo"
ruta.suffix    # ".txt"
ruta.parent    # Path("directorio/subdir")

# Verificar
ruta.exists()     # True/False
ruta.is_file()    # True/False
ruta.is_dir()     # True/False

# Navegar
for item in Path(".").iterdir():
    print(item.name)

# Buscar
archivos_py = list(Path(".").glob("**/*.py"))

# Crear
Path("nueva_carpeta").mkdir(parents=True, exist_ok=True)
Path("archivo.txt").touch()

# Operaciones
ruta.rename("nuevo_nombre.txt")  # Renombrar
ruta.unlink()                     # Eliminar archivo
Path("carpeta").rmdir()           # Eliminar directorio vacío
```

## ⚠️ Errores comunes

| Error | Causa | Solución |
|-------|-------|----------|
| `FileNotFoundError` | El archivo no existe | Verificar con `os.path.exists()` o `ruta.exists()` |
| `PermissionError` | Sin permisos de lectura/escritura | Verificar permisos del archivo |
| `FileExistsError` | Modo `"x"` y el archivo ya existe | Usar `"w"` o verificar antes |
| `json.JSONDecodeError` | JSON mal formado | Validar formato, usar `try/except` |
| Líneas vacías en CSV | Falta `newline=""` | Usar `open(..., newline="")` |
| Archivo sobrescrito | Usar `"w"` en vez de `"a"` | Usar `"a"` para agregar contenido |

## 🧠 Principios del Zen aplicados

| Principio | Aplicación en archivos |
|-----------|----------------------|
| **Beautiful is better than ugly** | `pathlib` con `/` vs `os.path.join()` |
| **Simple is better than complex** | `with open()` cierra automáticamente |
| **Readability counts** | `fila["nombre"]` vs `fila[0]` |
| **Explicit is better than implicit** | `newline=""` al escribir CSV |
| **Errors should never pass silently** | `try/except` al leer archivos |

## 🔑 Mnemotécnico: dump vs dumps

| Función | Dirección | Truco |
|---------|-----------|-------|
| `json.dump()` | Objeto → archivo | **dump** = volcar en archivo |
| `json.dumps()` | Objeto → string | dump**s** = dump + **s**tring |
| `json.load()` | archivo → objeto | **load** = cargar desde archivo |
| `json.loads()` | string → objeto | load**s** = load + **s**tring |

---

*Módulo 7 — Manejo de Archivos | Curso de Python con Quarto*
