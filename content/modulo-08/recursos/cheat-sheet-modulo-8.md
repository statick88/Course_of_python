# Cheat Sheet — Módulo 8: Módulos y Paquetes

## Importar módulos

```python
import math                          # Importar todo el módulo
from math import pi, sqrt            # Importar funciones específicas
import datetime as dt                # Importar con alias
from math import *                   # ❌ NO USAR — importa todo
```

## Biblioteca estándar esencial

| Módulo | Funciones clave | Uso |
|--------|----------------|-----|
| `math` | `sqrt()`, `pi`, `ceil()`, `floor()` | Matemáticas |
| `random` | `randint()`, `choice()`, `shuffle()`, `sample()` | Aleatorios |
| `datetime` | `now()`, `today()`, `strftime()`, `timedelta()` | Fechas/horas |
| `os` | `getcwd()`, `listdir()`, `path.exists()` | Sistema operativo |
| `pathlib` | `Path()`, `.name`, `.suffix`, `.parent` | Rutas de archivos |
| `json` | `dumps()`, `loads()`, `dump()`, `load()` | Datos JSON |
| `re` | `findall()`, `sub()`, `search()` | Expresiones regulares |
| `sys` | `path`, `argv`, `exit()` | Intérprete Python |
| `collections` | `Counter`, `defaultdict`, `namedtuple` | Estructuras de datos |

## Crear un módulo

```python
# mi_modulo.py
def mi_funcion():
    """Docstring explica qué hace."""
    pass

if __name__ == "__main__":
    # Solo se ejecuta con: python mi_modulo.py
    print("Ejecutado directamente")
```

## Crear un paquete

```
mi_paquete/
├── __init__.py      # from .modulo import funcion
├── modulo_a.py
└── modulo_b.py
```

```python
# __init__.py
from .modulo_a import funcion_a
from .modulo_b import funcion_b

__all__ = ["funcion_a", "funcion_b"]
```

## pip — Comandos esenciales

```bash
pip install paquete              # Instalar
pip install paquete==1.0         # Versión específica
pip install --upgrade paquete    # Actualizar
pip uninstall paquete            # Desinstalar
pip list                         # Listar instalados
pip show paquete                 # Detalles del paquete
pip freeze > requirements.txt    # Guardar dependencias
pip install -r requirements.txt  # Instalar desde archivo
```

## Entornos virtuales

```bash
# Crear
python -m venv venv

# Activar (Mac/Linux)
source venv/bin/activate

# Activar (Windows)
venv\Scripts\activate

# Desactivar
deactivate
```

## Importaciones relativas

```python
from .modulo import func      # Mismo nivel
from ..modulo import func     # Un nivel arriba
from ...modulo import func    # Dos niveles arriba
```

## Errores comunes

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError` | Módulo no instalado o ruta incorrecta | `pip install` o verificar ruta |
| `ImportError` | Nombre incorrecto o circular | Verificar nombre, romper ciclo |
| Sombrear módulo estándar | Tu archivo se llama `math.py` | Renombrar tu archivo |
| Conflicto de versiones | Dos proyectos, mismo Python | Usar entornos virtuales |

## Zen de Python aplicado

| Principio | Aplicación |
|-----------|------------|
| Batteries included | Usa la biblioteca estándar primero |
| Explicit is better than implicit | `import math` en vez de `from math import *` |
| Readability counts | Nombres de módulos claros y descriptivos |
| Simple is better than complex | 3 comandos para entornos virtuales |
| Namespaces are one honking great idea | Paquetes y entornos como namespaces |

---

> **Recuerda:** Antes de instalar un paquete externo, revisa si la biblioteca estándar ya tiene lo que necesitas.
