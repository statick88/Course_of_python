# Guía del Instructor — Módulo 8: Módulos y Paquetes

## Objetivos de Aprendizaje

Al finalizar este módulo, el estudiante será capaz de:

1. Importar módulos built-in y externos
2. Crear y organizar tus propios módulos
3. Comprender la diferencia entre módulos y paquetes
4. Usar pip para instalar paquetes externos
5. Crear y manejar entornos virtuales

## Duración Estimada

- **Teoría**: 2.5 horas
- **Práctica**: 3 horas
- **Desafíos**: 1.5 horas
- **Total**: 7 horas

## Estructura de la Sesión

### Sesión 1: Importar Módulos (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-30 min | Repaso Módulo 7 | Archivos |
| 30-75 min | Importar módulos | 01-importar-modulos.qmd |
| 75-120 min | Módulos estándar | 02-modulos-estandar.qmd |

### Sesión 2: Crear Módulos y Paquetes (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-45 min | Crear tus propios módulos | 03-crear-modulos.qmd |
| 45-90 min | Paquetes | 04-paquetes.qmd |
| 90-120 min | pip y entornos virtuales | 05-pip-paquetes.qmd, 06-entornos-virtuales.qmd |

### Sesión 3: Desafíos (2 horas)

| Tiempo | Actividad | Material |
|--------|-----------|----------|
| 0-60 min | Desafíos 1-4 | desafios/01-04 |
| 60-120 min | Desafíos 5-7 | desafios/05-07 |

## Preguntas Frecuentes Anticipadas

### ¿Cuál es la diferencia entre import y from...import?

**Respuesta:** 
- `import modulo`: Trae todo el módulo, usas `modulo.funcion()`
- `from modulo import funcion`: Trae solo esa función, usas `funcion()`

### ¿Qué es __name__ == "__main__"?

**Respuesta:** Cuando ejecutas un archivo directamente, su `__name__` es `"__main__"`. Cuando se importa, es el nombre del módulo.

```python
# useful.py
def utiles():
    print("soy útil")

if __name__ == "__main__":
    # Esto solo se ejecuta si corres python useful.py directamente
    utiles()
```

### ¿Cómo instalo un paquete?

**Respuesta:** Con pip:
```bash
pip install nombre_del_paquete
```

### ¿Qué es un entorno virtual?

**Respuesta:** Un entorno aislado donde puedes instalar paquetes sin afectar el sistema o otros proyectos.

## Analogías para Enseñar

### Módulo como una herramienta
> "Un módulo es como una herramienta en un taller. La importas (la tomas prestada) y la usas para tu trabajo."

### Entorno virtual como un cuarto de proyectos
> "Cada proyecto tiene su propio cuarto. Los materiales (paquetes) de un cuarto no se mezclan con los de otro."

## Soluciones de Desafíos

### Desafío 2: Generador de Fechas

```python
from datetime import datetime, timedelta

def generar_rango_fechas(inicio, dias):
    fecha = datetime.strptime(inicio, "%Y-%m-%d")
    return [(fecha + timedelta(days=i)).strftime("%Y-%m-%d") 
            for i in range(dias)]

# Uso
fechas = generar_rango_fechas("2026-01-01", 7)
for f in fechas:
    print(f)
```

### Desafío 3: Aleatorios Avanzados

```python
import random
import string

def generar_contrasena(longitud=12, incluir_simbolos=True):
    caracteres = string.ascii_letters + string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def generar_usuario(nombre):
    numero = random.randint(100, 999)
    return f"{nombre.lower()}{numero}"

print(generar_contrasena())  # Ej: aB3$kL9#mNp
print(generar_usuario("Ana"))  # ana234
```

### Desafío 7: Proyecto Modular

```
mi_proyecto/
├── main.py
├── utils/
│   ├── __init__.py
│   ├── fechas.py
│   └── validacion.py
└── datos/
    └── usuarios.json
```

```python
# main.py
from utils import fechas, validacion

if validacion.validar_email("correo@ejemplo.com"):
    print(fechas.fecha_hoy())
```

## Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| ModuleNotFoundError | Módulo no instalado o ruta incorrecta | Verificar instalación o PYTHONPATH |
| Circular import | Módulos se importan mutuamente | Reorganizar el código |
| ImportError | Paquete no compatible | Verificar versión de Python |

## Evaluación

| Criterio | Peso |
|----------|------|
| Desafíos completados | 40% |
| Estructura de módulos | 25% |
| Uso de imports correctos | 20% |
| Documentación | 15% |